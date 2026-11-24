# Métricas de Usabilidade

Especificação de perguntas, hipóteses e métricas de **Usabilidade** para a funcionalidade _Planejar formatura_ do No Fluxo UnB, avaliada por meio de **Inspeção Heurística** (método ergonômico de Nielsen/ISO 9241-11) conduzida internamente pela equipe avaliadora, eliminando a dependência de participantes externos.

---

## 1. Subcaracterísticas Avaliadas (ISO/IEC 25010)

1. **Operabilidade (_Operability_):** facilidade e controle fornecidos pela interface ao navegar semestres, interagir com o grafo curricular e manipular controles de crédito.
2. **Apreensibilidade (_Learnability_):** clareza visual e terminológica que permite ao estudante compreender a previsão de formatura e o conceito de matérias críticas de maneira autônoma.

---

## 2. Questão GQM e Hipótese Associada

- **Questão `Q-OP-01`:** A interface da tela de planejamento atende às heurísticas ergonômicas de usabilidade essenciais para operação e apreensão autônoma?
- **Hipótese `H-OP-01`:** A interface apresenta violações heurísticas relevantes nas tarefas avaliadas.
- **Objetivo associado:** [`OBJ-OP`](visaoGeral.md#31-objetivo-geral-de-medicao-nivel-conceitual)
- **Métricas associadas:** [`MET-OP-01` (TCH)](#met-op-01-taxa-de-conformidade-heuristica-tch) · [`MET-OP-01b` (ISVH)](#met-op-01b-indice-de-severidade-de-violacoes-heuristicas-isvh)
- **Matriz de rastreabilidade:** [Matriz Geral](../../../rastreabilidade.md)

---

## 3. Tarefas de Referência para a Inspeção

A inspeção heurística orienta-se pela verificação das 10 Heurísticas de Nielsen durante o percurso das três tarefas centrais do fluxo ([Software Escolhido](../../fase1/softwareEscolhido.md#31-fluxo-de-uso-avaliado)):

**Tabela 1 — Tarefas de Referência para a Inspeção.**

| ID | Tarefa Inspecionada | Foco da Inspeção Heurística | Heurísticas-Chave |
| :---: | :--- | :--- | :---: |
| **T1** | Localizar Previsão de Formatura | Visibilidade e destaque das informações essenciais (semestre previsto e semestres restantes) sem sobrecarga cognitiva. | #1 (Status do sistema)<br>#8 (Design minimalista) |
| **T2** | Interpretar Matérias Críticas | Clareza conceitual e affordance visual dos nós destacados como críticos e sua relação no grafo/painel. | #2 (Mundo real)<br>#6 (Reconhecimento) |
| **T3** | Ajustar Limite de Créditos | Eficiência do controle interativo, feedback ao recalcular o plano e facilidade de desfazer ou redefinir. | #1 (Feedback)<br>#3 (Liberdade)<br>#5 (Prevenção de erros) |

*Fonte: elaboração da equipe, conforme os registros e referências desta página.*

---

## 4. Fichas das Métricas de Usabilidade

### `MET-OP-01` — Taxa de Conformidade Heurística (TCH)

**Tabela 2 — MET-OP-01 — Taxa de Conformidade Heurística (TCH).**

| Campo | Especificação |
| :--- | :--- |
| **Identificador** | `MET-OP-01` |
| **Nome** | Taxa de Conformidade Heurística (TCH) |
| **Característica** | Usabilidade — Operabilidade (*Operability*) |
| **Questão GQM** | `Q-OP-01`: A interface atende às heurísticas ergonômicas de usabilidade? |
| **Hipótese Relacionada** | **`H-OP-01`**: Violações de layout e ergonomia causam atrito e reduzem a operabilidade da ferramenta. |
| **Definição** | Percentual de itens de verificação ergonômica atendidos satisfatoriamente pela interface `/plano-formatura` no checklist padronizado de inspeção. Unidade: percentual (%). |
| **Cálculo** | `TCH = (Nconformes / Nitens) × 100`, com `Nitens = 10`. Usar os itens consolidados pelo protocolo. |
| **Fonte** | Checklist padronizado de inspeção heurística preenchido consensualmente pelos avaliadores da equipe. |
| **Coleta** | 1. Executar a aplicação com histórico autorizado carregado.<br>2. Dois ou mais avaliadores inspecionam a interface executando os fluxos `T1`, `T2` e `T3`.<br>3. Avaliar cada item do checklist como Conforme (1) ou Não Conforme (0).<br>4. Consolidar os resultados em sessão de alinhamento e calcular a taxa final. |
| **Níveis de Julgamento** | - **Excelente:** `TCH ≥ 85%`.<br>- **Aceitável:** `70% ≤ TCH < 85%` (interface operável, com fricções pontuais de design).<br>- **Crítico:** `TCH < 70%`. |
| **Questão associada** | [`Q-OP-01`](visaoGeral.md#32-questoes-de-medicao-nivel-operacional) |
| **Hipótese associada** | [`H-OP-01`](visaoGeral.md#2-hipoteses-operacionais-e-matriz-de-validacao) |
| **Objetivo associado** | [`OBJ-OP`](visaoGeral.md#31-objetivo-geral-de-medicao-nivel-conceitual) |
| **Matriz de rastreabilidade** | [Matriz Geral](../../../rastreabilidade.md) |

*Fonte: elaboração da equipe, conforme os registros e referências desta página.*

---

### `MET-OP-01b` — Índice de Severidade de Violações Heurísticas (ISVH)

**Tabela 3 — MET-OP-01b — Índice de Severidade de Violações Heurísticas (ISVH).**

| Campo | Especificação |
| :--- | :--- |
| **Identificador** | `MET-OP-01b` |
| **Nome** | Índice de Severidade de Violações Heurísticas (ISVH) |
| **Característica** | Usabilidade — Apreensibilidade (*Learnability*) |
| **Questão GQM** | `Q-OP-01`: A interface atende às heurísticas ergonômicas de usabilidade? |
| **Hipótese Relacionada** | **`H-OP-01`**: A presença de problemas graves de usabilidade compromete a apreensão autônoma do plano. |
| **Definição** | Soma ponderada do impacto dos problemas ergonômicos identificados, com base na escala de severidade de Nielsen (0 a 4). |
| **Cálculo** | `ISVH = 4 × Ncatastrofico + 3 × Nmaior + 2 × Nmenor + Ncosmetico`. Contar as violações consolidadas por severidade. |
| **Fonte** | Planilha de registro de problemas heurísticos e severidades atribuídas pelos avaliadores. |
| **Coleta** | Para cada item não conforme na `MET-OP-01`, a equipe classifica a gravidade:<br>- **1 (Cosmético):** não atrapalha a execução (ex.: detalhe visual).<br>- **2 (Menor):** causa leve lentidão ou dúvida temporária.<br>- **3 (Maior):** dificulta consideravelmente a realização da tarefa.<br>- **4 (Catastrófico):** impede a conclusão ou induz o usuário ao erro crítico. |
| **Níveis de Julgamento** | - **Excelente:** `Ncatastrofico = 0`, `Nmaior = 0` e `ISVH ≤ 5`.<br>- **Aceitável:** `Ncatastrofico = 0`, `Nmaior ≤ 1` e `ISVH ≤ 12`.<br>- **Crítico:** `Ncatastrofico ≥ 1` ou `Nmaior > 1` ou `ISVH > 12`. |
| **Questão associada** | [`Q-OP-01`](visaoGeral.md#32-questoes-de-medicao-nivel-operacional) |
| **Hipótese associada** | [`H-OP-01`](visaoGeral.md#2-hipoteses-operacionais-e-matriz-de-validacao) |
| **Objetivo associado** | [`OBJ-OP`](visaoGeral.md#31-objetivo-geral-de-medicao-nivel-conceitual) |
| **Matriz de rastreabilidade** | [Matriz Geral](../../../rastreabilidade.md) |

*Fonte: elaboração da equipe, conforme os registros e referências desta página.*

---

As faixas são critérios da equipe. No ISVH, aplicar Excelente primeiro; depois Aceitável, se não atender à primeira faixa; os demais valores válidos são Críticos. O julgamento de Q-OP-01 usa o pior nível entre TCH e ISVH, conforme a [regra conjunta](visaoGeral.md#22-regra-de-julgamento-conjunto). Uma métrica isolada não refuta a hipótese. Sem coleta completa e consenso previstos, registrar Inconclusivo.

## 5. Checklist Heurístico Padronizado (Nielsen)

**Tabela 4 — Checklist Heurístico Padronizado (Nielsen).**

| # | Heurística de Referência | Item de Verificação na Interface `/plano-formatura` | Foco |
| :---: | :--- | :--- | :---: |
| **1** | Visibilidade do estado (#1) | A tela informa visualmente se o plano está atualizado, em processamento ou com dados pendentes? | `T3` |
| **2** | Correspondência (#2) | Termos como "matérias críticas", "créditos" e "período" são claros para o contexto acadêmico da UnB? | `T2` |
| **3** | Controle e liberdade (#3) | É fácil desfazer uma alteração de créditos ou retornar à configuração inicial sem recarregar a página? | `T3` |
| **4** | Consistência e padrões (#4) | Os nós do grafo seguem cores e convenções consistentes para aprovadas, pendentes e críticas? | `T1, T2` |
| **5** | Prevenção de erros (#5) | O controle de créditos impede a inserção de valores inválidos (negativos ou acima do limite máximo)? | `T3` |
| **6** | Reconhecimento (#6) | O semestre previsto de formatura é evidente de imediato, sem exigir que o aluno conte semestres manualmente? | `T1` |
| **7** | Flexibilidade e eficiência (#7) | A navegação pelo grafo e linha do tempo oferece atalhos ou zoom responsivo para turmas densas? | `T1, T2` |
| **8** | Design minimalista (#8) | O layout evita acúmulo excessivo de nós e rótulos sobrepostos que concorram pela atenção visual? | `T1, T2` |
| **9** | Tratamento de erros (#9) | Mensagens de aviso e restrições curriculares são descritivas e orientam como resolver o problema? | `T3` |
| **10** | Ajuda e documentação (#10) | Existem legendas, tooltips explicativos ou orientações contextuais sobre o funcionamento do plano? | `T2` |

*Fonte: elaboração da equipe, conforme os registros e referências desta página.*

## 6. Referências

Referências usadas nesta página, conforme [Referências — Fase 2](../../../referencias/fase2.md) e [Referências — Fase 3](../../../referencias/fase3.md).

- BASILI, Victor R.; CALDIERA, Gianluigi; ROMBACH, H. Dieter. **The Goal Question Metric Approach**. *Encyclopedia of Software Engineering*, John Wiley & Sons, v. 2, p. 528-532, 1994. Disponível em: <https://ntrs.nasa.gov/citations/19940026214>.
- INTERNATIONAL ORGANIZATION FOR STANDARDIZATION. **ISO 9241-11:2018**: Ergonomics of human-system interaction — Part 11: Usability: Definitions and concepts. Genebra: ISO, 2018.
- INTERNATIONAL ORGANIZATION FOR STANDARDIZATION. **ISO/IEC 25010:2011**: Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models. Genebra: ISO, 2011.
- NIELSEN, Jakob. **10 Usability Heuristics for User Interface Design**. Nielsen Norman Group, 1994. Disponível em: <https://www.nngroup.com/articles/ten-usability-heuristics/>.
- NIELSEN, Jakob. **Heuristic Evaluation**. In: NIELSEN, Jakob; MACK, Robert L. (Org.). *Usability Inspection Methods*. Nova York: John Wiley & Sons, 1994. p. 25-62.
- NIELSEN, Jakob. **Severity Ratings for Usability Problems**. Nielsen Norman Group, 1995. Disponível em: <https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/>. Acesso em: 14 nov. 2026.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Elaboração da especificação de usabilidade, tarefas padronizadas, fichas MET-OP-01 e MET-OP-01b | 16/10 | [c821ea3](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/c821ea3) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Remoção de referências a divisões internas de pessoas e padronização documental | 16/10 | [81912ba](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/81912bac5e02d7429e2d05446544ec9636891f5e) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Simplificação textual e concisão mantendo coerência com GQM e ISO 9241-11 | 24/10 | [b31d87e](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/b31d87e) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Substituição de testes com participantes externos por Avaliação Heurística interna de Nielsen (TCH e ISVH) | 25/10 | [8330fa6](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/8330fa6ce8a670d083d8718eada13606616f064c) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Correção do julgamento conjunto e das fórmulas de usabilidade | 15/11 | [8d625c1](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/8d625c1a87436bf186efb0abffb6682e1916a3d5) |
| [Yasmim de Souza Santos](https://github.com/eii-yahs) | Inclusão das referências utilizadas na página | 22/11 | Não commitado |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Inclusão de campos de rastreabilidade bidirecional nas fichas de usabilidade (TCH e ISVH) | 23/11 | [0b37cf6](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/0b37cf68e64f7e1d9021604848841415f141a2ae) |