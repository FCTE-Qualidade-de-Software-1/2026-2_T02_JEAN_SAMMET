#!/usr/bin/env python3
"""Apura TBR a partir de chamadas revisadas, sem disparar requisições.

Uso: python3 testes/teste_controle_acesso_tbr.py relatorio.json
Formato: testes/modelos_coleta/tbr.json. Coletar no ambiente autorizado após
confirmar alvo e controle positivo. Não incluir tokens nos arquivos.
"""
import argparse
import json
from pathlib import Path


def evidencia_existe(valor, base):
    return isinstance(valor,str) and bool(valor.strip()) and (base / valor).is_file()


def analisar(dados, base=Path('.')):
    base=Path(base)
    saida={'status':'Inconclusivo','tbr':None,'planejados':0,'validos':0,'bloqueados':0,'inconclusivos':0}
    if dados.get('protecao_exigida') is False and evidencia_existe(dados.get('fonte_requisito'),base):
        return dict(saida,status='Não aplicável',motivo='Requisito documentado não exige proteção nesta operação')
    planejados=dados.get('casos_planejados',[])
    if (not isinstance(planejados,list) or len(planejados)<10
        or not all(isinstance(c,str) and c.strip() for c in planejados)
        or len(set(planejados))!=len(planejados)):
        return dict(saida,motivo='Definir ao menos dez casos distintos antes da coleta')
    saida.update(planejados=len(planejados),inconclusivos=len(planejados))
    positivo=dados.get('controle_positivo',{})
    if (dados.get('protecao_exigida') is not True
        or not evidencia_existe(dados.get('fonte_requisito'),base)
        or not isinstance(dados.get('url'),str) or not dados['url'].startswith('https://')
        or dados.get('metodo') not in ('GET','POST','PUT','PATCH','DELETE')
        or dados.get('payload_validado') is not True
        or positivo.get('operacao_confirmada') is not True
        or type(positivo.get('status_http')) is not int or not 200<=positivo['status_http']<300
        or not evidencia_existe(positivo.get('evidencia'),base)):
        return dict(saida,motivo='Alvo, requisito, payload ou controle positivo não demonstrados')
    casos=dados.get('casos',[])
    if not isinstance(casos,list) or any(not isinstance(c,dict) for c in casos):
        return dict(saida,motivo='Lista de casos inválida')
    ids=[c.get('id') for c in casos]
    if any(i not in planejados for i in ids) or len(set(ids))!=len(ids):
        return dict(saida,motivo='Caso desconhecido ou repetido; registrar repetições em outra execução')
    acessos=0
    for caso in casos:
        status=caso.get('status_http')
        if (caso.get('condicao_validada') is not True
            or not evidencia_existe(caso.get('evidencia'),base)
            or type(status) is not int):
            continue
        if status in (401,403):
            saida['validos']+=1
            saida['bloqueados']+=1
        elif caso.get('execucao_indevida_comprovada') is True:
            saida['validos']+=1
            acessos+=1
    saida['inconclusivos']=saida['planejados']-saida['validos']
    if saida['validos']:
        saida['tbr']=100*saida['bloqueados']/saida['validos']
    if acessos:
        saida['status']='Não conforme (Crítico)'
    elif saida['validos']==saida['planejados']:
        saida['status']='Conforme'
    saida['motivo']='404/405/erros e respostas sem prova de execução indevida não demonstram acesso; cobertura parcial não aprova a bateria.'
    return saida


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('relatorio',type=Path)
    args=parser.parse_args()
    try:
        resultado=analisar(json.loads(args.relatorio.read_text()),args.relatorio.parent)
    except (OSError,ValueError,TypeError,KeyError,AttributeError) as exc:
        resultado={'status':'Inconclusivo','tbr':None,'motivo':str(exc)}
    print(json.dumps(resultado,ensure_ascii=False,indent=2))
    return 2 if resultado['status']=='Inconclusivo' else 0


if __name__=='__main__':
    raise SystemExit(main())
