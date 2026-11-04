from . import formatacao
from .estado_issue import concluida_em, esta_aberta_em
from .resultado_marco import ResultadoMarco
from .tabelas_markdown import link_da_issue, tabela


def link_do_responsavel(login: str) -> str:
    return f"[@{login}](https://github.com/{login})"


def renderizar_issues(resultado: ResultadoMarco) -> str:
    referencia = resultado.referencia
    linhas = []
    for issue in resultado.issues:
        aberta = esta_aberta_em(issue, referencia)
        responsaveis = ", ".join(link_do_responsavel(login) for login in issue.responsaveis)
        conclusao = concluida_em(issue, referencia)
        linhas.append(
            [
                link_da_issue(issue.numero, issue.url),
                issue.titulo,
                responsaveis or "Não atribuído",
                "Aberta" if aberta else "Concluída",
                formatacao.data(issue.aberta_em),
                formatacao.data(conclusao) if conclusao else "—",
            ]
        )

    if not linhas:
        return "### Issues do Milestone\n\nNenhuma Issue foi encontrada neste Milestone."

    return "\n\n".join(
        [
            "### Issues do Milestone",
            "A tabela considera o estado das Issues na data de referência do Milestone. "
            "Os responsáveis são os usuários atualmente associados às Issues no GitHub.",
            tabela(
                ["Issue", "Tarefa", "Responsáveis", "Estado", "Abertura", "Conclusão"],
                linhas,
            ),
        ]
    )
