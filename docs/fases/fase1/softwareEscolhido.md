# Software Escolhido: No Fluxo UnB

## 1. Identificação

| Item | Descrição |
| :--- | :--- |
| Nome | No Fluxo UnB / NoFluxoUNB |
| Repositório de referência | [unb-mds/2025-1-NoFluxoUNB](https://github.com/unb-mds/2025-1-NoFluxoUNB) |
| Site | [no-fluxo.crianex.com](https://no-fluxo.crianex.com) |
| Descrição | Aplicação web de apoio à visualização da estrutura curricular e ao planejamento acadêmico de estudantes da UnB |
| Tipo de produto | Aplicação web com interface no navegador, serviços de backend e integrações externas |

## 2. Tipo de produto

O software é uma **aplicação web de apoio ao planejamento acadêmico**. O usuário interage por uma interface no navegador, e algumas funções dependem de serviços de backend e de dados curriculares. O produto também inclui recursos de IA, mas eles não serão o foco desta avaliação.

## 3. Descrição simplificada dos componentes

| Componente | Responsabilidade geral | Relevância para a avaliação |
| :--- | :--- | :--- |
| Frontend web | Apresenta a interface e permite ao estudante interagir com o fluxograma e as funções disponíveis | Principal objeto dos testes de usabilidade e observação funcional |
| Backend TypeScript/Node.js | Expõe serviços usados pela interface e coordena parte da lógica da aplicação | Pode ser consultado na análise funcional e na inspeção limitada de segurança, se o código relevante estiver disponível |
| Banco e autenticação Supabase | Fornece serviços de dados e autenticação usados pelo sistema | Relevante para observar controles de acesso e tratamento de dados, sem testes invasivos |
| Agente/serviços Python e integrações de IA | Implementam parte das funções assistidas por IA e/ou busca semântica | Fora do foco principal, salvo se necessário para entender uma função observada |
| Scripts de coleta de dados | Obtêm ou atualizam dados curriculares a partir de fontes externas | A qualidade dos dados pode afetar a adequação funcional; os dados usados nos testes precisam ter referência conhecida |

A estrutura acima é uma visão de alto nível baseada na organização e documentação públicas do repositório. Ela não pretende ser um diagrama completo de implantação, nem garante que todos os componentes sejam usados em todas as telas.

## 4. Restrições para a avaliação

- **Dados pessoais:** não usar históricos reais de terceiros sem autorização. Preferir dados sintéticos ou dados de teste explicitamente autorizados.
- **Serviços externos:** a disponibilidade e o comportamento de provedores externos não são totalmente controlados pela equipe.
- **Segurança:** não realizar testes de intrusão, tentativas de contornar autenticação ou acesso a dados alheios. A avaliação ficará limitada a observações e inspeção não invasiva.

## 5. Implicações para a avaliação

| É viável avaliar | Limite da conclusão |
| :--- | :--- |
| Comparar informações apresentadas em cenários específicos com dados curriculares de referência | Não comprova correção para todos os cursos, matrizes ou históricos |
| Observar se participantes concluem tarefas predefinidas na interface | Uma amostra pequena não representa todos os estudantes |
| Verificar, sem exploração invasiva, controles de acesso e possíveis exposições observáveis no fluxo selecionado | Não comprova ausência de vulnerabilidades nem equivale a teste de penetração |
| Consultar documentação e código público para compreender componentes relevantes | Não garante que a versão em produção seja idêntica ao código consultado |

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Criação do molde da página | 15/10 | [828688f](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/828688feb645eebfcd428e11b4b9f87585253b9b) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Preenchimento com os dados do No Fluxo UnB | 15/10 | [559e7a9](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/559e7a94f159c2caeb4dc9d5996ba9392d0862ac) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Atualização da pagina | 16/10 | [a6af5fc](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/a6af5fc9dd7113834f334660210ce67b31465d0a) |