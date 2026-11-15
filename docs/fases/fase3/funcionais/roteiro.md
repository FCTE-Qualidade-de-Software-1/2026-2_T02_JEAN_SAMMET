# Roteiro de avaliação funcional

O roteiro aplica as [métricas da Fase 2](../../fase2/funcionais/GQM.md) usando uma única entrada acadêmica oficial autorizada: **H0**. O histórico original foi fornecido pelo usuário e permanece fora do repositório. A versão usada para preparar os cenários foi sanitizada e normalizada em `testes/referencias/h0_sanitizado.json`, com evidência documental redigida em `testes/evidencias/funcionais/H0_sanitizado.pdf`.

## 1. Entrada e cenários

### 1.1 Entrada H0

| Campo | Conteúdo usado na avaliação |
|---|---|
| Curso / matriz | Engenharia de Software, FCTE/UnB; matriz 6360/1 — 2017.1 |
| Período letivo mais recente | 2026.2 |
| Registros de componentes com status | 41: 33 `APROVADO`, 7 `MATRICULADO` e 1 `TRANCADO` |
| Equivalências obrigatórias concluídas | 5, declaradas como cumpridas no próprio SIGAA |
| Equivalências obrigatórias em andamento | 2, com status `MATRICULADO`; ainda não contam como concluídas |
| Obrigatórias pendentes | 14 disciplinas, totalizando 1.050h |
| Outras exigências pendentes | Duas cadeias de seletividade de 60h cada e ENADE concluinte (0h), mantidas fora do denominador de disciplinas da CDO |
| Arquivos normalizados | `testes/referencias/h0_sanitizado.json`, `testes/evidencias/funcionais/h0_registros.csv`, `h0_obrigacoes_pendentes.csv` e `h0_equivalencias.csv` |

O H0 não inclui nome, matrícula, nascimento, documento, CPF, índices acadêmicos ou código de autenticação. O PDF sanitizado remove esses campos; o PDF original não deve ser versionado. Não há notas numéricas na entrada normalizada: apenas status, período, código e carga horária necessários à avaliação.

As 14 disciplinas obrigatórias pendentes somam 1.050h, valor consistente com o quadro-resumo de obrigatórias pendentes do SIGAA. As duas cadeias de seletividade (120h) e o ENADE são exigências separadas, não disciplinas obrigatórias do denominador de `MET-FUN-03`.

### 1.2 Cenários controlados

Todos os cenários mantêm H0 fixo. Somente a configuração da interface muda.

| Cenário | Configuração | Finalidade |
|---|---|---|
| C0 — Base | H0, alvo de 24 créditos/360h; registrar trabalho, objetivo e período selecionados | Conferir importação do histórico, regras e plano inicial |
| C1 — Carga menor | H0, alvo de 20 créditos/300h; demais escolhas iguais a C0 | Conferir a configuração de carga e o recálculo |
| C2 — Carga maior | H0, alvo de 32 créditos/480h; demais escolhas iguais a C0 | Conferir limite curricular e recálculo |
| C3 — Trabalho/estágio | H0; alternar somente essa resposta em relação a C0 | Conferir representação e efeito apenas se especificado |
| C4 — Objetivo | H0; alternar velocidade/equilíbrio em relação a C0 | Conferir representação e efeito apenas se especificado |
| C5 — Quantidade de matérias | H0; comparar 4, 6 e 8 matérias, mantendo trabalho e objetivo fixos | Conferir as cargas sugeridas exibidas no onboarding: 240/360/480h |

C0–C2 usam cargas-alvo e não pressupõem que o valor esteja selecionado por padrão. C1/C2 dependem de o campo aceitar os valores; confirmar no piloto. C3/C4 não pressupõem efeito algorítmico não documentado. C5 permite conferir a associação exibida no onboarding, mas o comportamento do plano exige saída observável.

## 2. Preparação comum

1. Carregar H0 e confirmar a matriz 6360/1. Comparar a importação com `h0_registros.csv` e `h0_equivalencias.csv`, sem incluir identificadores pessoais.
2. Registrar versão/commit do produto, data/hora com fuso, navegador, viewport, zoom e identificador da execução.
3. Antes de gerar o plano, montar o resultado esperado com as regras da matriz, a lista de pendências do H0 e as políticas de status documentadas.
4. Executar C0 e salvar o plano completo, todos os semestres, disciplinas, avisos e não alocadas. Nas variações, mudar um controle por vez e restaurar C0.
5. Registrar uma linha por execução em `execucoes.csv` e uma linha por unidade verificada em `verificacoes_funcionais.csv`. Usar `1` ou `0` em `conforme` somente com comparação observada; usar `INCONCLUSIVO` para falha de coleta e manter pendente quando a execução não ocorreu.

