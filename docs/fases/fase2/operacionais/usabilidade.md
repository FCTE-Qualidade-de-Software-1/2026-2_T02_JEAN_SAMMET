# Métricas de Usabilidade

Este documento detalha a especificação das perguntas, hipóteses e métricas de **Usabilidade** para a funcionalidade _Planejar formatura_ do No Fluxo UnB, focando na facilidade de operação e compreensão por parte dos estudantes de graduação da UnB.

---

## 1. Característica e Subcaracterísticas Avaliadas

Conforme o [Modelo de Qualidade](../../fase1/modeloDeQualidade.md) baseado na **ISO/IEC 25010:2011**, a Usabilidade é investigada através de duas subcaracterísticas centrais:

1. **Operabilidade (_Operability_):** grau em que a interface tem atributos que tornam fácil sua operação e controle pelo aluno ao navegar pelos semestres, ajustar créditos e interagir com o grafo.
2. **Apreensibilidade (_Learnability_):** grau em que o software permite ao estudante compreender rapidamente o significado das informações geradas (como a previsão de formatura e o conceito de matérias críticas) sem depender de treinamento formal ou suporte humano.

---

## 2. Questão GQM e Hipótese Associada

### Questão GQM: `Q-OP-01`
> **"Os estudantes conseguem realizar as tarefas essenciais na tela de planejamento com autonomia, sem necessidade de assistência externa?"**

### Hipótese Operacional: `H-OP-01`
> **Hipótese:** A interface da tela `/plano-formatura` concentra alta densidade de nós de disciplinas, conexões de dependência e controles simultâneos, fazendo com que uma proporção relevante de alunos hesite ou necessite de auxílio para identificar o semestre previsto de formatura e compreender quais matérias são críticas.

---

## 3. Tarefas de Avaliação Padronizadas

