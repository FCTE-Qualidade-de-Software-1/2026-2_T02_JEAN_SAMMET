# Fase 3 — Plano de avaliação

O plano prepara a coleta das sete métricas funcionais e cinco operacionais da [Fase 2](../fase2/funcionais/GQM.md). A coleta completa, o cálculo e o julgamento pertencem à Fase 4. O [piloto](piloto.md) verifica a viabilidade dos procedimentos e fica separado dos resultados definitivos.

## 1. Organização

| Parte | Conteúdo |
|---|---|
| [Roteiro funcional](funcionais/roteiro.md) | CT-01 a CT-07: entradas, referências, passos e resultados esperados |
| [Fontes curriculares](funcionais/fontes.md) | Matriz 6360/1, regras verificadas e lacunas |
| [Plano operacional](metricasOperacionais.md) | Usabilidade, dependências, armazenamento e acesso |
| [Ambiente e dados](operacionais/ambienteERecursos.md) | Conta de teste, histórico autorizado e cenários planejados |
| [Cronograma e riscos](operacionais/cronogramaERiscos.md) | Ordem, esforço e condições de execução |
| [Rastreabilidade](operacionais/rastreabilidade.md) | Questão, métrica, procedimento e evidência |
| [Piloto](piloto.md) | Observações exploratórias e verificações ainda necessárias |

## 2. Registro e decisão

Cada execução identifica caso, entrada, cenário, responsável, data/hora com fuso, ambiente, versão conhecida, regra, resultado esperado, observado, cálculo e evidência. Os modelos ficam em `testes/modelos_coleta/`. Criar uma cópia por execução e preservar os modelos vazios.

- **Conforme/Não conforme:** há regra e dados válidos para aplicar a ficha da Fase 2.
- **Pendente de especificação:** falta regra ou efeito esperado documentado.
- **Inconclusivo:** a coleta ou a evidência não permite julgar.
- **Sem cobertura:** a entrada disponível não permite executar a condição planejada; registrar a lacuna, sem taxa ou aprovação.
- **Não aplicável:** uma regra conhecida não se aplica ao cenário; justificar.

Não usar ausência de dados como zero. Preservar também falhas e repetições, com o motivo. Resultados de entradas, cenários, versões ou ferramentas diferentes são identificados separadamente.

## 3. Prontidão para a coleta

A proposta está documentada, mas a coleta definitiva depende de conferir a entrada do histórico oficial autorizado e a viabilidade das variações planejadas, os avaliadores, o ambiente e o cronograma. O par de co-requisitos e a equivalente foram confirmados no SIGAA; falta validar sua entrada no site. A TBR aguarda identificação e validação da rota protegida. A entrada H0 é mantida nos cenários C0–C5; casos que exijam condições ausentes terão cobertura limitada, sem inventar novos históricos. As demais lacunas estão registradas por caso.

Na inspeção exploratória foi usada a sessão disponibilizada pelo usuário, que já continha dados pessoais. Esses dados e o PDF do histórico não integram os artefatos versionados nem a massa de medição. Após a rejeição do PDF sintético no piloto, a coleta usará o histórico oficial autorizado, com evidências sanitizadas. Cenários que não puderem ser reproduzidos terão a limitação declarada.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Organização do plano integrado e dos critérios de prontidão | 15/11 | [aa0c61f](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/aa0c61fac5e9d2db19adec76fd052a2bb6b04b90) |