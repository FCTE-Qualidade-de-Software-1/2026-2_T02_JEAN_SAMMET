# Análise dos resultados e julgamento da qualidade — Métricas operacionais

A avaliação compara os dados de H0 com as fichas e a regra conjunta da [Fase 2](../../fase2/operacionais/visaoGeral.md). Os [dados brutos](dadosBrutos.md) identificam a origem e a cobertura de cada medida; a [avaliação de usabilidade](avaliacaoUsabilidade.md) apresenta os dez itens e o consenso de Gustavo e Gabriel.

## 1. Julgamento das métricas de usabilidade

### 1.1 TCH — Taxa de Conformidade Heurística

O consenso registrou **oito itens conformes em dez**: `TCH = (8/10) × 100 = 80%`. Pela ficha, Excelente exige pelo menos 85%; Aceitável corresponde a valores de 70% até menos de 85%. O resultado é **Aceitável**.

Os itens não conformes foram a clareza dos termos “críticas/estratégicas” e a explicação do ajuste de créditos inválidos. As tarefas permaneceram executáveis, mas essas lacunas podem gerar dúvidas durante a interpretação e a configuração do plano.

### 1.2 ISVH — Índice de Severidade de Violações Heurísticas

Foram consolidados **dois problemas menores, ambos de severidade 2**, sem problemas maiores ou catastróficos: `ISVH = (4 × 0) + (3 × 0) + (2 × 2) + (1 × 0) = 4`.

O resultado é **Excelente**, pois não há problema maior/catastrófico e a soma é menor ou igual a 5. Cada problema é contado uma vez no consenso, sem duplicá-lo por ter sido identificado pelos dois avaliadores. O nível de ISVH não elimina as não conformidades do checklist.

## 2. Julgamento das métricas de segurança

### 2.1 IRP — Índice de Risco Ponderado de Dependências

A análise dos **100 scripts do cliente** não reconheceu componentes com suas versões. Sem inventário verificável, não há base para contar vulnerabilidades nem calcular um IRP representativo. O julgamento é **Inconclusivo**.

Um relatório sem componentes reconhecidos não equivale a ausência de vulnerabilidades. É necessário obter componentes/versões verificáveis, dentro do escopo acessível, e reaplicar a análise. Dependências do servidor não foram avaliadas.

### 2.2 GED-C — Grau de Exposição de Dados no Cliente

Foram identificadas **três chaves com dados pessoais legíveis**: `nofluxo_user` no localStorage e dois fragmentos de cookie, `sb-auth-token.0` e `sb-auth-token.1`. A apuração usa a união por origem, mecanismo e chave nos três estados, sem contar novamente uma chave presente em mais de um estado.

Assim, `GED-C = 3`, contra a meta de zero, resultando em **Não conforme**. A presença de Secure/SameSite ou a codificação base64 dos cookies não muda a constatação de legibilidade. O resultado descreve o armazenamento observado; não estabelece, isoladamente, uma conclusão de conformidade legal.

### 2.3 TBR — Taxa de Bloqueio em Rotas Não Autenticadas

O controle positivo alcançou a rota real de geração do plano com **HTTP 200**. Das dez condições negativas previstas, sete foram executadas com a condição de teste validada; todas retornaram **HTTP 401**: `TBR executada = (7/7) × 100 = 100%`.

Esse percentual é favorável **nas sete chamadas executadas**, mas a bateria permanece **Inconclusiva**, pois faltam condições isoladas de token expirado com assinatura válida, papel insuficiente e token revogado. As três condições ausentes não foram contadas como bloqueios nem substituídas por tokens apenas malformados.

## 3. Quadro de resumo

A coluna de meta explicita o nível desejado definido pelas faixas da Fase 2. Em TCH, ISVH e IRP, a referência é **Excelente**; um resultado pode ser classificado como Aceitável sem atingir esse nível.

| Métrica | Cálculo / resultado | Meta / critério da Fase 2 | Julgamento | Cobertura |
|---|---|---|---|---|
| **MET-OP-01 — TCH** | 8/10 = **80%** | ≥ 85% (Excelente); Aceitável: 70% ≤ TCH < 85% | **Aceitável** | Dez itens; avaliações de Gustavo/Gabriel e consenso |
| **MET-OP-01b — ISVH** | 2 × 2 = **4** | ≤ 5 pontos, sem problemas maiores ou catastróficos (Excelente) | **Excelente** | Dois problemas menores consolidados |
| **MET-OP-02 — IRP** | **Sem valor calculável** | ≤ 5 pontos, sem vulnerabilidades críticas ou altas (Excelente); requer inventário verificável | **Inconclusivo** | 100 scripts examinados, sem componente/versão reconhecido |
| **MET-OP-02b — GED-C** | União dos estados = **3 chaves** | 0 chaves com dados pessoais legíveis | **Não conforme** | Três estados; localStorage, sessionStorage e cookies |
| **MET-OP-02c — TBR** | 7/7 = **100% no recorte** | 100% de bloqueio, com toda a bateria prevista válida e concluída | **Inconclusivo para a bateria** | Sete de dez condições executadas; três sem cobertura |

