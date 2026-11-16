# Rastreabilidade da avaliação

A matriz liga as necessidades da Fase 1 às perguntas e metas da Fase 2, aos procedimentos da Fase 3 e aos resultados de EC-01. Sete questões funcionais e duas operacionais cobrem as doze métricas.

**Tabela 1 — Rastreabilidade da avaliação.**

| Necessidade | Questão / hipótese | Métrica | Procedimento | Resultado / meta | Resposta e registro |
| --- | --- | --- | --- | --- | --- |
| Sequência curricular | Q-FUN-01 / H-FUN-01 | TVP | [CT-01](../funcionais/roteiro.md) | **0% / 0%** | [Registro](../../fase4/funcionais/dadosBrutos.md#ct-01-pre-requisitos) · [Resposta GQM](../../fase4/funcionais/analiseResultados.md#q-fun-01-o-plano-respeita-os-pre-requisitos-oficiais) |
| Co-requisitos | Q-FUN-02 / H-FUN-02 | TVC | [CT-02](../funcionais/roteiro.md) | **0% / 0%** | [Registro](../../fase4/funcionais/dadosBrutos.md#ct-02-co-requisitos) · [Resposta GQM](../../fase4/funcionais/analiseResultados.md#q-fun-02-o-plano-respeita-os-co-requisitos-oficiais) |
| Obrigatórias contempladas | Q-FUN-03 / H-FUN-03 | CDO | [CT-03](../funcionais/roteiro.md) | **93,33% / 100%** | [Registro](../../fase4/funcionais/dadosBrutos.md#ct-03-obrigatorias-pendentes) · [Resposta GQM](../../fase4/funcionais/analiseResultados.md#q-fun-03-todas-as-disciplinas-obrigatorias-pendentes-aplicaveis-sao-contempladas) |
| Histórico preservado | Q-FUN-04 / H-FUN-04 | TDH | [CT-04](../funcionais/roteiro.md) | **0% / 0%** | [Registro](../../fase4/funcionais/dadosBrutos.md#ct-04-tratamento-do-historico) · [Resposta GQM](../../fase4/funcionais/analiseResultados.md#q-fun-04-o-historico-e-os-status-sao-interpretados-conforme-as-regras-documentadas) |
| Equivalências válidas | Q-FUN-05 / H-FUN-05 | TAE | [CT-05](../funcionais/roteiro.md) | **0% / 0%** | [Registro](../../fase4/funcionais/dadosBrutos.md#ct-05-equivalencias) · [Resposta GQM](../../fase4/funcionais/analiseResultados.md#q-fun-05-as-equivalencias-respeitam-a-fonte-curricular-e-sua-vigencia) |
| Preferências com efeito | Q-FUN-06 / H-FUN-06 | COO | [CT-06](../funcionais/roteiro.md) | **71,43% / 100%** | [Registro](../../fase4/funcionais/dadosBrutos.md#ct-06-onboarding) · [Resposta GQM](../../fase4/funcionais/analiseResultados.md#q-fun-06-o-onboarding-produz-o-comportamento-documentado-ou-prometido) |
| Restrições atendidas | Q-FUN-07 / H-FUN-07 | TVS | [CT-07](../funcionais/roteiro.md) | **0%; 10%; 33,33% / 0% por tipo** | [Registro](../../fase4/funcionais/dadosBrutos.md#ct-07-restricoes-semestrais) · [Resposta GQM](../../fase4/funcionais/analiseResultados.md#q-fun-07-o-plano-respeita-oferta-semestre-inicial-e-limites-de-carga-verificaveis) |
| Interface operável | Q-OP-01 / H-OP-01 | TCH | T1–T3 e checklist | **80%→100% / ≥85%** | [Notas](../../fase4/operacionais/avaliacaoUsabilidade.md) · [Antes/depois](../../fase4/operacionais/acaoMelhoria.md#4-comparacao-das-metricas) |
| Problemas de uso controlados | Q-OP-01 / H-OP-01 | ISVH | Severidade e consenso | **4→0 / ≤5, sem maior/catastrófico** | [Consenso](../../fase4/operacionais/avaliacaoUsabilidade.md#3-calculo-e-julgamento) |
| Dependências no inventário | Q-OP-02 / H-OP-02 | IRP | INV-01 e pesos | **3 / ≤5, sem crítica/alta** | [Inventário](../../fase4/operacionais/dadosBrutos.md#3-dependencias-inventario-inv-01) |
| Proteção de dados no cliente | Q-OP-02 / H-OP-02 | GED-C | Inspeção dos três estados | **3 / 0 chaves** | [Estados e chaves](../../fase4/operacionais/dadosBrutos.md#4-armazenamento-ged-c) |
| Acesso restrito | Q-OP-02 / H-OP-02 | TBR | Controle positivo e dez condições | **100% / 100%** | [Bateria](../../fase4/operacionais/dadosBrutos.md#5-controle-de-acesso-bateria-de-dez-condicoes) |

*Fonte: elaboração da equipe, conforme os registros e referências desta página.*

A relação TAE também apoia Q-FUN-03, pois equivalências afetam a lista de pendências. A [análise funcional](../../fase4/funcionais/analiseResultados.md#4-julgamento-das-hipoteses-funcionais) e a [operacional](../../fase4/operacionais/analiseResultados.md#5-julgamento-das-hipoteses-operacionais) contêm todos os vereditos. O [encerramento](../../fase4/conclusao.md) responde ao propósito da Fase 1 e reúne as recomendações.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Criação da matriz de rastreabilidade bidirecional completa da Fase 1 à Fase 4 para métricas operacionais | 14/11 | [6594e5c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/6594e5c2349ee5fc4dc632f07b97bc8191357819) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Rastreabilidade das doze métricas aos procedimentos e às evidências | 15/11 | [aa0c61f](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/aa0c61fac5e9d2db19adec76fd052a2bb6b04b90) |