## 3. Casos de teste

### CT-01 — Pré-requisitos (`MET-FUN-01`)

- **Entrada:** C0; `FGA0170` consta como aprovada em 2026.1 e `FGA0211` consta no quadro de obrigatórias pendentes do H0. Também foi observado o par FGA0009/FGA0011.
- **Referência:** FGA0211 exige FGA0170. A sequência FGA0009→FGA0011 aparece no fluxo do produto e foi considerada válida pelo avaliador (semestres 9→10), mas sua regra/vigência oficial não está transcrita no JSON curricular do pacote. MAT0025 está aprovada e MAT0026 foi aprovada em 2024.2; essa relação é contexto histórico já satisfeito, não evidência de ordenação futura.
- **Passos:** conferir se FGA0211 aparece no plano; se aparecer, registrar seu semestre e confirmar que FGA0170 já está satisfeita. Não contar a relação MAT0026/MAT0025 como teste de sequência futura.
- **Esperado:** nenhuma disciplina dependente deve ser alocada antes da satisfação válida do pré-requisito.
- **Registro:** `TVP = NVP / NRP × 100`. Sem disciplina dependente no plano ou sem saída observável, não calcular.

### CT-02 — Co-requisitos (`MET-FUN-02`)

- **Entrada:** H0 contém FGA0071 e FGA0073 aprovadas; não contém FGA0072 nem FGA0074.
- **Referência:** FGA0072 e FGA0074 são optativas co-requisitadas reciprocamente; o pré-requisito indicado é `ENE0277 OU (FGA0073 E FGA0071)`.
- **Passos:** verificar se o planejador permite selecionar explicitamente o par. Se permitir, selecionar ambas sem alterar o histórico e verificar suas alocações e pré-requisitos. Registrar cada direção da relação.
- **Esperado:** quando ambas forem selecionadas e permanecerem pendentes, devem atender à regra de co-requisito definida pela fonte. Não simular aprovação prévia de nenhuma delas.
- **Registro:** `TVC = NVC / NRC × 100`. Se o planejador não permitir selecionar o par, registrar ausência de cobertura; não classificar como conforme.

### CT-03 — Obrigatórias pendentes (`MET-FUN-03`)

- **Entrada:** C0 e as 14 disciplinas obrigatórias listadas em `h0_obrigacoes_pendentes.csv`: FGA0150, FGA0060, FGA0278, FGA0208, FGA0211, FGA0210, FGA0244, FGA0109, FGA0240, FGA0021, FGA0206, FGA0009, FGA0250 e FGA0011.
- **Passos:** comparar essa lista com o plano completo. Considerar as cinco equivalências aprovadas como cumpridas; manter as duas equivalências matriculadas como não concluídas. FGA0060 aparece como `TRANCADO` e não pode ser contado como aprovada.
- **Esperado:** todas as 14 disciplinas obrigatórias pendentes devem aparecer no plano ou ter justificativa rastreável de oferta/regra. As cadeias 6 e 7 e ENADE ficam registradas separadamente e não integram o denominador de disciplinas da CDO.
- **Registro:** `CDO = DPC / 14 × 100`. O número 14 é o denominador de referência extraído do H0; `DPC` só pode ser preenchido após comparar com o plano observado.

### CT-04 — Status do histórico (`MET-FUN-04`)

- **Entrada:** os 41 registros acadêmicos de H0: 33 `APROVADO`, 7 `MATRICULADO` e 1 `TRANCADO`.
- **Passos:** verificar cada código e status reconhecido pelo sistema; conferir especialmente FGA0060 (`TRANCADO`) e os sete componentes `MATRICULADO`, inclusive as duas equivalências em andamento.
- **Esperado:** `MATRICULADO` não equivale a aprovação concluída; `TRANCADO` não equivale a aprovação; `APROVADO` deve ser reconhecido como concluído. Projeção da conclusão de uma disciplina em andamento só pode ser julgada conforme política documentada.
- **Registro:** `TDH = NDH / NVH × 100`. A distribuição do H0 é a linha de base, não o resultado da importação no produto.

### CT-05 — Equivalências (`MET-FUN-05`; apoio a `MET-FUN-03`)

