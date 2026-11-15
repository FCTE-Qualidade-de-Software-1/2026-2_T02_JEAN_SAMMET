# Análise dos Resultados e Julgamento da Qualidade (Fase 4)

Este documento realiza a **análise comparativa dos dados brutos contra os critérios de pontuação e níveis de julgamento** definidos na Fase 2 ([Métricas Operacionais](../../fase2/metricasOperacionais.md)), concluindo com o **julgamento formal da qualidade** e a **validação empírica das hipóteses operacionais** segundo o processo **ISO/IEC 25040:2011/2024**.

---

## 1. Julgamento das Métricas de Usabilidade

### 1.1 `MET-OP-01` — Taxa de Conformidade Heurística (TCH)

* **Fórmula de Cálculo:**
  $$TCH = \left( \frac{N_{\text{itens\_conformes}}}{N_{\text{total\_itens}}} \right) \times 100 = \left( \frac{7}{10} \right) \times 100 = \mathbf{70{,}0\%}$$
* **Confronto com os Níveis de Julgamento da Fase 2:**
  * *Excelente:* $TCH \ge 85\%$
  * *Aceitável:* $70\% \le TCH < 85\%$
  * *Crítico:* $TCH < 70\%$
* **Julgamento:** **`ACEITÁVEL`**
* **Interpretação:** A interface da rota `/plano-formatura` atinge o patamar limítrofe de aceitabilidade. Sete das dez heurísticas clássicas de Nielsen foram atendidas, garantindo operabilidade básica e permitindo que o estudante navegue e interprete o fluxo, ainda que com fricções de usabilidade em funções específicas.

---

### 1.2 `MET-OP-01b` — Índice de Severidade de Violações Heurísticas (ISVH)

* **Fórmula de Cálculo:**
  $$ISVH = (4 \times N_{\text{catastrófico}}) + (3 \times N_{\text{maior}}) + (2 \times N_{\text{menor}}) + (1 \times N_{\text{cosmético}})$$
  $$ISVH = (4 \times 0) + (3 \times 1) + (2 \times 1) + (1 \times 1) = 0 + 3 + 2 + 1 = \mathbf{6\text{ pontos}}$$
* **Confronto com os Níveis de Julgamento da Fase 2:**
  * *Excelente:* $N_{\text{catastrófico}} = 0$, $N_{\text{maior}} = 0$ e $ISVH \le 5$
  * *Aceitável:* $N_{\text{catastrófico}} = 0$, $N_{\text{maior}} \le 1$ e $ISVH \le 12$
  * *Crítico:* $N_{\text{catastrófico}} \ge 1$ ou $N_{\text{maior}} > 1$ ou $ISVH > 12$
* **Julgamento:** **`ACEITÁVEL`**
* **Interpretação:** A ausência de falhas catastróficas ($N_{\text{catastrófico}} = 0$) e a presença de apenas uma violação de severidade maior ($N_{\text{maior}} = 1$) mantêm o índice global em 6 pontos, dentro do limite de aceitabilidade ($\le 12$). Contudo, o Item 3 (falta de botão de desfazer/resetar) representa a maior barreira ergonômica observada na ferramenta.

---

## 2. Julgamento das Métricas de Segurança

### 2.1 `MET-OP-02` — Vulnerabilidades em Dependências (DVCD / IRP)

* **Fórmula de Cálculo:**
  $$IRP = (10 \times 0) + (5 \times 0) + (2 \times 0) + (1 \times 0) = \mathbf{0\text{ pontos}}$$
* **Confronto com os Níveis de Julgamento da Fase 2:**
  * *Excelente:* $N_{\text{crítica}} = 0$, $N_{\text{alta}} = 0$ e $IRP \le 5$
  * *Aceitável:* $N_{\text{crítica}} = 0$, $N_{\text{alta}} \le 2$ e $IRP \le 20$
  * *Crítico:* $N_{\text{crítica}} \ge 1$ ou $N_{\text{alta}} > 2$
* **Julgamento:** **`EXCELENTE`**
* **Interpretação:** A auditoria via Retire.js sobre os pacotes compilados em produção não detectou nenhuma biblioteca JavaScript de terceiros com vulnerabilidades públicas catalogadas (CVEs), evidenciando alta integridade na cadeia de componentes entregues ao navegador.

---

### 2.2 `MET-OP-02b` — Grau de Exposição de Dados Pessoais no Cliente (GED-C)

* **Fórmula de Cálculo:**
  $$GED\text{-}C = \mathbf{0\text{ chaves sensíveis}}$$
