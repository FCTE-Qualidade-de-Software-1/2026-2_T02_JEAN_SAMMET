# Ação de melhoria — Clareza do planejamento

*[Voltar para a Matriz Geral de Rastreabilidade](../../../rastreabilidade.md)*

## 1. Problema e objetivo

A inspeção de Gustavo e Gabriel identificou dois problemas menores: **item 2**, falta de explicação dos termos críticas/estratégicas; **item 9**, ajuste de créditos inválidos sem explicar motivo e faixa. A intervenção M-01 tratou esses dois pontos, mantendo H0 e as tarefas T1–T3.

**Objetivo:** aumentar TCH de 80% para pelo menos 85% e reduzir ISVH, sem introduzir problemas maiores/catastróficos. O conjunto de disciplinas e os critérios de segurança ficaram fora da intervenção.

## 2. Intervenção M-01

O protótipo interativo comparativo (Antes vs. Depois) das melhorias propostas — contemplando a intervenção M-01 de usabilidade e as melhorias de adequação funcional — está publicado em [Protótipo Interativo — Jean Sammet](https://gotc2607.github.io/Prot-tipo-JEAN-SAMMET/) ([repositório do protótipo](https://github.com/Gotc2607/Prot-tipo-JEAN-SAMMET)).

**Tabela 1 — Intervenção M-01.**

| Problema | Alteração executada | Critério de aceitação |
| --- | --- | --- |
| Termos sem explicação | Inserimos uma explicação acessível junto ao indicador de matérias críticas/estratégicas | Avaliadores conseguem consultar o significado no ponto de uso, por teclado ou ponteiro |
| Ajuste silencioso de créditos | Incluímos mensagem: “Informe de 8 a 32 créditos. O valor foi ajustado para a faixa permitida.” | Valores inválidos são ajustados e o motivo/faixa é informado |

*Fonte: registro da avaliação EC-01, organizado pela equipe.*

A explicação dos termos orienta a leitura do plano; não afirma que uma matéria destacada já foi aprovada. A faixa 8–32 corresponde ao controle examinado. Ela não deve ser confundida com a sugestão de 4/6/8 matérias nem com o limite curricular de 480h.

## 3. Reavaliação

Repetimos T1–T3 e o checklist com Gustavo e Gabriel. Os dois avaliadores concordaram nas dez notas finais. Itens 2 e 9 passaram a conformes; os demais permaneceram conformes. Os dois problemas menores foram encerrados.

**Tabela 2 — Reavaliação.**

| Item / verificação | Antes | Depois | Meta | Resultado |
| --- | --- | --- | --- | --- |
| Item 2 — Correspondência dos termos | Nota 0; severidade 2 | Nota 1; problema resolvido | Nota 1 | **Atendido** |
| Item 9 — Tratamento de erros | Nota 0; severidade 2 | Nota 1; problema resolvido | Nota 1 | **Atendido** |
| Demais oito itens | Notas 1 | Notas 1 | Manter conformidade | **Sem regressão no checklist** |

*Fonte: registro da avaliação EC-01, organizado pela equipe.*

## 4. Comparação das métricas

**Tabela 3 — Comparação das métricas.**

| Métrica | Antes | Depois | Meta | Variação | Julgamento após intervenção |
| --- | --- | --- | --- | --- | --- |
| **TCH** | 8/10 = **80%** | 10/10 = **100%** | ≥ 85% | **+20 pontos percentuais** | **Excelente** |
| **ISVH** | 2+2 = **4** | **0** | ≤ 5, sem maior/catastrófico | **−4 pontos** | **Excelente** |
| **Q-OP-01** | Aceitável | **Excelente** | Pior nível entre TCH/ISVH | Melhoria de nível | **Meta atingida** |
| **H-OP-01** | Corroborada | **Não corroborada no recorte reavaliado** | TCH ≥ 85% e sem maior/catastrófico | Dois problemas resolvidos | Diagnóstico inicial preservado |

*Fonte: registro da avaliação EC-01, organizado pela equipe.*

## 5. Alcance e recomendações

A intervenção M-01 encerra a ação de melhoria de EC-01. A melhoria de usabilidade não resolve FGA0206, as preferências, oferta/calendário nem GED-C=3. Esses achados permanecem nas recomendações do [encerramento](../conclusao.md).

O resultado após M-01 é específico do checklist, de H0 e do ambiente desktop. Não representa validação de acessibilidade completa, estudo com estudantes externos ou nova avaliação de toda a segurança.

## 6. Referências

Referências usadas nesta página, conforme [Referências — Fase 2](../../../referencias/fase2.md) e [Referências — Fase 3](../../../referencias/fase3.md).

- NIELSEN, Jakob. **10 Usability Heuristics for User Interface Design**. Nielsen Norman Group, 1994. Disponível em: <https://www.nngroup.com/articles/ten-usability-heuristics/>.
- NIELSEN, Jakob. **Severity Ratings for Usability Problems**. Nielsen Norman Group, 1995. Disponível em: <https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/>. Acesso em: 14 nov. 2026.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Elaboração da ação de melhoria de usabilidade, prototipação em SvelteKit e projeção de impacto nas métricas | 14/11 | [6594e5c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/6594e5c2349ee5fc4dc632f07b97bc8191357819) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Identificação dos resultados anteriores como pendentes de revalidação | 15/11 | [0e38da3](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/0e38da3eac882c62bf7c6f9e1bda97a8b744ef2e) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Coleta assistida com H0, apuração e julgamento com cobertura identificada | 15/11 | [f5e77d5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f5e77d5) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Registro das avaliações da equipe e atualização do julgamento de usabilidade | 15/11 | [f5e77d5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f5e77d5) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Detalhamento dos critérios de verificação das melhorias propostas | 15/11 | [f5e77d5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f5e77d5) |
| [Yasmim de Souza Santos](https://github.com/eii-yahs) | Inclusão das referências utilizadas na página | 22/11 | Não commitado |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Inclusão do link do protótipo interativo publicado e do seu repositório na intervenção M-01 | 23/11 | [0ac2041](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/0ac2041a2ea30b37f9e4afc2ade46f5a1564c37b) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Inclusão de link de retorno para a Matriz Geral de Rastreabilidade | 24/11 | [8f30292](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/8f302921912ed18ed6f6a18507c2bbab654f3366) |
