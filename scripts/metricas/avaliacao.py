from datetime import datetime, timedelta

from .calculo_ciclo import ResultadoCiclo
from .calculo_tct import ResultadoTct
from .calculo_tsa import ResultadoTsa
from .configuracao import HORAS_ALERTA_PRAZO, LIMITE_ALERTA_TCT, META_CICLO_DIAS, META_TCT
from .formatacao import decimal


def avaliar_tct(resultado: ResultadoTct, prazo: datetime | None, referencia: datetime) -> str:
    if resultado.tct is None:
        return "Não aplicável (não há Issues planejadas)"
    if resultado.tct >= META_TCT:
        return "Meta atingida"
    if prazo is not None and referencia > prazo:
        return "Prazo encerrado sem atingir a meta"
    faltam = prazo - referencia if prazo is not None else None
    if faltam is not None and faltam <= timedelta(hours=HORAS_ALERTA_PRAZO) and resultado.tct < LIMITE_ALERTA_TCT:
        return "Alerta de atraso: reatribuir as pendências prioritárias"
    return "Em andamento"


def avaliar_ciclo(resultado: ResultadoCiclo) -> str:
    if resultado.media_dias is None:
        return "Não aplicável (nenhuma Issue concluída)"
    meta = decimal(META_CICLO_DIAS, 1)
    if resultado.media_dias <= META_CICLO_DIAS:
        return f"Dentro da meta de até {meta} dias"
    return f"Acima da meta de até {meta} dias"


def avaliar_tsa(resultado: ResultadoTsa) -> str:
    if not resultado.itens:
        return "Não aplicável (nenhuma Issue aberta)"
    paradas = sum(1 for item in resultado.itens if item.acima_do_limite)
    if paradas == 0:
        return "Conforme (nenhuma Issue parada)"
    return f"Alerta: {paradas} Issue(s) parada(s) acima do limite"
