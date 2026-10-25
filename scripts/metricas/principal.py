import argparse
import os
import sys
from pathlib import Path

from .cliente_github import ClienteGithub
from .configuracao import ARQUIVO_PAINEL, DIRETORIO_DADOS
from .execucao import executar
from .formatacao import dias, percentual
from .tempo import instante_atual


def ler_argumentos(argumentos: list[str] | None):
    analisador = argparse.ArgumentParser(prog="python -m scripts.metricas")
    analisador.add_argument("--repositorio", default=os.environ.get("GITHUB_REPOSITORY"))
    analisador.add_argument("--dados", type=Path, default=DIRETORIO_DADOS)
    analisador.add_argument("--painel", type=Path, default=ARQUIVO_PAINEL)
    analisador.add_argument("--aplicar-rotulos", action="store_true")
    return analisador.parse_args(argumentos)


def imprimir_resumo(resultados, acoes: list[str]) -> None:
    for resultado in resultados:
        print(
            f"{resultado.marco.titulo}: TCT {percentual(resultado.tct.tct)}, "
            f"TC médio {dias(resultado.ciclo.media_dias)}, {resultado.situacao_tsa}"
        )
    for acao in acoes:
        print(acao)


def principal(argumentos: list[str] | None = None) -> int:
    parametros = ler_argumentos(argumentos)
    if not parametros.repositorio:
        print("Informe --repositorio ou defina GITHUB_REPOSITORY (dono/nome).", file=sys.stderr)
        return 2
    cliente = ClienteGithub(os.environ.get("GITHUB_TOKEN", ""))
    resultados, acoes = executar(
        cliente,
        parametros.repositorio,
        parametros.dados,
        parametros.painel,
        parametros.aplicar_rotulos,
        instante_atual(),
    )
    imprimir_resumo(resultados, acoes)
    return 0
