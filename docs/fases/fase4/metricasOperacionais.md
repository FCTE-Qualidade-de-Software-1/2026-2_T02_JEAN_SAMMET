# Avaliação operacional — Fase 4

A coleta encontrou **três chaves com dados pessoais legíveis no cliente**. As sete condições negativas válidas da API foram bloqueadas com 401; três condições permanecem sem cobertura. A usabilidade foi julgada **Aceitável** (TCH=80%; ISVH=4); a SCA continua inconclusiva.

## Quadro de resumo

A coluna de meta explicita o nível desejado definido pelas faixas da Fase 2. Em TCH, ISVH e IRP, a referência é **Excelente**; um resultado pode ser classificado como Aceitável sem atingir esse nível.

| Métrica | Resultado | Meta / nível desejado | Julgamento |
|---|---|---|---|
| TCH | **80%** — oito de dez itens conformes | ≥ 85% (Excelente) | **Aceitável** |
| ISVH | **4** — dois problemas menores | ≤ 5 pontos, sem problemas maiores ou catastróficos (Excelente) | **Excelente** |
| IRP | Sem inventário verificável de componentes/versões | ≤ 5 pontos, sem vulnerabilidades críticas ou altas (Excelente) | **Inconclusivo** |
| GED-C | **3 chaves** com dados pessoais legíveis | 0 chaves com dados pessoais legíveis | **Não conforme** |
| TBR | **100% nas sete chamadas executadas**; sete de dez condições cobertas | 100% de bloqueio, com toda a bateria prevista válida e concluída | **Inconclusivo para a bateria** |

## Síntese do julgamento da qualidade

A **usabilidade é Aceitável**, pelo pior nível entre TCH e ISVH. Gustavo e Gabriel registraram dois problemas menores: clareza dos termos do planejamento e explicação do ajuste de créditos inválidos. H-OP-01 foi corroborada pelo resultado de TCH abaixo de 85%.

A **segurança apresenta ressalva comprovada no armazenamento**, com GED-C=3, enquanto dependências e a bateria completa de controle de acesso permanecem inconclusivas. H-OP-02 foi corroborada nesse componente; os dados não sustentam uma declaração global de conformidade.

As prioridades são revisar a persistência de dados, esclarecer a interface e completar a cobertura de segurança. A [análise detalhada](operacionais/analiseResultados.md) apresenta cálculos, critérios, respostas formais ao GQM e julgamento das hipóteses.

## Documentação da avaliação

| Página | Conteúdo |
|---|---|
| [Dados brutos](operacionais/dadosBrutos.md) | Estados de storage, scanner, chamadas e origem das avaliações |
| [Análise e julgamento](operacionais/analiseResultados.md) | Métricas, cobertura e respostas GQM/hipóteses |
| [Avaliação de usabilidade](operacionais/avaliacaoUsabilidade.md) | Notas de Gustavo/Gabriel, consenso e cálculo |
| [Encaminhamento de melhoria](operacionais/acaoMelhoria.md) | Prioridades propostas a partir dos achados atuais |

Os resultados antigos não substituem esta execução. As notas de usabilidade e o consenso foram transcritos conforme os resultados confirmados por Gustavo. A avaliação operacional permanece parcial; não se declara segurança global com uma única medida favorável.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Elaboração da página principal da Fase 4 para métricas operacionais e consolidação dos resultados | 14/11/2026 | [6594e5c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/6594e5c2349ee5fc4dc632f07b97bc8191357819) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Identificação dos resultados anteriores como pendentes de revalidação | 15/11 | [0e38da3](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/0e38da3eac882c62bf7c6f9e1bda97a8b744ef2e) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Coleta assistida com H0, apuração e julgamento com cobertura identificada | 15/11 | Não commitado |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Registro das avaliações da equipe e atualização do julgamento de usabilidade | 15/11 | Não commitado |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Ampliação da análise, respostas GQM e síntese dos julgamentos | 15/11 | Não commitado |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Explicitação das metas nas tabelas de resultados e avaliação | 15/11 | Não commitado |
