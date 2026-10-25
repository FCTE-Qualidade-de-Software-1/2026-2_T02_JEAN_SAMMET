from dataclasses import dataclass
from datetime import datetime

from .calculo_burndown import PontoBurndown
from .calculo_ciclo import ResultadoCiclo
from .calculo_tct import ResultadoTct
from .calculo_tsa import ResultadoTsa
from .modelos import Issue, Marco


@dataclass(frozen=True)
class ResultadoMarco:
    marco: Marco
    referencia: datetime
    inicio: datetime | None
    issues: tuple[Issue, ...]
    tct: ResultadoTct
    ciclo: ResultadoCiclo
    tsa: ResultadoTsa
    burndown: tuple[PontoBurndown, ...]
    situacao_tct: str
    situacao_ciclo: str
    situacao_tsa: str
