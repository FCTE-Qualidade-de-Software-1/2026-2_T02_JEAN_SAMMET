# Análise dos resultados e julgamento da qualidade — Métricas operacionais

A execução **EC-01** aplica as fichas e a regra conjunta da [Fase 2](../../fase2/operacionais/visaoGeral.md). Os [registros](dadosBrutos.md) identificam universos, contratos e resultados. A avaliação inicial e a reavaliação de interface são julgadas separadamente.

## 1. Julgamento das métricas de usabilidade

### 1.1 TCH — Taxa de Conformidade Heurística

**Antes: TCH=8/10×100=80%, Aceitável.** A meta de excelência é pelo menos 85%; a faixa Aceitável vai de 70% a menos de 85%. Os itens 2 e 9 apresentaram problemas na explicação de termos e no ajuste de créditos inválidos. As tarefas T1–T3 permaneceram executáveis.

### 1.2 ISVH — Índice de Severidade de Violações Heurísticas

**Antes: ISVH=4×0+3×0+2×2+1×0=4, Excelente.** Foram dois problemas menores, sem problemas maiores ou catastróficos. Cada problema é contado uma vez no consenso, não uma vez por avaliador.

O julgamento conjunto inicial é **Aceitável**, pelo pior nível entre TCH e ISVH. Após a [melhoria](acaoMelhoria.md), os valores foram TCH=100% e ISVH=0, ambos Excelentes.

## 2. Julgamento das métricas de segurança

### 2.1 IRP — Índice de Risco Ponderado de Dependências

INV-01 contém três componentes de referência e dois achados únicos: um moderado e um baixo. **IRP=10×0+5×0+2×1+1×1=3 pontos, Excelente**, pois não há crítica/alta e o valor é menor ou igual a 5. A classificação se restringe ao inventário; não equivale a aprovação de todos os componentes ou do backend.

### 2.2 GED-C — Grau de Exposição de Dados no Cliente

A união dos estados E0–E2 contém **três chaves com dados pessoais legíveis**. Como a meta é zero, **GED-C=3, Não conforme**. Codificação base64 e flags de cookie não foram tratadas como cifragem. O achado não estabelece, isoladamente, conclusão de conformidade legal.

### 2.3 TBR — Taxa de Bloqueio de Requisições Não Autorizadas

O controle positivo retornou 200; as dez condições negativas foram bloqueadas com 401/403. **TBR=10/10×100=100%, Conforme no recorte.** O contrato distingue token inválido, expirado, revogado e credencial válida sem o papel necessário. Um erro 404/405 não seria contado como bloqueio válido.

## 3. Quadro de resumo

**Tabela 1 — Quadro de resumo.**

| Métrica | Cálculo / resultado | Meta / nível desejado | Julgamento inicial |
| --- | --- | --- | --- |
| **MET-OP-01 — TCH** | 8/10 = **80%** | ≥ 85% (Excelente) | **Aceitável** |
| **MET-OP-01b — ISVH** | 2 × 2 = **4 pontos** | ≤ 5, sem problemas maiores/catastróficos | **Excelente** |
| **MET-OP-02 — IRP** | 2 × 1 + 1 × 1 = **3 pontos** | ≤ 5, sem vulnerabilidades críticas/altas | **Excelente no inventário** |
| **MET-OP-02b — GED-C** | **3 chaves** na união dos estados | **0 chaves** com dados pessoais legíveis | **Não conforme** |
| **MET-OP-02c — TBR** | 10/10 = **100%** | **100%**, com bateria completa válida | **Conforme no recorte** |

*Fonte: registro da avaliação EC-01, organizado pela equipe.*

As metas de TCH, ISVH e IRP correspondem à faixa Excelente da Fase 2. Aceitável permanece um nível válido para usabilidade, ainda que abaixo da meta de excelência. A intervenção não altera os resultados de segurança.

## 4. Respostas formais às questões GQM

### Q-OP-01 — A interface da tela de planejamento atende às heurísticas ergonômicas de usabilidade essenciais para operação e apreensão autônoma?

**Resposta inicial: sim, em nível Aceitável, com duas ressalvas menores.** O consenso registrou oito itens conformes e severidade total 4. A interpretação dos termos críticas/estratégicas e a explicação do ajuste de créditos exigiram melhoria.

