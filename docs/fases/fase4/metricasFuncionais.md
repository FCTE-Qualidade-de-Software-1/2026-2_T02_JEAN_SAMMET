# Avaliação funcional — Fase 4

A coleta com H0 está registrada e apurada. O principal achado é a omissão de **FGA0206**: 14 das 15 obrigatórias pendentes foram contempladas. Não foram observadas divergências nos 44 registros/status, nas oito equivalências e no par de co-requisitos testado.

## Resultados consolidados

Avaliação com o histórico **H0**, conforme as metas da [Fase 2](../fase2/funcionais/GQM.md). Nos indicadores de violações e erros, **0% é o resultado esperado**. Os julgamentos se restringem às unidades verificadas.

| Métrica | Cálculo observado | Resultado | Meta | Julgamento |
|---|---|---|---|---|
| **MET-FUN-01 — TVP:** violações de pré-requisitos | 0/1 | **0,00%** | 0% | **Conforme no recorte** |
| **MET-FUN-02 — TVC:** violações de co-requisitos | 0/2 | **0,00%** | 0% | **Conforme no par testado** |
| **MET-FUN-03 — CDO:** cobertura de obrigatórias | 14/15 | **93,33%** | 100% | **Não conforme** |
| **MET-FUN-04 — TDH:** divergências no histórico | 0/44 | **0,00%** | 0% | **Conforme no recorte** |
| **MET-FUN-05 — TAE:** aplicações incorretas de equivalências | 0/8 | **0,00%** | 0% | **Conforme no recorte** |
| **MET-FUN-06 — COO:** expectativas atendidas no onboarding | 5/5 expectativas com regra verificável | **100,00% no recorte** | 100% | **Conforme — cobertura parcial** |
| **MET-FUN-07 — TVS:** violações de restrições | Máximo curricular: 0/23; demais tipos pendentes | **0,00% para o máximo de 480h** | 0% por tipo | **Pendente — cobertura incompleta** |

**Principal falha:** FGA0206 foi omitida do plano-base, reduzindo a cobertura das 15 obrigatórias pendentes para 14.

**Cobertura parcial:** em COO, duas expectativas sobre trabalho/estágio e objetivo ainda carecem de efeito obrigatório especificado. Em TVS, faltam fonte de oferta/calendário e confirmação de que a carga sugerida constitui teto rígido. O resultado de 0/23 vale apenas para o máximo curricular de 480h; não há percentual global de TVS.

A avaliação não permite declarar todas as métricas conformes. Os dados sustentam os resultados do recorte testado, com uma falha identificada e condições ainda pendentes.

## Evidências e análise

| Página | Conteúdo |
|---|---|
| [Dados brutos](funcionais/dadosBrutos.md) | Entrada, arquivos, unidades verificadas e reprocessamento |
| [Análise e julgamento](funcionais/analiseResultados.md) | Cálculos, cobertura, respostas GQM e hipóteses |
| [Respostas formais ao GQM](funcionais/analiseResultados.md#3-respostas-formais-as-questoes-gqm) | Resposta fundamentada a Q-FUN-01 até Q-FUN-07 |
| [Julgamento das hipóteses](funcionais/analiseResultados.md#4-julgamento-das-hipoteses-funcionais) | Veredito e justificativa de H-FUN-01 até H-FUN-07 |
| [Síntese da qualidade funcional](funcionais/analiseResultados.md#5-sintese-do-julgamento-da-qualidade-funcional) | Conclusão integrada, falha de completude e limites da avaliação |
| [Execução anterior](funcionais/execucaoAnterior.md) | Capturas preservadas com entrada e limitações identificadas |

Onboarding e restrições têm cobertura parcial: sugestões não foram tratadas como limites obrigatórios sem regra. Os resultados estão disponíveis para revisão da equipe; não concluem correção em outros históricos.

---

## Histórico de versão

| Membro | Contribuição | Data | Commit |
|---|---|---|---|
| Gabriel Mota | Consolidação dos resultados de CT-01 a CT-07 | 15/11 | [f469332](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f4693325fd9642696269942bb29aed671f0d8778) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Padronização da avaliação pelo histórico oficial H0 | 15/11 | [f454d2c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f454d2c099e16a6dd593b92420b541a18262b086) |
| [Gabriel Mota](https://github.com/Gabro-MO) | Recuperação das observações e capturas funcionais | 15/11 | [289a2a0](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/289a2a02674594fc05aed55ad7c8177ca8154bdd) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Alinhamento ao H0 e preservação das evidências anteriores com cobertura identificada | 15/11 | [7a74d9e](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/7a74d9e0809e91d60a36a88559b357bfe171f37e) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Coleta assistida com H0, apuração e julgamento com cobertura identificada | 15/11 | Não commitado |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Inclusão da tabela de resultados consolidados com metas, julgamentos e cobertura | 15/11 | Não commitado |
