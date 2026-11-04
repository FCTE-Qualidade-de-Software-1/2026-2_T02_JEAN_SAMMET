from . import formatacao
from .configuracao import (
    DATAS_FINAIS_BURNDOWN,
    JANELA_LINHA_DE_BASE_HORAS,
    LIMITE_TSA_DIAS,
)
from .renderizacao_marco import renderizar_marco
from .resultado_marco import ResultadoMarco


def ordenar_marcos(resultados: list[ResultadoMarco]) -> list[ResultadoMarco]:
    return sorted(resultados, key=lambda resultado: resultado.marco.numero)


def renderizar_metodologia() -> str:
    janela = formatacao.decimal(JANELA_LINHA_DE_BASE_HORAS, 0)
    limite = formatacao.decimal(LIMITE_TSA_DIAS, 0)
    datas_finais = ", ".join(
        f"Milestone #{numero}: {data_fim.strftime('%d/%m/%Y')}"
        for numero, data_fim in sorted(DATAS_FINAIS_BURNDOWN.items())
    )
    descricao_burndown = (
        f"**Burndown:** data final configurada para {datas_finais}; a linha ideal segue até essa data, "
        "enquanto a linha real é exibida até a data de referência da coleta. "
        "Nos demais Milestones encerrados, o gráfico termina no prazo ou, se o marco foi encerrado antes, na data do encerramento. "
        "Milestones ainda abertos sem data final específica continuam até o prazo ou a data de referência, o que for mais distante."
    )
    itens = [
        "**Fonte:** API do GitHub (Milestones, Issues, responsáveis e linha do tempo de cada Issue).",
        "**Frequência:** atualização em alterações de Issues e Milestones, comentários em Issues, "
        "execução manual do workflow ou rotina diária agendada.",
        f"**Linha de base:** Issues que entraram no Milestone até {janela} horas após a entrada da primeira. "
        "As que entram depois são contadas como adicionadas e não alteram Nplanejado.",
        "**Data de referência:** o momento da coleta para Milestones abertos e a data de encerramento "
        "para Milestones encerrados, de modo que resultados antigos não mudam.",
        "**Estado e datas das Issues:** calculados considerando o histórico até a data de referência. "
        "Os responsáveis refletem as atribuições atuais exibidas pelo GitHub.",
        "**Atividade (TSA):** comentário, commit ou Pull Request vinculado, mudança de status e mudança de "
        "responsável feitos por pessoas. Eventos de automação, edições de título e de rótulo não contam. "
        "Sem eventos, vale a data de abertura da Issue.",
        f"**Alerta de tarefa parada:** Issues abertas acima de {limite} dias sem atividade recebem o rótulo "
        "`sem-atividade`, removido quando voltam a ter movimento.",
        "**Prazo:** fim do dia da data limite do Milestone, no horário de Brasília.",
        descricao_burndown,
        "**Dados manuais:** esforço, custo equivalente, decisões e registros históricos são mantidos no "
        "arquivo-fonte `scripts/metricas/acompanhamento.md` e incorporados a esta página durante a geração.",
        "**Definições:** consulte [Gestão do Projeto](psm-cid.md), [Calendário e Progresso](calendario-progresso.md), "
        "[Recursos e Custos](recursos-custos.md) e [Desempenho do Processo](desempenho-processo.md).",
    ]
    return "\n".join(f"- {item}" for item in itens)


def renderizar_painel(
    resultados: list[ResultadoMarco],
    prefixo_imagem: str,
    conteudo_manual: str = "",
) -> str:
    ordenados = ordenar_marcos(resultados)
    cabecalho = [
        "# Acompanhamento do Projeto",
        "O acompanhamento utiliza dados do repositório Git para observar a evolução das atividades, "
        "a distribuição do trabalho e o cumprimento do planejamento da equipe. Esta página reúne, "
        "em um único lugar, as métricas de Issues e Milestones coletadas automaticamente do GitHub "
        "e as informações que dependem dos registros manuais da equipe. Os resultados servem de "
        "referência para as definições de [Calendário e Progresso](calendario-progresso.md), "
        "[Recursos e Custos](recursos-custos.md) e [Desempenho do Processo](desempenho-processo.md).",
        "## Como os dados são coletados",
        renderizar_metodologia(),
        "## Acompanhamento dos Milestones",
    ]
    if not ordenados:
        cabecalho.append("Nenhum Milestone foi encontrado no repositório.")
    secoes = [
        renderizar_marco(resultado, indice, prefixo_imagem)
        for indice, resultado in enumerate(ordenados, start=1)
    ]
    partes = cabecalho + secoes
    if conteudo_manual.strip():
        partes.append(conteudo_manual.strip())
    return "\n\n".join(partes) + "\n"
