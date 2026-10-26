from datetime import datetime
from pathlib import Path

from .gravacao import gravar_marco, gravar_painel, prefixo_relativo
from .leitura_marcos import listar_marcos
from .processamento_marco import processar_marco
from .renderizacao_painel import renderizar_painel
from .resultado_marco import ResultadoMarco
from .rotulos import garantir_rotulo, sincronizar_rotulos


def sincronizar_marcos_abertos(cliente, repositorio: str, resultados: list[ResultadoMarco]) -> list[str]:
    abertos = [resultado for resultado in resultados if resultado.marco.estado == "open"]
    if not abertos:
        return []
    garantir_rotulo(cliente, repositorio)
    acoes = []
    for resultado in abertos:
        acoes.extend(sincronizar_rotulos(cliente, repositorio, resultado.issues, resultado.tsa))
    return acoes


def executar(
    cliente,
    repositorio: str,
    raiz_dados: Path,
    arquivo_painel: Path,
    aplicar_rotulos: bool,
    agora: datetime,
) -> tuple[list[ResultadoMarco], list[str]]:
    marcos = listar_marcos(cliente, repositorio)
    resultados = [processar_marco(cliente, repositorio, marco, agora) for marco in marcos]
    for resultado in resultados:
        gravar_marco(resultado, raiz_dados)
    texto = renderizar_painel(resultados, prefixo_relativo(raiz_dados, arquivo_painel))
    gravar_painel(texto, arquivo_painel)
    acoes = sincronizar_marcos_abertos(cliente, repositorio, resultados) if aplicar_rotulos else []
    return resultados, acoes
