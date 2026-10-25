# Métricas de Usabilidade

Especificação de perguntas, hipóteses e métricas de **Usabilidade** para a funcionalidade _Planejar formatura_ do No Fluxo UnB, focando na operação e apreensão pelos estudantes.

---

## 1. Subcaracterísticas Avaliadas (ISO/IEC 25010)

1. **Operabilidade (_Operability_):** facilidade com que o aluno opera e controla a interface ao navegar semestres, ajustar créditos e interagir com o grafo.
2. **Apreensibilidade (_Learnability_):** rapidez com que o aluno compreende o significado das saídas (previsão de formatura e matérias críticas) sem treinamento ou suporte.

---

## 2. Questão GQM e Hipótese Associada

- **Questão `Q-OP-01`:** Os estudantes realizam as tarefas essenciais na tela de planejamento com autonomia, sem necessidade de assistência externa?
- **Hipótese `H-OP-01`:** A densidade de nós e controles na tela `/plano-formatura` gera hesitação ou demanda auxílio para identificar o semestre de formatura e as matérias críticas.

---

## 3. Tarefas de Avaliação Padronizadas

Baseadas no fluxo real de uso ([Software Escolhido](../../fase1/softwareEscolhido.md#31-fluxo-de-uso-avaliado)):

| ID | Tarefa | Condição de Sucesso | Perfil |
| :---: | :--- | :--- | :--- |
| **T1** | Localizar Previsão de Formatura | Acessar `/plano-formatura` e relatar verbalmente o semestre previsto e os semestres restantes em até 60s sem auxílio. | Concluinte / Meio de curso |
| **T2** | Interpretar Matérias Críticas | Identificar e apontar ao menos duas matérias críticas e seus respectivos semestres futuros no painel/grafo. | Aluno com reprovações ou atraso |
| **T3** | Ajustar Limite de Créditos | Alterar o limite de créditos por semestre (ex.: 20 créditos) e confirmar a atualização visual do plano. | Aluno estagiário / trabalhador |

---

## 4. Fichas das Métricas de Usabilidade

### `MET-OP-01` — Taxa de Sucesso na Realização de Tarefas (TSRT)

| Campo | Especificação |
| :--- | :--- |
| **Identificador** | `MET-OP-01` |
| **Nome** | Taxa de Sucesso na Realização de Tarefas (TSRT) |
| **Característica** | Usabilidade — Operabilidade (*Operability*) |
| **Questão GQM** | `Q-OP-01`: Os estudantes realizam as tarefas essenciais com autonomia? |
| **Hipótese Relacionada** | **`H-OP-01`**: A densidade de nós e controles gera hesitação e demanda auxílio para encontrar a previsão e matérias críticas. |
| **Definição** | Proporção de estudantes que concluem cada tarefa ($T_1, T_2, T_3$) de forma autônoma, sem assistência do avaliador. Unidade: percentual (%). |
| **Cálculo** | Taxa por tarefa:<br>$$TSRT_j = \left( \frac{N_{\text{sucesso\_sem\_ajuda}, j}}{N_{\text{tentativas\_validas}, j}} \right) \times 100$$<br>Taxa global consolidada (média das $K = 3$ tarefas):<br>$$TSRT_{\text{global}} = \frac{1}{K} \sum_{j=1}^{K} TSRT_j$$ |
| **Fonte** | Planilhas de observação direta e gravações de tela ($N \ge 5$ participantes). |
| **Coleta** | 1. Recrutar 5 alunos de diferentes semestres da UnB.<br>2. Configurar ambiente com conta de teste e histórico sintético.<br>3. Aplicar as tarefas $T_1$, $T_2$ e $T_3$ usando *Think Aloud*.<br>4. Registrar: sucesso autônomo (1), com ajuda (0) ou falha/desistência (0).<br>5. Calcular as taxas individuais e global. |
| **Níveis de Julgamento** | - **Excelente:** $TSRT_j \ge 85\%$ e $TSRT_{\text{global}} \ge 90\%$ (alta operabilidade, refuta `H-OP-01`).<br>- **Aceitável:** $70\% \le TSRT_j < 85\%$ (usável, mas com fricção perceptível).<br>- **Crítico:** $TSRT_j < 70\%$ (baixa affordance ou layout confuso; **confirma `H-OP-01`** e subsidia melhoria na Fase 4). |

---

### `MET-OP-01b` — Taxa de Conclusão com Assistência (TCA)

| Campo | Especificação |
| :--- | :--- |
| **Identificador** | `MET-OP-01b` |
| **Nome** | Taxa de Conclusão com Assistência (TCA) |
| **Característica** | Usabilidade — Apreensibilidade (*Learnability*) |
| **Questão GQM** | `Q-OP-01`: Os estudantes realizam as tarefas essenciais com autonomia? |
| **Hipótese Relacionada** | **`H-OP-01`**: A incompreensão das saídas visuais transfere para o estudante a necessidade de pedir auxílio externo. |
| **Definição** | Proporção de tentativas em que o participante só atingiu o objetivo após solicitar intervenção ou receber ajuda do avaliador. Unidade: percentual (%). |
| **Cálculo** | $$TCA_j = \left( \frac{N_{\text{ajuda}, j}}{N_{\text{tentativas\_validas}, j}} \right) \times 100$$ |
| **Fonte** | Folhas de observação direta das sessões de teste. |
| **Coleta** | Coletada em paralelo com a `MET-OP-01`. Cada intervenção ou pedido explícito de ajuda é registrado como evento de assistência. |
| **Níveis de Julgamento** | - **Desejável:** $TCA_j \le 10\%$ (autonomia do usuário, refuta `H-OP-01`).<br>- **Tolerável:** $10\% < TCA_j \le 25\%$ (demanda tooltips ou melhorias de onboarding).<br>- **Crítico:** $TCA_j > 25\%$ (interface pouco autoexplicativa; **confirma `H-OP-01`**). |

---

## 5. Análise com Heurísticas de Nielsen

Os resultados de usabilidade serão confrontados com três heurísticas-chave:

1. **Visibilidade do Estado do Sistema (Heurística #1):** o sistema fornece feedback imediato ao alterar o limite de créditos ($T_3$)?
2. **Correspondência com o Mundo Real (Heurística #2):** o conceito de "matérias críticas" é intuitivo para os alunos da UnB?
3. **Controle e Liberdade do Usuário (Heurística #3):** é fácil desfazer ou resetar configurações no plano gerado?

Observações qualitativas das sessões alimentarão o relatório da Fase 4 com propostas de melhoria de interface.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Elaboração da especificação de usabilidade, tarefas padronizadas, fichas MET-OP-01 e MET-OP-01b | 16/10 | [c821ea3](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/c821ea3) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Remoção de referências a divisões internas de pessoas e padronização documental | 16/10 | [81912ba](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/81912bac5e02d7429e2d05446544ec9636891f5e) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Simplificação textual e concisão mantendo coerência com GQM e ISO 9241-11 | 24/10 | [corrente] |