- **Entrada:** cinco equivalências concluídas e duas equivalências em andamento, conforme `h0_equivalencias.csv`.
- **Equivalências concluídas:** FGA0146 → FGA0147; FGA0307 → FGA0184; FGA0312 → FGA0138; FGA0313 → FGA0172; FGA0314 → FGA0238.
- **Equivalências em andamento:** FGA0303 → FGA0150 e FGA0315 → FGA0278. Ambas estão `MATRICULADO` em 2026.2 e os destinos continuam no quadro de pendências.
- **Esperado:** as cinco equivalências `APROVADO` e explicitamente declaradas como cumpridas pelo SIGAA devem satisfazer suas obrigatórias de destino; as duas matriculadas não podem ser tratadas como concluídas.
- **Registro:** `TAE = NEI / NRE × 100`, após comparar a interpretação do produto. Não usar MAT0138 como ocorrência de H0: esse código não aparece como disciplina cursada nesta entrada.

### CT-06 — Opções do onboarding (`MET-FUN-06`)

- **Entrada:** C0 e variações C3–C5 com H0 fixo.
- **Passos:** percorrer trabalho/estágio, quantidade de matérias e objetivo. Alterar somente uma opção por vez. Para C5, conferir as opções 4/6/8 e as cargas exibidas de 240/360/480h.
- **Esperado:** seleção e carga sugerida devem ser representadas conforme o texto da interface. Efeito algorítmico de trabalho/estágio e objetivo só é julgável se houver requisito ou promessa documentada antes da execução.
- **Registro:** `COO = NEC / NEV × 100`; contar apenas expectativas previamente especificadas e realmente testadas. Lacuna de especificação não deve ser convertida em falha.
- **Resultado informado:** C5-4 (240h) gerou 300h no semestre 9; C5-6 (360h) gerou 390h; C5-8 (480h) gerou 540h (captura pendente). C3 e C4 foram inconclusivos, pois não houve mudança visual identificável entre Antes/Depois.

### CT-07 — Restrições semestrais (`MET-FUN-07`)

- **Entrada:** H0 fixo; nesta execução foram usadas as variantes C5-4/C5-6/C5-8, com alvos de 240h, 360h e 480h.
- **Referência:** matriz 6360/1, mínimo de 240h e máximo de 480h por período, com exceções do último semestre a interpretar.
- **Passos:** somar as cargas por semestre e comparar tanto com o alvo configurado no cenário quanto com os limites globais da matriz; separar divergência do alvo de violação do máximo global. Conferir oferta/calendário apenas com fonte oficial do período avaliado.
- **Esperado:** nenhuma carga deve exceder o alvo rígido do cenário (quando assim especificado) nem o máximo de 480h. A especificação original não esclarece se 240/360/480h são limites rígidos, metas exatas ou preferências; documentar essa ressalva no julgamento.
- **Resultado informado:** 300h no semestre 9 para alvo 240h; 390h para alvo 360h; 540h para alvo 480h. A captura de 480h está pendente e o relato foi registrado em `LEMBRETE-CT-07-06-480h.md`.
- **Registro:** `TVS = NVS / NRS × 100`, por tipo de restrição.
## 4. Estado da execução e cobertura

A execução funcional de 15/11/2026 foi informada pelo avaliador e registrada em `testes/evidencias/funcionais/execucoes.csv` e `verificacoes_funcionais.csv`. As capturas e o lembrete da imagem ausente ficam em `testes/evidencias/funcionais/execucao-2026-11-15/`. Os resultados consolidados, cálculos e limitações estão em [Análise dos Resultados e Julgamento](../../fase4/funcionais/analiseResultados.md).

A pré-checagem DNS anterior permanece no log como histórico de uma tentativa diferente e não invalida a execução posteriormente reportada. Permanecem pendentes a cobertura integral de CT-05 (2/7), a captura de CT-07-06-480h.png, a fonte curricular oficial da sequência FGA0009→FGA0011 e o esclarecimento formal sobre a semântica dos alvos 240/360/480h. Horário/fuso e ambiente de execução não foram informados e não foram inferidos.

A avaliação usa um histórico autorizado e configurações distintas; não representa uma amostra de estudantes nem perfis acadêmicos independentes. Resultados parciais não comprovam correção para condições ausentes.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Gabriel Mota](https://github.com/Gabro-MO) | Normalização de H0, sanitização da evidência e adequação dos cenários à entrada real | 15/11/2026 | [b07997f](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/b07997f34eb1a595571e3e5abd3cc4e15002949b) |
