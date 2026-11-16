<!--
ARQUIVO-FONTE DO PAINEL CONSOLIDADO

Este arquivo não é uma página independente do menu. O script `python -m scripts.metricas`
incorpora seu conteúdo ao `docs/gestaoProjeto/painel.md` sempre que coleta os dados do GitHub.

Mantenha aqui as informações que não podem ser obtidas automaticamente, como esforço,
custo equivalente, decisões gerenciais e registros históricos. Issues, responsáveis, datas,
indicadores e gráficos atuais são gerados pelo script e não precisam ser duplicados aqui.
-->

## Recursos e Custos (Esforço em Horas e Custo Equivalente)

Esta categoria analisa o esforço estimado e realizado pela equipe, a variação entre esses valores e o custo financeiro equivalente, utilizando um valor didático por hora profissional como referência.

**Indicadores:**

- Esforço Total Estimado (<code>E<sub>e</sub></code>).
- Esforço Total Realizado (<code>E<sub>r</sub></code>).
- Variação do Esforço (<code>V<sub>e</sub></code>).
- Custo Financeiro Equivalente.

**Fórmulas:**

- Esforço Total Realizado: <code>E<sub>r</sub> = &Sigma; H<sub>r</sub></code>
- Variação do Esforço: <code>V<sub>e</sub> = (|E<sub>r</sub> − E<sub>e</sub>| / E<sub>e</sub>) × 100</code>
- Custo Equivalente Estimado: <code>C<sub>e</sub> = E<sub>e</sub> × V<sub>h</sub></code>
- Custo Equivalente Realizado: <code>C<sub>r</sub> = E<sub>r</sub> × V<sub>h</sub></code>

Em que:

- <code>H<sub>r</sub></code> representa as horas realizadas em cada atividade.
- <code>E<sub>e</sub></code> representa o esforço total estimado.
- <code>E<sub>r</sub></code> representa o esforço total realizado.
- <code>V<sub>e</sub></code> representa a variação percentual absoluta entre o esforço estimado e o realizado.
- <code>V<sub>h</sub></code> representa o valor didático da hora profissional.
- <code>C<sub>e</sub></code> representa o custo financeiro equivalente estimado.
- <code>C<sub>r</sub></code> representa o custo financeiro equivalente ao esforço realizado.

| Métrica / Parâmetro | Valor Estimado | Valor Realizado |
| :--- | :---: | :---: |
| Esforço Total da Equipe | 21,0 horas | **43,0 horas** |
| Média de Esforço por Integrante (6 membros) | 3,5 h/membro | **7,17 h/membro** |
| Variação do Esforço (<code>V<sub>e</sub></code>) | - | **104,76%** (acima do limite de 10%) |
| Valor Didático da Hora Profissional (<code>V<sub>h</sub></code>) | R$ 50,00/hora | R$ 50,00/hora |
| **Custo Financeiro Equivalente Total** | **R$ 1.050,00** | **R$ 2.150,00** |

**Análise e interpretação gerencial**

Em 16/11, a equipe atualizou o esforço total acumulado para **43,0 horas**. Esse total já inclui os registros anteriores e não deve ser somado novamente a eles. A estimativa inicial permanece em **21,0 horas**. A diferença é de **22,0 horas**, equivalente a **104,76%** da estimativa inicial, acima da referência de 10%.

Como o total acumulado inclui trabalho posterior à Entrega 1, essa comparação indica o crescimento em relação à estimativa inicial; não mede isoladamente a precisão das estimativas de cada entrega. O registro histórico da Entrega 1 permanece preservado abaixo.

A média aritmética é de **7,17 horas por integrante** (43 ÷ 6); não representa a distribuição individual efetiva. Ao valor didático de **R$ 50,00/h**, o custo equivalente realizado é **R$ 2.150,00**, frente aos **R$ 1.050,00** estimados. Esses valores não representam despesas financeiras efetivas. As horas são declaradas pela equipe e mantidas neste arquivo-fonte, sem inferência automática a partir das issues.

## Registro Histórico da Entrega 1 — Fase 1: Definição e Caracterização

O [Milestone 1 (Entrega 1)](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/milestone/1) corresponde à Fase 1 — Definição e Caracterização, com prazo limite em **18/10/2026**. A entrega foi encerrada dentro do período planejado. O estado atual das Issues, os responsáveis cadastrados no GitHub, as datas, os indicadores e o gráfico de Burndown são apresentados na seção automática do Milestone 1.

### Responsáveis e datas registrados originalmente

A tabela abaixo preserva os nomes e a atribuição registrados na documentação original. Ela é um registro histórico; para consultar os responsáveis e estados atuais, utilize a tabela automática de Issues do Milestone 1.

