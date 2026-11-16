# Análise e julgamento — Métricas funcionais

Resultados derivados dos CSVs e das [evidências de H0](dadosBrutos.md), conforme as fichas da [Fase 2](../../fase2/funcionais/GQM.md). A coleta está disponível para revisão da equipe.

A [tabela de resultados consolidados](../metricasFuncionais.md#resultados-consolidados) reúne cálculo, resultado, meta e julgamento para consulta rápida.

## 1. Métricas e cobertura

| Métrica | Cálculo | Resultado | Meta | Julgamento e alcance |
|---|---|---|---|---|
| TVP — pré-requisitos | 0/1 | **0%** | 0% | Conforme na relação FGA0170→FGA0211; projeção condicionada à aprovação |
| TVC — co-requisitos | 0/2 | **0%** | 0% | Conforme no par FGA0072/FGA0074 explicitamente selecionado |
| CDO — obrigatórias | 14/15 | **93,33%** | 100% | **Não conforme:** FGA0206 omitida |
| TDH — histórico | 0/44 | **0%** | 0% | Conforme nos registros/status, com normalização das equivalências oficiais |
| TAE — aplicações incorretas de equivalências | 0/8 | **0%** | 0% | Conforme nas seis concluídas e duas em andamento |
| COO — onboarding | 5/5 expectativas válidas | **100% no recorte** | 100% | Representação de carga conforme; efeitos algorítmicos de C3/C4 pendentes |
| TVS — restrições | Máximo curricular: 0/23 | **0% nesse tipo** | 0% por tipo de restrição | Oferta/calendário e semântica do teto sugerido pendentes; sem percentual global |

Ausência de fonte ou de expectativa obrigatória não foi convertida em aprovação ou defeito.

## 2. Evidências determinantes

**Obrigatórias:** FGA0206 consta no quadro de pendências de H0 e não aparece no plano-base completo. A resposta também contém `materiasNaoAlocadas=[]`. A ausência da disciplina, e não essa lista isolada, fundamenta CDO=14/15.

**Co-requisitos:** após seleção pelo recurso de optativas, os cartões de FGA0072 (30h) e FGA0074 (60h) apareceram em **2027.1**. Cada direção foi conferida; os registros acadêmicos permaneceram em 37 APR/7 MATR. O texto do assistente não foi usado como única prova.

![Par de optativas no mesmo semestre](img/h0/ct02-par-2027-1.jpg)

*Figura 1 — Cartões de FGA0072/FGA0074 na coluna 2027.1. Fonte: No Fluxo, coleta de 15/11. Recorte sem identificação; cenário C0 com seleção explícita do par.*

**Cargas:** C0 gerou 360/360/150h; C1, 300/420/150h; C2, 480/390h. C5-4 gerou 240/240/300/90h; C5-6, 360/360/150h; C5-8, 480/390h. As somas incluem reservas identificadas. Há saídas acima da sugestão escolhida, mas nenhuma acima de 480h nas 23 verificações planejadas. Não se confirmou regra que torne toda sugestão um teto rígido.

## 3. Respostas formais às questões GQM

As respostas seguem as perguntas e regras de decisão da [Fase 2](../../fase2/funcionais/GQM.md). Um resultado favorável descreve as unidades verificadas; não comprova correção de toda a matriz ou de todos os históricos.

### Q-FUN-01 — O plano respeita os pré-requisitos oficiais?

**Resposta: sim, na relação avaliada.** FGA0170 permanece matriculada no semestre 2026.2 e FGA0211 foi posicionada em 2027.1. A interface distingue o semestre em curso da projeção condicionada à aprovação. Assim, a dependente não antecede a conclusão projetada do pré-requisito: `TVP = 0/1 × 100 = 0%`, atendendo à meta de zero violações.

O resultado não afirma que FGA0170 já foi aprovada. A sequência de TCC 1/2 ficou fora do cálculo porque não havia fonte oficial com vigência anexada para julgá-la nesta execução.

### Q-FUN-02 — O plano respeita os co-requisitos oficiais?

**Resposta: sim, no par explicitamente selecionado.** FGA0072 e FGA0074 apareceram na mesma coluna, 2027.1. As duas direções da relação recíproca foram verificadas e nenhuma foi violada: `TVC = 0/2 × 100 = 0%`.

A seleção das optativas não alterou os 44 registros acadêmicos de H0. O julgamento foi sustentado pela posição dos cartões, pelo registro do grafo e pela captura, e não apenas pelo texto de confirmação do recurso de seleção.

### Q-FUN-03 — Todas as disciplinas obrigatórias pendentes aplicáveis são contempladas?

**Resposta: não.** Das 15 obrigatórias pendentes de H0, 14 aparecem no plano-base completo: `CDO = 14/15 × 100 = 93,33%`, abaixo da meta de 100%. **FGA0206 foi omitida**, sem indicação na lista de disciplinas não alocadas.

A questão também utiliza TAE, pois equivalências incorretas poderiam alterar as pendências. As oito relações verificadas foram tratadas corretamente, mas esse resultado não compensa a omissão. Como uma das métricas aplicáveis não atende à meta, Q-FUN-03 é **Não conforme**.

### Q-FUN-04 — O histórico e os status são interpretados conforme as regras documentadas?

**Resposta: sim, nos 44 registros conferidos.** Foram preservados os 37 registros APR e os sete MATR, com suas ocorrências por código e período. Não houve divergência confirmada: `TDH = 0/44 × 100 = 0%`.

A comparação considera a representação de equivalências pelo código de destino oficial. Isso não elimina os registros originais da referência nem permite tratar uma disciplina matriculada como concluída. A projeção de aprovação no plano futuro foi distinguida do estado acadêmico real.

### Q-FUN-05 — As equivalências respeitam a fonte curricular e sua vigência?

**Resposta: sim, nas oito relações aplicáveis verificadas.** Seis equivalências concluídas foram reconhecidas como satisfeitas, sem duplicação indevida nas pendências futuras; as duas em andamento mantiveram a condição de matrícula. O resultado foi `TAE = 0/8 × 100 = 0%`, atendendo à meta.

O julgamento cobre as relações documentadas para H0. Não valida automaticamente outras matrizes, cadeias de equivalência ou vigências que não fizeram parte da referência.

### Q-FUN-06 — O onboarding produz o comportamento documentado ou prometido?

**Resposta: parcialmente demonstrado.** As cinco expectativas verificáveis de representação da carga foram atendidas: `COO = 5/5 × 100 = 100% no recorte`. Os valores enviados e representados foram compatíveis com as configurações de carga examinadas.

As duas expectativas sobre trabalho/estágio e objetivo do planejamento continuam **pendentes de especificação**. Os planos observados não bastam para decidir que essas opções necessariamente deveriam alterar a seleção de disciplinas. Portanto, o percentual favorável não encerra a questão: o julgamento permanece **Conforme no recorte, com cobertura parcial**.

### Q-FUN-07 — O plano respeita oferta, semestre inicial e limites de carga verificáveis?

**Resposta: o máximo curricular foi respeitado; a resposta global permanece pendente.** Nenhuma das 23 verificações de carga futura ultrapassou 480h, incluindo as reservas explícitas de optativas: `TVS máximo curricular = 0/23 × 100 = 0%`.

Faltam referências suficientes para julgar oferta/calendário e para estabelecer se a carga sugerida deve funcionar como teto rígido. Uma saída acima da sugestão escolhida não foi classificada como defeito sem essa regra. As restrições são apuradas por tipo, sem somar unidades de naturezas distintas em um percentual global.

## 4. Julgamento das hipóteses funcionais

| Hipótese | Julgamento | Fundamentação e alcance |
|---|---|---|
| **H-FUN-01 — Violação de pré-requisitos** | **Não corroborada na relação testada** | FGA0170→FGA0211 respeitada na projeção condicionada à aprovação; TVP=0/1. Outras relações não foram integralmente avaliadas. |
| **H-FUN-02 — Violação de co-requisitos** | **Não corroborada no par testado** | FGA0072/FGA0074 alocadas em 2027.1; TVC=0/2. |
| **H-FUN-03 — Omissão de obrigatórias pendentes** | **Corroborada** | FGA0206 ausente; CDO=14/15, inferior à meta de 100%. |
| **H-FUN-04 — Tratamento indevido de disciplinas em andamento** | **Não corroborada no recorte** | TDH=0/44; status acadêmico MATR separado da aprovação projetada. |
| **H-FUN-05 — Equivalências ignorando relações ou vigência** | **Não corroborada nas relações verificadas** | TAE=0/8, sem erro confirmado de reconhecimento, status ou efeito nas pendências. Não abrange cadeias fora de H0. |
| **H-FUN-06 — Opções do onboarding sem o efeito prometido** | **Inconclusiva para a hipótese completa** | Cinco expectativas de carga atendidas; efeitos obrigatórios de trabalho/estágio e objetivo ainda não especificados. |
| **H-FUN-07 — Divergência do semestre estimado em relação ao calendário oficial** | **Inconclusiva** | A ausência de violação do máximo de 480h não verifica a hipótese sobre calendário/falha de consulta do período. Falta a referência e a condição correspondente. |

“Não corroborada” significa que o problema não foi observado no recorte; não representa prova de inexistência em todo o produto.

## 5. Síntese do julgamento da qualidade funcional

O plano preservou os registros de H0, aplicou corretamente as equivalências verificadas e respeitou as relações de pré/co-requisito examinadas. Esses resultados demonstram atendimento às metas nesses recortes de correção funcional.

Entretanto, **a completude funcional não atingiu a meta**, pois uma obrigatória pendente foi omitida. Um plano aparentemente válido por semestre pode continuar incompleto; por isso, a lista vazia de disciplinas não alocadas não deve ser tomada como garantia de cobertura curricular.

A avaliação funcional é, portanto, **favorável nos recortes conformes, com falha comprovada de completude e cobertura ainda parcial em onboarding e restrições**. Não foi calculada uma média das sete métricas: seus numeradores, metas e unidades representam aspectos diferentes. A prioridade funcional é investigar FGA0206 e repetir CT-03, conferindo também relações e equivalências após a correção.

## 6. Limitações

Um único histórico e configurações pareadas não representam todos os alunos. A versão do servidor não foi identificada; datas e respostas foram preservadas por execução. A aprovação do semestre atual é projetada condicionalmente, sem modificar o status acadêmico MATR. Os resultados devem ser repetidos se houver mudança relevante no produto.

---

## Histórico de versão

| Membro | Contribuição | Data | Commit |
|---|---|---|---|
| Gabriel Mota | Consolidação das observações CT-01 a CT-07, cálculo e respostas GQM | 15/11 | [1bc6aca](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/1bc6acac9640bf2f81bd53039c24ab5507f88b92) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Padronização da avaliação pelo histórico oficial H0 | 15/11 | [f454d2c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f454d2c099e16a6dd593b92420b541a18262b086) |
| [Gabriel Mota](https://github.com/Gabro-MO) | Recuperação das observações e capturas funcionais | 15/11 | [289a2a0](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/289a2a02674594fc05aed55ad7c8177ca8154bdd) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Alinhamento ao H0 e preservação das evidências anteriores com cobertura identificada | 15/11 | [7a74d9e](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/7a74d9e0809e91d60a36a88559b357bfe171f37e) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Coleta assistida com H0, apuração e julgamento com cobertura identificada | 15/11 | Não commitado |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Ligação com a tabela de resultados consolidados da avaliação funcional | 15/11 | Não commitado |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Ampliação da análise, respostas GQM e síntese dos julgamentos | 15/11 | Não commitado |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Explicitação das metas nas tabelas de resultados e avaliação | 15/11 | Não commitado |
