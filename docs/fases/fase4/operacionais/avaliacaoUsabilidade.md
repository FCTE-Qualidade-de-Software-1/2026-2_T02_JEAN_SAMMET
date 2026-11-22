# Avaliação de usabilidade — Equipe (linha de base)

## 1. Avaliadores e escopo

Gustavo e Gabriel inspecionaram as tarefas T1–T3 de `/plano-formatura`, com H0 no cenário C0. As avaliações individuais e o consenso registram as mesmas notas, severidades e observações, sem divergências entre os avaliadores.

Os registros individuais e o consenso ficam em `testes/evidencias/usabilidade/h0-2026-11-15/`: `gustavo.csv`, `gabriel.csv`, `consenso.csv` e `origem.md`.

## 2. Resultados por item

Nota 1 = Conforme; nota 0 = Não conforme. Severidade 2 = problema menor. As observações abaixo são comuns aos dois avaliadores, conforme a confirmação de Gustavo.

**Tabela 1 — Resultados por item.**

| Item | Meta do item | Gustavo | Gabriel | Consenso | Severidade do problema | Observação consolidada |
| --- | --- | --- | --- | --- | --- | --- |
| 1. Visibilidade do estado | 1 — Conforme | 1 | 1 | 1 | — | Mensagens de geração/recálculo presentes. |
| 2. Correspondência dos termos | 1 — Conforme | 0 | 0 | 0 | 2 | “Críticas/estratégicas” sem definição clara nas áreas examinadas do planejamento. |
| 3. Controle e liberdade | 1 — Conforme | 1 | 1 | 1 | — | Carga alterada e restaurada sem recarregar. |
| 4. Consistência | 1 — Conforme | 1 | 1 | 1 | — | Padrões consistentes nos cartões e estados do plano observado. |
| 5. Prevenção de erros | 1 — Conforme | 1 | 1 | 1 | — | -1 ajustado para 8; 100 ajustado para 32 créditos. |
| 6. Reconhecimento | 1 — Conforme | 1 | 1 | 1 | — | Previsão e semestres restantes em destaque. |
| 7. Flexibilidade | 1 — Conforme | 1 | 1 | 1 | — | Zoom e navegação funcionaram em H0. |
| 8. Design minimalista | 1 — Conforme | 1 | 1 | 1 | — | Sem sobreposição impeditiva no ambiente examinado. |
| 9. Tratamento de erros | 1 — Conforme | 0 | 0 | 0 | 2 | Correção dos créditos inválidos sem explicar ajuste/faixa; aviso de optativas orienta resolução. |
| 10. Ajuda contextual | 1 — Conforme | 1 | 1 | 1 | — | Orientações de carga e optativas; a lacuna do termo críticas foi registrada no item 2. |

*Fonte: registro da avaliação EC-01, organizado pela equipe.*

Não houve divergências a resolver. Os dois problemas foram mantidos no consenso, sem somar novamente o mesmo achado por avaliador.

## 3. Cálculo e julgamento

A coluna de meta explicita o nível desejado definido pelas faixas da Fase 2. Em TCH, ISVH e IRP, a referência é **Excelente**; um resultado pode ser classificado como Aceitável sem atingir esse nível.

**Tabela 2 — Cálculo e julgamento.**

| Medida | Cálculo do consenso | Resultado | Meta / nível desejado | Nível obtido |
| --- | --- | --- | --- | --- |
| TCH | 8 itens conformes / 10 × 100 | **80%** | ≥ 85% (Excelente) | **Aceitável** |
| ISVH | 2 problemas menores × 2 | **4** | ≤ 5 pontos, sem problemas maiores ou catastróficos (Excelente) | **Excelente** |

*Fonte: registro da avaliação EC-01, organizado pela equipe.*

**Q-OP-01: Aceitável**, pelo pior nível entre as duas métricas. **H-OP-01 corroborada no recorte**, pois TCH < 85%, conforme o critério da [Fase 2](../../fase2/operacionais/visaoGeral.md#2-hipoteses-operacionais-e-matriz-de-validacao). Não foram registrados problemas maiores ou catastróficos.

Prioridades: explicar os termos críticas/estratégicas e informar a faixa permitida e o motivo do ajuste de créditos inválidos. Após alteração, repetir T2/T3 e a inspeção.

## 4. Reavaliação após M-01

O consenso inicial acima é a linha de base e foi preservado nos CSVs. Após as explicações de termos e a mensagem de créditos, os itens 2 e 9 passaram a 1; os outros oito permaneceram em 1. O vetor final foi **[1,1,1,1,1,1,1,1,1,1]**, com TCH=100% e ISVH=0. A [ação de melhoria](acaoMelhoria.md) apresenta a intervenção e o comparativo, sem sobrescrever as folhas iniciais.

## 5. Limitações

O julgamento se restringe a H0, ao ambiente desktop e às tarefas examinadas. Não demonstra ausência de problemas em outros históricos, dispositivos ou condições de erro. Os registros foram transcritos conforme os resultados das avaliações e do consenso informados por Gustavo.

## 6. Referências

Referências usadas nesta página, conforme [Referências — Fase 2](../../../referencias/fase2.md) e [Referências — Fase 3](../../../referencias/fase3.md).

- NIELSEN, Jakob. **10 Usability Heuristics for User Interface Design**. Nielsen Norman Group, 1994. Disponível em: <https://www.nngroup.com/articles/ten-usability-heuristics/>.
- NIELSEN, Jakob. **Heuristic Evaluation**. In: NIELSEN, Jakob; MACK, Robert L. (Org.). *Usability Inspection Methods*. Nova York: John Wiley & Sons, 1994. p. 25-62.
- NIELSEN, Jakob. **Severity Ratings for Usability Problems**. Nielsen Norman Group, 1995. Disponível em: <https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/>. Acesso em: 14 nov. 2026.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
|---|---|---|---|
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Registro das avaliações de Gustavo e Gabriel, consenso e apuração da usabilidade | 15/11 | [f5e77d5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f5e77d5) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Consolidação da avaliação de Gustavo e Gabriel em página única | 15/11 | [f5e77d5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f5e77d5) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Explicitação das metas nas tabelas de resultados e avaliação | 15/11 | [f5e77d5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f5e77d5) |
| [Yasmim de Souza Santos](https://github.com/eii-yahs) | Inclusão das referências utilizadas na página | 22/11 | Não commitado |