# Especificação da Avaliação — Métricas Operacionais

Este documento centraliza e introduz as perguntas e métricas operacionais desenvolvidas sob o método **Goal-Question-Metric (GQM)** para avaliar a funcionalidade _Planejar formatura_ do No Fluxo UnB, abrangendo os aspectos de experiência do usuário e segurança da informação do produto de software.

Para garantir legibilidade, profundidade técnica e facilidade de consulta, a documentação foi modularizada em seções especializadas:

---

## Navegação pelas Páginas da Fase 2 (Operacionais)

| Seção / Página | Foco e Conteúdo Principal | Hipótese Relacionada | Métricas Relacionadas |
| :--- | :--- | :---: | :---: |
| **[1. Visão Geral e Estrutura GQM](operacionais/visaoGeral.md)** | Contexto da Fase 1, stakeholders, Objetivo GQM, hipóteses operacionais e árvore hierárquica completa. | `H-OP-01`<br>`H-OP-02` | Todas |
| **[2. Métricas de Usabilidade](operacionais/usabilidade.md)** | Inspeção heurística de Nielsen (checklist ergonômico), tarefas de referência $T_1, T_2, T_3$ e ISO 9241-11. | `H-OP-01` | `MET-OP-01`<br>`MET-OP-01b` |
| **[3. Métricas de Segurança](operacionais/seguranca.md)** | Auditoria SCA (`npm audit`), persistência no cliente (`localStorage`), bloqueio em rotas e conformidade LGPD/OWASP. | `H-OP-02` | `MET-OP-02`<br>`MET-OP-02b`<br>`MET-OP-02c` |
| **[4. Protocolo de Coleta e Condições de Teste](operacionais/protocolo.md)** | Roteiro de inspeção heurística da equipe, fichas de ambiente e comandos de auditoria/inspeção. | `H-OP-01`<br>`H-OP-02` | Todas |
| **[5. Referências](operacionais/referencias.md)** | Normas técnicas (ISO/IEC, ISO 9241), frameworks de segurança (OWASP), LGPD e metodologia GQM. | — | Todas |

---

## Resumo da Estrutura GQM com Hipóteses

```mermaid
graph TD
    Goal["Objetivo GQM Operacional:<br/>Avaliar Usabilidade e Segurança da funcionalidade Planejar Formatura"]
    
    Goal --> H1["<b>Hipótese H-OP-01</b>:<br/>Violações heurísticas comprometem a operabilidade e a apreensão"]
    Goal --> H2["<b>Hipótese H-OP-02</b>:<br/>Retenção de dados no cliente e dependências desatualizadas geram vulnerabilidades"]
    
    H1 --> Q1["Q-OP-01: A interface atende às heurísticas ergonômicas de usabilidade?"]
    H2 --> Q2["Q-OP-02: O sistema resguarda a confidencialidade e restringe o acesso contra vulnerabilidades?"]
    
    Q1 --> M1["MET-OP-01: Taxa de Conformidade Heurística (TCH)"]
    Q1 --> M1b["MET-OP-01b: Índice de Severidade de Violações Heurísticas (ISVH)"]
    
    Q2 --> M2["MET-OP-02: Densidade de Vulnerabilidades Conhecidas (DVCD)"]
    Q2 --> M2b["MET-OP-02b: Grau de Exposição de Dados no Cliente (GED-C)"]
    Q2 --> M2c["MET-OP-02c: Taxa de Bloqueio em Rotas Não Autenticadas (TBR)"]
```

---

## Integração com as Métricas Funcionais

As métricas operacionais complementam diretamente as métricas de adequação funcional ([Métricas Funcionais](funcionais/visaoGeral.md)). A correlação entre a proteção dos dados dos estudantes, a clareza da interface e a conformidade do plano com as regras acadêmicas da UnB assegura a validade global da avaliação segundo o processo **ISO/IEC 25040**.

---

## Referências Bibliográficas

As referências metodológicas, normativas técnicas (ISO/IEC e ISO 9241), diretrizes de segurança (OWASP) e legislação de proteção de dados (LGPD) que fundamentam a especificação destas métricas encontram-se detalhadas em [Referências das Métricas Operacionais](operacionais/referencias.md) e consolidadas na página geral de [Referências da Fase 2](../../referencias/fase2.md).

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Modularização das páginas operacionais em subdocumentos especializados e estruturação do índice geral | 16/10 | [f8219c0](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f8219c0) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Remoção de referências a divisões internas de pessoas e padronização documental | 16/10 | [81912ba](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/81912bac5e02d7429e2d05446544ec9636891f5e) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Ajuste do sumário de métricas operacionais para Usabilidade e Segurança | 16/10 | [3584382](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/3584382ccfb17e27db841b011ce415fa1503cbbc) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Remoção de emojis nos títulos, correção de links relativos e inclusão das referências operacionais | 18/10 | [acadb8d](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/acadb8d) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Inclusão das hipóteses operacionais na tabela de navegação e na árvore GQM | 24/10 | [corrente] |

