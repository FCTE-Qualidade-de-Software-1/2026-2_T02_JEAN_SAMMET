# Recursos e Custos

## 1. Objetivo

Esta categoria avalia o esforço de pessoal, em horas, dedicado ao desenvolvimento das atividades e estima o custo financeiro equivalente do projeto. O objetivo é acompanhar a diferença entre o esforço planejado e o realizado, além de estimar o valor econômico do trabalho desenvolvido pela equipe.

Neste projeto, a análise considera as horas estimadas e realizadas por tarefa e o valor didático de referência de R$ 50,00 por hora.

**Origem das medidas:** Recursos e Custos é uma categoria de informação do PSM, descrita por McGarry et al. (2001). O esforço estimado e o realizado são obtidos a partir dos registros de horas por Issue. O valor de R$ 50,00 por hora é uma referência didática, enquanto os limites para a variação do esforço foram definidos pela equipe.

---

## 2. Modelo de Informação do PSM

| Elemento | Especificação aplicada à equipe |
|---|---|
| **Necessidade de informação** | O esforço em horas e o custo financeiro equivalente do projeto estão alinhados com o planejamento inicial? |
| **Conceito mensurável** | Esforço de pessoal em horas trabalhadas e custo financeiro equivalente por Milestone. |
| **Entidade e atributos** | Issues vinculadas ao Milestone, considerando o esforço estimado e o esforço realizado em cada tarefa. |
| **Medidas básicas** | <code>H<sub>e</sub></code>: esforço estimado, em horas, por Issue.<br><code>H<sub>r</sub></code>: esforço realizado, em horas, por Issue ou integrante.<br><code>V<sub>h</sub></code>: valor de referência da hora profissional, fixado em R$ 50,00/h. |
| **Medidas derivadas** | Esforço total estimado, esforço total realizado, variação percentual do esforço e custo financeiro equivalente. |
| **Indicadores e visualização** | Tabela comparativa entre o esforço estimado e o realizado por Issue, acompanhada dos totais e do custo equivalente do Milestone. |
| **Critérios de decisão** | Variação de até 10%: adequada. Variação superior a 20%: alerta para revisão das estimativas e do planejamento. Entre esses limites, a equipe acompanha o desvio e avalia a necessidade de ajustes. |

### 2.1. Fórmulas das métricas

**Esforço total estimado**

Soma das horas estimadas para as tarefas planejadas:

<code>E<sub>e</sub> = Σ H<sub>e</sub></code>

**Esforço total realizado**

Soma das horas efetivamente dedicadas às tarefas:

<code>E<sub>t</sub> = Σ H<sub>r</sub></code>

**Variação do esforço**

Calcula a diferença percentual absoluta entre o esforço realizado e o estimado:

<code>V<sub>e</sub> = (|E<sub>t</sub> − E<sub>e</sub>| / E<sub>e</sub>) × 100</code>

Quando o esforço estimado for zero, a variação será considerada não aplicável, pois não é possível realizar essa divisão.

**Custo financeiro equivalente**

Estimativa do valor econômico do esforço realizado:

<code>Custo = E<sub>t</sub> × V<sub>h</sub></code>

O custo é uma estimativa didática e não representa uma despesa financeira efetiva do projeto.

---

## 3. Observações metodológicas

- O esforço realizado na Fase 1 foi consolidado ao final do Milestone por meio de **consenso retroativo da equipe**. Os integrantes revisaram as atividades executadas em cada Issue e registraram o tempo aproximado dedicado.
- O valor de R$ 50,00 por hora é uma referência hipotética adotada para simular o cálculo do custo equivalente no contexto acadêmico.
- A variação do esforço é calculada somente para tarefas concluídas, evitando que atividades ainda em andamento distorçam a comparação entre o planejamento e a execução.
- Os limites de 10% e 20% são critérios internos de acompanhamento definidos pela equipe. Eles não representam limites universais do PSM.
- A faixa de equilíbrio individual permite observar diferenças de esforço entre os integrantes. Sua interpretação deve considerar a distribuição de responsabilidades e a complexidade das tarefas.

---

## 4. Acompanhamento

Os resultados de esforço em horas e custo financeiro equivalente do Milestone 1 podem ser consultados na página [Acompanhamento do Projeto](acompanhamento.md).

### Histórico de contribuições

| Nome do membro | Contribuição | Data | Commit |
|---|---|---|---|
| [Ana Beatriz](https://github.com/AnnaBeatrizAraujo) | Criação da página de Gestão do Projeto | 15/10/2026 | [e372470](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/e372470367e2d110094e26eaac1220c5a3bd2fe9) |
| [Gustavo Fornaciaro](https://github.com/GUGOFO) | Declaração da origem da métrica | 25/10/2026 | [792b187](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/792b187ac98c876b47b42606e9c15a4f0e4ddf41) |
