# Características de Qualidade

## 1. Método de priorização

Para selecionar as características, será utilizada uma matriz de **impacto × risco**. Cada característica recebe uma nota de 1 a 5 em cada eixo, e a prioridade é calculada pelo produto das notas.

- **Impacto:** consequência para o estudante caso a característica apresente problemas. A nota 1 representa impacto baixo e 5 representa impacto muito alto.
- **Risco:** estimativa inicial da possibilidade de a característica apresentar problemas no fluxo avaliado, considerando a complexidade do sistema e o que pode ser verificado no código e na aplicação. A nota é uma hipótese de planejamento, não uma conclusão de defeito.
- **Prioridade:** impacto × risco. As notas deverão ser revistas se a inspeção inicial ou as medições das próximas fases trouxerem evidências novas.

## 2. Avaliação das candidatas

| Característica (ISO/IEC 25010) | Impacto (1–5) | Risco (1–5) | Pontuação | Selecionada |
| :--- | :---: | :---: | :---: | :---: |
| Adequação funcional | 5 | 4 | 20 | Sim |
| Segurança | 5 | 3 | 15 | Sim |
| Usabilidade | 4 | 3 | 12 | Sim |
| Eficiência de desempenho | 3 | 3 | 9 | Não |
| Confiabilidade | 4 | 2 | 8 | Não |
| Compatibilidade | 2 | 2 | 4 | Não |
| Manutenibilidade | 3 | 1 | 3 | Não |

As pontuações são uma priorização preliminar da equipe e não resultados medidos. A escolha considera o risco de o estudante interpretar incorretamente um plano acadêmico, a presença de dados pessoais no fluxo de uso e a necessidade de compreender e operar a interface sem dificuldade excessiva.

## 3. Características selecionadas

| Prioridade | Característica | Norma de referência | Justificativa |
| :---: | :--- | :--- | :--- |
| 1 | Adequação funcional | ISO/IEC 25010 | O No Fluxo UnB auxilia o estudante a visualizar a estrutura curricular e organizar disciplinas futuras. A avaliação verificará se as informações e funções do fluxo selecionado correspondem aos dados de entrada e às regras curriculares usadas como referência. Um resultado incorreto pode levar a decisões acadêmicas inadequadas. |
| 2 | Segurança | ISO/IEC 25010 | O fluxo pode envolver autenticação e dados acadêmicos pessoais. A avaliação será limitada a verificações não invasivas e à inspeção do comportamento observável e da documentação/código público, sem tentativa de invasão, exploração de vulnerabilidades ou acesso a dados de terceiros. |
| 3 | Usabilidade | ISO/IEC 25010 | O estudante precisa localizar informações, compreender os estados das disciplinas e concluir tarefas do fluxo de planejamento. A avaliação inspecionará se as tarefas predefinidas atendem a critérios ergonômicos e heurísticas de usabilidade, pela equipe avaliadora. |

## 4. Trade-offs e características não selecionadas

- **Eficiência de desempenho:** é relevante, mas será deixada fora do foco principal para manter o trabalho executável no prazo. Não serão realizados testes de carga ou estresse em produção.
- **Confiabilidade:** é importante, porém, nesta avaliação, erros de conteúdo que possam ser confrontados com regras e dados de referência serão tratados principalmente sob adequação funcional. Isso não significa que as duas características sejam equivalentes.
- **Compatibilidade:** testes extensivos em múltiplos navegadores, sistemas operacionais e dispositivos aumentariam o esforço. O estudo ficará restrito ao ambiente de teste declarado no plano de avaliação.
- **Manutenibilidade:** análise aprofundada de arquitetura e cobertura de código não é necessária para responder às perguntas centrais desta avaliação.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Criação do molde da página | 15/10 | [828688f](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/828688feb645eebfcd428e11b4b9f87585253b9b) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Pontuação impacto × risco, justificativas e seleção das características | 16/10 | [106ddd5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/106ddd54ca773213a62318d809bc06db010d8232) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Atualização da pagina | 16/10 | [a6af5fc](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/a6af5fc9dd7113834f334660210ce67b31465d0a) |
