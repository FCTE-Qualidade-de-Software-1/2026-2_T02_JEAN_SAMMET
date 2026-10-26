from .cliente_github import ErroApi
from .configuracao import (
    COR_ROTULO_SEM_ATIVIDADE,
    DESCRICAO_ROTULO_SEM_ATIVIDADE,
    ROTULO_SEM_ATIVIDADE,
)


def garantir_rotulo(cliente, repositorio: str) -> None:
    try:
        cliente.enviar(
            "POST",
            f"/repos/{repositorio}/labels",
            {
                "name": ROTULO_SEM_ATIVIDADE,
                "color": COR_ROTULO_SEM_ATIVIDADE,
                "description": DESCRICAO_ROTULO_SEM_ATIVIDADE,
            },
        )
    except ErroApi as erro:
        if erro.status != 422:
            raise


def aplicar_rotulo(cliente, repositorio: str, numero: int) -> None:
    cliente.enviar("POST", f"/repos/{repositorio}/issues/{numero}/labels", {"labels": [ROTULO_SEM_ATIVIDADE]})


def remover_rotulo(cliente, repositorio: str, numero: int) -> None:
    try:
        cliente.enviar("DELETE", f"/repos/{repositorio}/issues/{numero}/labels/{ROTULO_SEM_ATIVIDADE}")
    except ErroApi as erro:
        if erro.status != 404:
            raise


def sincronizar_rotulos(cliente, repositorio: str, issues, resultado_tsa) -> list[str]:
    paradas = {item.numero for item in resultado_tsa.itens if item.acima_do_limite}
    acoes = []
    for issue in issues:
        possui = ROTULO_SEM_ATIVIDADE in issue.rotulos
        deve_possuir = issue.numero in paradas
        if deve_possuir and not possui:
            aplicar_rotulo(cliente, repositorio, issue.numero)
            acoes.append(f"rótulo aplicado em #{issue.numero}")
        if possui and not deve_possuir:
            remover_rotulo(cliente, repositorio, issue.numero)
            acoes.append(f"rótulo removido de #{issue.numero}")
    return acoes
