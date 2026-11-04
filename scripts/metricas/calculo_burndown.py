from dataclasses import dataclass
from datetime import date, datetime

from .estado_issue import esta_aberta_em
from .modelos import Issue
from .tempo import dia_local, fim_do_dia_local, sequencia_de_dias


@dataclass(frozen=True)
class PontoBurndown:
    dia: date
    restantes: int | None
    ideal: float | None


def ultimo_dia_do_grafico(
    prazo: datetime | None,
    referencia: datetime,
    primeiro: date,
    encerrado: bool = False,
    data_fim: date | None = None,
) -> date:
    dia_referencia = dia_local(referencia)
    if data_fim is not None:
        # Mantém o eixo até o prazo configurado, mesmo quando ele ainda é futuro.
        return max(data_fim, primeiro)
    if prazo is None:
        return max(dia_referencia, primeiro)
    dia_prazo = dia_local(prazo)
    if encerrado:
        return max(min(dia_prazo, dia_referencia), primeiro)
    return max(dia_prazo, dia_referencia, primeiro)


def valor_ideal(total: int, deslocamento: int, duracao: int | None) -> float | None:
    if duracao is None:
        return None
    if duracao <= 0:
        return 0.0
    return total * (1 - min(deslocamento, duracao) / duracao)


def contar_restantes(planejadas: tuple[Issue, ...], dia: date, referencia: datetime) -> int | None:
    if dia > dia_local(referencia):
        return None
    momento = min(fim_do_dia_local(dia), referencia)
    return sum(1 for issue in planejadas if esta_aberta_em(issue, momento))


def calcular_burndown(
    planejadas: tuple[Issue, ...],
    inicio: datetime | None,
    prazo: datetime | None,
    referencia: datetime,
    encerrado: bool = False,
    data_fim: date | None = None,
) -> tuple[PontoBurndown, ...]:
    if inicio is None or not planejadas:
        return ()
    primeiro = dia_local(inicio)
    ultimo = ultimo_dia_do_grafico(prazo, referencia, primeiro, encerrado, data_fim)
    dias = sequencia_de_dias(primeiro, ultimo)
    fim_planejado = data_fim or (dia_local(prazo) if prazo is not None else None)
    duracao = (fim_planejado - primeiro).days if fim_planejado is not None else None
    return tuple(
        PontoBurndown(
            dia=dia,
            restantes=contar_restantes(planejadas, dia, referencia),
            ideal=valor_ideal(len(planejadas), (dia - primeiro).days, duracao),
        )
        for dia in dias
    )
