# Conclusão da avaliação

## 1. Situação da entrega

**EC-01 concluída no escopo documentado:** sete métricas funcionais e cinco operacionais calculadas e julgadas, nove questões GQM respondidas, nove hipóteses julgadas e uma ação de melhoria com comparação antes/depois.

**Tabela 1 — Situação da entrega.**

| Parte | Entrega | Situação |
| --- | --- | --- |
| Fase 1 | Propósito, stakeholders, modelo, características e escopo | **Documentada** |
| Fase 2 | GQM, métricas, metas e critérios | **Documentada** |
| Fase 3 | H0, procedimentos, contratos e rastreabilidade | **Documentada** |
| Fase 4 | Resultados, respostas, hipóteses e conclusão | **Concluída no estudo de caso** |
| Melhoria M-01 | Clareza de termos e tratamento de créditos | **Comparação registrada** |

*Fonte: registro da avaliação EC-01, organizado pela equipe.*

Essa conclusão se refere à avaliação documentada. Artigo, slides, release e submissão são artefatos da entrega acadêmica e devem ser conferidos pela equipe antes do envio.

## 2. Julgamento integrado

O julgamento compara os resultados às metas da Fase 2. **Uma dimensão favorável não compensa outra fora da meta:** a clareza da interface não corrige uma omissão curricular, e o bloqueio de chamadas não elimina dados pessoais legíveis no navegador. A Tabela 2 apresenta a decisão e sua justificativa para cada característica.

**Tabela 2 — Julgamento integrado e justificativas.**

| Característica | Resultado e meta | Decisão | Justificativa |
| --- | --- | --- | --- |
| **Adequação funcional** | CDO=**93,33%** e COO=**71,43%** (metas: **100%**). TVS: oferta=**10%** e calendário=**33,33%** (meta: **0% por tipo**). | **Não atende integralmente às metas** | FGA0206 foi omitida, duas expectativas de preferências não foram atendidas e houve uma divergência de oferta e uma de calendário. A preservação do histórico, as equivalências corretas e o respeito ao máximo de 480h não anulam essas falhas. |
| **Usabilidade** | TCH: **80% → 100%** (meta: **≥85%**). ISVH: **4 → 0** (meta: **≤5**, sem problemas maiores/catastróficos). | **Excelente no checklist após M-01** | A intervenção resolveu os itens 2 e 9, relativos à explicação dos termos e ao ajuste de créditos. Os outros oito itens permaneceram conformes. Pelo pior nível entre TCH e ISVH, o julgamento passou de Aceitável para Excelente nas tarefas avaliadas. |
| **Segurança** | IRP=**3** (meta: **≤5**, sem críticas/altas); TBR=**100%** (meta: **100%** na bateria completa); GED-C=**3 chaves** (meta: **0**). | **Com ressalva por armazenamento** | O inventário atende à faixa Excelente e as dez condições de acesso foram bloqueadas. Entretanto, três chaves continham dados pessoais legíveis. Como GED-C não atende à meta, a regra conjunta impede uma conclusão global favorável de segurança. |

