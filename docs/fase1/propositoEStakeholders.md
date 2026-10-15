# Propósito da Avaliação e Partes Interessadas

## 1. Propósito da avaliação

### 1.1 Por que avaliar

O No Fluxo UnB é usado por alunos para decidir o que cursar nos próximos semestres e quando se formar. Na tela "Planejar formatura" (ver [Software Escolhido](softwareEscolhido.md)), o aluno vê o semestre previsto de formatura, as matérias críticas e a sequência de disciplinas. Se essas informações estiverem erradas (pré-requisito ignorado, horas de optativa mal contadas, previsão incorreta), o aluno pode se matricular de forma inadequada e atrasar a formatura.

O próprio projeto reconhece que o plano é uma estimativa: o algoritmo (Motor 2) é uma heurística e a documentação dos mantenedores lista limitações conhecidas (ver [Software Escolhido, seção 3.8](softwareEscolhido.md#38-limitacoes-conhecidas)). Avaliar a qualidade dessa tela gera evidências sobre o quanto o aluno pode confiar no plano, e onde ele precisa ser conferido com a coordenação do curso.

### 1.2 Para quem

- Para a **Crianex e os mantenedores** do No Fluxo UnB, como subsídio para priorizar correções. O software é código aberto (GPL-3.0) e aceita contribuições.
- Para os **alunos da UnB**, como referência sobre o que a ferramenta entrega bem e o que deve ser conferido em outras fontes.
- Para a **Profa. Cristiane Ramos**, como avaliação acadêmica do processo de avaliação de produto (ISO/IEC 25040) aplicado pela equipe.

### 1.3 Como os resultados serão usados

| Decisão a apoiar | Quem decide | Resultado da avaliação que a sustenta |
| :--- | :--- | :--- |
| Priorizar quais limitações do Motor 2 corrigir primeiro | Mantenedores | Métricas e julgamentos por característica de qualidade (Fases 2 e 4) |
| Decidir se o plano gerado pode ser usado sem conferência adicional ou se deve ser validado com a coordenação do curso | Alunos | Resultado da avaliação de adequação do plano às regras da matriz |
| Escolher a ação de melhoria que a equipe entrega na Entrega 2 (por exemplo, correção parcial no código ou protótipo) | Equipe avaliadora, com a Profa. Cristiane Ramos | Oportunidades de melhoria identificadas na Fase 4 |

*Proposta inicial: ajustar com a equipe.*

## 2. Requisitante e partes interessadas

**Requisitante:** a avaliação é demandada pela disciplina FGA0315, na figura da Profa. Cristiane Ramos. A Crianex e os mantenedores são os beneficiários técnicos das recomendações. [Definir se a equipe vai contatá-los, por exemplo, por issue ou pull request no repositório do software.]

**Compradores:** não há. O software é gratuito para o estudante, conforme o README do projeto.

### 2.1 Perfis de usuários

| Perfil | Situação | Uso típico da tela "Planejar formatura" |
| :--- | :--- | :--- |
| Aluno concluinte | Poucas disciplinas restantes | Conferir a data de formatura e o que falta, inclusive optativas |
| Aluno de meio de curso | Cursando semestres intermediários | Decidir a carga de créditos por semestre e antecipar disciplinas críticas |
| Aluno com atraso ou reprovações | Disciplinas bloqueadas por pré-requisito | Descobrir a sequência mínima de matérias para se formar |
| Aluno em matriz antiga (inativa) | Ainda cursa pela matriz anterior | Planejar conforme a matriz em que está vinculado |
| Aluno com equivalências e módulo livre | Aproveitamentos de outros cursos ou disciplinas | Entender como disciplinas equivalentes entram no plano |
| Aluno que trabalha ou estagia | Disponibilidade reduzida | Ajustar a carga por semestre à rotina |
| Aluno que usa recursos de acessibilidade | Alto contraste, texto ampliado, menos movimento | Usar o plano sem barreiras (o software oferece esses recursos) |

Os perfis valem para quem tem conta: o modo anônimo não acessa o plano de formatura.

### 2.2 Partes interessadas

| Stakeholder | Papel | Necessidades | Critério de sucesso | Influência na avaliação (hipótese) |
| :--- | :--- | :--- | :--- | :--- |
| Alunos de graduação da UnB | Usuários finais | Plano correto, fácil de entender e rápido de obter | O plano reflete a matriz e o histórico, e o aluno o usa sem ajuda | Orientam o foco no fluxo do aluno e a priorização de adequação funcional e usabilidade |
| Crianex e mantenedores | Desenvolvedor, operador e dona do produto | Saber onde o plano falha e o que corrigir primeiro, mantendo o produto gratuito e o custo de IA sob controle | Relatório com evidências reproduzíveis e sugestões acionáveis | Definem o que dá para medir (código público, produção sem acesso) e orientam eficiência e manutenibilidade |
| Coordenação do curso e orientação acadêmica | Usuários indiretos | Planos coerentes com a matriz e com as regras do curso | Alunos orientados com menos erros de planejamento | Reforçam a importância da adequação funcional |
| UnB e SIGAA | Fonte dos dados (histórico oficial em PDF e páginas públicas coletadas por scraping) | Uso adequado dos dados institucionais; o software não é ferramenta oficial | Dados tratados com cuidado e sem alegar caráter oficial | Motivam a atenção à proteção de dados pessoais |
| Supabase | Fornecedor da plataforma (login e banco de dados) | Uso dentro dos termos do serviço | Sem testes intrusivos ou de carga | Limita testes de segurança e de capacidade |
| Maritaca e Google | Fornecedores de IA (modelos Sabiá e embeddings Gemini) | Uso dentro de cota e custo | Sem consumo excessivo de cota | Limitam a avaliação do assistente Darcy |
| Equipe avaliadora | Executa a avaliação | Concluir o processo com rastreabilidade | Entregas completas e coerentes entre as fases | Conduz a seleção e o escopo conforme o prazo e o conhecimento da equipe |
| Profa. Cristiane Ramos | Requisitante acadêmica e avaliadora | Aplicação correta do processo SQuaRE | Atendimento aos critérios de cada fase | Define premissas e limites do trabalho |

A ligação entre os stakeholders e as características escolhidas será explicitada em [Características de Qualidade](caracteristicasDeQualidade.md), e as limitações de acesso em [Escopo](escopo.md).

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Criação do molde da página | 15/10 | [828688f](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/828688feb645eebfcd428e11b4b9f87585253b9b) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Preenchimento com os dados do No Fluxo UnB | 15/10 | [559e7a9](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/559e7a94f159c2caeb4dc9d5996ba9392d0862ac) |