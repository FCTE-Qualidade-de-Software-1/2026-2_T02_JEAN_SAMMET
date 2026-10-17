# Escopo, Profundidade e Objetos de Avaliação

<!-- Critério 6. Nível máximo: racional para cada corte + limites de validade dos resultados. -->

## 1. O que será avaliado agora

| Objeto de avaliação | Característica relacionada | Profundidade |
| :--- | :--- | :--- |
| Interface da tela "Planejar formatura" (Frontend SvelteKit, rota `/plano-formatura`, onboarding e grafo de disciplinas) | Usabilidade (Apreensibilidade e Operabilidade) | Testes com participantes baseados em tarefas pré-definidas, gravação de sessão e registro de taxa de sucesso e erros. |
| Armazenamento local no cliente (`localStorage` / `sessionStorage`) e rotas protegidas (`POST /planejamento/gerar-plano`) | Segurança (Confidencialidade e Autenticidade) | Inspeção de artefatos de dados acadêmicos retidos no navegador pós-processamento de histórico e verificação de bloqueio (HTTP 401/403) a chamadas não autenticadas. |
| Árvore de dependências do frontend e backend (`package.json` / `package-lock.json`) | Segurança (Integridade de Dependências) | Auditoria automatizada de vulnerabilidades conhecidas (Software Composition Analysis - SCA via `npm audit`) classificadas por severidade (CVEs). |
| Regras de ordenação, pré-requisitos, co-requisitos e cobertura de disciplinas obrigatórias do plano | Adequação Funcional (Correção e Completude) | Execução de cenários de teste com históricos sintéticos confrontados com a matriz curricular oficial da UnB. |

## 2. O que fica fora

| Item excluído | Motivo |
| :--- | :--- |
| Testes de carga, estresse e volume em produção | A infraestrutura é mantida por terceiros e o backend impõe limite de 120 requisições por minuto por IP; testes volumosos poderiam degradar o serviço para usuários reais ou causar bloqueio do IP. |
| Testes de segurança invasivos / pentest destrutivo / ataques DoS | Não autorizados pela mantenedora e pelos termos de uso dos provedores (Supabase e Crianex). A avaliação de segurança restringe-se a métodos não invasivos: auditoria estática de dependências (SCA), inspeção de retenção de dados no cliente e controle de acesso a endpoints. |
| Avaliação das respostas do assistente Darcy AI | Depende de chamadas externas pagas a modelos de linguagem (Maritaca e Google Gemini), sujeitas a cotas diárias e não-determinismo que inviabiliza testes reprodutíveis com baixo custo. |
| Testes em múltiplos sistemas operacionais móveis (smartphones/tablets) | Restrição de cronograma e escopo; priorização do uso em ambiente desktop, onde o grafo interativo é prioritariamente manipulado. |
| Históricos escolares reais de terceiros sem autorização formal | Conformidade com a Lei Geral de Proteção de Dados (LGPD); serão utilizados exclusivamente históricos sintéticos construídos pela equipe. |

## 3. Limites de validade dos resultados

1. **Ambiente de execução vs. Produção:** A verificação de segurança no cliente e as rotas protegidas são avaliadas em navegadores e endpoints controlados. Variações em políticas de segurança da CDN ou configurações dinâmicas de nuvem em produção podem diferir do ambiente analisado.
2. **Amostragem de Usuários:** Os testes de usabilidade são realizados com uma amostra de conveniência de estudantes da UnB executando tarefas padronizadas. Conclusões sobre apreensibilidade são limitadas aos perfis representados na amostra.
3. **Versão do Código:** A análise de segurança de dependências (`npm audit`) tem como referência estrita o commit `87b5475` do repositório público. A Crianex pode realizar atualizações em produção que não estejam refletidas imediatamente no branch principal do repositório público.
4. **Matriz Curricular Alvo:** Os testes funcionais e operacionais concentram-se primariamente na matriz do curso de Engenharia de Software da FGA/UnB (matriz 6360/1). Embora os componentes do Motor 2 sejam genéricos, particularidades de regras de outros cursos não são generalizáveis a partir desta amostra.

## 4. Premissas

- **Ambiente de Hardware e Software dos Testes:**
  - Sistema operacional: Linux / Windows / macOS em arquitetura x86_64/arm64.
  - Navegador padrão: Google Chrome (versão estável mais recente) e Mozilla Firefox em resolução mínima de 1920×1080 (Full HD).
  - Ambiente de desenvolvimento: Node.js versão 20.x e gerenciador de pacotes npm/pnpm para execução das auditorias de dependências e testes.
- **Contas de Acesso:** Disponibilidade de contas de teste cadastradas no No Fluxo UnB para permitir a autenticação obrigatória da rota `/plano-formatura`.
- **Dados de Entrada:** Históricos acadêmicos sintéticos em formato PDF (estruturados conforme o padrão gerado pelo SIGAA UnB) e dados manuais correspondentes, contendo diferentes situações curriculares (aluno iniciante, concluinte, com reprovações e com trancamentos).

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Criação do molde da página | 15/10 | [828688f](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/828688feb645eebfcd428e11b4b9f87585253b9b) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Detalhamento do escopo operacional, exclusões, limites e premissas | 16/10 | [106ddd5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/106ddd54ca773213a62318d809bc06db010d8232) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Ajuste do escopo para Adequação Funcional, Usabilidade e Segurança | 16/10 | [91b3fa1](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/91b3fa1) |