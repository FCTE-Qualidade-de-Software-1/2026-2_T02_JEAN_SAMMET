
# Recursos e Custos

## 1. Objetivo

Esta categoria avalia como as tarefas ativas estão distribuídas entre os integrantes da equipe. A medição busca identificar concentrações de atividades que possam exigir uma revisão da distribuição do trabalho.

Neste projeto, a análise utiliza a quantidade de Issues atribuídas a cada integrante, e não uma estimativa financeira ou de horas trabalhadas.

## 2. Modelo de Informação do PSM

| Elemento do Modelo PSM | Especificação Aplicada à Equipe |
| :--- | :--- |
| **Necessidade de Informação** | A distribuição das tarefas entre os integrantes está equilibrada? |
| **Conceito Mensurável** | Distribuição das tarefas ativas entre os integrantes da equipe. |
| **Entidade e Atributo** | Issues ativas atribuídas a cada integrante durante o Milestone atual. |
| **Medida Básica** | **Ni:** número de Issues ativas atribuídas ao integrante i. **Ntotal:** número total de Issues ativas atribuídas à equipe. |
| **Medida Derivada e Fórmula** | **Distribuição de Tarefas por Integrante (DTI):** DTIi = (Ni / Ntotal) × 100. **Média de Tarefas por Integrante (MTI):** MTI = Ntotal / Nintegrantes. |
| **Indicador e Visualização** | Gráfico de barras com a quantidade de Issues ativas por integrante, acompanhado da porcentagem de distribuição. |
| **Critérios de Decisão (Definidos pela Equipe)** | **Meta do Grupo:** manter a distribuição de tarefas próxima da média da equipe, considerando diferenças de complexidade e disponibilidade. **Alerta de Sobrecarga:** se um integrante concentrar mais de 35% das Issues ativas, revisar a distribuição das tarefas. **Referência de Equilíbrio:** considerar como sinal de atenção uma diferença superior a 20% em relação à média de tarefas por integrante. |

## 3. Observações Metodológicas

- Para o cálculo, considerar apenas Issues ativas atribuídas aos integrantes da equipe.
- Issues sem responsável definido devem ser identificadas separadamente e não contabilizadas como tarefas atribuídas a um integrante.
- A quantidade de Issues não representa, isoladamente, o esforço necessário para concluí-las. Sempre que possível, considerar também a complexidade das tarefas.
- O cálculo de DTI pressupõe que Ntotal > 0. Se não houver Issues ativas, a medida deverá ser registrada como não aplicável.
- Os limites de 35% e 20% são critérios internos de acompanhamento definidos pela equipe, e não padrões universais do PSM.

## 4. Acompanhamento

A distribuição das tarefas deve ser analisada com base nas Issues e em seus responsáveis. Os dados disponíveis e o estado atual das atividades podem ser consultados na página [Acompanhamento do Projeto](acompanhamento.md).
