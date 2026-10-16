# Métricas de Manutenibilidade

Este documento detalha a especificação das perguntas, hipóteses e métricas de **Manutenibilidade** para o componente de planejamento de formatura (Motor 2) do No Fluxo UnB, focando na testabilidade e segurança técnica para evolução do código pelos desenvolvedores e mantenedores.

---

## 1. Característica e Subcaracterísticas Avaliadas

De acordo com o [Modelo de Qualidade](../../fase1/modeloDeQualidade.md) baseado na norma **ISO/IEC 25010:2011**, a Manutenibilidade é avaliada a partir das seguintes subcaracterísticas:

1. **Testabilidade (_Testability_):** grau de facilidade com que critérios de teste podem ser estabelecidos e testes automatizados podem ser executados para determinar se o Motor 2 satisfaz os requisitos funcionais.
2. **Modularidade e Analisabilidade (_Modularity and Analysability_):** grau em que o algoritmo do Motor 2 é estruturado de forma desacoplada, permitindo diagnosticar defeitos, avaliar o impacto de alterações e modificar regras acadêmicas com baixo risco de regressão.

---

## 2. Questão GQM e Hipótese Associada

### Questão GQM: `Q-OP-03`
> **"Em que nível o componente central do Motor 2 está coberto por testes automatizados para suportar refatorações e correções de defeitos com segurança?"**

### Hipótese Operacional: `H-OP-03`
> **Hipótese:** O serviço `backend/src/services/plano_formatura.service.ts` concentra toda a lógica de negócio da heurística de planejamento com regras intrincadas de desempate, pré-requisitos e ordenação, porém a suíte de testes automatizados existente no repositório deixa ramificações condicionais críticas sem cobertura, elevando o risco de efeitos colaterais indesejados durante manutenções corretivas.

---

## 3. O Componente Avaliado: O Motor 2