* **Confronto com os Níveis de Julgamento da Fase 2:**
  * *Conforme (Desejável):* $GED\text{-}C = 0$
  * *Não Conforme (Crítico):* $GED\text{-}C \ge 1$
* **Julgamento:** **`CONFORME (DESEJÁVEL)`**
* **Interpretação:** A aplicação não retém dados acadêmicos ou identificadores dos estudantes (matrícula, notas, IRA) em texto claro no `localStorage` ou `sessionStorage`, mantendo apenas preferências cosméticas de interface (`theme: "dark"`). Cumpre integralmente os requisitos da LGPD para proteção da privacidade em repouso.

---

### 2.3 `MET-OP-02c` — Taxa de Bloqueio em Rotas Não Autenticadas (TBR)

* **Fórmula de Cálculo:**
  $$TBR = \left( \frac{N_{\text{respostas\_401\_ou\_403}}}{10} \right) \times 100 = \left( \frac{0}{10} \right) \times 100 = \mathbf{0{,}0\%}$$
* **Confronto com os Níveis de Julgamento da Fase 2:**
  * *Conforme (Mandatório):* $TBR = 100\%$ (Bloqueio estrito com 401 ou 403)
  * *Crítico (Falha Grave):* $TBR < 100\%$
* **Julgamento:** **`NÃO CONFORME (CRÍTICO)`**
* **Interpretação:** As requisições enviadas ao endpoint responderam com `HTTP 405 Method Not Allowed`. Sob a ótica estrita da especificação da Fase 2 (que exigia respostas específicas de autorização HTTP 401/403), a métrica é julgada como Não Conforme. Essa constatação evidencia que a camada de borda (Nginx) rejeita o verbo antes de avaliar o token, ou que o serviço de planejamento é consumido internamente sem exposição de rota REST pública direta.

---

## 3. Validação das Hipóteses Operacionais

O confronto dos dados experimentais contra os critérios formais de validação definidos na Fase 2 consolida o seguinte resultado:

| Hipótese | Enunciado Documentado na Fase 2 | Critério Formal de Validação | Resultado Empírico | Veredito |
| :---: | :--- | :--- | :--- | :---: |
| **`H-OP-01`** | A tela `/plano-formatura` concentra violações heurísticas, comprometendo a facilidade de uso e a apreensão das saídas. | **Confirmada** se $TCH < 85\%$ ou se for identificada qualquer violação com severidade maior ou catastrófica ($N_{\text{maior}} \ge 1$ ou $N_{\text{catastrófico}} \ge 1$). | $TCH = 70{,}0\%$ ($< 85\%$) e $N_{\text{maior}} = 1$ no Item 3 (Controle do usuário). | **`CONFIRMADA`** |
| **`H-OP-02`** | O processamento no navegador com retenção em `localStorage` e dependências desatualizadas pode expor dados sensíveis e vulnerabilidades conhecidas. | **Confirmada** se $IRP > 5$, $GED\text{-}C \ge 1$ chave sensível ou $TBR < 100\%$. | $IRP = 0$, $GED\text{-}C = 0$, mas $TBR = 0{,}0\%$ ($< 100\%$). | **`CONFIRMADA PARCIALMENTE`** |

---

## 4. Comparação com os Critérios GQM e Resposta Formal às Questões de Medição

Em estrita consonância com o método **Goal-Question-Metric (GQM)** e as atividades de encerramento da **ISO/IEC 25040**, os valores medidos empiricamente são comparados contra a grade de decisão para responder de maneira conclusiva às questões formuladas na Fase 2:

### 4.1 Tabela Comparativa: Valores Medidos vs. Critérios de Julgamento GQM

| Questão GQM | Métrica | Valor Obtido na Avaliação | Critérios de Julgamento GQM (Fase 2) | Nível Atingido |
| :---: | :---: | :---: | :--- | :---: |
| **`Q-OP-01`** | **`MET-OP-01` (TCH)** | **`70,0%`** | • Excelente: $TCH \ge 85\%$<br>• **Aceitável: $70\% \le TCH < 85\%$**<br>• Crítico: $TCH < 70\%$ | **Aceitável** |
| **`Q-OP-01`** | **`MET-OP-01b` (ISVH)** | **`6 pts`** | • Excelente: $N_{\text{cat}} = 0, N_{\text{maior}} = 0, ISVH \le 5$<br>• **Aceitável: $N_{\text{cat}} = 0, N_{\text{maior}} \le 1, ISVH \le 12$**<br>• Crítico: $N_{\text{cat}} \ge 1, N_{\text{maior}} > 1$ ou $ISVH > 12$ | **Aceitável** |
| **`Q-OP-02`** | **`MET-OP-02` (DVCD/IRP)** | **`0 pts`** | • **Excelente: $N_{\text{crít}} = 0, N_{\text{alta}} = 0, IRP \le 5$**<br>• Aceitável: $N_{\text{crít}} = 0, N_{\text{alta}} \le 2, IRP \le 20$<br>• Crítico: $N_{\text{crít}} \ge 1$ ou $N_{\text{alta}} > 2$ | **Excelente** |
| **`Q-OP-02`** | **`MET-OP-02b` (GED-C)** | **`0 chaves`** | • **Conforme (Desejável): $GED\text{-}C = 0$**<br>• Não Conforme (Crítico): $GED\text{-}C \ge 1$ | **Conforme** |
| **`Q-OP-02`** | **`MET-OP-02c` (TBR)** | **`0,0%`** | • Conforme (Mandatório): $TBR = 100\%$<br>• **Crítico (Falha Grave): $TBR < 100\%$** | **Não Conforme** |

