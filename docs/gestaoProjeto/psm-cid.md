# Gestão do Projeto 

## 1. Introdução

A gestão interna do projeto utiliza o modelo PSM/CID para monitorar a execução das atividades da equipe a partir de evidências do repositório Git (Issues, Milestones, Commits e Pull Requests). Enquanto a avaliação do produto de software segue o SQuaRE e o método GQM, o acompanhamento do grupo abrange três categorias obrigatórias:

- **Calendário e Progresso:** acompanha o cumprimento dos prazos e a conclusão das Issues planejadas (Tabela 1).
- **Recursos e Custos:** avalia a distribuição da quantidade de tarefas entre os integrantes (Tabela 2)
- **Desempenho dos Processos:** mede o tempo médio de resolução das demandas encerradas (Tabela 3)

A especificação detalhada de cada categoria é apresentada a seguir, nas Tabelas 1, 2 e 3.

## 2. Modelos de Informação do PSM 

### Tabela 1: Categoria — Calendário e Progresso

| Elemento do Modelo PSM | Especificação Aplicada à Equipe |
| :--- | :--- |
| **Necessidade de Informação** | A equipe está conseguindo cumprir o cronograma planejado para o Milestone atual? |
| **Conceito Mensurável** | Progresso de conclusão das unidades de trabalho (Work Items) do Milestone. |
| **Entidade e Atributo** | Issues do repositório comprometidas no planejamento inicial do Milestone ativo e seu estado de conclusão. |
| **Medida Básica** | N<sub>conc</sub>: número de Issues do planejamento inicial concluídas.<br>N<sub>planejado</sub>: número total de Issues comprometidas na linha de base do Milestone. |
| **Medida Derivada e Fórmula** | **Taxa de Conclusão de Tarefas:**<br><p align="center"><strong>TCT = (N<sub>conc</sub> / N<sub>planejado</sub>) × 100</strong></p> |
| **Indicador e Visualização** | Gráfico de burndown ou barra de progresso do Milestone no GitHub. |
| **Critérios de Decisão (Definidos pela Equipe)** | **Meta do Grupo:** TCT = 100% na data limite do Milestone.<br>**Alerta de Atraso:** se TCT <escape><</escape> 75% a 24 horas do prazo final, reatribuir as pendências prioritárias entre os integrantes. |

**Observações metodológicas:**

- A linha de base corresponde ao conjunto de Issues comprometidas no planejamento inicial do Milestone. Recomenda-se registrar esse conjunto no início do ciclo.
- Novas Issues adicionadas durante o ciclo devem ser identificadas separadamente, evitando alterações retroativas no total planejado.
- O cálculo pressupõe que N<sub>planejado</sub> > 0. Caso não existam tarefas planejadas, a TCT deverá ser registrada como não aplicável.
- O critério de conclusão de uma Issue deve ser aplicado de maneira consistente.

### Tabela 2: Categoria — Recursos e Custos

| Elemento do Modelo PSM | Especificação Aplicada à Equipe |
| :--- | :--- |
| **Necessidade de Informação** | A distribuição das tarefas entre os integrantes está equilibrada? |
| **Conceito Mensurável** | Distribuição das tarefas ativas entre os integrantes da equipe. |
| **Entidade e Atributo** | Issues ativas atribuídas a cada integrante durante o Milestone atual. |
| **Medida Básica** | **N<sub>i</sub>:** número de Issues ativas atribuídas ao integrante *i*.<br>**N<sub>total</sub>:** número total de Issues ativas atribuídas à equipe. |
| **Medida Derivada e Fórmula** | **Distribuição de Tarefas por Integrante (DTI):**<br>DTI<sub>i</sub> = (N<sub>i</sub> / N<sub>total</sub>) × 100<br><br>**Média de Tarefas por Integrante (MTI):**<br>MTI = N<sub>total</sub> / N<sub>integrantes</sub> |
| **Indicador e Visualização** | Gráfico de barras com a quantidade de Issues ativas por integrante, acompanhado da porcentagem de distribuição. |
| **Critérios de Decisão (Definidos pela Equipe)** | **Meta do Grupo:** manter a distribuição de tarefas próxima da média da equipe, considerando diferenças de complexidade e disponibilidade.<br>**Alerta de Sobrecarga:** se um integrante concentrar mais de 35% das Issues ativas, revisar a distribuição das tarefas.<br>**Referência de Equilíbrio:** considerar como sinal de atenção uma diferença superior a 20% em relação à média de tarefas por integrante. |

**Observações metodológicas:**

- Para o cálculo, considerar apenas Issues ativas atribuídas aos integrantes da equipe.
- Issues sem responsável definido devem ser identificadas separadamente e não contabilizadas como tarefas atribuídas a um integrante.
- A quantidade de Issues não representa, isoladamente, o esforço necessário para concluí-las. Sempre que possível, considerar também a complexidade das tarefas.
- O cálculo de DTI pressupõe que N<sub>total</sub> > 0. Se não houver Issues ativas, a medida deverá ser registrada como não aplicável.
- Os limites de 35% e 20% são critérios internos de acompanhamento definidos pela equipe, e não padrões universais do PSM.
---

### Tabela 3: Categoria — Desempenho do Processo