No repositório público do software ([Software Escolhido](../../fase1/softwareEscolhido.md#32-modulos)), o Motor 2 é implementado no arquivo:
* **Caminho:** `backend/src/services/plano_formatura.service.ts`
* **Linguagem e Ambiente:** TypeScript, executado sobre Node.js 20 e Express 4.
* **Complexidade do Algoritmo:** o serviço recebe o histórico escolar e a estrutura curricular do curso, calcula pesos de criticidade (dependentes diretos e indiretos), ordena as disciplinas e as aloca semestre a semestre respeitando um teto máximo de carga horária.

A avaliação da cobertura de testes deste componente é um pré-requisito mandatório para a **Fase 4**: qualquer intervenção da equipe para corrigir as limitações de co-requisitos ou de opções do onboarding só poderá ser considerada segura se os testes automatizados garantirem a não regressão do sistema.

---

## 4. Fichas Completas das Métricas de Manutenibilidade

### Ficha da Métrica Principal: `MET-OP-03` — Cobertura de Ramificações do Motor 2 (CR-M2)

| Campo | Especificação Metodológica |
| :--- | :--- |
| **Identificador** | `MET-OP-03` |
| **Nome da Métrica** | Cobertura de Ramificações do Motor 2 (CR-M2) |
| **Característica / Subcaracterística** | Manutenibilidade — Testabilidade (*Testability*) |
| **Pergunta GQM Relacionada** | `Q-OP-03`: Em que nível o componente central do Motor 2 está coberto por testes automatizados para suportar refatorações e correções de defeitos com segurança? |
| **1. Definição** | Percentual de ramificações condicionais de decisão (*branches* — estruturas `if/else`, operadores ternários, desvios lógicos) exercitadas pela suíte de testes automatizados existente especificamente no arquivo `backend/src/services/plano_formatura.service.ts`. Unidade: percentual (%). |
| **2. Procedimento de Cálculo** | O cálculo é processado pela ferramenta de instrumentação e relatório de testes (Jest / Vitest / Istanbul):<br><br>$$CR\text{-}M2 = \left( \frac{B_{\text{exercitadas}}}{B_{\text{totais}}} \right) \times 100$$<br>Onde:<br>- $B_{\text{exercitadas}}$: quantidade de ramos condicionais percorridos por ao menos um caso de teste automatizado.<br>- $B_{\text{totais}}$: total de ramos condicionais instrumentados no arquivo alvo. |
| **3. Fonte dos Dados** | Relatório de cobertura (*Coverage Report*) gerado localmente pelo test runner do backend no commit de referência `87b5475` do repositório oficial. |
| **4. Procedimento de Coleta** | 1. Clonar o repositório oficial no commit `87b5475`.<br>2. Navegar até o subdiretório `backend/` e instalar as dependências com `npm install`.<br>3. Executar o comando de testes automatizados com instrumentação de cobertura isolada para o serviço de planejamento:<br>&nbsp;&nbsp;&nbsp;&nbsp;`npm run test -- --coverage --collectCoverageFrom="src/services/plano_formatura.service.ts"`<br>4. Extrair os valores percentuais consolidados de `% Branch` e inspecionar o relatório HTML detalhado em `coverage/lcov-report/index.html`.<br>5. Mapear linhas e blocos que ficaram em vermelho (não exercitados). |
| **5. Critérios de Interpretação e Níveis de Julgamento** | - **Nível Excelente:** $CR\text{-}M2 \ge 75\%$. A vasta maioria dos fluxos lógicos e caminhos de exceção está coberta por testes automatizados, permitindo manutenções com alto grau de confiança.<br>- **Nível Aceitável / Moderado:** $60\% \le CR\text{-}M2 < 75\%$. Os fluxos principais estão cobertos, mas caminhos de borda e exceções não são validados automaticamente.<br>- **Nível Crítico / Inaceitável:** $CR\text{-}M2 < 60\%$. Alta vulnerabilidade técnica a falhas de regressão; qualquer correção de regras acadêmicas pela equipe no Motor 2 exigirá obrigatoriamente a criação prévia de testes de unidade antes da modificação do código. |

---

### Ficha da Métrica Complementar: `MET-OP-03b` — Cobertura de Linhas do Motor 2 (CL-M2)

| Campo | Especificação Metodológica |
| :--- | :--- |
| **Identificador** | `MET-OP-03b` |
| **Nome da Métrica** | Cobertura de Linhas do Motor 2 (CL-M2) |
| **Característica / Subcaracterística** | Manutenibilidade — Analisabilidade (*Analysability*) |
| **Pergunta GQM Relacionada** | `Q-OP-03`: Em que nível o componente central do Motor 2 está coberto por testes automatizados para suportar refatorações e correções de defeitos com segurança? |
| **1. Definição** | Percentual de linhas de código executáveis percorridas ao menos uma vez durante a execução dos testes automatizados no arquivo `plano_formatura.service.ts`. Unidade: percentual (%). |
| **2. Procedimento de Cálculo** | $$CL\text{-}M2 = \left( \frac{L_{\text{exercitadas}}}{L_{\text{totais}}} \right) \times 100$$ |
| **3. Fonte dos Dados** | Coluna `% Lines` do relatório gerado pelo test runner em `coverage/index.html`. |
| **4. Procedimento de Coleta** | Coletada simultaneamente com a métrica `MET-OP-03`. |
| **5. Critérios de Interpretação e Níveis de Julgamento** | - **Nível Desejável:** $CL\text{-}M2 \ge 80\%$. A quase totalidade das instruções do serviço é exercitada pela suíte de testes.<br>- **Nível Tolerável:** $65\% \le CL\text{-}M2 < 80\%$. Trechos secundários não são executados.<br>- **Nível Crítico:** $CL\text{-}M2 < 65\%$. Há partes expressivas do algoritmo operando sem qualquer verificação contínua. |

---

## 5. Análise de Pontos Cegos e Rastreabilidade de Manutenção

A instrumentação de cobertura não serve apenas para gerar um número abstrato, mas para identificar os **pontos cegos** do algoritmo do No Fluxo UnB. Na coleta empírica, a equipe inspecionará qualitativamente se os testes existentes cobrem:

1. **Tratamento de co-requisitos:** O que acontece quando uma disciplina exige outra simultaneamente? O código trata essa regra ou a ignora silenciosamente?
2. **Estouro de carga horária semestral:** Se o limite de créditos for atingido no semestre, o algoritmo aloca a disciplina no período seguinte de forma correta ou a descarta sem aviso?
3. **Equivalências curriculares:** As substituições de disciplinas antigas por novas passam por rotinas testadas com casos de borda?

Essa análise apoiará diretamente os entregáveis das Fases 3 e 4, conectando a avaliação de produto à Engenharia de Software aplicada.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Elaboração da especificação de manutenibilidade, isolamento do Motor 2, fichas MET-OP-03 e MET-OP-03b | 16/10 | [e194ba2](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/e194ba2) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Remoção de referências a divisões internas de pessoas e padronização documental | 16/10 | [c19a4e8](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/c19a4e8) |
