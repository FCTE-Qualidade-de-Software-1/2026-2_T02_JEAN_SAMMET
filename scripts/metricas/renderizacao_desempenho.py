from . import formatacao
from .configuracao import LIMITE_TSA_DIAS, META_CICLO_DIAS
from .resultado_marco import ResultadoMarco
from .tabelas_markdown import link_da_issue, tabela


def renderizar_ciclo(resultado: ResultadoMarco) -> str:
    meta = formatacao.dias(META_CICLO_DIAS)
    partes = [
        f"**Tempo de Ciclo (TC).** Meta do grupo: média de até {meta}.  \n"
        "**Fórmulas:** TC = Data de Conclusão − Data de Criação; "
        "TC<sub>médio</sub> = soma dos tempos de ciclo / número de Issues concluídas. "
        "TC representa o intervalo entre a abertura e a conclusão de uma Issue; "
        "TC<sub>médio</sub> representa a média dos tempos de ciclo das Issues concluídas."
    ]
    if resultado.ciclo.itens:
        linhas = [
            [
                link_da_issue(item.numero, item.url),
                item.titulo,
                formatacao.data_hora(item.aberta_em),
                formatacao.data_hora(item.concluida_em),
                formatacao.dias(item.dias),
            ]
            for item in resultado.ciclo.itens
        ]
        partes.append(tabela(["Issue", "Título", "Aberta em", "Concluída em", "TC"], linhas))
    partes.append(
        tabela(
            ["Métrica", "Valor Calculado", "Situação"],
            [["Tempo Médio de Ciclo", formatacao.dias(resultado.ciclo.media_dias), resultado.situacao_ciclo]],
        )
    )
    return "\n\n".join(partes)


def renderizar_tsa(resultado: ResultadoMarco) -> str:
    limite = formatacao.dias(LIMITE_TSA_DIAS)
    partes = [
        f"**Tempo sem Atividade (TSA).** Alerta para Issues abertas acima de {limite}.  \n"
        "**Fórmula:** TSA = Data de Referência − Data da Última Atividade. "
        "O TSA representa o tempo transcorrido desde a última atividade registrada, "
        "considerando a data de referência adotada."
    ]
    if resultado.tsa.itens:
        linhas = [
            [
                link_da_issue(item.numero, item.url),
                item.titulo,
                formatacao.data_hora(item.ultima_atividade),
                formatacao.dias(item.dias),
                "Parada" if item.acima_do_limite else "Em dia",
            ]
            for item in resultado.tsa.itens
        ]
        partes.append(tabela(["Issue", "Título", "Última atividade", "TSA", "Situação"], linhas))
    partes.append(f"Situação: {resultado.situacao_tsa}.")
    return "\n\n".join(partes)


def renderizar_desempenho(resultado: ResultadoMarco) -> str:
    return "\n\n".join(["### Desempenho do Processo", renderizar_ciclo(resultado), renderizar_tsa(resultado)])
