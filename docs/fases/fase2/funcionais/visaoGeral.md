# Especificação da Avaliação — Métricas Funcionais

Este documento especifica as perguntas e métricas de **adequação funcional** para avaliar a funcionalidade _Planejar formatura_ do No Fluxo UnB, com foco no Motor 2. A avaliação procura verificar se os planos gerados são coerentes com o histórico do aluno e com as regras acadêmicas aplicáveis, sem tratar limitações documentadas como defeitos antes da execução dos testes.

A estrutura segue o método **Goal-Question-Metric (GQM)** e complementa as métricas operacionais descritas em [`Metricas Operacionais`](../metricasOperacionais.md).

## 1. Contexto da avaliação

### 1.1 Propósito e decisões apoiadas

O No Fluxo UnB auxilia o estudante a decidir quais disciplinas cursar nos próximos semestres e quando poderá concluir o curso. Na tela _Planejar formatura_, o Motor 2 organiza disciplinas por semestre e apresenta uma previsão de formatura. Um plano com pré-requisitos ignorados, co-requisitos omitidos, disciplinas obrigatórias ausentes ou histórico interpretado incorretamente pode levar a decisões acadêmicas inadequadas e até atrasar a graduação.

A avaliação funcional deve produzir evidências para:

- **Alunos da UnB:** entender em que medida o plano corresponde ao histórico e à matriz curricular e quando precisa ser conferido com a coordenação do curso.
- **Crianex e mantenedores:** localizar comportamentos que merecem correção e priorizar melhorias com base em evidências reproduzíveis.
- **Coordenação e orientação acadêmica:** apoiar a identificação de planos incompatíveis com as regras do curso.
- **Equipe avaliadora e requisitante acadêmica:** fundamentar a avaliação de qualidade do produto e a proposta de melhoria da etapa seguinte.

O plano é uma estimativa produzida por uma heurística e o No Fluxo UnB não é uma ferramenta oficial da UnB. A avaliação não deve apresentar os resultados como garantia institucional de formatura.

### 1.2 Escopo e referência de execução

O objeto funcional principal é o Motor 2, localizado no código de referência como `backend/src/services/plano_formatura.service.ts`, acionado pela rota `POST /planejamento/gerar-plano`.

| Item                      | Referência para a avaliação                                                                                                                                     |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Software                  | No Fluxo UnB, funcionalidade _Planejar formatura_.                                                                                                              |
| Versão do código          | Commit de referência `87b5475`, identificado na documentação da Fase 1.                                                                                         |
| Curso/matriz prioritários | Engenharia de Software da FGA/UnB, matriz identificada na documentação como **6360/1 ou 2017.1**, descrita como inativa no sistema observado.                   |
| Dados de teste            | Históricos sintéticos ou dos membros da equipe e entrevistados que permitirem o uso                                                                             |
| Entradas relevantes       | Histórico e status das disciplinas, matriz curricular, pré-requisitos, co-requisitos, equivalências, oferta de turmas e opções do onboarding.                   |
| Saídas relevantes         | Disciplinas e semestres planejados, matérias pendentes/críticas, semestre previsto de formatura e informações de integralização disponíveis na interface.       |
| Limite de validade        | Os resultados valem para os cenários, a matriz, os dados, a versão e o ambiente registrados. Não provam que a versão em produção é idêntica ao código avaliado. |

### 1.3 Hipóteses funcionais documentadas

Os itens abaixo foram registrados na Fase 1 como **hipóteses que precisam ser testadas**, não como defeitos confirmados.

| Hipótese documentada                                                                                                                                                                        | Risco para a adequação funcional                                                                                                                            | Métrica/cenário relacionado    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| As respostas do onboarding sobre trabalho/estágio e objetivo aparecem no fluxo, mas, no serviço analisado, são descritas como valores padrão que não participam da seleção das disciplinas. | A opção apresentada ao aluno pode não produzir o comportamento esperado. É necessário confirmar o comportamento prometido antes de classificá-lo como erro. | `MET-FUN-06`; cenário `CT-06`. |
| Disciplinas com matrícula em andamento são tratadas como aprovadas para planejar semestres futuros.                                                                                         | O plano pode diferir do resultado real caso o aluno seja reprovado; a avaliação deve verificar a regra documentada e a clareza do comportamento.            | `MET-FUN-04`; cenário `CT-04`. |
| Uma lista vazia de disciplinas não alocadas não garante, por si só, que todas as obrigatórias entraram no plano.                                                                            | O plano pode omitir disciplinas pendentes sem que a ausência seja evidente.                                                                                 | `MET-FUN-03`; cenário `CT-03`. |
| Há casos em que uma disciplina pode ser alocada sem sua co-requisitada.                                                                                                                     | O plano pode violar uma relação curricular de co-requisito.                                                                                                 | `MET-FUN-02`; cenário `CT-02`. |
| A expansão de equivalências é descrita como uma única passagem, filtrada por curso e sem considerar a vigência.                                                                             | Equivalências encadeadas ou relacionadas a matrizes antigas podem ser aplicadas incorretamente.                                                             | `MET-FUN-05`; cenário `CT-05`. |
| Se a consulta ao período letivo falhar, o período atual pode ser estimado pela data do sistema.                                                                                             | O plano pode começar em semestre diferente do calendário acadêmico aplicável.                                                                               | `MET-FUN-07`; cenário `CT-07`. |

| Nome do Membro                                                    | Contribuição                                                                                          | Data       | Commit                                                                                                                            |
| :---------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------- | :--------- | :-------------------------------------------------------------------------------------------------------------------------------- |
| [Gabriel Mota](https://github.com/Gabro-MO)                       | Elaboração inicial das perguntas GQM, fichas de métricas funcionais e protocolo de cenários de teste. | 16/10/2026 | [9306147](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/9306147e05a3017e02f9bedaf2c75a8287ef1c8b) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Ajuste de consistência do foco GQM e remoção de referências a divisões internas de pessoas            | 16/10/2026 | [81912ba](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/81912bac5e02d7429e2d05446544ec9636891f5e) |
| [Gabriel Mota](https://github.com/Gabro-MO)                       | Divisão do arquivo principal em varias paginas e ajustes a estrutura                                  | 16/10/2026 | [e60f42c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/e60f42cea76bd6f39f2c6069ecdbce438b4e941a)                                                                                                                              |