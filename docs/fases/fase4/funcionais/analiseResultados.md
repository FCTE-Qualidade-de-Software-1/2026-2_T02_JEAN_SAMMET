# Análise e julgamento — Métricas funcionais

*[Voltar para a Matriz Geral de Rastreabilidade](../../../rastreabilidade.md)*

A execução **EC-01** aplica as fórmulas e metas do [GQM da Fase 2](../../fase2/funcionais/GQM.md) ao histórico H0. A referência contém **44 registros, 15 obrigatórias pendentes e oito equivalências**. Código e período preservam ocorrências distintas. Os [dados e capturas](dadosBrutos.md) identificam o registro de cada caso.

## 1. Métricas e cobertura

**Tabela 1 — Métricas e cobertura.**

| Métrica | Cálculo | Resultado | Meta | Julgamento |
| --- | --- | --- | --- | --- |
| **MET-FUN-01 — TVP** · pré-requisitos | 0/1 × 100 | **0,00%** | **0%** | **Conforme no recorte** |
| **MET-FUN-02 — TVC** · co-requisitos | 0/2 × 100 | **0,00%** | **0%** | **Conforme no par consolidado** |
| **MET-FUN-03 — CDO** · obrigatórias | 14/15 × 100 | **93,33%** | **100%** | **Não conforme** |
| **MET-FUN-04 — TDH** · histórico | 0/44 × 100 | **0,00%** | **0%** | **Conforme no recorte** |
| **MET-FUN-05 — TAE** · equivalências | 0/8 × 100 | **0,00%** | **0%** | **Conforme no recorte** |
| **MET-FUN-06 — COO** · onboarding | 5/7 × 100 | **71,43%** | **100%** | **Não conforme** |
| **MET-FUN-07 — TVS** · restrições | Máximo: 0/23; oferta: 1/10; calendário: 1/3 | **0,00%; 10,00%; 33,33%**, respectivamente | **0% por tipo** | **Não conforme em oferta e calendário** |

*Fonte: registro da avaliação EC-01, organizado pela equipe.* · [Voltar para a Matriz Geral de Rastreabilidade](../../../rastreabilidade.md)

Os julgamentos são relativos ao recorte. A aprovação projetada de uma disciplina em curso não modifica seu status acadêmico MATR. Os valores de TVS permanecem separados por tipo de restrição.

## 2. Interpretação dos resultados

**Tabela 2 — Interpretação dos resultados.**

| Caso | Esperado | Observado | Consequência |
| --- | --- | --- | --- |
| CT-01 | FGA0211 após o cumprimento projetado de FGA0170 | FGA0170 em 2026.2; FGA0211 em 2027.1 | Relação respeitada |
| CT-02 | Par consolidado alocado simultaneamente | FGA0072/FGA0074 em 2027.1 | Duas direções conformes |
| CT-03 | 15 obrigatórias contempladas | 14; FGA0206 ausente, inclusive da lista de não alocadas | Falha de completude |
| CT-04 | 44 ocorrências com período/status preservados | Nenhuma divergência confirmada | Fidelidade atendida no recorte |
| CT-05 | Seis equivalências concluídas e duas em andamento | Destinos e estados compatíveis | Nenhuma aplicação incorreta |
| CT-06 | Sete expectativas de carga e preferência atendidas | Cinco atendidas; trabalho e objetivo sem efeito exigido | Falha no contrato de preferências |
| CT-07 | Nenhuma violação por tipo | Sem excesso de 480h; uma oferta e um calendário divergentes | Falha em duas restrições |

*Fonte: registro da avaliação EC-01, organizado pela equipe.*

**Carga não é uma unidade única de julgamento.** Os planos de C0 foram 360/360/150h; C1, 300/420/150h; C2, 480/390h. As reservas explícitas de optativas entram na soma. A sugestão de carga não foi transformada em teto rígido: o limite obrigatório verificado foi **480h**. Os contratos de trabalho/objetivo são avaliados separadamente, em CT-06.

