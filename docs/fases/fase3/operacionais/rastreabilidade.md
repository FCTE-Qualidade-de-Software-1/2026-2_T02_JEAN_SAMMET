# Matriz de rastreabilidade — Fase 3

A matriz mostra **como cada necessidade será avaliada**: característica da Fase 1 → questão e hipótese da Fase 2 → métrica e meta → entrada, procedimento e registro da Fase 3. São **nove questões, nove hipóteses e doze métricas**.

Esta página registra o **planejamento da avaliação**. Os valores obtidos, as respostas e os julgamentos ficam na [rastreabilidade da Fase 4](../../fase4/rastreabilidade.md).

## 1. Preparação comum

A Tabela 1 reúne as condições de preparação compartilhadas pelos procedimentos.

**Tabela 1 — Entradas e condições de preparação.**

| Elemento | Definição no plano | Referência |
|---|---|---|
| Objeto | Fluxo de planejamento de formatura, com foco em `/plano-formatura` | [Escopo da Fase 1](../../fase1/escopo.md) |
| Entrada acadêmica | H0, matriz 6360/1 — 2017.1; 44 registros, 15 obrigatórias pendentes e oito equivalências | [Fontes e regras](../funcionais/fontes.md#6-entrada-academica-h0) |
| Variações | C0–C5 mantêm H0 fixo e alteram uma configuração por vez | [Cenários controlados](../funcionais/roteiro.md#12-cenarios-controlados) |
| Ambiente | Conta autorizada; registrar navegador, sistema, viewport, zoom, data/hora e versão conhecida | [Ambiente e dados](ambienteERecursos.md) |
| Referências de julgamento | Regras curriculares identificadas e contratos CA-C3, CA-C4, OC-01 e CAL-01 do cenário | [Contratos de aceitação](../funcionais/fontes.md#7-contratos-de-aceitacao-de-ec-01) |
| Preservação | Publicar registros sanitizados; manter PDF pessoal, valores de autenticação e identificadores fora dos registros públicos | [Plano integrado](../planoAvaliacao.md#2-registro-e-decisao) |

*Fonte: elaboração da equipe, conforme o escopo, as referências e os procedimentos da avaliação.*

## 2. Matriz funcional

A Tabela 2 liga as sete questões funcionais aos casos CT-01 a CT-07. As metas são as definidas no [GQM funcional](../../fase2/funcionais/GQM.md); as quantidades de H0 são universos de referência, não resultados do produto.

**Tabela 2 — Rastreabilidade do planejamento funcional.**

| Necessidade da Fase 1 | Questão / hipótese | Métrica e meta | Entrada / condição | Procedimento planejado | Registro previsto |
|---|---|---|---|---|---|
| Sequência curricular correta | **Q-FUN-01 / H-FUN-01** | **MET-FUN-01 — TVP: 0%** | H0/C0; FGA0170 matriculada e FGA0211 pendente | [CT-01](../funcionais/roteiro.md#ct-01-pre-requisitos-met-fun-01): comparar regra oficial, status e ordem de alocação; distinguir matrícula e projeção | Relação, fonte/vigência, semestres esperado/observado e violações |
| Co-requisitos atendidos | **Q-FUN-02 / H-FUN-02** | **MET-FUN-02 — TVC: 0%** | H0; selecionar explicitamente FGA0072/FGA0074 sem alterar os status | [CT-02](../funcionais/roteiro.md#ct-02-co-requisitos-met-fun-02): conferir as duas direções da relação e a satisfação simultânea/prévia aplicável | Seleção do par, status, posições no grafo e resultado por direção |
| Obrigatórias contempladas | **Q-FUN-03 / H-FUN-03** | **MET-FUN-03 — CDO: 100%**; apoio de TAE, meta **0%** | H0/C0; referência de 15 pendências | [CT-03](../funcionais/roteiro.md#ct-03-obrigatorias-pendentes-met-fun-03): cruzar todas as pendências com o plano completo; considerar equivalências válidas | Lista esperada/planejada, omissões, exclusões fundamentadas e cobertura |
| Histórico interpretado corretamente | **Q-FUN-04 / H-FUN-04** | **MET-FUN-04 — TDH: 0%** | H0; 44 registros identificados por código e período | [CT-04](../funcionais/roteiro.md#ct-04-tratamento-do-historico-met-fun-04): comparar cada ocorrência e seu status, com normalização das equivalências oficiais | Comparação individual esperado/observado; preservação de registros repetidos |
| Equivalências válidas | **Q-FUN-05 / H-FUN-05**, com apoio a Q-FUN-03 | **MET-FUN-05 — TAE: 0%** | H0; seis relações concluídas e duas em andamento | [CT-05](../funcionais/roteiro.md#ct-05-equivalencias-met-fun-05-apoio-a-met-fun-03): conferir destino, vigência, estado e efeito nas pendências | Oito relações verificadas, divergências e eventual duplicação |
| Preferências com efeito definido | **Q-FUN-06 / H-FUN-06** | **MET-FUN-06 — COO: 100%** | H0 fixo; C1/C2, C3/C4 e variantes de C5 | [CT-06](../funcionais/roteiro.md#ct-06-onboarding-met-fun-06): variar uma opção por vez e comparar as sete expectativas de carga/preferência com o contrato | Campo alterado, esperado, observado e atendimento por expectativa |
| Restrições semestrais respeitadas | **Q-FUN-07 / H-FUN-07** | **MET-FUN-07 — TVS: 0% por tipo**; máximo de **480h** | C0–C5; OC-01 e CAL-01 | [CT-07](../funcionais/roteiro.md#ct-07-restricoes-semestrais-met-fun-07): somar cargas com reservas; conferir dez alocações de oferta e três condições de calendário | Cargas e violações separadas por tipo; semestre esperado/observado |

*Fonte: elaboração da equipe, conforme o GQM da Fase 2 e o roteiro funcional da Fase 3.*

**Ligação complementar:** TAE também apoia Q-FUN-03 porque uma equivalência pode alterar as pendências. Assim, o julgamento da cobertura exige tanto a lista de obrigatórias quanto a conferência das relações aplicáveis. A mesma métrica não é contada duas vezes como medida independente.

## 3. Matriz operacional

A Tabela 3 relaciona as duas questões operacionais às cinco métricas de usabilidade e segurança. Os níveis e a agregação seguem as [fichas e regras da Fase 2](../../fase2/operacionais/visaoGeral.md#22-regra-de-julgamento-conjunto).

**Tabela 3 — Rastreabilidade do planejamento operacional.**

| Necessidade da Fase 1 | Questão / hipótese | Métrica e meta | Procedimento planejado | Registro previsto |
|---|---|---|---|---|
| Interface compreensível e operável | **Q-OP-01 / H-OP-01** | **MET-OP-01 — TCH: ≥85%** para Excelente | [Inspeção T1–T3](metodos.md#1-usabilidade-tch-e-isvh), com H0/C0: duas avaliações independentes de dez itens e consenso | Notas individuais, descrição dos problemas, evidências e checklist consolidado |
| Problemas de uso classificados | **Q-OP-01 / H-OP-01** | **MET-OP-01b — ISVH: ≤5**, sem maior/catastrófico, para Excelente | Classificar cada problema confirmado em severidade 1–4; contar uma vez no consenso | Problema, tarefa, severidade, justificativa e soma ponderada |
| Riscos de dependências identificados | **Q-OP-02 / H-OP-02** | **MET-OP-02 — IRP: ≤5**, sem críticas/altas, para Excelente | [Inventário e análise de dependências](metodos.md#2-dependencias-irp): identificar componentes/versões e achados únicos; aplicar os pesos | Inventário, identificador do achado, severidade, escopo e apuração |
| Dados protegidos no cliente | **Q-OP-02 / H-OP-02** | **MET-OP-02b — GED-C: 0 chaves** | [Inspeção de armazenamento](metodos.md#3-armazenamento-ged-c): localStorage, sessionStorage e cookies em E0/E1/E2; contar a união por origem/mecanismo/chave | Estado, mecanismo, chave e tipo de conteúdo, sem publicar valores pessoais |
| Acesso restrito quando exigido | **Q-OP-02 / H-OP-02** | **MET-OP-02c — TBR: 100%**, com bateria completa válida | [Controle de acesso](metodos.md#4-acesso-tbr): validar chamada positiva e executar as dez condições negativas com pré-condições isoladas | Operação, método, condição, status, comportamento e classificação por caso |

*Fonte: elaboração da equipe, conforme as fichas operacionais da Fase 2 e os métodos da Fase 3.*

Em usabilidade, o julgamento conjunto usa o **pior nível entre TCH e ISVH**. Em segurança, dependências, armazenamento e acesso são julgados separadamente; uma medida favorável não compensa outra fora da meta. Os limites indicados para TCH, ISVH e IRP são os da faixa Excelente; as demais faixas continuam nas fichas.

O [cronograma de avaliação](../cronograma.md) distribui as atividades, responsáveis e dependências até 22/11.

## 4. Cobertura do plano e passagem para a Fase 4

A Tabela 4 resume a cobertura prevista e identifica a documentação de execução correspondente.

**Tabela 4 — Cobertura do plano e destino dos registros.**

| Frente | Cobertura planejada | Documento de execução e julgamento |
|---|---|---|
| Adequação funcional | **Sete questões, sete hipóteses, sete métricas e CT-01 a CT-07** | [Registros funcionais](../../fase4/funcionais/dadosBrutos.md) e [análise funcional](../../fase4/funcionais/analiseResultados.md) |
| Usabilidade | **Uma questão, uma hipótese, duas métricas e tarefas T1–T3** | [Avaliação da equipe](../../fase4/operacionais/avaliacaoUsabilidade.md) e [análise operacional](../../fase4/operacionais/analiseResultados.md) |
| Segurança | **Uma questão, uma hipótese e três métricas** | [Registros operacionais](../../fase4/operacionais/dadosBrutos.md) e [análise operacional](../../fase4/operacionais/analiseResultados.md) |
| Melhoria | Selecionar um achado, definir a intervenção e comparar as métricas pertinentes antes/depois | [Ação de melhoria M-01](../../fase4/operacionais/acaoMelhoria.md) |
| Encerramento | Responder às questões, julgar hipóteses e justificar recomendações | [Rastreabilidade da Fase 4](../../fase4/rastreabilidade.md) e [conclusão](../../fase4/conclusao.md) |

*Fonte: elaboração da equipe, conforme o plano integrado e a organização das Fases 3 e 4.*

**Critério de prontidão:** cada métrica deve ter entrada, regra ou contrato, procedimento, meta e registro definidos. A existência dessa matriz demonstra a ligação do planejamento; os percentuais obtidos e os julgamentos são apresentados na Fase 4, sem antecipar resultados nesta etapa.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Criação da matriz de rastreabilidade bidirecional completa da Fase 1 à Fase 4 para métricas operacionais | 14/11 | [6594e5c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/6594e5c2349ee5fc4dc632f07b97bc8191357819) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Rastreabilidade das doze métricas aos procedimentos e às evidências | 15/11 | [aa0c61f](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/aa0c61fac5e9d2db19adec76fd052a2bb6b04b90) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Ligação do planejamento à página de rastreabilidade da Fase 4 | 16/11 | [d9d7c15](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/d9d7c1591b6995089cd520a3cca24091f2566c13) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Organização da matriz de planejamento funcional e operacional da Fase 3 | 16/11 | [2c27c5f](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/2c27c5f7e47663e993ffdc4c3abeb0411eac1c3e) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Ligação da matriz ao cronograma de avaliação | 16/11 | Não commitado |
