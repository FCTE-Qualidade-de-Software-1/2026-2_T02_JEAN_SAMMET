from dataclasses import dataclass
from datetime import datetime

from .estado_issue import concluida_em
from .modelos import Issue
from .tempo import dias_entre


@dataclass(frozen=True)
class CicloDaIssue:
    numero: int
    titulo: str
    url: str
    aberta_em: datetime
    concluida_em: datetime
    dias: float


@dataclass(frozen=True)
class ResultadoCiclo:
    itens: tuple[CicloDaIssue, ...]
    media_dias: float | None


def calcular_ciclo(issues, referencia: datetime) -> ResultadoCiclo:
    itens = []
    for issue in issues:
        conclusao = concluida_em(issue, referencia)
        if conclusao is None:
            continue
        itens.append(
            CicloDaIssue(
                numero=issue.numero,
                titulo=issue.titulo,
                url=issue.url,
                aberta_em=issue.aberta_em,
                concluida_em=conclusao,
                dias=dias_entre(issue.aberta_em, conclusao),
            )
        )
    media = sum(item.dias for item in itens) / len(itens) if itens else None
    return ResultadoCiclo(tuple(itens), media)
