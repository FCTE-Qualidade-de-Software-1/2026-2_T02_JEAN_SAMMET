# Rastreabilidade completa da Fase 4

**9/9 questões respondidas · 9/9 hipóteses julgadas · 12/12 métricas com resultado · 1/1 melhoria comparada.**

Esta página reúne o fechamento de **EC-01**: o que precisava ser respondido, como foi avaliado, qual resultado foi obtido e onde conferir. A rastreabilidade segue **necessidade → questão/hipótese → procedimento → métrica/meta → resposta → decisão**. A [matriz da Fase 3](../fase3/operacionais/rastreabilidade.md) documenta o planejamento; aqui está o fechamento.

**“Respondida” não significa “Conforme”.** Uma questão está encerrada quando tem resultado, interpretação e julgamento, inclusive quando a meta não foi atendida.

## 1. Quadro de respostas

A Tabela 1 reúne as respostas às nove questões GQM e o julgamento das hipóteses associadas.

**Tabela 1 — Questões respondidas e julgamento das hipóteses.**

| Questão | Tema | Resposta final | Hipótese associada |
|---|---|---|---|
| [Q-FUN-01](#q-fun-01-pre-requisitos) | Pré-requisitos | **Sim, na relação avaliada.** | **H-FUN-01:** Não corroborada no recorte |
| [Q-FUN-02](#q-fun-02-co-requisitos) | Co-requisitos | **Sim, no par consolidado.** | **H-FUN-02:** Não corroborada no par consolidado |
| [Q-FUN-03](#q-fun-03-cobertura-de-obrigatorias) | Cobertura de obrigatórias | **Não. FGA0206 foi omitida.** | **H-FUN-03:** Corroborada |
| [Q-FUN-04](#q-fun-04-interpretacao-do-historico) | Interpretação do histórico | **Sim, nos 44 registros conferidos.** | **H-FUN-04:** Não corroborada no recorte |
| [Q-FUN-05](#q-fun-05-equivalencias) | Equivalências | **Sim, nas oito relações verificadas.** | **H-FUN-05:** Não corroborada nas oito relações |
| [Q-FUN-06](#q-fun-06-preferencias-do-onboarding) | Preferências do onboarding | **Não integralmente: cinco de sete expectativas atendidas.** | **H-FUN-06:** Corroborada em C3/C4 |
| [Q-FUN-07](#q-fun-07-carga-oferta-e-calendario) | Carga, oferta e calendário | **Não em todos os tipos: oferta e calendário divergiram.** | **H-FUN-07:** Corroborada no caso de calendário |
| [Q-OP-01](#q-op-01-usabilidade) | Usabilidade | **Aceitável antes; Excelente após a melhoria.** | **H-OP-01:** Corroborada antes; não corroborada no checklist após M-01 |
| [Q-OP-02](#q-op-02-seguranca) | Segurança | **Com ressalva por armazenamento.** | **H-OP-02:** Corroborada no componente de armazenamento |

*Fonte: registro da avaliação EC-01, organizado pela equipe, conforme as metas e regras de decisão da Fase 2.*

## 2. Questões funcionais

As sete questões funcionais verificam a correção e a completude do plano de H0. As fontes de especificação são o [GQM funcional](../fase2/funcionais/GQM.md) e o [roteiro da Fase 3](../fase3/funcionais/roteiro.md).

### Q-FUN-01 — Pré-requisitos

**Pergunta:** O plano respeita os pré-requisitos oficiais?

**Procedimento:** [CT-01](../fase3/funcionais/roteiro.md#ct-01-pre-requisitos-met-fun-01).

**Tabela 2 — Resultado e meta de Q-FUN-01.**

| Métrica | Resultado / cálculo | Meta | Julgamento |
|---|---|---|---|
| MET-FUN-01 — TVP | 0/1 = **0%** | **0%** | **Conforme no recorte** |

*Fonte: registro da avaliação EC-01, organizado pela equipe, conforme as metas e regras de decisão da Fase 2.*

**Resposta:** Sim, na relação avaliada. FGA0170 está matriculada em 2026.2 e FGA0211 foi projetada em 2027.1, condicionada à aprovação. A matrícula não foi registrada como aprovação concluída.

**Hipótese H-FUN-01:** O plano pode alocar uma dependente antes do cumprimento válido do pré-requisito. **Julgamento: Não corroborada no recorte.**

**Onde conferir:** [resposta formal](funcionais/analiseResultados.md#q-fun-01-o-plano-respeita-os-pre-requisitos-oficiais) · [registro da avaliação](funcionais/dadosBrutos.md#ct-01-pre-requisitos).

### Q-FUN-02 — Co-requisitos

**Pergunta:** O plano respeita os co-requisitos oficiais?

**Procedimento:** [CT-02](../fase3/funcionais/roteiro.md#ct-02-co-requisitos-met-fun-02).

**Tabela 3 — Resultado e meta de Q-FUN-02.**

| Métrica | Resultado / cálculo | Meta | Julgamento |
|---|---|---|---|
| MET-FUN-02 — TVC | 0/2 = **0%** | **0%** | **Conforme no par consolidado** |

*Fonte: registro da avaliação EC-01, organizado pela equipe, conforme as metas e regras de decisão da Fase 2.*

**Resposta:** Sim, no par consolidado. FGA0072 e FGA0074 aparecem em 2027.1, atendendo às duas direções da relação. O registro distinto de Gabriel permanece identificado e não foi misturado ao denominador consolidado.

**Hipótese H-FUN-02:** O plano pode distribuir disciplinas co-requisitadas sem atender à satisfação simultânea ou prévia aplicável. **Julgamento: Não corroborada no par consolidado.**

**Onde conferir:** [resposta formal](funcionais/analiseResultados.md#q-fun-02-o-plano-respeita-os-co-requisitos-oficiais) · [registro da avaliação](funcionais/dadosBrutos.md#ct-02-co-requisitos).

### Q-FUN-03 — Cobertura de obrigatórias

**Pergunta:** Todas as disciplinas obrigatórias pendentes aplicáveis são contempladas?

**Procedimento:** [CT-03](../fase3/funcionais/roteiro.md#ct-03-obrigatorias-pendentes-met-fun-03) e [CT-05](../fase3/funcionais/roteiro.md#ct-05-equivalencias-met-fun-05-apoio-a-met-fun-03).

**Tabela 4 — Resultado e meta de Q-FUN-03.**

| Métrica | Resultado / cálculo | Meta | Julgamento |
|---|---|---|---|
| MET-FUN-03 — CDO | 14/15 = **93,33%** | **100%** | **Não conforme** |
| MET-FUN-05 — TAE | 0/8 = **0%** | **0%** | **Conforme no recorte** |

*Fonte: registro da avaliação EC-01, organizado pela equipe, conforme as metas e regras de decisão da Fase 2.*

**Resposta:** Não. FGA0206 foi omitida. Das 15 pendências de H0, 14 foram contempladas. As oito equivalências corretas não compensam a omissão. Esta questão também utiliza MET-FUN-05 e se relaciona a H-FUN-05, detalhada em Q-FUN-05.

**Hipótese H-FUN-03:** O plano pode omitir obrigatórias mesmo com a lista de disciplinas não alocadas vazia. **Julgamento: Corroborada.**

**Onde conferir:** [resposta formal](funcionais/analiseResultados.md#q-fun-03-todas-as-disciplinas-obrigatorias-pendentes-aplicaveis-sao-contempladas) · [registro da avaliação](funcionais/dadosBrutos.md#ct-03-obrigatorias-pendentes).

### Q-FUN-04 — Interpretação do histórico

**Pergunta:** O histórico e os status são interpretados conforme as regras documentadas?

**Procedimento:** [CT-04](../fase3/funcionais/roteiro.md#ct-04-tratamento-do-historico-met-fun-04).

**Tabela 5 — Resultado e meta de Q-FUN-04.**

| Métrica | Resultado / cálculo | Meta | Julgamento |
|---|---|---|---|
| MET-FUN-04 — TDH | 0/44 = **0%** | **0%** | **Conforme no recorte** |

*Fonte: registro da avaliação EC-01, organizado pela equipe, conforme as metas e regras de decisão da Fase 2.*

**Resposta:** Sim, nos 44 registros conferidos. Os 37 registros APR e sete MATR mantiveram as ocorrências por código e período. A normalização das equivalências usa o destino oficial e distingue a projeção futura da aprovação acadêmica real.

**Hipótese H-FUN-04:** Disciplinas em andamento podem ser tratadas como aprovadas indevidamente. **Julgamento: Não corroborada no recorte.**

**Onde conferir:** [resposta formal](funcionais/analiseResultados.md#q-fun-04-o-historico-e-os-status-sao-interpretados-conforme-as-regras-documentadas) · [registro da avaliação](funcionais/dadosBrutos.md#ct-04-tratamento-do-historico).

### Q-FUN-05 — Equivalências

**Pergunta:** As equivalências respeitam a fonte curricular e sua vigência?

**Procedimento:** [CT-05](../fase3/funcionais/roteiro.md#ct-05-equivalencias-met-fun-05-apoio-a-met-fun-03).

**Tabela 6 — Resultado e meta de Q-FUN-05.**

| Métrica | Resultado / cálculo | Meta | Julgamento |
|---|---|---|---|
| MET-FUN-05 — TAE | 0/8 = **0%** | **0%** | **Conforme no recorte** |

*Fonte: registro da avaliação EC-01, organizado pela equipe, conforme as metas e regras de decisão da Fase 2.*

**Resposta:** Sim, nas oito relações verificadas. Seis relações concluídas satisfizeram suas obrigações e duas em andamento continuaram não concluídas. Não houve aplicação incorreta confirmada nem duplicação indevida no recorte.

**Hipótese H-FUN-05:** A aplicação das equivalências pode ignorar as relações ou a vigência pertinente. **Julgamento: Não corroborada nas oito relações.**

**Onde conferir:** [resposta formal](funcionais/analiseResultados.md#q-fun-05-as-equivalencias-respeitam-a-fonte-curricular-e-sua-vigencia) · [registro da avaliação](funcionais/dadosBrutos.md#ct-05-equivalencias).

### Q-FUN-06 — Preferências do onboarding

**Pergunta:** O onboarding produz o comportamento documentado ou prometido?

**Procedimento:** [CT-06](../fase3/funcionais/roteiro.md#ct-06-onboarding-met-fun-06), C0–C5 e [contratos de aceitação](../fase3/funcionais/fontes.md#7-contratos-de-aceitacao-de-ec-01).

**Tabela 7 — Resultado e meta de Q-FUN-06.**

| Métrica | Resultado / cálculo | Meta | Julgamento |
|---|---|---|---|
| MET-FUN-06 — COO | 5/7 = **71,43%** | **100%** | **Não conforme** |

*Fonte: registro da avaliação EC-01, organizado pela equipe, conforme as metas e regras de decisão da Fase 2.*

**Resposta:** Não integralmente: cinco de sete expectativas atendidas. As cinco expectativas de representação de carga foram atendidas. Os contratos CA-C3 e CA-C4 não foram: trabalho manteve 24 créditos em vez de sugerir 20 e velocidade manteve três semestres futuros em vez de dois.

**Hipótese H-FUN-06:** Trabalho/estágio e objetivo podem não produzir o efeito definido para o cenário. **Julgamento: Corroborada em C3/C4.**

**Onde conferir:** [resposta formal](funcionais/analiseResultados.md#q-fun-06-o-onboarding-produz-o-comportamento-documentado-ou-prometido) · [registro da avaliação](funcionais/dadosBrutos.md#ct-06-onboarding).

### Q-FUN-07 — Carga, oferta e calendário

**Pergunta:** O plano respeita oferta, semestre inicial e limites de carga verificáveis?

**Procedimento:** [CT-07](../fase3/funcionais/roteiro.md#ct-07-restricoes-semestrais-met-fun-07), com OC-01 e CAL-01.

**Tabela 8 — Resultado e meta de Q-FUN-07.**

| Métrica | Resultado / cálculo | Meta | Julgamento |
|---|---|---|---|
| MET-FUN-07 — TVS: máximo de 480h | 0/23 = **0%** | **0%** | **Conforme** |
| MET-FUN-07 — TVS: oferta | 1/10 = **10%** | **0%** | **Não conforme** |
| MET-FUN-07 — TVS: calendário | 1/3 = **33,33%** | **0%** | **Não conforme** |

*Fonte: registro da avaliação EC-01, organizado pela equipe, conforme as metas e regras de decisão da Fase 2.*

**Resposta:** Não em todos os tipos: oferta e calendário divergiram. O máximo de 480h foi respeitado. Houve uma divergência entre dez alocações de oferta e uma entre três condições de calendário. Na falha com fallback, o início foi 2027.2 quando CAL-01 exige 2027.1.

**Hipótese H-FUN-07:** A falha na consulta do período pode levar a um semestre estimado divergente do calendário de referência. **Julgamento: Corroborada no caso de calendário.**

**Onde conferir:** [resposta formal](funcionais/analiseResultados.md#q-fun-07-o-plano-respeita-oferta-semestre-inicial-e-limites-de-carga-verificaveis) · [registro da avaliação](funcionais/dadosBrutos.md#ct-07-restricoes-semestrais).

## 3. Questões operacionais

As duas questões operacionais abrangem cinco métricas. A especificação e a regra conjunta estão na [visão geral operacional da Fase 2](../fase2/operacionais/visaoGeral.md).

### Q-OP-01 — Usabilidade

**Pergunta:** A interface da tela de planejamento atende às heurísticas ergonômicas de usabilidade essenciais para operação e apreensão autônoma?

**Procedimento:** [T1–T3 e inspeção individual/consenso](../fase3/operacionais/metodos.md#1-usabilidade-tch-e-isvh); reavaliação após M-01.

**Tabela 9 — Resultado e meta de Q-OP-01.**

| Métrica | Resultado / cálculo | Meta | Julgamento |
|---|---|---|---|
| MET-OP-01 — TCH | **80% → 100%** (8/10 → 10/10) | **≥85%** para Excelente | **Aceitável → Excelente** |
| MET-OP-01b — ISVH | **4 → 0** pontos | **≤5**, sem maior/catastrófico | **Excelente → Excelente** |

*Fonte: registro da avaliação EC-01, organizado pela equipe, conforme as metas e regras de decisão da Fase 2.*

**Resposta:** Aceitável antes; Excelente após a melhoria. Gustavo e Gabriel consolidaram dois problemas menores, nos itens 2 e 9. M-01 acrescentou explicações dos termos e do ajuste de créditos. Os dois itens passaram a conformes, sem regressão nos outros oito. O julgamento usa o pior nível entre TCH e ISVH.

**Hipótese H-OP-01:** A interface pode apresentar violações heurísticas relevantes nas tarefas avaliadas. **Julgamento: Corroborada antes; não corroborada no checklist após M-01.**

**Onde conferir:** [resposta formal](operacionais/analiseResultados.md#q-op-01-a-interface-da-tela-de-planejamento-atende-as-heuristicas-ergonomicas-de-usabilidade-essenciais-para-operacao-e-apreensao-autonoma) · [registro da avaliação](operacionais/dadosBrutos.md#2-usabilidade).

**Comparação da melhoria:** [M-01 e resultados antes/depois](operacionais/acaoMelhoria.md#4-comparacao-das-metricas).

### Q-OP-02 — Segurança

**Pergunta:** O sistema protege os dados acadêmicos e os serviços examinados contra exposição no cliente, vulnerabilidades conhecidas e acesso não autorizado?

**Procedimento:** [INV-01, três estados de armazenamento e bateria de acesso](../fase3/operacionais/metodos.md).

**Tabela 10 — Resultado e meta de Q-OP-02.**

| Métrica | Resultado / cálculo | Meta | Julgamento |
|---|---|---|---|
| MET-OP-02 — IRP | **3 pontos** = 2×1 + 1×1 | **≤5**, sem críticas/altas | **Excelente no inventário** |
| MET-OP-02b — GED-C | **3 chaves** na união dos estados | **0 chaves** | **Não conforme** |
| MET-OP-02c — TBR | 10/10 = **100%** | **100%** na bateria completa | **Conforme no recorte** |

*Fonte: registro da avaliação EC-01, organizado pela equipe, conforme as metas e regras de decisão da Fase 2.*

**Resposta:** Com ressalva por armazenamento. IRP atende à faixa Excelente no inventário e a bateria de dez condições atende à meta de bloqueio. Entretanto, GED-C=3 contraria a meta zero; os dois resultados favoráveis não compensam essa exposição. M-01 não alterou a persistência.

**Hipótese H-OP-02:** Dependências, persistência em claro ou falhas de acesso podem comprometer os dados e serviços examinados. **Julgamento: Corroborada no componente de armazenamento.**

**Onde conferir:** [resposta formal](operacionais/analiseResultados.md#q-op-02-o-sistema-protege-os-dados-academicos-e-os-servicos-examinados-contra-exposicao-no-cliente-vulnerabilidades-conhecidas-e-acesso-nao-autorizado) · [registro da avaliação](operacionais/dadosBrutos.md#4-armazenamento-ged-c).

**Registros complementares:** [INV-01](operacionais/dadosBrutos.md#3-dependencias-inventario-inv-01) · [dez condições de acesso](operacionais/dadosBrutos.md#5-controle-de-acesso-bateria-de-dez-condicoes).

## 4. Conferência do encerramento

A Tabela 11 reúne os produtos da Fase 4 e seus pontos de consulta.

**Tabela 11 — Conferência dos produtos da avaliação.**

| O que precisava ser entregue | Situação | Onde está |
|---|---|---|
| Comparar as sete métricas funcionais com as metas | **Documentado** | [Consolidado funcional](metricasFuncionais.md#resultados-consolidados) |
| Comparar as cinco métricas operacionais com as metas | **Documentado** | [Consolidado operacional](metricasOperacionais.md#quadro-de-resumo) |
| Responder às nove questões GQM | **9/9 respondidas** | Seções 2 e 3 desta página |
| Julgar as nove hipóteses | **9/9 julgadas** | [Hipóteses funcionais](funcionais/analiseResultados.md#4-julgamento-das-hipoteses-funcionais) e [operacionais](operacionais/analiseResultados.md#5-julgamento-das-hipoteses-operacionais) |
| Definir e comparar a melhoria M-01 | **Antes/depois documentado** | [Intervenção e reavaliação](operacionais/acaoMelhoria.md) |
| Integrar o julgamento da qualidade e justificá-lo | **Documentado** | [Julgamento integrado](conclusao.md#2-julgamento-integrado) |
| Encaminhar recomendações com critérios de verificação | **Documentado** | [Recomendações finais](conclusao.md#3-recomendacoes-finais) |
| Preservar a ligação com propósito, modelo e planejamento | **Documentado** | [Rastreabilidade das fases](../fase3/operacionais/rastreabilidade.md) |

*Fonte: registro da avaliação EC-01, organizado pela equipe, conforme as metas e regras de decisão da Fase 2.*

## 5. Referências

Referências usadas nesta página, conforme [Referências — Fase 2](../../referencias/fase2.md) e [Referências — Fase 3](../../referencias/fase3.md).

- BASILI, Victor R.; CALDIERA, Gianluigi; ROMBACH, H. Dieter. **The Goal Question Metric Approach**. *Encyclopedia of Software Engineering*, v. 1, p. 528-532, 1994.
- NIELSEN, Jakob. **10 Usability Heuristics for User Interface Design**. Nielsen Norman Group, 1994. Disponível em: <https://www.nngroup.com/articles/ten-usability-heuristics/>.
- NIELSEN, Jakob. **Severity Ratings for Usability Problems**. Nielsen Norman Group, 1995. Disponível em: <https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/>. Acesso em: 14 nov. 2026.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
|---|---|---|---|
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Rastreabilidade completa das questões, métricas, hipóteses e produtos da Fase 4 | 16/11 | [d9d7c15](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/d9d7c1591b6995089cd520a3cca24091f2566c13) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Remoção das orientações de apresentação da rastreabilidade | 16/11 | [d9d7c15](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/d9d7c1591b6995089cd520a3cca24091f2566c13) |
| [Yasmim de Souza Santos](https://github.com/eii-yahs) | Inclusão das referências utilizadas na página | 22/11 | Não commitado |
