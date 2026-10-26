from datetime import date, datetime, timedelta, timezone

from .configuracao import FUSO


def ler_instante(texto: str) -> datetime:
    return datetime.fromisoformat(texto.replace("Z", "+00:00")).astimezone(timezone.utc)


def instante_atual() -> datetime:
    return datetime.now(timezone.utc)


def fim_do_dia(texto: str) -> datetime:
    dia = ler_instante(texto).date()
    return datetime(dia.year, dia.month, dia.day, 23, 59, 59, tzinfo=FUSO).astimezone(timezone.utc)


def fim_do_dia_local(dia: date) -> datetime:
    return datetime(dia.year, dia.month, dia.day, 23, 59, 59, tzinfo=FUSO).astimezone(timezone.utc)


def dia_local(instante: datetime) -> date:
    return instante.astimezone(FUSO).date()


def dias_entre(inicio: datetime, fim: datetime) -> float:
    return (fim - inicio).total_seconds() / 86400


def sequencia_de_dias(inicio: date, fim: date) -> list[date]:
    quantidade = (fim - inicio).days
    return [inicio + timedelta(days=indice) for indice in range(quantidade + 1)]
