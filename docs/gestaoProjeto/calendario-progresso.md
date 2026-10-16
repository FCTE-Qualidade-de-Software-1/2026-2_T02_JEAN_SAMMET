
# Calendário e Progresso

## 1. Objetivo

Esta categoria acompanha o cumprimento do cronograma planejado e a conclusão das tarefas comprometidas no Milestone ativo. A medição permite identificar atrasos e orientar a redistribuição das pendências prioritárias.

## 2. Modelo de Informação do PSM

| Elemento do Modelo PSM | Especificação Aplicada à Equipe |
| :--- | :--- |
| **Necessidade de Informação** | A equipe está conseguindo cumprir o cronograma planejado para o Milestone atual? |
| **Conceito Mensurável** | Progresso de conclusão das unidades de trabalho (Work Items) do Milestone. |
| **Entidade e Atributo** | Issues do repositório comprometidas no planejamento inicial do Milestone ativo e seu estado de conclusão. |
| **Medida Básica** | **Nconc:** número de Issues do planejamento inicial concluídas. **Nplanejado:** número total de Issues comprometidas na linha de base do Milestone. |
| **Medida Derivada e Fórmula** | **Taxa de Conclusão de Tarefas (TCT):** TCT = (Nconc / Nplanejado) × 100 |
| **Indicador e Visualização** | Gráfico de burndown ou barra de progresso do Milestone no GitHub. |
| **Critérios de Decisão (Definidos pela Equipe)** | **Meta do Grupo:** TCT = 100% na data limite do Milestone. **Alerta de Atraso:** se TCT < 75% a 24 horas do prazo final, reatribuir as pendências prioritárias entre os integrantes. |

## 3. Observações Metodológicas

- A linha de base corresponde ao conjunto de Issues comprometidas no planejamento inicial do Milestone. Recomenda-se registrar esse conjunto no início do ciclo.
- Novas Issues adicionadas durante o ciclo devem ser identificadas separadamente, evitando alterações retroativas no total planejado.
- O cálculo pressupõe que Nplanejado > 0. Caso não existam tarefas planejadas, a TCT deverá ser registrada como não aplicável.
- O critério de conclusão de uma Issue deve ser aplicado de maneira consistente.

## 4. Acompanhamento

Os dados atuais do Milestone e o progresso das tarefas podem ser consultados na página [Acompanhamento do Projeto](acompanhamento.md).
