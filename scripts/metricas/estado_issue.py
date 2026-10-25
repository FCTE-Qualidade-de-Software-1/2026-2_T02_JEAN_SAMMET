from datetime import datetime

from .configuracao import EVENTOS_DE_ESTADO
from .modelos import Issue


def possui_historico_de_estado(issue: Issue) -> bool:
    return any(evento.tipo in EVENTOS_DE_ESTADO for evento in issue.eventos)


def eventos_de_estado_ate(issue: Issue, instante: datetime):
    selecionados = [
        evento
        for evento in issue.eventos
        if evento.tipo in EVENTOS_DE_ESTADO and evento.criado_em <= instante
    ]
    return sorted(selecionados, key=lambda evento: evento.criado_em)


def esta_aberta_em(issue: Issue, instante: datetime) -> bool:
    if not possui_historico_de_estado(issue):
        return issue.fechada_em is None or instante < issue.fechada_em
    aberta = True
    for evento in eventos_de_estado_ate(issue, instante):
        aberta = evento.tipo == "reopened"
    return aberta


def concluida_em(issue: Issue, instante: datetime) -> datetime | None:
    if esta_aberta_em(issue, instante):
        return None
    if not possui_historico_de_estado(issue):
        return issue.fechada_em
    fechamentos = [
        evento.criado_em
        for evento in eventos_de_estado_ate(issue, instante)
        if evento.tipo == "closed"
    ]
    return max(fechamentos)
