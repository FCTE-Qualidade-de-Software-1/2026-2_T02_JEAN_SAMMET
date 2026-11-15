# Análise dos Resultados e Julgamento — Métricas Funcionais (Fase 4)

> **Conclusão desta versão: inconclusiva por ausência de execução formal.** As regras e os critérios estão definidos na Fase 2, mas não há linhas de verificação funcional na coleta da Fase 4 e o piloto não gerou um plano completo. Não calcular percentuais com denominador inexistente nem interpretar ausência de registro como resultado igual a zero.

## 1. Método de processamento

A unidade de análise é a relação, disciplina pendente, verificação de status, equivalência, expectativa ou restrição efetivamente examinada no respectivo caso. Só compõem o denominador os registros com `conforme=1` ou `conforme=0`, evidência rastreável e fonte/regra identificada. Registros em branco, pendentes, não aplicáveis ou sem evidência são informados como cobertura ausente e não entram no cálculo.

As fórmulas e metas reproduzem o [GQM da Fase 2](../../fase2/funcionais/GQM.md). Para métricas de erro, `conforme=0` representa uma violação; para métricas de cobertura/conformidade, `conforme=1` representa uma unidade atendida. `MET-FUN-07` é calculada por tipo de restrição quando a fonte ou a unidade de aferição diferir.

## 2. Cálculo e confronto das sete métricas

| Métrica | Fórmula | Meta da Fase 2 | Evidência válida nesta versão | Resultado / julgamento |
| :---: | :--- | :---: | :---: | :--- |
| `MET-FUN-01` — TVP | `(NVP / NRP) × 100` | `0%` | `NRP`: não disponível | **Não calculado — pendente de CT-01** |
| `MET-FUN-02` — TVC | `(NVC / NRC) × 100` | `0%` | `NRC`: não disponível | **Não calculado — pendente de CT-02** |
| `MET-FUN-03` — CDO | `(DPC / DOP) × 100` | `100%` | `DOP` e `DPC`: não disponíveis | **Não calculado — pendente de CT-03** |
| `MET-FUN-04` — TDH | `(NDH / NVH) × 100` | `0%` | `NVH`: não disponível | **Não calculado — pendente de CT-04** |
| `MET-FUN-05` — TAE | `(NEI / NRE) × 100` | `0%` | `NRE`: não disponível | **Não calculado — pendente de CT-05** |
| `MET-FUN-06` — COO | `(NEC / NEV) × 100` | `100%` | `NEV`: não disponível; expectativas parciais | **Não calculado — pendente de especificação e CT-06** |
| `MET-FUN-07` — TVS | `(NVS / NRS) × 100`, por tipo | `0%` | `NRS`: não disponível | **Não calculado — pendente de CT-07** |

Não há numerador igual a zero a reportar: os numeradores também não foram observados. Um denominador igual a zero ou ausente não representa aprovação e não autoriza classificar a métrica como Não aplicável, salvo quando a regra conhecida efetivamente não se aplica à entrada. Na situação atual, a falta do histórico carregado e do plano final é pendência de execução/coleta.

### 2.1 Evidência parcial do piloto

A exploração de 15/11 identificou a matriz 6360/1, as opções de carga e o recálculo visual do controle de créditos. A captura preservada mostra um valor intermediário de 14 créditos/210h, enquanto 24 créditos/360h foi registrado como referência no piloto. Como a execução não gerou um plano final e não registrou as alocações por semestre, a observação não fornece numerador ou denominador para `MET-FUN-06` ou `MET-FUN-07`. Tampouco permite inferir as métricas de pré-requisito, co-requisito, cobertura, status ou equivalência.

## 3. Validação das hipóteses funcionais

