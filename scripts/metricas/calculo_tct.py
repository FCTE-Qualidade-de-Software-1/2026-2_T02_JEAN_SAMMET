from dataclasses import dataclass
from datetime import datetime

from .estado_issue import esta_aberta_em
from .modelos import Issue


@dataclass(frozen=True)
class ResultadoTct:
    planejadas: int
    concluidas: int
    adicionadas: int
    adicionadas_concluidas: int
    tct: float | None


def contar_concluidas(issues, referencia: datetime) -> int:
    return sum(1 for issue in issues if not esta_aberta_em(issue, referencia))


def calcular_tct(planejadas: tuple[Issue, ...], adicionadas: tuple[Issue, ...], referencia: datetime) -> ResultadoTct:
    concluidas = contar_concluidas(planejadas, referencia)
    tct = concluidas / len(planejadas) * 100 if planejadas else None
    return ResultadoTct(
        planejadas=len(planejadas),
        concluidas=concluidas,
        adicionadas=len(adicionadas),
        adicionadas_concluidas=contar_concluidas(adicionadas, referencia),
        tct=tct,
    )
