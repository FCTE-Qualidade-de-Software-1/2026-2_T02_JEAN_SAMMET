from . import formatacao
from .resultado_marco import ResultadoMarco
from .tabelas_markdown import tabela


def renderizar_calendario(resultado: ResultadoMarco, numero_figura: int, prefixo_imagem: str) -> str:
    tct = resultado.tct
    adicionadas = f"{tct.adicionadas} ({tct.adicionadas_concluidas} concluídas)"
    parametros = tabela(
        ["Parâmetro", "Valor Observado"],
        [
            ["Issues planejadas (Nplanejado)", str(tct.planejadas)],
            ["Issues concluídas (Nconc)", str(tct.concluidas)],
            ["Issues adicionadas após a linha de base", adicionadas],
            ["Taxa de Conclusão de Tarefas (TCT)", formatacao.percentual(tct.tct)],
            ["Situação da meta do grupo", resultado.situacao_tct],
        ],
    )
    partes = ["### Calendário e Progresso", parametros]
    if resultado.burndown:
        titulo = resultado.marco.titulo
        imagem = f"{prefixo_imagem}/marco-{resultado.marco.numero}/burndown.png"
        partes.append(f"![Gráfico de Burndown do {titulo}]({imagem})")
        partes.append(
            f"**Figura {numero_figura}: Burndown do {titulo}. "
            "Fonte: elaboração automática com dados do repositório.**"
        )
    return "\n\n".join(partes)
