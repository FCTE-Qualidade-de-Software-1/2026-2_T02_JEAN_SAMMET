# Evidências de Usabilidade (Fase 3 / Fase 4)

Este diretório armazena os dados brutos e planilhas de inspeção heurística para as métricas `MET-OP-01` ($TCH$) e `MET-OP-01b` ($ISVH$), em conformidade com o método de **Nielsen (1994)** e a norma **ISO/IEC 25040:2011/2024**.

---

## 1. Avaliador Responsável

* **Avaliador:** [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) (Avaliador nominal designado no [Protocolo da Fase 2](../../docs/fases/fase2/operacionais/protocolo.md)).
* **Data da Inspeção:** 14/11/2026
* **Ambiente:** Google Chrome em Janela Anônima (1920 × 1080, zoom 100%).
* **URL:** `https://no-fluxo.crianex.com/plano-formatura`
* **Arquivo de Dados Brutos:** [`avaliacao_individual_giovani.csv`](avaliacao_individual_giovani.csv)

---

## 2. Resultados Consolidados da Avaliação

* **Itens Conformes:** 7 / 10
* **Taxa de Conformidade Heurística ($TCH$ - `MET-OP-01`):** **70,0%** (Status: **Aceitável**)
* **Violações Registradas:**
  * **Item 3 (Controle e liberdade do usuário):** Não Conforme — **Severidade 3 (Maior)**. *Falta de mecanismo direto para desfazer ou resetar alterações de créditos sem recarregar a página.*
  * **Item 9 (Recuperação de erros):** Não Conforme — **Severidade 2 (Menor)**. *Mensagens insuficientes ou genéricas em casos de conflitos ou incompatibilidades curriculares.*
  * **Item 10 (Ajuda e documentação):** Não Conforme — **Severidade 1 (Cosmético)**. *Carência de tooltips ou pequenas legendas contextuais explicando regras do motor de planejamento.*
* **Índice de Severidade ($ISVH$ - `MET-OP-01b`):**
  $$ISVH = (4 \times 0) + (3 \times 1) + (2 \times 1) + (1 \times 1) = \mathbf{6\text{ pontos}}$$
  (Status: **Aceitável**).

---

## 3. Conclusão e Validação da Hipótese $H\text{-}OP\text{-}01$

* **Hipótese:** A interface concentra violações heurísticas que geram atrito na operabilidade.
* **Veredito:** **Confirmada** ($TCH < 85\%$ e presença de $N_{\text{maior}} = 1$).
* **Ação de Melhoria Embasada:** Implementação de botão de reversão de estado / saída de emergência na interface SvelteKit (Item 3).
