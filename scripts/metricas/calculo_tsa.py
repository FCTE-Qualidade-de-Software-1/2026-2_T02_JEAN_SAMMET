from dataclasses import dataclass
from datetime import datetime

from .configuracao import EVENTOS_DE_ATIVIDADE
from .estado_issue import esta_aberta_em
from .modelos import Issue
from .tempo import dias_entre


@dataclass(frozen=True)
class SemAtividadeDaIssue:
    numero: int
    titulo: str
    url: str
    ultima_atividade: datetime
    dias: float
    acima_do_limite: bool


@dataclass(frozen=True)
class ResultadoTsa:
    itens: tuple[SemAtividadeDaIssue, ...]
    maior_dias: float | None


def ultima_atividade(issue: Issue, referencia: datetime) -> datetime:
    candidatos = [
        evento.criado_em
        for evento in issue.eventos
        if evento.tipo in EVENTOS_DE_ATIVIDADE
        and not evento.automacao
        and evento.criado_em <= referencia
    ]
    return max(candidatos, default=issue.aberta_em)


def calcular_tsa(issues, referencia: datetime, limite_dias: float) -> ResultadoTsa:
    itens = []
    for issue in issues:
        if not esta_aberta_em(issue, referencia):
            continue
        atividade = ultima_atividade(issue, referencia)
        dias = dias_entre(atividade, referencia)
        itens.append(
            SemAtividadeDaIssue(
                numero=issue.numero,
                titulo=issue.titulo,
                url=issue.url,
                ultima_atividade=atividade,
                dias=dias,
                acima_do_limite=dias > limite_dias,
            )
        )
    maior = max((item.dias for item in itens), default=None)
    return ResultadoTsa(tuple(itens), maior)