| Hipótese | Caso / métrica | Evidência exigida | Estado nesta versão | Veredito |
| :---: | :--- | :--- | :--- | :--- |
| `H-FUN-01` | `CT-01` / `MET-FUN-01` | Relações de pré-requisito presentes em `H0`, fonte/vigência e semestres do plano completo. | Plano final não gerado; sem relações observadas. | **Não avaliada** |
| `H-FUN-02` | `CT-02` / `MET-FUN-02` | Par co-requisitado aplicável à entrada e alocação no plano. | Seleção do par no planejador ainda não confirmada. | **Não avaliada** |
| `H-FUN-03` | `CT-03` / `MET-FUN-03` | Lista de obrigatórias satisfeitas e pendentes em `H0`, cruzada com todos os semestres do plano. | `H0` não está disponível no pacote e não há plano final. | **Não avaliada** |
| `H-FUN-04` | `CT-04` / `MET-FUN-04` | Status reais presentes na entrada e tratamento observado para cada categoria. | Importação e saída não registradas. | **Não avaliada** |
| `H-FUN-05` | `CT-05` / `MET-FUN-05`; impacto em `CT-03` | Equivalência presente em `H0`, regra oficial e efeito sobre pendências. | A equivalência MAT0138/MAT0026 foi consultada na fonte, mas sua ocorrência na entrada não foi confirmada. | **Não avaliada** |
| `H-FUN-06` | `CT-06` / `MET-FUN-06` | Expectativa verificável por opção, valores aceitos e comparação pareada. | Opções foram observadas; efeitos de trabalho/estágio e objetivo carecem de especificação identificável. | **Pendente de especificação e execução** |
| `H-FUN-07` | `CT-07` / `MET-FUN-07` | Cargas alocadas por semestre, limites e calendário/oferta para o período. | Apenas controle e recálculo visual observados; sem plano final ou calendário de coleta. | **Não avaliada** |

As hipóteses são riscos a verificar, não defeitos presumidos. A ausência de teste não confirma nem refuta qualquer hipótese.

## 4. Respostas formais às questões GQM

| Questão | Métricas | Estado consolidado |
| :---: | :--- | :--- |
| `Q-FUN-01` — O plano respeita os pré-requisitos oficiais? | `MET-FUN-01` | **Pendente de execução** |
| `Q-FUN-02` — O plano respeita os co-requisitos oficiais? | `MET-FUN-02` | **Pendente de execução** |
| `Q-FUN-03` — Todas as obrigatórias pendentes aplicáveis são contempladas? | `MET-FUN-03`, `MET-FUN-05` | **Pendente de execução** |
| `Q-FUN-04` — O histórico e os status são interpretados conforme as regras documentadas? | `MET-FUN-04` | **Pendente de execução** |
| `Q-FUN-05` — As equivalências respeitam a fonte curricular e sua vigência? | `MET-FUN-05` | **Pendente de execução** |
| `Q-FUN-06` — O onboarding produz o comportamento documentado ou prometido? | `MET-FUN-06` | **Pendente de especificação e execução** |
| `Q-FUN-07` — O plano respeita oferta, semestre inicial e limites de carga verificáveis? | `MET-FUN-07` | **Pendente de execução** |

### 4.1 Resposta formal a `Q-FUN-01`

**Não é possível concluir nesta versão.** Não há plano completo nem relações de pré-requisito extraídas da entrada `H0` para comparar com os semestres planejados. As regras oficiais de FGA0211 e MAT0026 documentam exemplos de referência, mas não demonstram que essas relações estejam presentes no histórico autorizado nem como o motor as tratou. A questão permanece pendente até a execução de `CT-01`.

### 4.2 Resposta formal a `Q-FUN-02`

**Não é possível concluir nesta versão.** O par FGA0072/FGA0074 e suas regras foram identificados no SIGAA, mas a presença do par na entrada e a possibilidade de seleção no planejador ainda não foram verificadas. Sem uma relação aplicável e um plano observado, não há denominador para `TVC`; a questão permanece pendente até `CT-02`.

### 4.3 Resposta formal a `Q-FUN-03`