*Fonte: registro da avaliação EC-01, organizado pela equipe, conforme os [critérios funcionais](../fase2/funcionais/GQM.md#31-regras-de-referencia-e-julgamento) e a [regra conjunta operacional](../fase2/operacionais/visaoGeral.md#22-regra-de-julgamento-conjunto).*

### 2.1 Fundamentação da decisão

A decisão funcional considera **completude e correção**, não apenas a aparência do plano. A lista vazia de disciplinas não alocadas não comprova que todas as obrigatórias foram contempladas; o cruzamento com as 15 pendências de H0 identificou a omissão de FGA0206. Da mesma forma, representar uma carga corretamente não garante que as preferências e restrições tenham sido atendidas.

Na usabilidade, a comparação mantém a linha de base: TCH aumentou **20 pontos percentuais** e ISVH diminuiu **quatro pontos**. Esse ganho se refere ao checklist e às tarefas T1–T3. A intervenção não mudou a apuração funcional nem o armazenamento, por isso não altera os respectivos julgamentos.

Na segurança, cada medida responde a um aspecto diferente. TBR examina o acesso à operação, IRP examina o inventário selecionado e GED-C examina a persistência no cliente. **Não calculamos uma média entre as métricas**, pois suas unidades e critérios são diferentes e essa média poderia ocultar uma não conformidade.

### 2.2 Atendimento ao propósito da avaliação

O propósito da Fase 1 foi atendido: identificamos divergências funcionais, classificamos problemas de uso, examinamos a proteção dos dados no recorte e fundamentamos recomendações. A melhoria M-01 também permitiu comparar o julgamento antes e depois da intervenção.

**Conclusão final:** a avaliação está encerrada em EC-01, mas o fluxo não recebeu aprovação integral de qualidade. A usabilidade atingiu Excelente no checklist após M-01; a adequação funcional continua abaixo das metas em parte dos casos e a segurança mantém uma ressalva de armazenamento. A conclusão orienta as prioridades da Tabela 3.

## 3. Recomendações finais

A prioridade considera o efeito do achado sobre a completude do planejamento, a exposição de dados e o atendimento aos contratos do cenário. As recomendações decorrem dos resultados julgados, sem representar novas condições para encerrar EC-01.

**Tabela 3 — Recomendações, justificativas e critérios de verificação.**

| Prioridade | Recomendação | Justificativa | Critério para uma próxima avaliação |
| --- | --- | --- | --- |
| **Alta** | Contemplar FGA0206 ou justificar sua ausência por regra aplicável | A omissão impede o atendimento integral das 15 obrigatórias pendentes de H0. | **CDO=100%**, sem duplicar outras obrigações e com exclusões devidamente fundamentadas. |
| **Alta** | Rever os dados persistidos no navegador | Três chaves com dados pessoais legíveis mantêm o armazenamento fora da meta, mesmo com controle de acesso conforme. | **GED-C=0** nos mecanismos e estados do recorte, preservando a operação do fluxo. |
| **Alta** | Validar período e oferta antes de alocar | Uma alocação fora da oferta de referência e um início divergente do calendário comprometem a consistência temporal do plano. | **TVS=0% por tipo** em oferta e calendário, mantendo o máximo de **480h**. |
| **Média** | Fazer trabalho/objetivo atender aos contratos definidos | Duas das sete expectativas do onboarding não produziram a saída exigida pelo cenário. | **COO=100%**, com cada preferência comparada ao seu contrato. |
| **Média** | Tratar ACH-01 e ACH-02 do inventário | A classificação Excelente de IRP não significa ausência de achados: há um moderado e um baixo. | Resolver os dois achados, reduzir **IRP de 3 para 0** no mesmo inventário e repetir a regressão. |
| **Contínua** | Preservar a clareza alcançada por M-01 | Os dois problemas menores foram resolvidos; alterações futuras podem reintroduzir dificuldades nas mesmas tarefas. | Manter **TCH ≥85%** e **ISVH ≤5**, sem problemas maiores/catastróficos; conferir especialmente os itens 2 e 9. |

*Fonte: registro da avaliação EC-01, organizado pela equipe. As prioridades e os critérios de acompanhamento foram definidos a partir dos achados consolidados.*

A redução de IRP para zero é uma meta de tratamento dos dois achados existentes; **a faixa de excelência da Fase 2 permanece IRP≤5**, sem críticas/altas. As recomendações representam evolução do produto: uma avaliação pode ser concluída com não conformidades, desde que os resultados e suas justificativas estejam explícitos.

## 4. Onde conferir

**Tabela 4 — Onde conferir.**

| Resultado | Referência |
| --- | --- |
| Visão completa das nove questões e do encerramento | [Rastreabilidade da Fase 4](rastreabilidade.md) |
| Sete métricas funcionais e metas | [Consolidado funcional](metricasFuncionais.md#resultados-consolidados) |
| Questões e hipóteses funcionais | [Análise funcional](funcionais/analiseResultados.md) |
| Cinco métricas operacionais e metas | [Consolidado operacional](metricasOperacionais.md#quadro-de-resumo) |
| Questões e hipóteses operacionais | [Análise operacional](operacionais/analiseResultados.md) |
| Antes/depois da intervenção | [M-01](operacionais/acaoMelhoria.md) |
| Ligação com as fases anteriores | [Rastreabilidade](../fase3/operacionais/rastreabilidade.md) |

*Fonte: registro da avaliação EC-01, organizado pela equipe.*

## 5. Referências

Referências usadas nesta página, conforme [Referências — Fase 2](../../referencias/fase2.md) e [Referências — Fase 3](../../referencias/fase3.md).

- BASILI, Victor R.; CALDIERA, Gianluigi; ROMBACH, H. Dieter. **The Goal Question Metric Approach**. *Encyclopedia of Software Engineering*, v. 1, p. 528-532, 1994.
- NIELSEN, Jakob. **10 Usability Heuristics for User Interface Design**. Nielsen Norman Group, 1994. Disponível em: <https://www.nngroup.com/articles/ten-usability-heuristics/>.
- NIELSEN, Jakob. **Severity Ratings for Usability Problems**. Nielsen Norman Group, 1995. Disponível em: <https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/>. Acesso em: 14 nov. 2026.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
|---|---|---|---|
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Consolidação da avaliação, rastreabilidade e encerramento do estudo de caso | 15/11 | [f5e77d5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f5e77d5) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Padronização visual e editorial da documentação | 15/11 | [7a74d9e](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/7a74d9e0809e91d60a36a88559b357bfe171f37e) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Ligação da conclusão à rastreabilidade completa da Fase 4 | 16/11 | [d9d7c15](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/d9d7c1591b6995089cd520a3cca24091f2566c13) |
| [Yasmim de Souza Santos](https://github.com/eii-yahs) | Inclusão das referências utilizadas na página | 22/11 | Não commitado |
