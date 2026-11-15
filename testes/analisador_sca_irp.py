#!/usr/bin/env python3
"""Apura IRP de achados revisados; não executa scanner nem presume cobertura.

Uso: python3 testes/analisador_sca_irp.py relatorio.json
Formato: testes/modelos_coleta/sca.json. Preservar relatório bruto e inventário.
"""
import argparse
import json
from pathlib import Path

PESOS_SEVERIDADE = {"critical": 10, "high": 5, "moderate": 2, "low": 1}


def evidencia_existe(valor, base):
    return isinstance(valor, str) and bool(valor.strip()) and (base / valor).is_file()


def calcular_irp(contagens):
    if any(type(contagens.get(s)) is not int or contagens[s] < 0 for s in PESOS_SEVERIDADE):
        raise ValueError("Contagens ausentes, negativas ou não inteiras")
    return sum(contagens[s] * peso for s, peso in PESOS_SEVERIDADE.items())


def julgar_irp(contagens, irp, altas_so_desenvolvimento=None):
    if contagens['critical'] or irp > 20 or contagens['high'] > 2:
        return 'Crítico'
    if contagens['high']:
        if altas_so_desenvolvimento is False:
            return 'Crítico'
        if altas_so_desenvolvimento is None:
            return 'Inconclusivo'
        return 'Aceitável'
    return 'Excelente' if irp <= 5 else 'Aceitável'


def analisar(dados, base=Path('.')):
    base=Path(base)
    inconclusivo={'status':'Inconclusivo', 'irp':None}
    if (dados.get('cobertura_confirmada') is not True
        or not isinstance(dados.get('escopo'), str) or not dados['escopo'].strip()
        or not isinstance(dados.get('ferramenta'), str) or not dados['ferramenta'].strip()
        or not isinstance(dados.get('base_vulnerabilidades'), str) or not dados['base_vulnerabilidades'].strip()
        or not evidencia_existe(dados.get('relatorio_bruto'), base)
        or not isinstance(dados.get('inventario'), list) or not dados['inventario']
        or not isinstance(dados.get('achados'), list)):
        return dict(inconclusivo, motivo='Cobertura, inventário ou relatório bruto não demonstrados')
    inventario=set()
    for item in dados['inventario']:
        if not all(isinstance(item.get(k), str) and item[k].strip() for k in ('componente','versao')):
            return dict(inconclusivo, motivo='Componente ou versão sem identificação')
        inventario.add((item['componente'],item['versao']))
    unicos={}
    for achado in dados['achados']:
        if (not all(isinstance(achado.get(k), str) and achado[k].strip() for k in ('componente','versao','aviso'))
            or achado.get('severidade') not in PESOS_SEVERIDADE
            or (achado['componente'],achado['versao']) not in inventario):
            return dict(inconclusivo, motivo='Achado inválido ou fora do inventário')
        chave=tuple(achado[k] for k in ('componente','versao','aviso'))
        if chave in unicos and unicos[chave] != achado:
            return dict(inconclusivo, motivo='Achados duplicados com informações divergentes')
        unicos[chave]=achado
    contagens={s:sum(a['severidade']==s for a in unicos.values()) for s in PESOS_SEVERIDADE}
    altas=[a.get('ambiente') for a in unicos.values() if a['severidade']=='high']
    so_dev=(False if 'producao' in altas else True if all(a=='desenvolvimento' for a in altas) else None)
    irp=calcular_irp(contagens)
    return {'status':julgar_irp(contagens,irp,so_dev), 'irp':irp,
            'contagens':contagens, 'escopo':dados['escopo'],
            'limite':'Apuração do recorte declarado; não conclui segurança integral nem H-OP-02.'}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('relatorio',type=Path)
    args=parser.parse_args()
    try:
        resultado=analisar(json.loads(args.relatorio.read_text()),args.relatorio.parent)
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as exc:
        resultado={'status':'Inconclusivo','irp':None,'motivo':str(exc)}
    print(json.dumps(resultado,ensure_ascii=False,indent=2))
    return 2 if resultado['status']=='Inconclusivo' else 0


if __name__=='__main__':
    raise SystemExit(main())
