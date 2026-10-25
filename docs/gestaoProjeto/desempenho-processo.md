# Desempenho do Processo

## 1. Objetivo

Esta categoria acompanha o tempo necessário para concluir as Issues e identifica tarefas abertas que permanecem sem atividade registrada por um período prolongado.

A análise permite verificar se as demandas estão sendo resolvidas dentro do tempo esperado e se existem tarefas que precisam de acompanhamento.

**Origem das medidas.** Desempenho do Processo é uma categoria de informação do PSM (McGARRY et al., 2001), e o tempo de ciclo é uma das medidas descritas no framework CID (PSM, 2021). Os limites de dois e três dias são critérios definidos pela equipe. Os dados vêm das datas de criação, conclusão e atividade das Issues no GitHub.

## 2. Modelo de Informação do PSM

| Elemento do Modelo PSM | Especificação Aplicada à Equipe |
| :--- | :--- |
| **Necessidade de Informação** | As tarefas estão sendo concluídas dentro do tempo esperado e permanecem em andamento regularmente? |
| **Conceito Mensurável** | Tempo de ciclo das Issues e tempo sem atividade das tarefas abertas. |
| **Entidade e Atributo** | Issues do repositório, considerando suas datas de criação, conclusão e última atividade registrada. |
| **Medida Básica** | **Tcriação:** data e hora de criação da Issue. **Tconclusão:** data e hora de conclusão da Issue. **Tatividade:** data e hora da última atividade registrada na Issue. |
| **Medida Derivada e Fórmula** | **Tempo de Ciclo (TC):** TC = Tconclusão − Tcriação. **Tempo sem Atividade (TSA):** TSA = data e hora atual − Tatividade. |
| **Indicador e Visualização** | Tempo médio de ciclo das Issues concluídas e lista de Issues abertas há mais de três dias sem atividade registrada. |
| **Critérios de Decisão (Definidos pela Equipe)** | **Meta do Grupo:** manter o tempo médio de ciclo das Issues em até dois dias. **Alerta de Tarefa Parada:** se uma Issue aberta permanecer sem atividade registrada por mais de três dias, verificar sua situação e definir os próximos passos. |

## 3. Observações Metodológicas

- O tempo de ciclo deve ser calculado apenas para Issues concluídas, utilizando a diferença entre as datas de conclusão e criação.
- Para calcular o tempo médio de ciclo, somar os tempos de ciclo das Issues concluídas no período e dividir pela quantidade dessas Issues.
- O tempo sem atividade deve ser acompanhado apenas para Issues ainda abertas.
- Para o cálculo do TSA, contam como atividade os seguintes eventos na Issue: comentário, commit ou Pull Request vinculado, mudança de status ou de coluna no quadro do Projeto e mudança de responsável. Edições de título ou de rótulo e eventos gerados por automação não contam. Tatividade é a data e hora do evento mais recente entre os que contam.
- Os limites de dois e três dias são critérios internos definidos pela equipe. Recomenda-se registrar o período de referência utilizado na análise.
- Se não houver Issues concluídas no período, o tempo médio de ciclo deverá ser registrado como não aplicável.

## 4. Acompanhamento

A amostra das Issues e suas datas de abertura e conclusão está disponível na página [Acompanhamento do Projeto](acompanhamento.md).

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Ana Beatriz](https://github.com/AnnaBeatrizAraujo) | Criação da página de Gestão do Projeto | 15/10/2026 | [e372470](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/e372470367e2d110094e26eaac1220c5a3bd2fe9) |
| [Gustavo Fornaciaro](https://github.com/GUGOFO) | Declaracao da origem da métrica | 25/10/2026 | [792b187](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/792b187ac98c876b47b42606e9c15a4f0e4ddf41) |