Para responder à questão `Q-OP-01` de forma empírica e controlada, foram estabelecidas três tarefas fundamentais baseadas no fluxo de uso real ([Software Escolhido](../../fase1/softwareEscolhido.md#31-fluxo-de-uso-avaliado)):

| ID | Nome da Tarefa | Descrição e Condição de Sucesso | Perfil Beneficiado |
| :---: | :--- | :--- | :--- |
| **T1** | Localizar a Previsão de Formatura | O aluno deve entrar na tela `/plano-formatura` e enunciar verbalmente o semestre previsto de formatura e os semestres restantes calculados pelo sistema.<br>**Sucesso:** relatar os valores exibidos no card de resumo sem auxílio em até 60 segundos. | Aluno concluinte e de meio de curso |
| **T2** | Interpretar Matérias Críticas | O aluno deve identificar quais disciplinas da sua grade foram classificadas como "matérias críticas" e em quais semestres futuros elas estão alocadas.<br>**Sucesso:** apontar ao menos duas matérias críticas e seu semestre correspondente no grafo/painel. | Aluno com reprovações ou atraso |
| **T3** | Ajustar Limite de Créditos | O aluno deve localizar o controle de limite de créditos por semestre, alterar o valor para um patamar específico (ex.: 20 créditos) e solicitar a atualização do plano.<br>**Sucesso:** ajustar o slider/input e confirmar a atualização visual do plano gerado. | Aluno trabalhador ou estagiário |

---

## 4. Fichas Completas das Métricas de Usabilidade

### Ficha da Métrica Principal: `MET-OP-01` — Taxa de Sucesso na Realização de Tarefas (TSRT)

| Campo | Especificação Metodológica |
| :--- | :--- |
| **Identificador** | `MET-OP-01` |
| **Nome da Métrica** | Taxa de Sucesso na Realização de Tarefas (TSRT) |
| **Característica / Subcaracterística** | Usabilidade — Operabilidade (*Operability*) |
| **Pergunta GQM Relacionada** | `Q-OP-01`: Os estudantes conseguem realizar as tarefas essenciais na tela de planejamento com autonomia? |
| **1. Definição** | Mede a proporção de estudantes avaliados que concluem com êxito cada tarefa padronizada ($T_1, T_2, T_3$) sem receber assistência ou dicas do avaliador durante a sessão experimental. Unidade: percentual (%). |
| **2. Procedimento de Cálculo** | Para cada tarefa específica $j$ ($j \in \{T_1, T_2, T_3\}$), a taxa individual é dada por:<br><br>$$TSRT_j = \left( \frac{N_{\text{sucesso\_sem\_ajuda}, j}}{N_{\text{tentativas\_validas}, j}} \right) \times 100$$<br>Onde:<br>- $N_{\text{sucesso\_sem\_ajuda}, j}$: quantidade de participantes que atingiram a condição de sucesso de forma totalmente autônoma.<br>- $N_{\text{tentativas\_validas}, j}$: total de participantes avaliados para a tarefa $j$.<br><br>A taxa consolidada de usabilidade da sessão é a média aritmética simples das tarefas:<br>$$TSRT_{\text{global}} = \frac{1}{K} \sum_{j=1}^{K} TSRT_j \quad (K = 3)$$ |
| **3. Fonte dos Dados** | Planilha padronizada de registro de sessões de usabilidade preenchida pelos avaliadores a partir de observação direta e/ou gravações de tela das sessões (amostra de $N \ge 5$ participantes). |
| **4. Procedimento de Coleta** | 1. Recrutar 5 alunos da UnB abrangendo diferentes momentos do curso (iniciante, meio de curso, formando).<br>2. Abrir o ambiente de teste com conta autenticada e histórico acadêmico sintético carregado.<br>3. Instruir o participante a executar sequencialmente as tarefas $T_1$, $T_2$ e $T_3$ conforme o roteiro padronizado, utilizando a técnica de *Think Aloud* (pensar em voz alta).<br>4. O avaliador cronometra a execução e anota se a conclusão ocorreu sem ajuda (1), com ajuda externa (0) ou falha/desistência (0).<br>5. Consolidar os dados brutos e calcular os percentuais por tarefa e global. |
| **5. Critérios de Interpretação e Níveis de Julgamento** | - **Nível Excelente:** $TSRT_j \ge 85\%$ e $TSRT_{\text{global}} \ge 90\%$. Indica alta operabilidade e interface intuitiva, aderente às normas de ergonomia de software (ISO 9241-11).<br>- **Nível Aceitável:** $70\% \le TSRT_j < 85\%$. Tarefa realizável pela maioria dos alunos, porém com fricção perceptível.<br>- **Nível Crítico / Inaceitável:** $TSRT_j < 70\%$. Evidencia falha grave de affordance visual, terminologia confusa ou desorganização de layout, servindo como subsídio mandatório para as propostas de melhoria na Fase 4. |

---

### Ficha da Métrica Complementar: `MET-OP-01b` — Taxa de Conclusão com Assistência (TCA)

| Campo | Especificação Metodológica |
| :--- | :--- |
| **Identificador** | `MET-OP-01b` |
| **Nome da Métrica** | Taxa de Conclusão com Assistência (TCA) |
| **Característica / Subcaracterística** | Usabilidade — Apreensibilidade (*Learnability*) |
| **Pergunta GQM Relacionada** | `Q-OP-01`: Os estudantes conseguem realizar as tarefas essenciais na tela de planejamento com autonomia? |
| **1. Definição** | Percentual de tarefas em que o estudante só atingiu o objetivo após solicitar intervenção, esclarecimento conceitual ou auxílio do avaliador para destravar a interação. Unidade: percentual (%). |
| **2. Procedimento de Cálculo** | $$TCA_j = \left( \frac{N_{\text{ajuda}, j}}{N_{\text{tentativas\_validas}, j}} \right) \times 100$$<br>Onde $N_{\text{ajuda}, j}$ é o número de tentativas em que o participante necessitou de suporte para concluir a tarefa $j$. |
| **3. Fonte dos Dados** | Folhas de observação direta das sessões com participantes e anotação das intervenções do avaliador. |
| **4. Procedimento de Coleta** | Registrada em concomitância com a coleta da métrica `MET-OP-01`. Cada solicitação explícita do participante como _"onde eu clico agora?"_ ou intervenção do avaliador após tempo limite é contabilizada como evento de assistência. |
| **5. Critérios de Interpretação e Níveis de Julgamento** | - **Nível Desejável:** $TCA_j \le 10\%$. Autonomia quase total do usuário.<br>- **Nível Tolerável:** $10\% < TCA_j \le 25\%$. Indica necessidade pontual de melhoria de dicas de interface (*tooltips* ou *onboarding* contextual).<br>- **Nível Crítico:** $TCA_j > 25\%$. A interface não se sustenta de forma independente, transferindo para o usuário a carga de adivinhar o comportamento dos controles. |

---

## 5. Análise de Heurísticas de Usabilidade e Barreiras Mapeadas

A interpretação das métricas operacionais de usabilidade será confrontada com as heurísticas consagradas de Jakob Nielsen:

1. **Visibilidade do Estado do Sistema (Heurística #1):**
   - Ao alterar o limite de créditos (Tarefa $T_3$), o sistema fornece retorno imediato ou o aluno fica em dúvida se o plano foi recalculado?
2. **Correspondência entre o Sistema e o Mundo Real (Heurística #2):**
   - O conceito de "matérias críticas" é intuitivo para os alunos da UnB ou se confunde com disciplinas obrigatórias pendentes comuns?
3. **Controle e Liberdade do Usuário (Heurística #3):**
   - Caso o estudante cometa um erro de configuração na tela de planejamento, é fácil desfazer ou resetar para a sugestão padrão do sistema?

As respostas qualitativas observadas durante as sessões de teste alimentarão o relatório final da Fase 4 com propostas de prototipação e correção de interface.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Elaboração da especificação de usabilidade, tarefas padronizadas, fichas MET-OP-01 e MET-OP-01b | 16/10 | [c821ea3](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/c821ea3) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Remoção de referências a divisões internas de pessoas e padronização documental | 16/10 | [c19a4e8](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/c19a4e8) |
