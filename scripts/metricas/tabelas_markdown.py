def escapar(texto) -> str:
    return str(texto).replace("|", "\\|")


def tabela(cabecalho: list[str], linhas: list[list[str]]) -> str:
    primeira = "| " + " | ".join(cabecalho) + " |"
    separador = "| " + " | ".join(":---" for _ in cabecalho) + " |"
    corpo = ["| " + " | ".join(escapar(celula) for celula in linha) + " |" for linha in linhas]
    return "\n".join([primeira, separador, *corpo])


def link_da_issue(numero: int, url: str) -> str:
    return f"[#{numero}]({url})"
