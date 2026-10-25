from datetime import datetime

from .modelos import Marco


def referencia_do_marco(marco: Marco, agora: datetime) -> datetime:
    if marco.estado == "closed" and marco.encerrado_em is not None:
        return min(marco.encerrado_em, agora)
    return agora
