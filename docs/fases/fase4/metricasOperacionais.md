# Execução e Conclusão da Avaliação — Métricas Operacionais (Fase 4)

Este documento centraliza e sintetiza os resultados da **Fase 4 — Executar e Concluir a Avaliação** do processo **ISO/IEC 25040:2011/2024**, apresentando os **dados brutos coletados**, a **análise comparativa com os critérios de julgamento da Fase 2**, a **validação das hipóteses operacionais** e a **ação de melhoria proposta**.

Toda a avaliação foi realizada sob a abordagem **estritamente Caixa-Preta (*Black-Box Testing*)** sobre a aplicação pública em produção `https://no-fluxo.crianex.com`, sem necessidade de acesso ao código-fonte interno.

---

## 1. Navegação pelas Páginas da Fase 4 (Métricas Operacionais)

| Seção / Página | Conteúdo e Foco Principal | Métricas Relacionadas |
| :--- | :--- | :---: |
| **[1. Dados Brutos e Evidências](operacionais/dadosBrutos.md)** | Catálogo completo dos registros experimentais, planilhas CSV, relatórios de auditoria e logs de rede coletados. | Todas |
| **[2. Análise dos Resultados e Julgamento](operacionais/analiseResultados.md)** | Comparação dos valores obtidos contra os níveis de pontuação da Fase 2, validação empírica de $H\text{-}OP\text{-}01$ e $H\text{-}OP\text{-}02$ e cruzamento com métricas funcionais. | Todas |
| **[3. Ação de Melhoria](operacionais/acaoMelhoria.md)** | Especificação técnica e prototipação da melhoria concreta priorizada (Implementação de botão de reversão de estado e controle do usuário). | `MET-OP-01`<br>`MET-OP-01b` |

---

## 2. Quadro Resumo dos Resultados Obtidos

| Métrica | Nome da Métrica | Característica / Foco | Valor Medido na Prática | Nível de Julgamento Obtido | Validação da Hipótese |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **`MET-OP-01`** | Taxa de Conformidade Heurística (TCH) | Usabilidade / Operabilidade | **`70,0%`** | **Aceitável** (Faixa 70%–84%) | **$H\text{-}OP\text{-}01$ Confirmada** |
| **`MET-OP-01b`** | Índice de Severidade de Violações (ISVH) | Usabilidade / Apreensibilidade | **`6 pontos`** | **Aceitável** (Faixa $\le 12$ pts) | **$H\text{-}OP\text{-}01$ Confirmada** |
| **`MET-OP-02`** | Vulnerabilidades em Dependências (DVCD / IRP) | Segurança / Integridade | **`IRP = 0`** (0 CVEs) | **Excelente** ($IRP \le 5$) | $H\text{-}OP\text{-}02$ Refutada no Cliente |
| **`MET-OP-02b`** | Exposição de Dados no Cliente (GED-C) | Segurança / Confidencialidade (LGPD) | **`GED-C = 0`** chaves | **Conforme / Desejável** | $H\text{-}OP\text{-}02$ Refutada no Storage |
| **`MET-OP-02c`** | Bloqueio em Rotas Não Autenticadas (TBR) | Segurança / Controle de Acesso | **`TBR = 0,0%`** (10/10 405 Method Not Allowed) | **Não Conforme (Crítico)** | **$H\text{-}OP\text{-}02$ Confirmada** |

---

## 3. Síntese do Julgamento da Qualidade

1. **Usabilidade:** O produto atende aos padrões mínimos operacionais ($TCH = 70{,}0\%$), oferecendo uma navegação viável, porém apresenta fricções concentradas na ausência de mecanismos para desfazer alterações de créditos (Item 3, severidade maior) e deficiências em mensagens de erro e legendas explicativas (Itens 9 e 10).
2. **Segurança do Cliente e Dados:** A aplicação demonstrou alta maturidade na entrega de pacotes web (nenhuma vulnerabilidade conhecida identificada nas bibliotecas JavaScript servidas via Retire.js) e total respeito à LGPD no armazenamento local (nenhum dado pessoal em claro no `localStorage`).
3. **Controle de Acesso em Rotas:** O endpoint avaliado respondeu com código de método não permitido (`HTTP 405`), confirmando que a rota não responde nos padrões de controle de acesso 401/403 ou não está exposta para consumo direto via POST não autenticado.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Elaboração da página principal da Fase 4 para métricas operacionais e consolidação dos resultados | 14/11/2026 | [6594e5c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/6594e5c2349ee5fc4dc632f07b97bc8191357819) |