**Não é possível concluir nesta versão.** A matriz de referência lista 39 componentes obrigatórios no recorte documentado, mas o conjunto de pendências depende do histórico real e das equivalências válidas nele presentes. A lista esperada não foi calculada para `H0` e o plano final não foi gerado. `MET-FUN-03` e o efeito de `MET-FUN-05` sobre as pendências permanecem sem mensuração; isso não significa cobertura de 100% nem ausência de omissões.

### 4.4 Resposta formal a `Q-FUN-04`

**Não é possível concluir nesta versão.** Não há comparação registrada entre os status de entrada, a interpretação do sistema e o tratamento no plano. Em particular, não se pode afirmar que disciplinas em andamento foram tratadas como aprovadas, nem que foram tratadas corretamente. A política para projeção de conclusão deve ser identificada e comparada em `CT-04`.

### 4.5 Resposta formal a `Q-FUN-05`

**Não é possível concluir nesta versão.** A equivalência MAT0138/MAT0026 foi confirmada na referência curricular, mas não há evidência de que MAT0138 ocorra em `H0` nem de como o motor atualiza as pendências. Não se presume equivalência transitiva. A questão permanece pendente até um caso aplicável e documentado em `CT-05`.

### 4.6 Resposta formal a `Q-FUN-06`

**Não é possível concluir nesta versão.** O piloto observou opções de trabalho/estágio, quantidade de matérias e objetivo, mas não foram registrados pares de planos com uma opção alterada por vez. Além disso, o efeito algorítmico esperado de trabalho/estágio e objetivo ainda não tem especificação identificável. A `COO` não deve considerar como erro a ausência de uma mudança que não tenha sido prometida. A questão depende da especificação e da execução de `CT-06`.

### 4.7 Resposta formal a `Q-FUN-07`

**Não é possível concluir nesta versão.** O piloto observou 24 créditos/360h como referência e recálculo do controle, mas não registrou a carga de cada semestre no plano gerado. Também faltam evidências do calendário e da oferta do período avaliado. A conversão apresentada no controle não substitui a conferência das alocações e do limite curricular de 480h. A questão permanece pendente até `CT-07`.

## 5. Rastreabilidade das issues

| Issue | Entrega relacionada | Situação comprovável nesta versão |
| :--- | :--- | :--- |
| [#27 — Executar Testes e Coletar Dados Brutos (Fase 4)](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/issues/27) | Preservar logs, capturas e formulários de execução. | **Parcial:** a observação exploratória do piloto está registrada; `CT-01` a `CT-07` ainda não têm execução formal nem plano final como evidência. |
| [#28 — Processar Métricas e Responder às Questões GQM](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/issues/28) | Calcular resultados, comparar critérios e responder às questões. | **Estrutura e processamento preparados; resultado empírico pendente:** fórmulas, processador e respostas formais estão documentados, mas não existem numeradores/denominadores para calcular valores reais. |

## 6. Próximas condições para encerramento

1. Confirmar a importação do histórico oficial autorizado `H0` sem copiar seus dados pessoais para o repositório.
2. Concluir a geração do plano no cenário `C0` e preservar uma captura/log sanitizado do plano completo.
3. Executar `CT-01` a `CT-07` apenas nas condições previstas no roteiro; declarar casos sem cobertura quando a ocorrência ou o recurso não existir.
4. Resolver a expectativa documentada de `CT-06` e obter calendário/oferta para as verificações correspondentes de `CT-07`.
5. Preencher os CSVs, executar o processador, revisar as saídas e substituir esta análise somente quando houver evidência válida. Manter histórico das execuções e não sobrescrever dados brutos.

## Histórico de versão

| Membro | Contribuição | Data | Commit |
|---|---|---|---|
| [Gabriel Mota](https://github.com/Gabro-MO) | Cálculo reprodutível, confronto GQM e respostas formais das métricas funcionais | 15/11/2026 | Não commitado |