| ID da Issue | Título da Tarefa | Atribuído a | Estado registrado | Data de Abertura | Data de Conclusão |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [**#1**](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/issues/1) | Introdução e Referencial Teórico | Yasmin e Gustavo | Concluída | 15/10/2026 | 18/10/2026 |
| [**#2**](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/issues/2) | Objetivos, Questões e Métricas (GQM) | Gabriel e Giovani | Concluída | 15/10/2026 | 18/10/2026 |
| [**#3**](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/issues/3) | Gráfico Hierárquico GQM | Gabriel e Giovani | Concluída | 15/10/2026 | 18/10/2026 |
| [**#4**](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/issues/4) | Configurar Gestão PSM/CID | Ana Beatriz e Victor | Concluída | 15/10/2026 | 18/10/2026 |
| [**#5**](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/issues/5) | Estruturar GitPage | Yasmin e Gustavo | Concluída | 15/10/2026 | 18/10/2026 |
| [**#6**](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/issues/6) | Compilar 1ª Versão em LaTeX | Ana Beatriz e Victor | Concluída | 15/10/2026 | 18/10/2026 |

**Análise e interpretação gerencial — Calendário e Progresso**

A equipe concluiu as atividades da Entrega 1 dentro do prazo limite estipulado para 18/10/2026. A evolução do trabalho teve dinâmica de desenvolvimento em lote, na qual as demandas foram elaboradas continuamente e parte significativa dos registros de conclusão foi formalizada próximo à data limite do Milestone. Por isso, a leitura do Burndown deve ser feita em conjunto com as datas efetivas registradas no histórico das Issues.

**Análise e interpretação gerencial — Desempenho do Processo**

O tempo médio de ciclo da Entrega 1 ficou acima da meta de até 2,0 dias. Esse resultado deve ser interpretado considerando o intervalo entre a abertura das Issues e o registro de conclusão, que ocorreu de forma concentrada próximo ao encerramento do Milestone. Para as entregas seguintes, recomenda-se registrar o andamento das atividades ao longo da execução, evitando que a percepção de progresso dependa predominantemente do fechamento das tarefas.

## Decisões de Gestão Registradas

Com base nos resultados observados para o Milestone 1, foram registradas as seguintes decisões gerenciais:

1. **Aprovação do Milestone 1:** considerando a conclusão das seis Issues previstas até o prazo limite de 18/10/2026, o marco foi considerado concluído para fins de acompanhamento da entrega da Fase 1.
2. **Acompanhamento do Esforço e Custo Equivalente (Recursos e Custos):** o esforço total realizado na Fase 1 foi de **20,0 horas**, apresentando uma variação de 4,76% em relação às 21,0 horas estimadas (<code>V<sub>e</sub> ≤ 10%</code>), resultando em um custo financeiro equivalente de **R$ 1.000,00**. A alocação de esforço acompanhou a complexidade de cada tarefa e o procedimento de consolidação por consenso retroativo da equipe mostrou-se adequado, devendo ser mantido para a Fase 2.
3. **Atenção ao tempo de ciclo:** o resultado ficou acima da meta estabelecida. Para os próximos marcos, recomenda-se acompanhar mais detalhadamente as datas de início, andamento e conclusão das Issues, evitando que o registro do progresso dependa predominantemente do fechamento concentrado das tarefas.
4. **Manutenção da atualização dos registros:** as informações sobre estado, responsáveis, datas e atividades devem continuar sendo atualizadas no repositório, permitindo que as métricas reflitam a execução real do projeto.

## Considerações Finais

A especificação e o acompanhamento das métricas têm como finalidade apoiar a equipe no monitoramento do projeto e na identificação de oportunidades de melhoria.

Os resultados observados deverão ser interpretados considerando o planejamento, o contexto e as limitações dos dados coletados. A atualização periódica das informações permite que a equipe identifique desvios e avalie a necessidade de ajustes na distribuição das tarefas e no cronograma.

## Histórico de Versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Ana Beatriz](https://github.com/AnnaBeatrizAraujo) | Criação da página de Gestão do Projeto | 15/10/2026 | [2802ef9](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/2802ef9469c1cff7f5ce41cc6c2f11972e9caac1) |
| [Ana Beatriz](https://github.com/AnnaBeatrizAraujo) | Atualização da página | 15/10/2026 | [e2f479f](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/e2f479f359f3d6d70d4b4e3ddc55e29e50edb7d4) |
| [Ana Beatriz](https://github.com/AnnaBeatrizAraujo) | Atualização das tabelas de Issues e Milestones | 16/10/2026 | [b67ec2c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/b67ec2c61c4df05d6c193b73a98f3b8eeaac7c32) |
| [Ana Beatriz](https://github.com/AnnaBeatrizAraujo) | Organização da seção Gestão do Projeto | 16/10/2026 | [e372470](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/e372470367e2d110094e26eaac1220c5a3bd2fe9) |
| [Ana Beatriz](https://github.com/AnnaBeatrizAraujo) | Atualização do progresso das Issues | 18/10/2026 | [d2b77cf](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/d2b77cf6bb91436494b004f225c771eed33ba46f) |
| [Ana Beatriz](https://github.com/AnnaBeatrizAraujo) | Atualização da conclusão das Issues | 18/10/2026 | [0e35ba5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/0e35ba589c078941f61ef6b425882fe07b0e9dff) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Registro separado das horas adicionais da Fase 3 | 15/11 | [0e38da3](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/0e38da3eac882c62bf7c6f9e1bda97a8b744ef2e) |
