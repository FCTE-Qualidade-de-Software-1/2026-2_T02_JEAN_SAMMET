# Características de Qualidade

<!-- Critério 5. Escolher 3 a 4 características (qualquer uma). Nível máximo: método explícito + trade-offs discutidos. -->

## 1. Método de priorização

Matriz **impacto x risco**: cada característica recebe nota de 1 a 5 em cada eixo; a pontuação é o produto das duas notas.

- **Impacto:** Consequência de uma deficiência ou falha da característica para os principais stakeholders (especialmente os alunos da UnB em seu planejamento acadêmico e os mantenedores da Crianex na evolução do produto). Varia de 1 (impacto irrelevante) a 5 (impacto crítico, gerando atraso na formatura ou inviabilização do uso).
- **Risco:** Probabilidade de a característica apresentar defeitos, deficiências ou limitações na versão avaliada, fundamentada nas limitações conhecidas documentadas do Motor 2, complexidade técnica e histórico de bugs. Varia de 1 (risco desprezível) a 5 (alto risco, problemas conhecidos e não mitigados).
- **Corte:** Seleção das 3 características com maior pontuação (Prioridade = Impacto × Risco), assegurando equilíbrio entre a correção das regras acadêmicas (Adequação Funcional), a experiência do usuário (Usabilidade) e a proteção de dados acadêmicos sensíveis (Segurança).

## 2. Avaliação das candidatas

| Característica (ISO/IEC 25010) | Impacto (1-5) | Risco (1-5) | Pontuação | Selecionada |
| :--- | :---: | :---: | :---: | :---: |
| Adequação funcional | 5 | 4 | 20 | Sim |
| Usabilidade | 5 | 3 | 15 | Sim |
| Segurança | 5 | 3 | 15 | Sim |
| Confiabilidade | 4 | 2 | 8 | Não |
| Eficiência de desempenho | 3 | 2 | 6 | Não |
| Manutenibilidade | 3 | 2 | 6 | Não |
| Compatibilidade | 3 | 2 | 6 | Não |
| Portabilidade | 2 | 2 | 4 | Não |

## 3. Características selecionadas

| Prioridade | Característica | Norma | Justificativa |
| :---: | :--- | :--- | :--- |
| 1 | Adequação funcional | ISO/IEC 25010 | **Crítica para o propósito do software:** Um plano de formatura com pré-requisitos violados, co-requisitos omitidos ou disciplinas obrigatórias esquecidas induz o aluno ao erro e pode atrasar sua graduação. O Motor 2 possui heurísticas e limitações técnicas documentadas que justificam risco elevado. |
| 2 | Usabilidade | ISO/IEC 25010 | **Essencial para a autonomia do estudante:** A interface da tela `/plano-formatura` concentra alta densidade de nós e semestres. O aluno precisa conseguir identificar sua previsão de formatura, interpretar matérias críticas e ajustar créditos sem necessitar de ajuda externa. |
| 3 | Segurança | ISO/IEC 25010 | **Mandatória pela sensibilidade dos dados acadêmicos:** O sistema processa históricos escolares completos (com notas, reprovações, matrícula e dados pessoais), exige autenticação em contas reais para acesso ao plano e persiste informações no Supabase. É indispensável verificar a proteção de dados no cliente (`localStorage`), controle de acesso e vulnerabilidades em dependências. |

## 4. Trade-offs e características não selecionadas

- **Eficiência de desempenho:** Embora a agilidade de resposta seja relevante, o planejamento de formatura é uma tarefa reflexiva e assíncrona, não em tempo real crítico. Tempos de resposta razoáveis são esperados, mas a correção acadêmica e a proteção contra vazamento de dados pessoais foram priorizadas.
- **Manutenibilidade:** A testabilidade do Motor 2 é importante para o ciclo de vida do código aberto, porém a avaliação focou diretamente nos aspectos que geram impacto imediato e risco legal aos estudantes (qualidade funcional, usabilidade e privacidade/segurança de dados).
- **Confiabilidade:** As falhas lógicas mais críticas manifestam-se primariamente como violações de regras acadêmicas, sendo capturadas diretamente pela característica de Adequação Funcional.
- **Compatibilidade e Portabilidade:** O software opera como PWA responsivo para a web. Testes multiplataforma extensivos demandariam esforço excessivo sem agregar valor crítico prioritário.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Criação do molde da página | 15/10 | [828688f](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/828688feb645eebfcd428e11b4b9f87585253b9b) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Pontuação impacto × risco, justificativas e seleção das características | 16/10 | [106ddd5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/106ddd54ca773213a62318d809bc06db010d8232) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Ajuste das características selecionadas para Adequação Funcional, Usabilidade e Segurança | 16/10 | [3584382](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/3584382ccfb17e27db841b011ce415fa1503cbbc) |