| Elemento do Modelo PSM | Especificação Aplicada à Equipe |
| :--- | :--- |
| **Necessidade de Informação** | As tarefas estão sendo concluídas dentro do tempo esperado e permanecem em andamento regularmente? |
| **Conceito Mensurável** | Tempo de ciclo das Issues e tempo sem atividade das tarefas abertas. |
| **Entidade e Atributo** | Issues do repositório, considerando suas datas de criação, conclusão e última atividade registrada. |
| **Medida Básica** | **T<sub>criação</sub>:** data e hora de criação da Issue.<br>**T<sub>conclusão</sub>:** data e hora de conclusão da Issue.<br>**T<sub>atividade</sub>:** data e hora da última atividade registrada na Issue. |
| **Medida Derivada e Fórmula** | **Tempo de Ciclo (TC):**<br>TC = T<sub>conclusão</sub> − T<sub>criação</sub><br><br>**Tempo sem Atividade (TSA):**<br>TSA = data e hora atual − T<sub>atividade</sub> |
| **Indicador e Visualização** | Tempo médio de ciclo das Issues concluídas e lista de Issues abertas há mais de três dias sem atividade registrada. |
| **Critérios de Decisão (Definidos pela Equipe)** | **Meta do Grupo:** manter o tempo médio de ciclo das Issues em até dois dias.<br>**Alerta de Tarefa Parada:** se uma Issue aberta permanecer sem atividade registrada por mais de três dias, verificar sua situação e definir os próximos passos. |

**Observações metodológicas:**

- O tempo de ciclo deve ser calculado apenas para Issues concluídas, utilizando a diferença entre as datas de conclusão e criação.
- Para calcular o tempo médio de ciclo, somar os tempos de ciclo das Issues concluídas no período e dividir pela quantidade dessas Issues.
- O tempo sem atividade deve ser acompanhado apenas para Issues ainda abertas.
- Para evitar diferenças de interpretação, a equipe deve definir quais eventos contam como atividade, como comentários, alterações de status ou atualizações relevantes.
- Os limites de dois e três dias são critérios internos definidos pela equipe. Recomenda-se registrar o período de referência utilizado na análise.
- Se não houver Issues concluídas no período, o tempo médio de ciclo deverá ser registrado como não aplicável.

## 3. Uso de Inteligência Artificial na Gestão do Projeto

A equipe utilizou o modelo de inteligência artificial Gemini exclusivamente para auxílio na estruturação formal das tabelas dos Modelos de Informação do PSM/CID e para revisão gramatical da documentação. Todas as equações, definições conceituais, delimitações de população e critérios de decisão foram revisados, corrigidos e validados diretamente pelos integrantes do grupo para garantir total conformidade com o contexto do projeto.

## 4. Acompanhamento do Projeto

O acompanhamento do projeto utiliza dados do repositório Git para observar a evolução das atividades, a distribuição do trabalho e o cumprimento do planejamento da equipe.

### 4.1. Issues

A tabela a seguir apresenta a amostragem das Issues cadastradas no repositório para a execução da Fase 1, fornecendo os dados brutos utilizados no cálculo do tempo de ciclo médio de resolução (LT<sub>médio</sub>) e na verificação da distribuição de tarefas (DTI).

| ID da Issue | Título da Tarefa | Atribuído a | Estado | Data de Abertura | Data de Conclusão |
| :--- | :--- | :--- | :--- | :--- | :--- |
| #1 | [Título da Tarefa 1] | [Nome do Integrante A] | [Concluída / Em andamento] | [DD/MM/AAAA] | [DD/MM/AAAA ou -] |
| #2 | [Título da Tarefa 2] | [Nome do Integrante B] | [Concluída / Em andamento] | [DD/MM/AAAA] | [DD/MM/AAAA ou -] |
| #3 | [Título da Tarefa 3] | [Nome do Integrante C] | [Concluída / Em andamento] | [DD/MM/AAAA] | [DD/MM/AAAA ou -] |
| #4 | [Título da Tarefa 4] | [Nome do Integrante D] | [Concluída / Em andamento] | [DD/MM/AAAA] | [DD/MM/AAAA ou -] |

### 4.2. Milestones

O acompanhamento dos marcos do projeto é realizado diretamente na infraestrutura do repositório Git:

- **Milestone Ativo:** [Link direto para o Milestone E1 no GitHub/GitLab]
- **Prazo Limite do Marco:** [DD/MM/AAAA]
- **Status do Progresso:** [X] de [Y] Issues concluídas (TCT = [Z]%).

### 4.3. Burndown

![Gráfico de Burndown / Progresso do Milestone](link_ou_caminho_da_imagem.png)

*Figura 1: Acompanhamento visual do progresso do Milestone e evolução do backlog de tarefas do grupo.*

## 5. Considerações Finais

A especificação e o acompanhamento das métricas têm como finalidade apoiar a equipe no monitoramento do projeto e na identificação de oportunidades de melhoria. Os resultados observados deverão ser interpretados considerando o planejamento, o contexto e as limitações dos dados coletados.

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Ana Beatriz](https://github.com/AnnaBeatrizAraujo) | Criação da pagina de Gessão do Projeto | 15/10 | [2802ef9](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/2802ef9469c1cff7f5ce41cc6c2f11972e9caac1) |
| [Ana Beatriz](https://github.com/AnnaBeatrizAraujo) | Atualizacao da pagina | 15/10 | [e2f479f](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/e2f479f359f3d6d70d4b4e3ddc55e29e50edb7d4) |