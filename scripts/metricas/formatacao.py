from datetime import datetime

from .configuracao import FUSO

NAO_APLICAVEL = "Não aplicável"


def decimal(valor: float, casas: int) -> str:
    return f"{valor:.{casas}f}".replace(".", ",")


def percentual(valor: float | None) -> str:
    if valor is None:
        return NAO_APLICAVEL
    return decimal(valor, 2) + "%"


def dias(valor: float | None) -> str:
    if valor is None:
        return NAO_APLICAVEL
    return decimal(valor, 1) + " dias"


def data(instante: datetime | None) -> str:
    if instante is None:
        return "Sem prazo definido"
    return instante.astimezone(FUSO).strftime("%d/%m/%Y")


def data_hora(instante: datetime | None) -> str:
    if instante is None:
        return "Sem prazo definido"
    return instante.astimezone(FUSO).strftime("%d/%m/%Y %H:%M")
