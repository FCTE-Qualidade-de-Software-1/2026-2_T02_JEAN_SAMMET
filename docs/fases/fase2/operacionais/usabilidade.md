# Métricas de Usabilidade

Especificação de perguntas, hipóteses e métricas de **Usabilidade** para a funcionalidade _Planejar formatura_ do No Fluxo UnB, avaliada por meio de **Inspeção Heurística** (método ergonômico de Nielsen/ISO 9241-11) conduzida internamente pela equipe avaliadora, eliminando a dependência de participantes externos.

---

## 1. Subcaracterísticas Avaliadas (ISO/IEC 25010)

1. **Operabilidade (_Operability_):** facilidade e controle fornecidos pela interface ao navegar semestres, interagir com o grafo curricular e manipular controles de crédito.
2. **Apreensibilidade (_Learnability_):** clareza visual e terminológica que permite ao estudante compreender a previsão de formatura e o conceito de matérias críticas de maneira autônoma.

---

## 2. Questão GQM e Hipótese Associada

- **Questão `Q-OP-01`:** A interface da tela de planejamento atende às heurísticas ergonômicas de usabilidade essenciais para operação e apreensão autônoma?
- **Hipótese `H-OP-01`:** A tela `/plano-formatura` concentra violações heurísticas (densidade excessiva de nós, feedback insuficiente de recálculo e terminologia ambígua), comprometendo a facilidade de uso e o entendimento das saídas.

---

## 3. Tarefas de Referência para a Inspeção

