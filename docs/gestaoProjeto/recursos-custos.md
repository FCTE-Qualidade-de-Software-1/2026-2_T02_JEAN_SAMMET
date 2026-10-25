# Recursos e Custos

## 1. Objetivo

Esta categoria avalia o esforço de pessoal em horas dedicado ao desenvolvimento das atividades e estima o custo financeiro equivalente do projeto [1-3]. A medição busca monitorar a aderência das horas reais ao planejamento inicial e calcular a valoração econômica de referência do trabalho realizado pela equipe.

Neste projeto, a análise utiliza o registro de horas dedicadas por tarefa e o valor didático de referência da hora profissional (R$ 50,00/h) para modelar o custo equivalente.

**Origem das medidas.** Recursos e Custos é uma categoria de informação do PSM (McGARRY et al., 2001). O esforço estimado e o realizado são lidos do registro de horas por Issue, o valor de R$ 50,00/h é uma referência didática, e os limites de 10% e 20% para a variação do esforço são critérios definidos pela equipe.

---

## 2. Modelo de Informação do PSM

| Elemento do Modelo PSM | Especificação Aplicada à Equipe |
| :--- | :--- |
| **Necessidade de Informação** | O esforço em horas e o custo financeiro equivalente do projeto estão alinhados com o planejamento inicial? [3, 4] |
| **Conceito Mensurável** | Esforço de pessoal em horas trabalhadas e custo financeiro equivalente do Milestone [1, 3]. |
| **Entidade e Atributo** | Issues do repositório no Milestone atual, considerando os atributos de esforço estimado (\(H_e\)) e esforço realizado (\(H_r\)) vinculados a cada tarefa [3, 5]. |
| **Medida Básica** | **\(H_e\):** esforço estimado em horas por Issue.<br>**\(H_r\):** esforço efetivamente realizado em horas por integrante/Issue.<br>**\(V_h\):** valor de referência didático da hora profissional (R$ 50,00/h) [3, 6]. |
| **Medida Derivada e Fórmula** | **Esforço Total Realizado (\(E_t\)):** \(E_t = \sum H_r\)<br>**Variação do Esforço (\(V_e\)):** \(V_e = \frac{|E_r - E_e|}{E_e} \times 100\)<br>**Custo Financeiro Equivalente:** \(Custo = E_t \times V_h\) [3, 6]. |
| **Indicador e Visualização** | Tabela comparativa de esforço estimado versus realizado por Issue e indicador do custo financeiro equivalente do Milestone. |
| **Critérios de Decisão (Definidos pela Equipe)** | **Meta de Variação de Esforço:** manter a variação do esforço estimado versus realizado em \(V_e \leq 10\%\) (adequado).<br>**Alerta de Desvio:** se \(V_e > 20\%\), revisar os critérios de estimativa para as próximas tarefas e reavaliar o planejamento.<br>**Faixa de Equilíbrio Individual:** manter o esforço por integrante dentro de uma faixa tolerável em relação à média da equipe. |

---

## 3. Observações Metodológicas

- O levantamento do esforço em horas realizado na Fase 1 foi consolidado ao final do Milestone por meio de **Consenso Retroativo da Equipe**, no qual os integrantes revisaram o escopo executado em cada Issue e registraram o tempo aproximado dedicado.
- O valor de referência de R$ 50,00/h é uma taxa de hora profissional hipotética/didática adotada para simular o cálculo do custo equivalente no contexto acadêmico, dado que o projeto não envolve orçamento financeiro real.
- A variação do esforço (\(V_e\)) é calculada apenas sobre Issues concluídas para evitar que tarefas em andamento distorçam a comparação entre o planejado e o realizado.
- Os limites de \(10\%\) para adequação e \(20\%\) para alerta de variação de esforço são critérios internos de acompanhamento definidos pela equipe e não normas universais rígidas do PSM.

---

## 4. Acompanhamento

A distribuição do esforço em horas e o custo financeiro equivalente calculados para o Milestone 1 podem ser consultados na página [Acompanhamento do Projeto](acompanhamento.md).

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Ana Beatriz](https://github.com/AnnaBeatrizAraujo) | Criação da página de Gestão do Projeto | 15/10/2026 | [e372470](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/e372470367e2d110094e26eaac1220c5a3bd2fe9) |
| [Ana Beatriz](https://github.com/AnnaBeatrizAraujo) | Criação da página de Gestão do Projeto | 15/10/2026 | [e372470](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/e372470367e2d110094e26eaac1220c5a3bd2fe9) |
| [Gustavo Fornaciaro](https://github.com/GUGOFO) | Declaracao da origem da métrica | 25/10/2026 | [792b187](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/792b187ac98c876b47b42606e9c15a4f0e4ddf41) |