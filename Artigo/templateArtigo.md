# Estrutura do Artigo

Estrutura da versão final do artigo (Entregas 1 e 2), um relato de experiência, com o conteúdo de cada seção e a página da GitPage de onde ele vem. O texto completo está em `latex/main.tex`. O artigo tem no máximo 15 páginas, sem contar a tabela de contribuição.

---

## Título

Avaliação da Qualidade do Planejamento de Formatura do No Fluxo UnB: Requisitos, Especificação, Projeto e Execução segundo a ISO/IEC 25040

## Autores, afiliação e contato

- Ana Beatriz Souza Araujo, Giovani De Oliveira Teodoro Coelho, Yasmim de Souza Santos, Gabriel Mota Oliveira, Gustavo Gomes Fornaciari e Vitor Lages Nogueira Araújo
- Faculdade de Ciências e Tecnologias em Engenharia (FCTE), Universidade de Brasília (UnB)
- E-mail institucional de cada autor (matrícula@aluno.unb.br) no `\email{}` do modelo SBC

## Abstract

- Mesmo conteúdo do Resumo, em inglês

## Resumo

- Contexto e objeto: fluxo de planejamento de formatura do No Fluxo UnB
- Método: processo da ISO/IEC 25040 (SQuaRE) e GQM
- O que foi feito nas Fases 1 e 2: requisitos, modelo adaptado da ISO/IEC 25010, pontos do Motor 2 a testar, 2 objetivos, 9 questões e 12 métricas
- O que foi feito nas Fases 3 e 4: execução com um histórico autorizado, principais achados, ação de melhoria e julgamento final

---

## 1. Introdução

- Contexto e problema: planos incorretos podem atrasar a graduação; o histórico pode conter dados pessoais
- Objeto: envio do histórico, fluxograma e tela "Planejar formatura" (objeto central)
- Objetivo geral e objetivos específicos (i) a (iv), cobertos pelas Fases 1 a 4
- Relato de experiência; links do repositório e da GitPage
- Organização do artigo

## 2. Referencial Teórico e Trabalhos Relacionados

Seção sem subseções.

- Um parágrafo sobre a SQuaRE: divisões, normas usadas e as três características da ISO/IEC 25010
- Trabalhos relacionados: Puspaningrum et al. (2017), Calabrese et al. (2018) e Carvalho (2016), e a diferença deste trabalho, incluindo a ação de melhoria com comparação antes e depois

## 3. Metodologia

Seção sem subseções. Origem: [Processo de Avaliação](../docs/metodologia/processoSquare.md)

- Processo da ISO/IEC 25040 em quatro fases e GQM; Fases 1 e 2 na Entrega 1 e Fases 3 e 4 na Entrega 2
- Passo a passo breve de cada uma das quatro fases
- Ferramentas usadas, incluindo o Retire.js e os scripts em Python da coleta
- Detalhamento completo no repositório Git

## 4. Resultados

Uma subseção por fase. A Fase 4 segue a estrutura do GQM: objetivo, questão, métrica, resposta e hipótese.

### 4.1 Fase 1: requisitos da avaliação

- Propósito e as quatro partes interessadas, em poucas linhas
- Descrição do produto, uma figura de tela, diagrama de contexto e uma linha sobre o ODS 4
- Seis pontos do Motor 2 registrados na análise do código, tratados como hipóteses
- Priorização por impacto e risco (só a ordem e a primeira colocada) junto com o modelo adaptado e sua figura
- Escopo, exclusões e limites de validade, condensados
- Origem: páginas da [Fase 1](../docs/fases/fase1/propositoEStakeholders.md)

### 4.2 Fase 2: especificação da avaliação

- Objetivos (tabela), gráfico GQM e o que as questões funcionais e operacionais verificam
- Questões e hipóteses (tabela), com uma hipótese associada a cada questão
- Métricas com a questão de cada uma (tabela)
- Coleta prevista e critérios de julgamento (tabela de níveis)
- Revisões pelas quais a especificação passou
- Origem: [Métricas Funcionais](../docs/fases/fase2/funcionais/visaoGeral.md) e [Métricas Operacionais](../docs/fases/fase2/metricasOperacionais.md)

### 4.3 Fase 3: projeto da avaliação

- Rejeição do PDF sintético e adoção do histórico oficial autorizado (44 registros, 15 obrigatórias pendentes e oito equivalências), com figura
- Cenários de uso sobre o mesmo histórico e regras de referência conferidas no SIGAA, com figura
- Procedimentos por característica: um caso de teste por questão funcional, inspeção de usabilidade por dois avaliadores e verificações de segurança
- Rodada inicial, cronograma e matriz de rastreabilidade, que liga cada questão e sua hipótese à métrica, à meta e ao procedimento
- Origem: [Plano Integrado](../docs/fases/fase3/planoAvaliacao.md), [Piloto e Prontidão](../docs/fases/fase3/piloto.md), [Roteiro funcional](../docs/fases/fase3/funcionais/roteiro.md), [Métodos operacionais](../docs/fases/fase3/operacionais/metodos.md) e [Matriz de Rastreabilidade](../docs/fases/fase3/operacionais/rastreabilidade.md)

### 4.4 Fase 4: execução e conclusão da avaliação

- Tabela com as nove questões: métrica, resultado e meta, resposta e julgamento da hipótese
- 4.4.1 Objetivo funcional: Q-FUN-01 a Q-FUN-07 e H-FUN-01 a H-FUN-07, primeiro as questões com resposta positiva e depois as com resposta negativa, com figuras dos achados
- 4.4.2 Objetivo operacional: Q-OP-01 e H-OP-01 antes e depois da ação de melhoria M-01; Q-OP-02 e H-OP-02
- Origem: [Rastreabilidade Completa](../docs/fases/fase4/rastreabilidade.md), [Análise funcional](../docs/fases/fase4/funcionais/analiseResultados.md), [Análise operacional](../docs/fases/fase4/operacionais/analiseResultados.md) e [Ação de Melhoria](../docs/fases/fase4/operacionais/acaoMelhoria.md)

## 5. Conclusão

- Síntese das quatro fases, com as respostas às questões e o julgamento das hipóteses
- Julgamento separado por característica, sem média entre as métricas
- Limites de validade dos resultados
- Recomendações por prioridade e próximo passo, ligados às questões que devem passar a ter resposta positiva
- Origem: [Conclusão da Avaliação](../docs/fases/fase4/conclusao.md)

---

## Declaração de Uso de Inteligência Artificial

- Uma frase por integrante: ferramenta, tarefa e como conferiu, com base em [Uso de IA](../docs/usoDeIA/IA.md)

## Disponibilidade dos Dados

- Link do repositório; registros da avaliação sem dados pessoais e histórico usado não publicado

## Referências

- Arquivo `latex/referencias.bib`

## Apêndice A - Tabela de Contribuição

- Integrante, matrícula, atividades nas Entregas 1 e 2 e percentual de esforço, com base em [Equipe](../docs/equipe/equipe.md)