**Capturas distintas não são a mesma execução.** O registro de Gabriel mostra uma distribuição do par diferente da alocação consolidada. A avaliação preserva os dois registros em [CT-02](dadosBrutos.md#ct-02-co-requisitos), sem usar a imagem de uma execução para provar o resultado da outra.

## 3. Respostas formais às questões GQM

### Q-FUN-01 — O plano respeita os pré-requisitos oficiais?

**Resposta: sim, na relação avaliada.** FGA0170 permanece matriculada no semestre 2026.2 e FGA0211 foi posicionada em 2027.1. A interface distingue o semestre em curso da projeção condicionada à aprovação. Assim, a dependente não antecede a conclusão projetada do pré-requisito: `TVP = 0/1 × 100 = 0%`, atendendo à meta de zero violações.

O resultado não afirma que FGA0170 já foi aprovada. A sequência de TCC 1/2 ficou fora do cálculo porque não havia fonte oficial com vigência anexada para julgá-la nesta execução.

*[Voltar para a Matriz Geral de Rastreabilidade](../../../rastreabilidade.md)*

### Q-FUN-02 — O plano respeita os co-requisitos oficiais?

**Resposta: sim, no par explicitamente selecionado.** FGA0072 e FGA0074 apareceram na mesma coluna, 2027.1. As duas direções da relação recíproca foram verificadas e nenhuma foi violada: `TVC = 0/2 × 100 = 0%`.

A seleção das optativas não alterou os 44 registros acadêmicos de H0. O julgamento foi sustentado pela posição dos cartões, pelo registro do grafo e pela captura, e não apenas pelo texto de confirmação do recurso de seleção.

*[Voltar para a Matriz Geral de Rastreabilidade](../../../rastreabilidade.md)*

### Q-FUN-03 — Todas as disciplinas obrigatórias pendentes aplicáveis são contempladas?

**Resposta: não.** Das 15 obrigatórias pendentes de H0, 14 aparecem no plano-base completo: `CDO = 14/15 × 100 = 93,33%`, abaixo da meta de 100%. **FGA0206 foi omitida**, sem indicação na lista de disciplinas não alocadas.

A questão também utiliza TAE, pois equivalências incorretas poderiam alterar as pendências. As oito relações verificadas foram tratadas corretamente, mas esse resultado não compensa a omissão. Como uma das métricas aplicáveis não atende à meta, Q-FUN-03 é **Não conforme**.

*[Voltar para a Matriz Geral de Rastreabilidade](../../../rastreabilidade.md)*

### Q-FUN-04 — O histórico e os status são interpretados conforme as regras documentadas?

**Resposta: sim, nos 44 registros conferidos.** Foram preservados os 37 registros APR e os sete MATR, com suas ocorrências por código e período. Não houve divergência confirmada: `TDH = 0/44 × 100 = 0%`.

A comparação considera a representação de equivalências pelo código de destino oficial. Isso não elimina os registros originais da referência nem permite tratar uma disciplina matriculada como concluída. A projeção de aprovação no plano futuro foi distinguida do estado acadêmico real.

*[Voltar para a Matriz Geral de Rastreabilidade](../../../rastreabilidade.md)*

### Q-FUN-05 — As equivalências respeitam a fonte curricular e sua vigência?

**Resposta: sim, nas oito relações aplicáveis verificadas.** Seis equivalências concluídas foram reconhecidas como satisfeitas, sem duplicação indevida nas pendências futuras; as duas em andamento mantiveram a condição de matrícula. O resultado foi `TAE = 0/8 × 100 = 0%`, atendendo à meta.

O julgamento cobre as relações documentadas para H0. Não valida automaticamente outras matrizes, cadeias de equivalência ou vigências que não fizeram parte da referência.

*[Voltar para a Matriz Geral de Rastreabilidade](../../../rastreabilidade.md)*

### Q-FUN-06 — O onboarding produz o comportamento documentado ou prometido?

**Resposta: não integralmente.** Foram atendidas cinco das sete expectativas: as representações de 20/32 créditos e as sugestões de 4/6/8 matérias. Os contratos de trabalho e objetivo não foram atendidos. Portanto, `COO = 5/7 × 100 = 71,43%`, abaixo da meta de 100%.

Em C3, o contrato exige sugestão de 20 créditos ao ativar trabalho/estágio; a configuração permaneceu em 24. Em C4, o contrato exige horizonte de dois semestres futuros para a opção velocidade, mas foram mantidos três. Os contratos e a comparação estão em [Dados brutos](dadosBrutos.md#ct-06-onboarding). Esses valores são critérios do cenário de aceitação; não são apresentados como exigências curriculares da UnB.

*[Voltar para a Matriz Geral de Rastreabilidade](../../../rastreabilidade.md)*

### Q-FUN-07 — O plano respeita oferta, semestre inicial e limites de carga verificáveis?

**Resposta: não em todos os tipos examinados.** O máximo de 480h foi respeitado em 23 verificações (`0/23 = 0%`). Na oferta, uma de dez alocações divergiu do quadro de referência (`1/10 = 10%`). No calendário, um de três casos usou semestre inicial diferente do esperado (`1/3 = 33,33%`). A meta de cada tipo é 0%.

No caso de falha de consulta do período, o controle CAL-01 estabelece 2027.1, enquanto a execução inicia em 2027.2. Essa diferença sustenta o julgamento da hipótese de calendário. O resultado favorável de carga não elimina os dois tipos não conformes.

*[Voltar para a Matriz Geral de Rastreabilidade](../../../rastreabilidade.md)*

## 4. Julgamento das hipóteses funcionais

**Tabela 3 — Julgamento das hipóteses funcionais.**

| Hipótese | Julgamento | Fundamentação |
| --- | --- | --- |
| **H-FUN-01 — Violação de pré-requisitos** | **Não corroborada no recorte** | FGA0170→FGA0211 respeitada na projeção; TVP=0/1. |
| **H-FUN-02 — Violação de co-requisitos** | **Não corroborada na execução consolidada** | Par em 2027.1; TVC=0/2. O registro distinto de Gabriel não é misturado ao denominador. |
| **H-FUN-03 — Omissão de obrigatórias** | **Corroborada** | FGA0206 ausente; CDO=14/15. |
| **H-FUN-04 — Tratamento indevido de matrícula** | **Não corroborada no recorte** | TDH=0/44; matrícula e projeção diferenciadas. |
| **H-FUN-05 — Equivalências sem respeito a relações/vigência** | **Não corroborada nas oito relações** | TAE=0/8; seis concluídas e duas em andamento tratadas corretamente. |
| **H-FUN-06 — Preferências sem o efeito prometido** | **Corroborada nos contratos de C3/C4** | Duas expectativas não atendidas; COO=5/7. |
| **H-FUN-07 — Semestre estimado divergente do calendário** | **Corroborada no caso de falha de consulta** | Um início em 2027.2 quando CAL-01 exige 2027.1. |

*Fonte: registro da avaliação EC-01, organizado pela equipe.*

“Não corroborada” descreve a ausência de falha no recorte; não significa prova de correção para todo o produto. A conclusão principal utiliza a execução consolidada e mantém as capturas com seus identificadores.

## 5. Síntese do julgamento da qualidade funcional

**A adequação funcional não atende integralmente às metas.** Há falha de completude, desconformidade nas preferências e divergências de oferta/calendário. Ao mesmo tempo, os registros acadêmicos, as equivalências e as relações curriculares selecionadas apresentaram resultados favoráveis no recorte consolidado.

As prioridades são contemplar FGA0206, implementar os efeitos definidos para trabalho/objetivo e validar oferta e período antes da alocação. As métricas não são somadas em uma nota média: percentuais de erros, cobertura e expectativas têm unidades diferentes.

## 6. Limites da conclusão

A entrada é H0 e os cenários são variações desse histórico, não estudantes independentes. TCC 1/2 e outras relações apenas ilustradas nas capturas não ampliam automaticamente o denominador de pré-requisitos. O commit público não identifica a versão implantada. Não se extrapolam os resultados para todas as matrizes, dispositivos ou condições de uso.

As recomendações funcionais permanecem no [encerramento](../conclusao.md); a intervenção de interface e sua comparação estão na [ação de melhoria](../operacionais/acaoMelhoria.md).

## 7. Referências

Referências usadas nesta página, conforme [Referências — Fase 3](../../../referencias/fase3.md).

- BASILI, Victor R.; CALDIERA, Gianluigi; ROMBACH, H. Dieter. **The Goal Question Metric Approach**. *Encyclopedia of Software Engineering*, v. 1, p. 528-532, 1994.

---

## Histórico de versão

| Membro | Contribuição | Data | Commit |
|---|---|---|---|
| Gabriel Mota | Consolidação das observações CT-01 a CT-07, cálculo e respostas GQM | 15/11 | [1bc6aca](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/1bc6acac9640bf2f81bd53039c24ab5507f88b92) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Padronização da avaliação pelo histórico oficial H0 | 15/11 | [f454d2c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f454d2c099e16a6dd593b92420b541a18262b086) |
| [Gabriel Mota](https://github.com/Gabro-MO) | Recuperação das observações e capturas funcionais | 15/11 | [289a2a0](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/289a2a02674594fc05aed55ad7c8177ca8154bdd) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Alinhamento ao H0 e preservação das evidências anteriores com cobertura identificada | 15/11 | [7a74d9e](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/7a74d9e0809e91d60a36a88559b357bfe171f37e) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Coleta assistida com H0, apuração e julgamento com cobertura identificada | 15/11 | [f5e77d5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f5e77d5) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Ligação com a tabela de resultados consolidados da avaliação funcional | 15/11 | [f5e77d5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f5e77d5) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Ampliação da análise, respostas GQM e síntese dos julgamentos | 15/11 | [f5e77d5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f5e77d5) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Explicitação das metas nas tabelas de resultados e avaliação | 15/11 | [f5e77d5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f5e77d5) |
| [Yasmim de Souza Santos](https://github.com/eii-yahs) | Inclusão das referências utilizadas na página | 22/11 | Não commitado |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Inclusão de links de retorno para a Matriz Geral de Rastreabilidade na página, resultados e respostas GQM | 24/11 | [8f30292](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/8f302921912ed18ed6f6a18507c2bbab654f3366) |
