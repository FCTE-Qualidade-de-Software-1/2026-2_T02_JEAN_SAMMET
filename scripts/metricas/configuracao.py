import os
from pathlib import Path
from zoneinfo import ZoneInfo

FUSO = ZoneInfo("America/Sao_Paulo")

META_TCT = 100.0
LIMITE_ALERTA_TCT = 75.0
HORAS_ALERTA_PRAZO = 24.0
META_CICLO_DIAS = 2.0
LIMITE_TSA_DIAS = 3.0
JANELA_LINHA_DE_BASE_HORAS = float(os.environ.get("JANELA_LINHA_DE_BASE_HORAS", "48"))

ROTULO_SEM_ATIVIDADE = "sem-atividade"
COR_ROTULO_SEM_ATIVIDADE = "d93f0b"
DESCRICAO_ROTULO_SEM_ATIVIDADE = "Issue aberta sem atividade acima do limite do TSA"

EVENTOS_DE_ESTADO = frozenset({"closed", "reopened"})

EVENTOS_DE_ATIVIDADE = frozenset(
    {
        "commented",
        "committed",
        "referenced",
        "cross-referenced",
        "connected",
        "assigned",
        "unassigned",
        "moved_columns_in_project",
        "project_v2_item_status_changed",
        "closed",
        "reopened",
    }
)

DIRETORIO_DADOS = Path("docs/gestaoProjeto/dados")
ARQUIVO_PAINEL = Path("docs/gestaoProjeto/painel.md")
