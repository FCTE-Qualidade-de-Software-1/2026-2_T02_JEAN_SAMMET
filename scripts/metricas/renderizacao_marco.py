from . import formatacao
from .renderizacao_calendario import renderizar_calendario
from .renderizacao_desempenho import renderizar_desempenho
from .resultado_marco import ResultadoMarco


def renderizar_cabecalho(resultado: ResultadoMarco) -> str:
    marco = resultado.marco
    estado = "Encerrado" if marco.estado == "closed" else "Aberto"
    linhas = [
        f"## {marco.titulo}",
        f"Estado: {estado}. Prazo limite: {formatacao.data_hora(marco.prazo)}. "
        f"Data de referência dos cálculos: {formatacao.data_hora(resultado.referencia)}. "
        f"[Ver Milestone no GitHub]({marco.url}).",
    ]
    return "\n\n".join(linhas)


def renderizar_marco(resultado: ResultadoMarco, numero_figura: int, prefixo_imagem: str) -> str:
    partes = [
        renderizar_cabecalho(resultado),
        renderizar_calendario(resultado, numero_figura, prefixo_imagem),
        renderizar_desempenho(resultado),
    ]
    return "\n\n".join(partes)
