from dataclasses import dataclass
from datetime import datetime, timedelta

from .modelos import Issue, Marco


@dataclass(frozen=True)
class LinhaDeBase:
    inicio: datetime | None
    planejadas: tuple[Issue, ...]
    adicionadas: tuple[Issue, ...]


def instante_de_entrada(issue: Issue, marco: Marco) -> datetime:
    entradas = [
        evento.criado_em
        for evento in issue.eventos
        if evento.tipo == "milestoned" and evento.marco == marco.titulo
    ]
    ultima_entrada = max(entradas) if entradas else issue.aberta_em
    return max(ultima_entrada, marco.criado_em)


def definir_linha_de_base(marco: Marco, issues: list[Issue], janela_horas: float) -> LinhaDeBase:
    if not issues:
        return LinhaDeBase(None, (), ())
    entradas = {issue.numero: instante_de_entrada(issue, marco) for issue in issues}
    inicio = min(entradas.values())
    limite = inicio + timedelta(hours=janela_horas)
    planejadas = tuple(issue for issue in issues if entradas[issue.numero] <= limite)
    adicionadas = tuple(issue for issue in issues if entradas[issue.numero] > limite)
    return LinhaDeBase(inicio, planejadas, adicionadas)