A inspeção heurística orienta-se pela verificação das 10 Heurísticas de Nielsen durante o percurso das três tarefas centrais do fluxo ([Software Escolhido](../../fase1/softwareEscolhido.md#31-fluxo-de-uso-avaliado)):

| ID | Tarefa Inspecionada | Foco da Inspeção Heurística | Heurísticas-Chave |
| :---: | :--- | :--- | :---: |
| **T1** | Localizar Previsão de Formatura | Visibilidade e destaque das informações essenciais (semestre previsto e semestres restantes) sem sobrecarga cognitiva. | #1 (Status do sistema)<br>#8 (Design minimalista) |
| **T2** | Interpretar Matérias Críticas | Clareza conceitual e affordance visual dos nós destacados como críticos e sua relação no grafo/painel. | #2 (Mundo real)<br>#6 (Reconhecimento) |
| **T3** | Ajustar Limite de Créditos | Eficiência do controle interativo, feedback ao recalcular o plano e facilidade de desfazer ou redefinir. | #1 (Feedback)<br>#3 (Liberdade)<br>#5 (Prevenção de erros) |

---

## 4. Fichas das Métricas de Usabilidade

### `MET-OP-01` — Taxa de Conformidade Heurística (TCH)

| Campo | Especificação |
| :--- | :--- |
| **Identificador** | `MET-OP-01` |
| **Nome** | Taxa de Conformidade Heurística (TCH) |
| **Característica** | Usabilidade — Operabilidade (*Operability*) |
| **Questão GQM** | `Q-OP-01`: A interface atende às heurísticas ergonômicas de usabilidade? |
| **Hipótese Relacionada** | **`H-OP-01`**: Violações de layout e ergonomia causam atrito e reduzem a operabilidade da ferramenta. |
| **Definição** | Percentual de itens de verificação ergonômica atendidos satisfatoriamente pela interface `/plano-formatura` no checklist padronizado de inspeção. Unidade: percentual (%). |
| **Cálculo** | $$TCH = \left( \frac{N_{\text{itens\_conformes}}}{N_{\text{total\_itens}}} \right) \times 100$$<br>Onde $N_{\text{itens\_conformes}}$ é o total de itens validados como conformes no checklist e $N_{\text{total\_itens}}$ é o número total de itens avaliados ($N = 10$). |
| **Fonte** | Checklist padronizado de inspeção heurística preenchido consensualmente pelos avaliadores da equipe. |
| **Coleta** | 1. Executar a aplicação com histórico sintético carregado.<br>2. Dois ou mais avaliadores inspecionam a interface executando os fluxos $T_1$, $T_2$ e $T_3$.<br>3. Avaliar cada item do checklist como Conforme (1) ou Não Conforme (0).<br>4. Consolidar os resultados em sessão de alinhamento e calcular a taxa final. |
| **Níveis de Julgamento** | - **Excelente:** $TCH \ge 85\%$ (alta aderência ergonômica, refuta `H-OP-01`).<br>- **Aceitável:** $70\% \le TCH < 85\%$ (interface operável, com fricções pontuais de design).<br>- **Crítico:** $TCH < 70\%$ (graves falhas de operabilidade; **confirma `H-OP-01`** e subsidia melhoria na Fase 4). |

---

### `MET-OP-01b` — Índice de Severidade de Violações Heurísticas (ISVH)

| Campo | Especificação |
| :--- | :--- |
| **Identificador** | `MET-OP-01b` |
| **Nome** | Índice de Severidade de Violações Heurísticas (ISVH) |
| **Característica** | Usabilidade — Apreensibilidade (*Learnability*) |
| **Questão GQM** | `Q-OP-01`: A interface atende às heurísticas ergonômicas de usabilidade? |
| **Hipótese Relacionada** | **`H-OP-01`**: A presença de problemas graves de usabilidade compromete a apreensão autônoma do plano. |
| **Definição** | Escoragem ponderada do impacto dos problemas ergonômicos identificados, com base na escala de severidade de Nielsen (0 a 4). |
| **Cálculo** | $$ISVH = (4 \times N_{\text{catastrófico}}) + (3 \times N_{\text{maior}}) + (2 \times N_{\text{menor}}) + (1 \times N_{\text{cosmético}})$$<br>Onde $N_s$ indica a quantidade de violações encontradas no nível de severidade $s$. |
| **Fonte** | Planilha de registro de problemas heurísticos e severidades atribuídas pelos avaliadores. |
| **Coleta** | Para cada item não conforme na `MET-OP-01`, a equipe classifica a gravidade:<br>- **1 (Cosmético):** não atrapalha a execução (ex.: detalhe visual).<br>- **2 (Menor):** causa leve lentidão ou dúvida temporária.<br>- **3 (Maior):** dificulta consideravelmente a realização da tarefa.<br>- **4 (Catastrófico):** impede a conclusão ou induz o usuário ao erro crítico. |
| **Níveis de Julgamento** | - **Excelente:** $N_{\text{catastrófico}} = 0$, $N_{\text{maior}} = 0$ e $ISVH \le 5$ (refuta `H-OP-01`).<br>- **Aceitável:** $N_{\text{catastrófico}} = 0$, $N_{\text{maior}} \le 1$ e $ISVH \le 12$.<br>- **Crítico:** $N_{\text{catastrófico}} \ge 1$ ou $N_{\text{maior}} > 1$ ou $ISVH > 12$ (**confirma `H-OP-01`**). |

---

## 5. Checklist Heurístico Padronizado (Nielsen)

| # | Heurística de Referência | Item de Verificação na Interface `/plano-formatura` | Foco |
| :---: | :--- | :--- | :---: |
| **1** | Visibilidade do estado (#1) | A tela informa visualmente se o plano está atualizado, em processamento ou com dados pendentes? | $T_3$ |
| **2** | Correspondência (#2) | Termos como "matérias críticas", "créditos" e "período" são claros para o contexto acadêmico da UnB? | $T_2$ |
| **3** | Controle e liberdade (#3) | É fácil desfazer uma alteração de créditos ou retornar à configuração inicial sem recarregar a página? | $T_3$ |
| **4** | Consistência e padrões (#4) | Os nós do grafo seguem cores e convenções consistentes para aprovadas, pendentes e críticas? | $T_1, T_2$ |
| **5** | Prevenção de erros (#5) | O controle de créditos impede a inserção de valores inválidos (negativos ou acima do limite máximo)? | $T_3$ |
| **6** | Reconhecimento (#6) | O semestre previsto de formatura é evidente de imediato, sem exigir que o aluno conte semestres manualmente? | $T_1$ |
| **7** | Flexibilidade e eficiência (#7) | A navegação pelo grafo e linha do tempo oferece atalhos ou zoom responsivo para turmas densas? | $T_1, T_2$ |
| **8** | Design minimalista (#8) | O layout evita acúmulo excessivo de nós e rótulos sobrepostos que concorram pela atenção visual? | $T_1, T_2$ |
| **9** | Tratamento de erros (#9) | Mensagens de aviso e restrições curriculares são descritivas e orientam como resolver o problema? | $T_3$ |
| **10** | Ajuda e documentação (#10) | Existem legendas, tooltips explicativos ou orientações contextuais sobre o funcionamento do plano? | $T_2$ |

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Elaboração da especificação de usabilidade, tarefas padronizadas, fichas MET-OP-01 e MET-OP-01b | 16/10 | [c821ea3](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/c821ea3) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Remoção de referências a divisões internas de pessoas e padronização documental | 16/10 | [81912ba](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/81912bac5e02d7429e2d05446544ec9636891f5e) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Simplificação textual e concisão mantendo coerência com GQM e ISO 9241-11 | 24/10 | [b31d87e](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/b31d87e) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Substituição de testes com participantes externos por Avaliação Heurística interna de Nielsen (TCH e ISVH) | 25/10 | [corrente] |


