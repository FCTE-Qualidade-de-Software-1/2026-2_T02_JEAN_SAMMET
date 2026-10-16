# Características de Qualidade

<!-- Critério 5. Escolher 3 a 4 características (qualquer uma). Nível máximo: método explícito + trade-offs discutidos. -->

## 1. Método de priorização

Matriz **impacto x risco**: cada característica recebe nota de 1 a 5 em cada eixo; a pontuação é o produto das duas notas.

- **Impacto:** Consequência de uma deficiência ou falha da característica para os principais stakeholders (especialmente os alunos da UnB em seu planejamento acadêmico e os mantenedores da Crianex na evolução do produto). Varia de 1 (impacto irrelevante) a 5 (impacto crítico, gerando atraso na formatura ou inviabilização do uso).
- **Risco:** Probabilidade de a característica apresentar defeitos, deficiências ou limitações na versão avaliada, fundamentada nas limitações conhecidas documentadas do Motor 2, complexidade técnica e histórico de bugs. Varia de 1 (risco desprezível) a 5 (alto risco, problemas conhecidos e não mitigados).
- **Corte:** Seleção das 4 características com maior pontuação (Prioridade = Impacto × Risco), assegurando equilíbrio entre a correção das regras acadêmicas (funcional) e os aspectos operacionais (usabilidade, desempenho e manutenibilidade).

## 2. Avaliação das candidatas

| Característica (ISO/IEC 25010) | Impacto (1-5) | Risco (1-5) | Pontuação | Selecionada |
| :--- | :---: | :---: | :---: | :---: |
| Adequação funcional | 5 | 4 | 20 | Sim |
| Usabilidade | 5 | 3 | 15 | Sim |
| Eficiência de desempenho | 4 | 3 | 12 | Sim |
| Manutenibilidade | 4 | 3 | 12 | Sim |
| Confiabilidade | 4 | 2 | 8 | Não |
| Segurança | 4 | 2 | 8 | Não |
| Compatibilidade | 3 | 2 | 6 | Não |
| Portabilidade | 2 | 2 | 4 | Não |

## 3. Características selecionadas

| Prioridade | Característica | Norma | Justificativa |
| :---: | :--- | :--- | :--- |
| 1 | Adequação funcional | ISO/IEC 25010 | **Crítica para o propósito do software:** Um plano de formatura com pré-requisitos violados, co-requisitos omitidos ou disciplinas obrigatórias esquecidas induz o aluno ao erro e pode atrasar sua graduação. O Motor 2 possui heurísticas e limitações técnicas documentadas que justificam risco elevado. |
| 2 | Usabilidade | ISO/IEC 25010 | **Essencial para a adoção e autonomia do estudante:** A interface da tela `/plano-formatura` apresenta alto volume de informações simultâneas (grafo de matérias, semestres, disciplinas críticas e alertas de optativas). O aluno precisa conseguir identificar sua previsão de formatura e interagir com o plano com clareza e sem ajuda externa. |
| 3 | Eficiência de desempenho | ISO/IEC 25010 | **Impacta diretamente a experiência de uso:** A geração do plano exige processamento combinatório no backend e posterior renderização do grafo interativo no frontend. Tempos elevados de resposta ou lentidão na renderização podem levar o estudante a abandonar o fluxo ou supor falha do sistema. |
| 4 | Manutenibilidade | ISO/IEC 25010 | **Fundamental para os mantenedores e para a sustentabilidade da ferramenta:** O No Fluxo UnB é um projeto de código aberto mantido por estudantes da UnB. Para viabilizar a correção das limitações conhecidas do Motor 2 e suportar futuras contribuições, é imprescindível avaliar a testabilidade e a cobertura de testes automatizados do núcleo do algoritmo. |

## 4. Trade-offs e características não selecionadas

- **Confiabilidade:** Embora a maturidade e tolerância a falhas sejam relevantes, as falhas mais críticas no contexto do No Fluxo manifestam-se primariamente como incorreções de regras acadêmicas (capturadas por Adequação Funcional) ou indisponibilidade temporária coberta por testes de tempo de resposta.
- **Segurança:** A camada de autenticação e persistência é provida pelo Supabase (serviço gerenciado de terceiros) e os termos de serviço impedem testes invasivos de intrusão ou segurança. Priorizou-se a privacidade via premissas de dados sintéticos em vez de métricas de teste de invasão.
- **Compatibilidade e Portabilidade:** O sistema já opera como aplicação web responsiva (PWA). Testes multiplataforma extensivos exigiriam esforço incompatível com o prazo acadêmico da avaliação, sem agregar tanto valor imediato quanto a correção do Motor 2 e a experiência em desktop.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Criação do molde da página | 15/10 | [828688f](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/828688feb645eebfcd428e11b4b9f87585253b9b) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Pontuação impacto × risco, justificativas e seleção das características | 16/10 | [106ddd5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/106ddd54ca773213a62318d809bc06db010d8232) |