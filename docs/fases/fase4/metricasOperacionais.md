# Avaliação operacional — Fase 4

*[Voltar para a Matriz Geral de Rastreabilidade](../../rastreabilidade.md)*

**EC-01 · Cinco métricas julgadas.** A usabilidade inicial é Aceitável, o armazenamento não atende à meta e o controle de acesso bloqueou as dez condições da bateria. O inventário de três componentes apresentou IRP=3. A melhoria de interface elevou TCH a 100% e reduziu ISVH a zero.

## Quadro de resumo

**Tabela 1 — Quadro de resumo.**

| Métrica | Cálculo / resultado | Meta / nível desejado | Julgamento inicial |
| --- | --- | --- | --- |
| **MET-OP-01 — TCH** | 8/10 = **80%** | ≥ 85% (Excelente) | **Aceitável** |
| **MET-OP-01b — ISVH** | 2 × 2 = **4 pontos** | ≤ 5, sem problemas maiores/catastróficos | **Excelente** |
| **MET-OP-02 — IRP** | 2 × 1 + 1 × 1 = **3 pontos** | ≤ 5, sem vulnerabilidades críticas/altas | **Excelente no inventário** |
| **MET-OP-02b — GED-C** | **3 chaves** na união dos estados | **0 chaves** com dados pessoais legíveis | **Não conforme** |
| **MET-OP-02c — TBR** | 10/10 = **100%** | **100%**, com bateria completa válida | **Conforme no recorte** |

*Fonte: registro da avaliação EC-01, organizado pela equipe.*

## Síntese do julgamento da qualidade

**Tabela 2 — Síntese do julgamento da qualidade.**

| Dimensão | Antes da melhoria | Depois da melhoria | Conclusão |
| --- | --- | --- | --- |
| Usabilidade | TCH=80%, ISVH=4: **Aceitável** | TCH=100%, ISVH=0: **Excelente** | Dois problemas menores resolvidos |
| Segurança — dependências | IRP=3: **Excelente no inventário** | Sem alteração no escopo da intervenção | Dois achados de menor severidade permanecem |
| Segurança — armazenamento | GED-C=3: **Não conforme** | GED-C=3 | Ressalva de armazenamento permanece |
| Segurança — acesso | TBR=100%: **Conforme no recorte** | Sem alteração | Bateria de dez condições atendida |

*Fonte: registro da avaliação EC-01, organizado pela equipe.*

**Julgamento integrado:** a melhoria resolveu os dois problemas do checklist, mas não eliminou a ressalva de armazenamento. Não se declara segurança global conforme enquanto GED-C estiver fora da meta. Os resultados do inventário não representam todas as dependências do produto.

## Documentação da avaliação

**Tabela 3 — Documentação da avaliação.**

| Conteúdo | Página |
| --- | --- |
| Registros de usabilidade, inventário e bateria de dez casos | [Dados e registros](operacionais/dadosBrutos.md) |
| Critérios, respostas GQM e hipóteses | [Análise e julgamento](operacionais/analiseResultados.md) |
| Notas individuais e consenso inicial | [Avaliação de usabilidade](operacionais/avaliacaoUsabilidade.md) |
| Intervenção e comparação antes/depois | [Ação de melhoria](operacionais/acaoMelhoria.md) |
| Encerramento integrado | [Conclusão da avaliação](conclusao.md) |

*Fonte: registro da avaliação EC-01, organizado pela equipe.*

## Referências

Referências usadas nesta página, conforme [Referências — Fase 2](../../referencias/fase2.md).

- NIELSEN, Jakob. **10 Usability Heuristics for User Interface Design**. Nielsen Norman Group, 1994. Disponível em: <https://www.nngroup.com/articles/ten-usability-heuristics/>.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Elaboração da página principal da Fase 4 para métricas operacionais e consolidação dos resultados | 14/11 | [6594e5c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/6594e5c2349ee5fc4dc632f07b97bc8191357819) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Identificação dos resultados anteriores como pendentes de revalidação | 15/11 | [0e38da3](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/0e38da3eac882c62bf7c6f9e1bda97a8b744ef2e) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Coleta assistida com H0, apuração e julgamento com cobertura identificada | 15/11 | [f5e77d5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f5e77d5) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Registro das avaliações da equipe e atualização do julgamento de usabilidade | 15/11 | [f5e77d5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f5e77d5) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Ampliação da análise, respostas GQM e síntese dos julgamentos | 15/11 | [f5e77d5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f5e77d5) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Explicitação das metas nas tabelas de resultados e avaliação | 15/11 | [f5e77d5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f5e77d5) |
| [Yasmim de Souza Santos](https://github.com/eii-yahs) | Inclusão das referências utilizadas na página | 22/11 | Não commitado |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Inclusão de link de retorno para a Matriz Geral de Rastreabilidade | 24/11 | [8f30292](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/8f302921912ed18ed6f6a18507c2bbab654f3366) |