## 4. Respostas formais às questões GQM

### Q-OP-01 — A interface da tela de planejamento atende às heurísticas ergonômicas de usabilidade essenciais para operação e apreensão autônoma?

**Resposta: sim, em nível Aceitável, com ressalvas.** A interface atendeu a oito dos dez itens e apresentou dois problemas menores. Pelo pior nível entre TCH (Aceitável) e ISVH (Excelente), o julgamento conjunto é **Aceitável**.

A equipe conseguiu localizar a previsão e operar os controles avaliados. As melhorias devem explicar a terminologia das matérias críticas/estratégicas e o motivo/faixa do ajuste de créditos. O resultado vale para H0, desktop e tarefas T1–T3; não representa um estudo com todos os perfis de estudantes.

### Q-OP-02 — O sistema protege os dados acadêmicos e os serviços examinados contra exposição no cliente, vulnerabilidades conhecidas e acesso não autorizado?

**Resposta: há uma ressalva comprovada de armazenamento, e a avaliação global permanece parcial.** GED-C=3 não atende à meta. As sete chamadas negativas executadas foram bloqueadas, mas expiração, revogação e papel insuficiente ainda não foram verificados. O risco de dependências permanece inconclusivo pela falta de componentes e versões reconhecidos.

Portanto, os dados não permitem declarar segurança global conforme. Também não demonstram acesso indevido nos sete casos executados. Cada conclusão é limitada ao componente efetivamente medido.

## 5. Julgamento das hipóteses operacionais

| Hipótese | Critério aplicável | Resultado | Julgamento |
|---|---|---|---|
| **H-OP-01 — Violações heurísticas relevantes nas tarefas avaliadas** | TCH < 85% ou presença de problema maior/catastrófico | TCH=80%; dois problemas menores; nenhum maior/catastrófico | **Corroborada no recorte**, pelo limiar de TCH |
| **H-OP-02 — Dependências, armazenamento ou controle de acesso podem comprometer dados/serviços** | Julgar os componentes separadamente; GED-C fora da meta corrobora o componente de armazenamento | GED-C=3; IRP e bateria TBR inconclusivos | **Corroborada no componente de armazenamento; resposta global parcial** |

H-OP-01 pode ser corroborada mesmo com usabilidade Aceitável: a hipótese utiliza o limiar de 85%, enquanto a faixa Aceitável começa em 70%. Não há contradição entre os dois julgamentos.

## 6. Síntese do julgamento da qualidade

| Dimensão | Síntese | Encaminhamento |
|---|---|---|
| **Usabilidade** | **Aceitável**, com dois problemas menores confirmados no consenso | Esclarecer termos e explicar o ajuste de créditos; repetir T2/T3 após alteração |
| **Segurança** | **Com ressalva comprovada e cobertura parcial** | Revisar persistência de dados; obter inventário de dependências e completar as três condições de acesso |
| **Integração com a avaliação funcional** | A operação da interface não garante a completude curricular: FGA0206 foi omitida | Investigar a omissão e repetir o cruzamento de obrigatórias, além de conferir as métricas operacionais |

A qualidade avaliada exige ações tanto sobre **completude do planejamento** quanto sobre **persistência de dados e clareza da interface**. Não se atribuiu uma nota média ao produto: um resultado favorável de usabilidade ou de bloqueio de chamadas não anula a falha funcional nem a exposição encontrada no cliente.

As [ações de melhoria](acaoMelhoria.md) são propostas fundamentadas nos achados. A implementação no produto e a medição posterior ainda precisam ser realizadas para demonstrar ganho de qualidade.

## 7. Reprocessamento e condições restantes

```bash
python3 testes/analisador_sca_irp.py testes/evidencias/seguranca/execucao-h0-2026-11-15/sca.json
python3 testes/teste_controle_acesso_tbr.py testes/evidencias/seguranca/execucao-h0-2026-11-15/tbr.json
```

Os dois comandos retornam Inconclusivo e código 2 nesta coleta, conforme a cobertura disponível. Para avançar, obter inventário verificável de componentes/versões e credenciais que isolem expiração, papel insuficiente e revogação. A documentação mantém essas lacunas explícitas.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Análise detalhada dos resultados, cálculo das 5 métricas operacionais e julgamento das hipóteses H-OP-01 e H-OP-02 | 14/11/2026 | [6594e5c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/6594e5c2349ee5fc4dc632f07b97bc8191357819) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Identificação dos resultados anteriores como pendentes de revalidação | 15/11 | [0e38da3](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/0e38da3eac882c62bf7c6f9e1bda97a8b744ef2e) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Coleta assistida com H0, apuração e julgamento com cobertura identificada | 15/11 | Não commitado |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Registro das avaliações da equipe e atualização do julgamento de usabilidade | 15/11 | Não commitado |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Ampliação da análise, respostas GQM e síntese dos julgamentos | 15/11 | Não commitado |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Explicitação das metas nas tabelas de resultados e avaliação | 15/11 | Não commitado |
