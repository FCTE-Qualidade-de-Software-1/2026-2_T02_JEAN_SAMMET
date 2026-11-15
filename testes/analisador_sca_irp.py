#!/usr/bin/env python3
"""Script de análise automatizada de relatórios SCA (npm audit --json) para cálculo do IRP.

Métrica: MET-OP-02 (Densidade de Vulnerabilidades Conhecidas em Dependências - DVCD)
Processo: ISO/IEC 25040:2011/2024 — Fase 3 / Fase 4
Fórmula:
    IRP = (10 * N_critica) + (5 * N_alta) + (2 * N_moderada) + (1 * N_baixa)
"""

import json
import os
import sys
from typing import Dict, Any, Tuple


PESOS_SEVERIDADE = {
    "critical": 10,
    "high": 5,
    "moderate": 2,
    "low": 1,
    "info": 0
}


def extrair_vulnerabilidades_npm(caminho_arquivo: str) -> Dict[str, int]:
    """Lê um arquivo JSON gerado por `npm audit --json` e extrai contagens por severidade."""
    if not os.path.exists(caminho_arquivo):
        print(f"[AVISO] Arquivo não encontrado: {caminho_arquivo}", file=sys.stderr)
        return {"critical": 0, "high": 0, "moderate": 0, "low": 0}

    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        dados: Dict[str, Any] = json.load(f)

    # Suporte para formato npm audit v7+ (campo 'metadata' -> 'vulnerabilities')
    if "metadata" in dados and "vulnerabilities" in dados["metadata"]:
        vulns = dados["metadata"]["vulnerabilities"]
        return {
            "critical": int(vulns.get("critical", 0)),
            "high": int(vulns.get("high", 0)),
            "moderate": int(vulns.get("moderate", 0)),
            "low": int(vulns.get("low", 0)),
        }
    
    # Suporte para formato alternativo (npm audit v6)
    if "vulnerabilities" in dados and isinstance(dados["vulnerabilities"], dict):
        contagens = {"critical": 0, "high": 0, "moderate": 0, "low": 0}
        for item in dados["vulnerabilities"].values():
            sev = item.get("severity", "low").lower()
            if sev in contagens:
                contagens[sev] += 1
        return contagens

    return {"critical": 0, "high": 0, "moderate": 0, "low": 0}


def calcular_irp(contagens: Dict[str, int]) -> int:
    """Calcula o Índice de Risco Ponderado (IRP)."""
    return (
        (contagens.get("critical", 0) * PESOS_SEVERIDADE["critical"]) +
        (contagens.get("high", 0) * PESOS_SEVERIDADE["high"]) +
        (contagens.get("moderate", 0) * PESOS_SEVERIDADE["moderate"]) +
        (contagens.get("low", 0) * PESOS_SEVERIDADE["low"])
    )


def julgar_irp(contagens_totais: Dict[str, int], irp_total: int) -> Tuple[str, str]:
    """Julga o resultado segundo os critérios da Fase 2 (MET-OP-02)."""
    criticas = contagens_totais.get("critical", 0)
    altas = contagens_totais.get("high", 0)

    if criticas == 0 and altas == 0 and irp_total <= 5:
        return "Excelente", "Refuta a hipótese H-OP-02 (Alta integridade de dependências)."
    elif criticas == 0 and altas <= 2 and irp_total <= 20:
        return "Aceitável", "Vulnerabilidades residuais em devDependencies; risco moderado."
    else:
        return "Crítico", "Confirma a hipótese H-OP-02 (Vulnerabilidades severas requerem intervenção imediata na Fase 4)."


def main():
    pasta_evidencias = os.path.join(os.path.dirname(__file__), "evidencias", "seguranca", "sca")
    arquivo_backend = os.path.join(pasta_evidencias, "audit-backend.json")
    arquivo_frontend = os.path.join(pasta_evidencias, "audit-frontend.json")

    # Permite passar arquivos via linha de comando
    if len(sys.argv) >= 3:
        arquivo_backend = sys.argv[1]
        arquivo_frontend = sys.argv[2]

    print("=================================================================")
    print("  ANÁLISE DE COMPOSIÇÃO DE SOFTWARE (SCA) — MÉTRICA MET-OP-02    ")
    print("=================================================================")

    vulns_backend = extrair_vulnerabilidades_npm(arquivo_backend)
    vulns_frontend = extrair_vulnerabilidades_npm(arquivo_frontend)

    irp_backend = calcular_irp(vulns_backend)
    irp_frontend = calcular_irp(vulns_frontend)

    totais = {
        k: vulns_backend.get(k, 0) + vulns_frontend.get(k, 0)
        for k in ["critical", "high", "moderate", "low"]
    }
    irp_total = irp_backend + irp_frontend
    status, mensagem = julgar_irp(totais, irp_total)

    print("\n--- Relatório de Vulnerabilidades por Módulo ---")
    print(f"{'Módulo':<15} | {'Crítica':<8} | {'Alta':<8} | {'Moderada':<8} | {'Baixa':<8} | {'IRP':<6}")
    print("-" * 65)
    print(f"{'Backend':<15} | {vulns_backend['critical']:<8} | {vulns_backend['high']:<8} | {vulns_backend['moderate']:<8} | {vulns_backend['low']:<8} | {irp_backend:<6}")
    print(f"{'Frontend':<15} | {vulns_frontend['critical']:<8} | {vulns_frontend['high']:<8} | {vulns_frontend['moderate']:<8} | {vulns_frontend['low']:<8} | {irp_frontend:<6}")
    print("-" * 65)
    print(f"{'Consolidado':<15} | {totais['critical']:<8} | {totais['high']:<8} | {totais['moderate']:<8} | {totais['low']:<8} | {irp_total:<6}")

    print("\n--- Julgamento da Qualidade (Fase 2 -> Fase 4) ---")
    print(f"Status Final:  {status.upper()}")
    print(f"Interpretação: {mensagem}")
    print("=================================================================\n")


if __name__ == "__main__":
    main()

