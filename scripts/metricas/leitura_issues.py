from .conversao_evento import converter_evento
from .modelos import Issue, Marco
from .tempo import ler_instante


def listar_eventos(cliente, repositorio: str, numero: int):
    brutos = cliente.listar(f"/repos/{repositorio}/issues/{numero}/timeline")
    eventos = (converter_evento(bruto) for bruto in brutos)
    return tuple(evento for evento in eventos if evento is not None)


def converter_issue(bruto: dict, eventos) -> Issue:
    fechada_em = ler_instante(bruto["closed_at"]) if bruto.get("closed_at") else None
    rotulos = tuple(rotulo["name"] for rotulo in bruto.get("labels", []))
    return Issue(
        numero=bruto["number"],
        titulo=bruto["title"],
        url=bruto["html_url"],
        aberta_em=ler_instante(bruto["created_at"]),
        fechada_em=fechada_em,
        rotulos=rotulos,
        eventos=eventos,
    )


def listar_issues(cliente, repositorio: str, marco: Marco) -> list[Issue]:
    brutos = cliente.listar(
        f"/repos/{repositorio}/issues",
        {"milestone": str(marco.numero), "state": "all"},
    )
    somente_issues = [bruto for bruto in brutos if "pull_request" not in bruto]
    issues = [
        converter_issue(bruto, listar_eventos(cliente, repositorio, bruto["number"]))
        for bruto in somente_issues
    ]
    return sorted(issues, key=lambda issue: issue.numero)