---

### 4.2 Resposta Formal à Questão `Q-OP-01` (Usabilidade)

> **Questão `Q-OP-01`:** *A interface da tela de planejamento atende às heurísticas ergonômicas de usabilidade essenciais para operação e apreensão autônoma?*

**Resposta Formal:**  
**Sim, em nível aceitável, com ressalvas funcionais específicas.**  
A avaliação empírica demonstrou que a interface atende a **70,0% das heurísticas ergonômicas de Nielsen (`MET-OP-01`)**, sustentando um Índice de Severidade de **6 pontos (`MET-OP-01b`)**, sem nenhuma violação catastrófica. O estudante consegue navegar satisfatoriamente pelas tarefas de localizar a estimativa de formatura ($T_1$) e interpretar o fluxo curricular ($T_2$). No entanto, a ferramenta apresenta deficiência relevante na **liberdade e controle do usuário** (Item 3, severidade 3), decorrente da ausência de botões para desfazer alterações ou restaurar configurações padrão ao manipular o controle de créditos ($T_3$), além de carência de legendas contextuais de auxílio (Item 10). Essas deficiências não impedem a operação básica, mas confirmam a hipótese $H\text{-}OP\text{-}01$ e fundamentam a necessidade da ação de melhoria proposta.

---

### 4.3 Resposta Formal à Questão `Q-OP-02` (Segurança)

> **Questão `Q-OP-02`:** *O sistema resguarda a confidencialidade dos dados acadêmicos e restringe o acesso aos serviços contra vulnerabilidades conhecidas e chamadas não autenticadas?*

**Resposta Formal:**  
**Sim para confidencialidade e integridade cliente; inconclusivo/não conforme para a rota REST direta.**  
A avaliação comprovou que a aplicação **resguarda integralmente a confidencialidade dos dados discentes no navegador**, apresentando **$GED\text{-}C = 0$ chaves sensíveis em texto claro no `localStorage` (`MET-OP-02b`)**, em estrito cumprimento às diretrizes da LGPD. Ademais, a análise de composição estática de software via Retire.js resultou em **$IRP = 0$ (`MET-OP-02`)**, atestando a ausência de componentes JavaScript desatualizados com vulnerabilidades conhecidas na entrega cliente. Por outro lado, para a métrica de controle de acesso (`MET-OP-02c`), a suíte de testes negativos obteve **$TBR = 0{,}0\%$**, visto que todas as requisições disparadas contra a rota de API foram interceptadas pelo servidor com `HTTP 405 Method Not Allowed`, em vez de processadas pelas regras de autenticação da aplicação (HTTP 401/403), indicando que o serviço não está exposto para consumo REST público desprotegido.

---

## 5. Integração e Validação Cruzada com Métricas Funcionais

A integração dos achados operacionais com as medições de Adequação Funcional revela uma correlação essencial:
- **Usabilidade × Funcionalidade:** O motor curricular gera a distribuição de semestres com boa precisão lógica, porém a interface falha em dar **liberdade de reversão ao estudante** ($TCH = 70{,}0\%$, Item 3 com severidade 3). Caso o aluno simule uma carga horária reduzida e deseje retornar ao plano inicial, ele é forçado a recarregar a página, gerando fricção desnecessária.
- **Conclusão Integrada:** A melhoria mais urgente para a ferramenta não está no algoritmo matemático de cálculo, mas na **ergonomia da interface**, justificando a priorização da Ação de Melhoria.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Análise detalhada dos resultados, cálculo das 5 métricas operacionais e julgamento das hipóteses H-OP-01 e H-OP-02 | 14/11/2026 | [6594e5c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/6594e5c2349ee5fc4dc632f07b97bc8191357819) |

