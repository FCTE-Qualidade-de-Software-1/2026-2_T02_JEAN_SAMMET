from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Evento:
    tipo: str
    criado_em: datetime
    automacao: bool
    marco: str | None


@dataclass(frozen=True)
class Issue:
    numero: int
    titulo: str
    url: str
    aberta_em: datetime
    fechada_em: datetime | None
    rotulos: tuple[str, ...]
    eventos: tuple[Evento, ...]


@dataclass(frozen=True)
class Marco:
    numero: int
    titulo: str
    url: str
    estado: str
    criado_em: datetime
    prazo: datetime | None
    encerrado_em: datetime | None
