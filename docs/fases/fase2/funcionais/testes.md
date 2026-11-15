# Protocolo de coleta — Métricas funcionais

Os casos usam o histórico oficial autorizado H0 e os cenários C0–C5 definidos no [roteiro da Fase 3](../../fase3/funcionais/roteiro.md). Condições ausentes na entrada serão declaradas como não cobertas, sem fabricar outros históricos. Antes de executar, definir o resultado esperado com base em regra oficial ou comportamento documentado. Registrar versão/commit, matriz e fonte curricular, entradas, plano gerado, cálculo e evidências. Uma hipótese não confirmada não deve ser classificada automaticamente como defeito.

A [regra de julgamento do GQM](GQM.md#31-regras-de-referencia-e-julgamento) define as fontes necessárias. Sem regra identificada, o caso permanece Pendente de especificação; erro de coleta é Inconclusivo.

## 1. Casos de teste

| ID | Cenário | Resultado esperado | Métrica | Evidência |
|---|---|---|---|---|
| `CT-01` | Disciplina pendente com pré-requisito aprovado ou pendente. | A dependente não deve preceder a satisfação válida do requisito. | `MET-FUN-01` | Fonte e vigência da regra, histórico, semestres no plano e captura/log. |
| `CT-02` | Par de co-requisitos pendentes; variar quando um já estiver satisfeito. | A alocação segue a regra oficial de satisfação simultânea ou prévia. | `MET-FUN-02` | Fonte, status e semestre de cada disciplina, resultado da verificação. |
| `CT-03` | Histórico com conjunto conhecido de obrigatórias pendentes. | Todas devem constar no plano, salvo exclusão justificada por regra oficial e política definida previamente. | `MET-FUN-03` | Lista esperada/gerada, omissões, justificativas e cobertura calculada. |
| `CT-04` | Histórico com disciplinas aprovadas, pendentes e em andamento. | O tratamento de cada status corresponde à regra documentada. | `MET-FUN-04` | Status de entrada, estado observado, divergências e capturas. |
| `CT-05` | Disciplina satisfeita por equivalência oficial; testar casos encadeados ou de matriz antiga apenas se houver fonte aplicável. | Pendências e disciplina substituta são tratadas conforme a equivalência e vigência. | `MET-FUN-03`, `MET-FUN-05` | Fonte/vigência, entradas, pendências antes/depois e plano. |
| `CT-06` | Manter o histórico fixo e variar trabalho/estágio, objetivo e limite de créditos, um campo por vez. | Cada efeito corresponde ao comportamento documentado; não exigir mudança na seleção de disciplinas sem essa expectativa. | `MET-FUN-06` | Campo/valor, fonte do comportamento, planos comparados e conclusão. |
| `CT-07` | Oferta e período letivo conhecidos; validar o limite de carga. Se seguro e viável, simular falha na consulta ao período fora da produção. | Alocações respeitam as restrições documentadas; eventual semestre estimado é comparado ao calendário oficial. | `MET-FUN-07` | Calendário/oferta, limite, semestres, alocações e logs. |

## 2. Registro de execução

| Campo | Registro |
|---|---|
| Caso, data/hora e responsável | `CT-__`; [preencher] |
| Commit/versão e ambiente | [preencher] |
| Matriz, versão da fonte e regra | [preencher] |
| Entrada e cenário | H0 / C__; [identificadores, sem dados pessoais] |
| Resultado esperado (pré-definido) | [preencher] |
| Resultado observado | [preencher] |
| Métrica(s) e cálculo | [preencher] |
| Evidência (captura, log ou exportação) | [caminho/link interno] |
| Classificação e justificativa | Conforme / Não conforme / Não aplicável / Pendente de especificação / Inconclusivo; [observações] |

## Histórico de versão

| Membro | Contribuição | Data | Commit |
|---|---|---|---|
| [Gabriel Mota](https://github.com/Gabro-MO) | Perguntas GQM, métricas e cenários iniciais. | 16/10/2026 | [9306147](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/9306147e05a3017e02f9bedaf2c75a8287ef1c8b) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Revisão do foco GQM e dos papéis da equipe. | 16/10/2026 | [81912ba](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/81912bac5e02d7429e2d05446544ec9636891f5e) |
| [Gabriel Mota](https://github.com/Gabro-MO) | Divisão do documento em páginas. | 16/10/2026 | [e60f42c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/e60f42cea76bd6f39f2c6069ecdbce438b4e941a) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Alinhamento dos estados de execução às regras do GQM | 15/11 | [8d625c1](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/8d625c1a87436bf186efb0abffb6682e1916a3d5) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Alinhamento da entrada autorizada e das condições de avaliação | 15/11 | [0e38da3](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/0e38da3eac882c62bf7c6f9e1bda97a8b744ef2e) |
