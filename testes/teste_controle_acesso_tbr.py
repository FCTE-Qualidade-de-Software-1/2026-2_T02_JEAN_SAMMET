#!/usr/bin/env python3
"""Script de automação da bateria de 10 testes negativos de controle de acesso para cálculo do TBR.

Métrica: MET-OP-02c (Taxa de Bloqueio em Rotas Não Autenticadas - TBR)
Processo: ISO/IEC 25040:2011/2024 — Fase 3 / Fase 4
Fórmula:
    TBR = (N_bloqueios_corretos / N_requisicoes_teste_invalidas) * 100
"""

import json
import os
import sys
import urllib.request
import urllib.error
from typing import Dict, List, Any, Tuple


DEFAULT_URL = "https://no-fluxo.crianex.com/api/planejamento/gerar-plano"

# Definição dos 10 Casos de Teste Padronizados na Fase 3
CASOS_DE_TESTE = [
    {
        "id": "REQ-01",
        "categoria": "Ausência Total",
        "descricao": "Disparo direto sem cabeçalho Authorization",
        "headers": {"Content-Type": "application/json"}
    },
    {
        "id": "REQ-02",
        "categoria": "Cabeçalho Vazio",
        "descricao": "Cabeçalho presente com string vazia",
        "headers": {"Content-Type": "application/json", "Authorization": ""}
    },
    {
        "id": "REQ-03",
        "categoria": "Esquema Inválido",
        "descricao": "Esquema Basic em endpoint Bearer",
        "headers": {"Content-Type": "application/json", "Authorization": "Basic dXN1YXJpbzoxMjM0NTY="}
    },
    {
        "id": "REQ-04",
        "categoria": "Bearer Sem Token",
        "descricao": "Palavra Bearer sem token anexado",
        "headers": {"Content-Type": "application/json", "Authorization": "Bearer "}
    },
    {
        "id": "REQ-05",
        "categoria": "Token Malformado",
        "descricao": "String alfanumérica arbitrária fora do formato JWT",
        "headers": {"Content-Type": "application/json", "Authorization": "Bearer string_aleatoria_invalida_sem_formato_jwt"}
    },
    {
        "id": "REQ-06",
        "categoria": "JWT com Assinatura Inválida",
        "descricao": "JWT estruturado com assinatura adulterada",
        "headers": {"Content-Type": "application/json", "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.assinatura_falsa_e_invalida"}
    },
    {
        "id": "REQ-07",
        "categoria": "JWT Expirado",
        "descricao": "JWT com expiração retroativa (exp: 1000000000)",
        "headers": {"Content-Type": "application/json", "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0ZSIsImV4cCI6MTAwMDAwMDAwMH0.assinatura_qualquer"}
    },
    {
        "id": "REQ-08",
        "categoria": "JWT sem Assinatura (alg: none)",
        "descricao": "Tentativa de bypass com algoritmo none",
        "headers": {"Content-Type": "application/json", "Authorization": "Bearer eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJzdWIiOiJhZG1pbiJ9."}
    },
    {
        "id": "REQ-09",
        "categoria": "Token com Papel Insuficiente",
        "descricao": "Token simulando perfil convidado/sem permissão",
        "headers": {"Content-Type": "application/json", "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJjb252aWRhZG8iLCJyb2xlIjoiZ3Vlc3QifQ.fake_signature"}
    },
    {
        "id": "REQ-10",
        "categoria": "Origem Cruzada não Autorizada (CORS)",
        "descricao": "Requisição anônima com Origin externa não autorizada",
        "headers": {"Content-Type": "application/json", "Origin": "https://origem-maliciosa-externa.org"}
    }
]

PAYLOAD_TESTE = {
    "matriculaCurricular": "6360/1",
    "semestreAtual": 5,
    "disciplinasConcluidas": ["FGA0168", "MAT0025"]
}


def executar_requisicao(url: str, headers: Dict[str, str], payload: Dict[str, Any]) -> Tuple[int, str]:
    """Envia uma requisição HTTP POST e captura o status retornado."""
    corpo_bytes = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=corpo_bytes, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req, timeout=10) as resposta:
            status = resposta.getcode()
            corpo = resposta.read().decode("utf-8", errors="ignore")[:200]
            return status, corpo
    except urllib.error.HTTPError as e:
        corpo = e.read().decode("utf-8", errors="ignore")[:200]
        return e.code, corpo
    except urllib.error.URLError as e:
        return 0, f"Falha de conexão: {e.reason}"
    except Exception as e:
        return 0, f"Erro inesperado: {str(e)}"


def julgar_tbr(tbr: float) -> Tuple[str, str]:
    """Julga o resultado da métrica TBR segundo os critérios da Fase 2."""
    if tbr >= 100.0:
        return "Conforme (Mandatório)", "Refuta vulnerabilidade de rota (Todas as requisições não autorizadas foram bloqueadas)."
    else:
        return "Não Conforme (Crítico)", "Confirma a hipótese H-OP-02 (Falha grave de controle de acesso; rota acessível sem autenticação)."


def main():
    target_url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_URL

    print("=================================================================")
    print("  TESTE DE CONTROLE DE ACESSO A ROTAS DE API — MÉTRICA MET-OP-02c")
    print(f"  Target URL: {target_url}")
    print("=================================================================\n")

    bloqueios_corretos = 0
    resultados = []

    for caso in CASOS_DE_TESTE:
        caso_id = caso["id"]
        descricao = caso["descricao"]
        headers = caso["headers"]

        status, corpo = executar_requisicao(target_url, headers, PAYLOAD_TESTE)

        # Bloqueio correto = 401 Unauthorized ou 403 Forbidden
        bloqueado = status in [401, 403]
        if bloqueado:
            bloqueios_corretos += 1

        resultados.append({
            "id": caso_id,
            "descricao": descricao,
            "status_http": status,
            "bloqueado": bloqueado,
            "corpo_prev": corpo
        })

        status_str = f"HTTP {status}" if status > 0 else "CONEXÃO FALHOU"
        ind = "[OK - BLOQUEADO]" if bloqueado else "[FALHA - PERMITIDO/ERRO]"
        print(f"[{caso_id}] {descricao:<55} -> {status_str:<12} {ind}")

    total_testes = len(CASOS_DE_TESTE)
    tbr = (bloqueios_corretos / total_testes) * 100.0
    status_julg, desc_julg = julgar_tbr(tbr)

    print("\n-----------------------------------------------------------------")
    print(f"Total de Requisições: {total_testes}")
    print(f"Bloqueios Corretos (401/403): {bloqueios_corretos}")
    print(f"Taxa de Bloqueio em Rotas Não Autenticadas (TBR): {tbr:.1f}%")
    print(f"Status do Julgamento: {status_julg}")
    print(f"Interpretação: {desc_julg}")
    print("-----------------------------------------------------------------\n")

    # Salva log em testes/evidencias/seguranca/api/
    pasta_log = os.path.join(os.path.dirname(__file__), "evidencias", "seguranca", "api")
    os.makedirs(pasta_log, exist_ok=True)
    arquivo_log = os.path.join(pasta_log, "resultado_tbr.log")

    with open(arquivo_log, "w", encoding="utf-8") as f:
        f.write(f"Alvo: {target_url}\n")
        f.write(f"TBR: {tbr:.1f}%\n")
        f.write(f"Status: {status_julg}\n\n")
        for r in resultados:
            f.write(f"{r['id']}: HTTP {r['status_http']} | Bloqueado: {r['bloqueado']} | {r['descricao']}\n")

    print(f"[INFO] Log gravado com sucesso em: {arquivo_log}\n")


if __name__ == "__main__":
    main()

