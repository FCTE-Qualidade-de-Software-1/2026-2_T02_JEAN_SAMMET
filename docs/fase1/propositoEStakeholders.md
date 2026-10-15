# Propósito da Avaliação e Partes Interessadas

## 1. Propósito da avaliação

### 1.1 Por que avaliar

O No Fluxo UnB é usado por alunos para decidir o que cursar nos próximos semestres e quando se formar. Na tela "Planejar formatura" (ver [Software Escolhido](softwareEscolhido.md)), o aluno vê o semestre previsto de formatura, as matérias críticas e a sequência de disciplinas. Se essas informações estiverem erradas (pré-requisito ignorado, horas de optativa mal contadas, previsão incorreta), o aluno pode se matricular de forma inadequada e atrasar a formatura. Avaliar a qualidade dessa tela gera evidências sobre o quanto o aluno pode confiar nela e onde ela precisa melhorar.

### 1.2 Para quem

- Para os **desenvolvedores e mantenedores** do No Fluxo UnB, como subsídio para priorizar melhorias.
- Para os **alunos da UnB**, como referência sobre o que a ferramenta entrega bem e o que deve ser conferido em outras fontes.
- Para a **Profa. Cristiane Ramos**, como avaliação acadêmica do processo de avaliação de produto (ISO/IEC 25040) aplicado pela equipe.

### 1.3 Como os resultados serão usados

| Decisão a apoiar | Quem decide | Resultado da avaliação que a sustenta |
| :--- | :--- | :--- |
| Priorizar correções e melhorias na tela "Planejar formatura" | Desenvolvedores / mantenedores | Métricas e julgamentos por característica de qualidade (Fases 2 e 4) |
| Decidir se o plano gerado pode ser usado sem conferência adicional ou se deve ser validado com a coordenação do curso | Alunos | Resultado da avaliação de adequação do plano às regras da matriz |
| Escolher a ação de melhoria que a equipe entrega na Entrega 2 | Equipe avaliadora, com a Profa. Cristiane Ramos | Oportunidades de melhoria identificadas na Fase 4 |

*Proposta inicial: ajustar com a equipe e, se houver contato, com os mantenedores.*

## 2. Requisitante e partes interessadas

**Requisitante:** a avaliação é demandada pela disciplina FGA0315, na figura da Profa. Cristiane Ramos. Os mantenedores do No Fluxo UnB são os beneficiários técnicos das recomendações. [Confirmar se haverá contato com eles.]

**Compradores:** não identificados; o uso parece gratuito para o aluno. [Confirmar.]

### 2.1 Perfis de usuários

| Perfil | Situação | Uso típico da tela "Planejar formatura" |
| :--- | :--- | :--- |
| Aluno concluinte | Poucas disciplinas restantes | Conferir a data de formatura e o que falta, inclusive optativas |
| Aluno de meio de curso | Cursando semestres intermediários | Decidir a carga de créditos por semestre e antecipar disciplinas críticas |
| Aluno com atraso ou reprovações | Disciplinas bloqueadas por pré-requisito | Descobrir a sequência mínima de matérias para se formar |
| Aluno em matriz antiga (inativa) | Ainda cursa pela matriz anterior | Planejar conforme a matriz em que está vinculado |
| Aluno em transição de curso ou com aproveitamentos | Equivalências e módulo livre | Entender como disciplinas equivalentes entram no plano |

### 2.2 Partes interessadas

| Stakeholder | Papel | Necessidades | Critério de sucesso | Influência na avaliação (hipótese) |
| :--- | :--- | :--- | :--- | :--- |
| Alunos de graduação da UnB | Usuários finais | Plano correto, fácil de entender e rápido de obter | O plano reflete a matriz e o histórico, e o aluno consegue usá-lo sem ajuda | Definem o foco no fluxo do aluno e orientam a priorização das características |
| Desenvolvedores / mantenedores | Desenvolvedor e operador | Saber onde a ferramenta falha e o que corrigir primeiro | Relatório objetivo, com evidências reproduzíveis | Definem o que é possível medir (acesso a código e ambiente) e o escopo |
| Coordenação do curso e orientação acadêmica | Usuários indiretos | Planos coerentes com a matriz e as regras do curso | Alunos orientados com menos erros de planejamento | Reforçam a importância da adequação funcional |
| UnB / SIGAA | Fornecedor do dado de origem (histórico oficial em PDF) | Uso adequado do documento oficial | Dados do aluno tratados com cuidado | Motivam a atenção à proteção de dados pessoais |
| Provedor do assistente de IA (Darcy AI) | Fornecedor de serviço [confirmar] | Uso correto do recurso | [confirmar] | Limitam o que pode ser avaliado no recurso de IA |
| Equipe avaliadora | Executa a avaliação | Concluir o processo com rastreabilidade | Entregas completas e coerentes entre as fases | Conduz seleção e escopo conforme o prazo e o conhecimento da equipe |
| Profa. Cristiane Ramos | Requisitante acadêmica e avaliadora | Aplicação correta do processo SQuaRE | Atendimento aos critérios de cada fase | Define premissas e limites do trabalho |

A ligação entre os stakeholders e as características escolhidas será explicitada em [Características de Qualidade](caracteristicasDeQualidade.md), e as limitações de acesso em [Escopo](escopo.md).

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Criação do molde da página | 15/10 | [828688f](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/tree/828688feb645eebfcd428e11b4b9f87585253b9b) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Preenchimento com os dados do No Fluxo UnB | 15/10 | [hash](URL-do-commit) |