**Após a intervenção: Excelente no checklist.** Os itens 2 e 9 passaram a conformes, sem regressão nos outros oito: TCH=100%, ISVH=0. A melhoria foi julgada no mesmo H0 e nas mesmas tarefas; não se extrapola o resultado para outros perfis ou dispositivos.

### Q-OP-02 — O sistema protege os dados acadêmicos e os serviços examinados contra exposição no cliente, vulnerabilidades conhecidas e acesso não autorizado?

**Resposta: há uma ressalva de segurança por armazenamento.** TBR atende à meta nas dez condições; INV-01 obtém IRP=3, nível Excelente no inventário. Entretanto, GED-C=3 não atende à meta de zero. Pela regra conjunta, o resultado favorável de acesso e dependências não compensa a exposição observada.

A conclusão é **segurança com ressalva no componente de armazenamento**, e não aprovação global. Os achados moderado/baixo também devem receber tratamento, embora o índice esteja na faixa Excelente.

## 5. Julgamento das hipóteses operacionais

**Tabela 2 — Julgamento das hipóteses operacionais.**

| Hipótese | Critério | Resultado inicial | Julgamento | Situação após a melhoria |
| --- | --- | --- | --- | --- |
| **H-OP-01 — Violações heurísticas relevantes** | TCH < 85% ou problema maior/catastrófico | TCH=80%, ISVH=4 | **Corroborada no recorte**, por TCH | **Não corroborada no checklist reavaliado:** TCH=100%, ISVH=0 |
| **H-OP-02 — Riscos em dependências, armazenamento ou acesso** | Julgar cada componente; GED-C fora da meta corrobora armazenamento | IRP=3; GED-C=3; TBR=100% | **Corroborada no armazenamento** | **Mantida:** intervenção não alterou persistência |

*Fonte: registro da avaliação EC-01, organizado pela equipe.*

A hipótese de usabilidade pode ser corroborada com nível Aceitável: seu limiar de 85% é superior ao início dessa faixa, em 70%. O resultado após a melhoria não apaga o diagnóstico inicial.

## 6. Síntese do julgamento da qualidade

**Tabela 3 — Síntese do julgamento da qualidade.**

| Dimensão | Resultado | Meta | Julgamento final |
| --- | --- | --- | --- |
| Usabilidade após intervenção | TCH=100%; ISVH=0 | TCH ≥ 85%; ISVH ≤ 5 e sem maior/catastrófico | **Excelente no recorte** |
| Dependências INV-01 | IRP=3 | ≤ 5 e sem críticas/altas | **Excelente no inventário** |
| Armazenamento | GED-C=3 | 0 | **Não conforme** |
| Acesso | TBR=100%, dez condições | 100% na bateria completa | **Conforme no recorte** |

*Fonte: registro da avaliação EC-01, organizado pela equipe.*

A melhoria tornou a interface mais clara nas tarefas avaliadas. **A qualidade operacional ainda exige tratamento da persistência de dados.** A [avaliação funcional](../funcionais/analiseResultados.md) acrescenta falhas de completude, preferências, oferta e calendário. Não se calcula uma nota média que esconda essas ressalvas.

## 7. Encerramento

As cinco métricas operacionais têm cálculo e julgamento, as duas questões GQM estão respondidas e as duas hipóteses foram julgadas. As ações restantes são recomendações de evolução do produto, não tarefas de coleta prometidas para concluir EC-01. O [encerramento integrado](../conclusao.md) reúne decisões, recomendações e limites.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Análise detalhada dos resultados, cálculo das 5 métricas operacionais e julgamento das hipóteses H-OP-01 e H-OP-02 | 14/11 | [6594e5c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/6594e5c2349ee5fc4dc632f07b97bc8191357819) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Identificação dos resultados anteriores como pendentes de revalidação | 15/11 | [0e38da3](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/0e38da3eac882c62bf7c6f9e1bda97a8b744ef2e) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Coleta assistida com H0, apuração e julgamento com cobertura identificada | 15/11 | [f5e77d5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f5e77d5) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Registro das avaliações da equipe e atualização do julgamento de usabilidade | 15/11 | [f5e77d5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f5e77d5) |