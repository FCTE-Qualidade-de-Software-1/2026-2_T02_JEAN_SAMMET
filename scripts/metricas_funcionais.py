#!/usr/bin/env python3
"""Processa os registros brutos das métricas funcionais da Fase 4.

A fonte é testes/evidencias/funcionais/verificacoes_funcionais.csv.
Somente verificações com conforme=0/1, evidência e referência identificadas
compõem os cálculos. MET-FUN-03/04/05 exigem cobertura integral dos universos
H0 (15/44/8); as demais usam as unidades aplicáveis efetivamente verificadas.
Registros ausentes nunca são convertidos em 0%.

Uso:
    python3 scripts/metricas_funcionais.py
    python3 scripts/metricas_funcionais.py --csv caminho/arquivo.csv
    python3 scripts/metricas_funcionais.py --json
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CSV_PADRAO = ROOT / "testes/evidencias/funcionais/verificacoes_funcionais.csv"
H0_JSON = ROOT / "testes/referencias/h0_sanitizado.json"

COLUNAS_OBRIGATORIAS = {
    "execucao_id",
    "caso",
    "metrica",
    "entrada_id",
    "cenario_id",
    "fonte_vigencia",
    "conforme",
    "evidencia",
}

METRICAS: dict[str, dict[str, str]] = {
    "MET-FUN-01": {
        "nome": "Violações de pré-requisitos (TVP)",
        "formula": "(NVP / NRP) × 100",
        "direcao": "zero",
        "meta": "0%",
        "casos": "CT-01",
        "numerador": "relações violadas",
        "denominador": "relações aplicáveis verificadas",
    },
    "MET-FUN-02": {
        "nome": "Violações de co-requisitos (TVC)",
        "formula": "(NVC / NRC) × 100",
        "direcao": "zero",
        "meta": "0%",
        "casos": "CT-02",
        "numerador": "relações violadas",
        "denominador": "relações aplicáveis verificadas",
    },
    "MET-FUN-03": {
        "nome": "Cobertura de obrigatórias pendentes (CDO)",
        "formula": "(DPC / DOP) × 100",
        "direcao": "cem",
        "meta": "100%",
        "casos": "CT-03",
        "numerador": "disciplinas pendentes contempladas",
        "denominador": "obrigatórias pendentes aplicáveis",
    },
    "MET-FUN-04": {
        "nome": "Divergências no tratamento do histórico (TDH)",
        "formula": "(NDH / NVH) × 100",
        "direcao": "zero",
        "meta": "0%",
        "casos": "CT-04",
        "numerador": "divergências confirmadas",
        "denominador": "verificações válidas de status",
    },
    "MET-FUN-05": {
        "nome": "Aplicação incorreta de equivalências (TAE)",
        "formula": "(NEI / NRE) × 100",
        "direcao": "zero",
        "meta": "0%",
        "casos": "CT-05",
        "numerador": "aplicações incorretas",
        "denominador": "relações de equivalência aplicáveis verificadas",
    },
    "MET-FUN-06": {
        "nome": "Conformidade das opções do onboarding (COO)",
        "formula": "(NEC / NEV) × 100",
        "direcao": "cem",
        "meta": "100%",
        "casos": "CT-06",
        "numerador": "expectativas atendidas",
        "denominador": "expectativas válidas previamente especificadas e testadas",
    },
    "MET-FUN-07": {
        "nome": "Violações de restrições semestrais (TVS)",
        "formula": "(NVS / NRS) × 100, por tipo de restrição",
        "direcao": "zero",
        "meta": "0% por tipo",
        "casos": "CT-07",
        "numerador": "violações confirmadas",
        "denominador": "verificações válidas por tipo de restrição",
    },
}

QUESTOES: dict[str, list[str]] = {
    "Q-FUN-01": ["MET-FUN-01"],
    "Q-FUN-02": ["MET-FUN-02"],
    "Q-FUN-03": ["MET-FUN-03", "MET-FUN-05"],
    "Q-FUN-04": ["MET-FUN-04"],
    "Q-FUN-05": ["MET-FUN-05"],
    "Q-FUN-06": ["MET-FUN-06"],
    "Q-FUN-07": ["MET-FUN-07"],
}


def _normalizar(valor: str) -> str:
    valor = unicodedata.normalize("NFKD", valor.strip().lower())
    return "".join(c for c in valor if not unicodedata.combining(c))


def _interpretar_conforme(valor: str) -> int | str | None:
    normalizado = _normalizar(valor)
    if normalizado in {"1", "sim", "true", "conforme", "atendido", "atendida"}:
        return 1
    if normalizado in {"0", "nao", "false", "nao conforme", "violado", "violada", "omitido", "omitida"}:
        return 0
    if normalizado in {"inconclusivo", "falha de coleta", "erro de coleta"}:
        return "inconclusivo"
    if normalizado in {"na", "n/a", "nao aplicavel"}:
        return "nao_aplicavel"
    if normalizado in {"pendente", "pendente de execucao", "pendente de especificacao", ""}:
        return None
    return "invalido"


def _avaliar_grupo_generico(metric_id: str, rows: list[dict[str, Any]]) -> dict[str, Any]:
    config = METRICAS[metric_id]
    valid = [row for row in rows if row["conforme_valor"] in (0, 1)]
    not_classified = len(rows) - len(valid)
    inconclusive_count = sum(row["conforme_valor"] == "inconclusivo" for row in rows)
    not_applicable_count = sum(row["conforme_valor"] == "nao_aplicavel" for row in rows)
    denominator = len(valid)

    result: dict[str, Any] = {
        "metrica": metric_id,
        "nome": config["nome"],
        "formula": config["formula"],
        "meta": config["meta"],
        "casos": config["casos"],
        "registros_recebidos": len(rows),
        "verificacoes_validas": denominator,
        "registros_sem_classificacao": not_classified,
        "valor_percentual": None,
        "numerador": None,
        "denominador": denominator,
        "status": "Pendente de execução",
    }

    if denominator == 0:
        if inconclusive_count:
            result["status"] = "Inconclusivo — falha de coleta registrada"
        elif rows and not_applicable_count == len(rows):
            result["status"] = "Não aplicável — justificar a regra em observacao"
        return result

    conformes = sum(row["conforme_valor"] == 1 for row in valid)
    nao_conformes = denominator - conformes

    if config["direcao"] == "zero":
        numerator = nao_conformes
        value = numerator / denominator * 100
        status = "Conforme" if numerator == 0 else "Não conforme"
    else:
        numerator = conformes
        value = numerator / denominator * 100
        status = "Conforme" if numerator == denominator else "Não conforme"

    result.update(
        {
            "numerador": numerator,
            "denominador": denominator,
            "valor_percentual": round(value, 4),
            "status": status,
        }
    )
    if not_classified:
        result["status"] += " — cobertura parcial"
    return result



def _carregar_unidades_referencia() -> dict[str, tuple[str, set[str]]]:
    """Carrega as unidades obrigatórias de CT-03, CT-04 e CT-05 diretamente de H0."""
    dados = json.loads(H0_JSON.read_text(encoding="utf-8"))
    obrigatorias = {
        item["codigo"]
        for item in dados["obrigacoes_pendentes_sigaa"]["disciplinas_obrigatorias_pendentes"]
        if item.get("tipo") == "disciplina_obrigatoria" and item.get("codigo")
    }
    componentes = {
        item["registro_id"]
        for item in dados["registros_academicos"]
        if item.get("registro_id")
    }
    equivalencias = dados["equivalencias_obrigatorias_concluidas"] + dados["equivalencias_obrigatorias_em_andamento"]
    relacoes = {
        f'{item["componente_aproveitado"]}->{item["obrigatoria_destino"]}'
        for item in equivalencias
    }
    return {
        "MET-FUN-03": ("disciplina", obrigatorias),
        "MET-FUN-04": ("registro_id", componentes),
        "MET-FUN-05": ("relacao", relacoes),
    }


def _avaliar_grupo_com_referencia(
    metric_id: str,
    rows: list[dict[str, Any]],
    campo_unidade: str,
    unidades_esperadas: set[str],
    avisos: list[str],
) -> dict[str, Any]:
    """Exige cobertura integral das unidades H0 para evitar percentuais inflados por amostra parcial."""
    por_unidade: dict[str, list[dict[str, Any]]] = defaultdict(list)
    extras: set[str] = set()
    for row in rows:
        unidade = str(row["registro"].get(campo_unidade, "")).strip()
        if unidade not in unidades_esperadas:
            extras.add(unidade or "(vazio)")
            continue
        por_unidade[unidade].append(row)

    duplicadas = {unidade for unidade, itens in por_unidade.items() if len(itens) != 1}
    ausentes = unidades_esperadas - set(por_unidade)
    validas: dict[str, dict[str, Any]] = {
        unidade: itens[0]
        for unidade, itens in por_unidade.items()
        if len(itens) == 1 and itens[0]["conforme_valor"] in (0, 1)
    }
    sem_classificacao = {
        unidade
        for unidade, itens in por_unidade.items()
        if len(itens) == 1 and itens[0]["conforme_valor"] not in (0, 1)
    }
    inconclusivas = {
        unidade
        for unidade, itens in por_unidade.items()
        if any(item["conforme_valor"] == "inconclusivo" for item in itens)
    }
    if extras:
        avisos.append(
            f"{metric_id}: unidades fora da referência H0 ignoradas em {campo_unidade}: "
            + ", ".join(sorted(extras))
        )
    if duplicadas:
        avisos.append(
            f"{metric_id}: unidades duplicadas impedem o fechamento: "
            + ", ".join(sorted(duplicadas))
        )

    referencia = len(unidades_esperadas)
    cobertura_completa = (
        len(validas) == referencia
        and not duplicadas
        and not ausentes
        and not sem_classificacao
    )
    base = _avaliar_grupo_generico(metric_id, list(validas.values()))
    base.update(
        {
            "registros_recebidos": len(rows),
            "verificacoes_validas": len(validas),
            "registros_sem_classificacao": len(sem_classificacao),
            "denominador": referencia,
            "unidades_referencia": referencia,
            "unidades_observadas": len(por_unidade),
            "unidades_ausentes": sorted(ausentes),
            "unidades_duplicadas": sorted(duplicadas),
            "unidades_sem_classificacao": sorted(sem_classificacao),
            "cobertura_referencia_percentual": round(len(validas) / referencia * 100, 2) if referencia else None,
        }
    )

    if not cobertura_completa:
        tem_violacao = any(item["conforme_valor"] == 0 for item in validas.values())
        if tem_violacao:
            base["status"] = "Não conforme — cobertura incompleta"
        elif inconclusivas:
            base["status"] = "Inconclusivo — cobertura incompleta"
        else:
            base["status"] = f"Pendente — cobertura {len(validas)}/{referencia}"
        # Não há percentual final enquanto cada unidade de referência não tiver
        # exatamente uma verificação válida e rastreável.
        base["numerador"] = None
        base["valor_percentual"] = None
        return base

    # A cobertura está completa: o denominador é o universo H0, não o número
    # acidental de linhas recebidas.
    conformes = sum(item["conforme_valor"] == 1 for item in validas.values())
    nao_conformes = referencia - conformes
    config = METRICAS[metric_id]
    numerador = nao_conformes if config["direcao"] == "zero" else conformes
    valor = numerador / referencia * 100
    base.update(
        {
            "numerador": numerador,
            "denominador": referencia,
            "valor_percentual": round(valor, 4),
            "status": "Conforme" if (numerador == 0 if config["direcao"] == "zero" else numerador == referencia) else "Não conforme",
        }
    )
    return base


def _avaliar_grupo(
    metric_id: str,
    rows: list[dict[str, Any]],
    referencias: dict[str, tuple[str, set[str]]],
    avisos: list[str],
) -> dict[str, Any]:
    if metric_id in referencias:
        campo, unidades = referencias[metric_id]
        return _avaliar_grupo_com_referencia(metric_id, rows, campo, unidades, avisos)
    return _avaliar_grupo_generico(metric_id, rows)

def processar_registros(registros: list[dict[str, str]]) -> dict[str, Any]:
    agrupados: dict[str, list[dict[str, Any]]] = defaultdict(list)
    avisos: list[str] = []
    ignorados = 0

    for numero, registro in enumerate(registros, start=2):
        metric_id = registro.get("metrica", "").strip().upper()
        if metric_id not in METRICAS:
            if metric_id:
                avisos.append(f"Linha {numero}: métrica desconhecida '{metric_id}' — ignorada.")
            ignorados += 1
            continue

        conforme_texto = registro.get("conforme", "")
        conforme_valor = _interpretar_conforme(conforme_texto)
        faltantes = [
            campo
            for campo in ("execucao_id", "caso", "cenario_id", "fonte_vigencia", "evidencia")
            if not registro.get(campo, "").strip()
        ]
        if faltantes:
            avisos.append(
                f"Linha {numero}: {metric_id} sem {', '.join(faltantes)} — não compõe o denominador."
            )
            ignorados += 1
            continue

        entrada_id = registro.get("entrada_id", "").strip().upper()
        if entrada_id != "H0":
            avisos.append(f"Linha {numero}: entrada '{entrada_id}' diferente de H0 — registro ignorado.")
            ignorados += 1
            continue

        caso_esperado = METRICAS[metric_id]["casos"]
        if registro.get("caso", "").strip().upper() != caso_esperado:
            avisos.append(
                f"Linha {numero}: {metric_id} deve estar associado a {caso_esperado}; registro ignorado."
            )
            ignorados += 1
            continue

        if conforme_valor == "invalido":
            avisos.append(f"Linha {numero}: valor de conforme não reconhecido '{conforme_texto}' — tratado como pendente.")
            conforme_valor = None

        agrupados[metric_id].append({"conforme_valor": conforme_valor, "registro": registro})

    resultados_metricas: dict[str, Any] = {}
    referencias = _carregar_unidades_referencia()
    for metric_id in METRICAS:
        rows = agrupados.get(metric_id, [])
        if metric_id != "MET-FUN-07":
            resultados_metricas[metric_id] = _avaliar_grupo(metric_id, rows, referencias, avisos)
            continue

        # A especificação exige resultado por tipo quando a unidade ou a fonte
        # da restrição diferir. O campo `relacao` identifica esse agrupamento.
        por_tipo: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for row in rows:
            tipo = row["registro"].get("relacao", "").strip() or "tipo não informado"
            por_tipo[tipo].append(row)
        grupos = {
            tipo: _avaliar_grupo_generico(metric_id, tipo_rows)
            for tipo, tipo_rows in sorted(por_tipo.items())
        }
        detailed_statuses = [item["status"] for item in grupos.values()]
        statuses = [status.split(" — ")[0] for status in detailed_statuses]
        aplicaveis = [status for status in statuses if status != "Não aplicável"]
        tem_cobertura_parcial = any("cobertura parcial" in status.lower() for status in detailed_statuses)
        if not grupos:
            status_global = "Pendente de execução"
        elif not aplicaveis:
            status_global = "Não aplicável — justificar a regra em cada tipo"
        elif "Não conforme" in aplicaveis:
            status_global = "Não conforme" if all(s in {"Conforme", "Não conforme", "Não aplicável"} for s in statuses) and not tem_cobertura_parcial else "Não conforme — cobertura parcial"
        elif all(s == "Conforme" for s in aplicaveis):
            if tem_cobertura_parcial:
                status_global = "Conforme — cobertura parcial"
            else:
                status_global = "Conforme" if len(aplicaveis) == len(statuses) else "Conforme — há tipos não aplicáveis"
        elif any(s.startswith("Inconclusivo") for s in statuses):
            status_global = "Inconclusivo — cobertura incompleta"
        else:
            status_global = "Pendente — cobertura incompleta"
        resultados_metricas[metric_id] = {
            "metrica": metric_id,
            "nome": METRICAS[metric_id]["nome"],
            "formula": METRICAS[metric_id]["formula"],
            "meta": METRICAS[metric_id]["meta"],
            "casos": METRICAS[metric_id]["casos"],
            "status": status_global,
            "por_tipo": grupos,
            "valor_percentual": None,
            "numerador": None,
            "denominador": None,
        }

    respostas: dict[str, dict[str, Any]] = {}
    for question_id, metric_ids in QUESTOES.items():
        metric_statuses: list[str] = []
        for metric_id in metric_ids:
            result = resultados_metricas[metric_id]
            metric_statuses.append(result["status"])

        has_failure = any(status.startswith("Não conforme") for status in metric_statuses)
        applicable_statuses = [status for status in metric_statuses if not status.startswith("Não aplicável")]
        all_pass = bool(applicable_statuses) and all(status == "Conforme" for status in applicable_statuses)
        all_not_applicable = bool(metric_statuses) and not applicable_statuses
        any_inconclusive = any(status.startswith("Inconclusivo") for status in metric_statuses)
        any_pending = any("Pendente" in status for status in metric_statuses)
        any_partial = any(
            "cobertura parcial" in status.lower() or "cobertura incompleta" in status.lower()
            for status in metric_statuses
        )

        if all_not_applicable:
            answer_status = "Não aplicável — justificar a regra"
        elif all_pass and not any_pending and not any_inconclusive and not any_partial:
            answer_status = "Conforme"
        elif has_failure:
            answer_status = (
                "Não conforme — resultado parcial"
                if any_pending or any_inconclusive or any_partial
                else "Não conforme"
            )
        elif any_inconclusive:
            answer_status = "Inconclusivo"
        elif all_pass or (all(status.startswith("Conforme") for status in applicable_statuses) and any_partial):
            answer_status = "Conforme — cobertura parcial"
        else:
            answer_status = "Pendente — cobertura/execução incompleta"

        respostas[question_id] = {
            "metricas": metric_ids,
            "status": answer_status,
            "resposta_formal": (
                "As métricas aplicáveis atendem às metas registradas."
                if answer_status == "Conforme"
                else "Não é possível concluir favoravelmente com a cobertura disponível; consultar os registros pendentes e as evidências por métrica."
            ),
        }

    return {
        "fonte": str(CSV_PADRAO),
        "total_registros_lidos": len(registros),
        "registros_ignorados": ignorados,
        "metricas": resultados_metricas,
        "questoes": respostas,
        "avisos": avisos,
    }


def carregar_csv(caminho: Path) -> list[dict[str, str]]:
    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo de coleta não encontrado: {caminho}")
    with caminho.open("r", encoding="utf-8-sig", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        campos = set(leitor.fieldnames or [])
        ausentes = sorted(COLUNAS_OBRIGATORIAS - campos)
        if ausentes:
            raise ValueError("Cabeçalho incompleto; faltam: " + ", ".join(ausentes))
        return list(leitor)


def _formatar_percentual(valor: float | None) -> str:
    if valor is None:
        return "—"
    return f"{valor:.2f}%".replace(".", ",")


def imprimir_markdown(resultado: dict[str, Any]) -> None:
    print("# Processamento das Métricas Funcionais\n")
    print(f"Registros lidos: **{resultado['total_registros_lidos']}**; registros ignorados: **{resultado['registros_ignorados']}**.\n")
    print("| Métrica | Numerador | Denominador | Valor | Meta | Julgamento |")
    print("| :--- | ---: | ---: | ---: | :---: | :--- |")
    for metric_id, item in resultado["metricas"].items():
        if metric_id == "MET-FUN-07":
            groups = item.get("por_tipo", {})
            if not groups:
                print(f"| `{metric_id}` | — | — | — | {item['meta']} | {item['status']} |")
            else:
                for tipo, sub in groups.items():
                    print(
                        f"| `{metric_id}` / {tipo} | {sub['numerador'] if sub['numerador'] is not None else '—'} "
                        f"| {sub['denominador']} | {_formatar_percentual(sub['valor_percentual'])} "
                        f"| {item['meta']} | {sub['status']} |"
                    )
            continue
        print(
            f"| `{metric_id}` | {item['numerador'] if item['numerador'] is not None else '—'} "
            f"| {item['denominador']} | {_formatar_percentual(item['valor_percentual'])} "
            f"| {item['meta']} | {item['status']} |"
        )

    print("\n## Respostas GQM\n")
    for question_id, item in resultado["questoes"].items():
        print(f"- **{question_id} — {item['status']}:** {item['resposta_formal']}")
    if resultado["avisos"]:
        print("\n## Avisos de qualidade dos registros\n")
        for aviso in resultado["avisos"]:
            print(f"- {aviso}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", type=Path, default=CSV_PADRAO, help="CSV de verificações funcionais")
    parser.add_argument("--json", action="store_true", help="Emite resultado estruturado em JSON")
    args = parser.parse_args(argv)

    try:
        registros = carregar_csv(args.csv)
        resultado = processar_registros(registros)
        resultado["fonte"] = str(args.csv)
    except (OSError, ValueError, csv.Error) as erro:
        print(f"Erro: {erro}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(resultado, ensure_ascii=False, indent=2))
    else:
        imprimir_markdown(resultado)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
