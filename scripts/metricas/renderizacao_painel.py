from . import formatacao
from .configuracao import JANELA_LINHA_DE_BASE_HORAS, LIMITE_TSA_DIAS
from .renderizacao_marco import renderizar_marco
from .resultado_marco import ResultadoMarco


def ordenar_marcos(resultados: list[ResultadoMarco]) -> list[ResultadoMarco]:
    return sorted(resultados, key=lambda r: (r.marco.estado == "closed", -r.marco.numero))


def renderizar_metodologia() -> str:
    janela = formatacao.decimal(JANELA_LINHA_DE_BASE_HORAS, 0)
    limite = formatacao.decimal(LIMITE_TSA_DIAS, 0)
    itens = [
        "**Fonte:** API do GitHub (Milestones, Issues e linha do tempo de cada Issue).",
        f"**Linha de base:** Issues que entraram no Milestone até {janela} horas após a entrada da primeira. "
        "As que entram depois são contadas como adicionadas e não alteram Nplanejado.",
        "**Data de referência:** o momento da coleta para Milestones abertos e a data de encerramento "
        "para Milestones encerrados, de modo que resultados antigos não mudam.",
        "**Atividade (TSA):** comentário, commit ou Pull Request vinculado, mudança de status e mudança de "
        "responsável feitos por pessoas. Eventos de automação, edições de título e de rótulo não contam. "
        "Sem eventos, vale a data de abertura da Issue.",
        f"**Alerta de tarefa parada:** Issues abertas acima de {limite} dias sem atividade recebem o rótulo "
        "`sem-atividade`, removido quando voltam a ter movimento.",
        "**Prazo:** fim do dia da data limite do Milestone, no horário de Brasília.",
    ]
    return "\n".join(f"- {item}" for item in itens)


def renderizar_painel(resultados: list[ResultadoMarco], prefixo_imagem: str) -> str:
    ordenados = ordenar_marcos(resultados)
    cabecalho = [
        "# Painel de Métricas Automáticas",
        "Esta página é gerada automaticamente a partir dos dados do repositório e atualizada a cada "
        "alteração em Issues e Milestones e uma vez por dia. As definições das métricas estão em "
        "[Gestão do Projeto](psm-cid.md). Recursos e Custos não são calculados aqui e constam em "
        "[Acompanhamento](acompanhamento.md).",
        "## Como os dados são coletados",
        renderizar_metodologia(),
    ]
    if not ordenados:
        cabecalho.append("Nenhum Milestone foi encontrado no repositório.")
    secoes = [
        renderizar_marco(resultado, indice, prefixo_imagem)
        for indice, resultado in enumerate(ordenados, start=1)
    ]
    return "\n\n".join(cabecalho + secoes) + "\n"
