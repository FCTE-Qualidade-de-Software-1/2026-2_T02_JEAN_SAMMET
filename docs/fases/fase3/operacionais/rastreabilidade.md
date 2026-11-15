# Matriz de Rastreabilidade Bidirecional — Métricas Operacionais

Este documento consolida a **rastreabilidade bidirecional** entre todas as fases do processo de avaliação da qualidade segundo a **ISO/IEC 25040:2011/2024**, demonstrando a correspondência direta entre as necessidades dos stakeholders (Fase 1), a especificação GQM (Fase 2), o projeto operacional de teste (Fase 3) e as evidências esperadas na execução (Fase 4).

---

## 1. Visão Geral da Rastreabilidade Entre as Fases

A integridade do processo de avaliação apoia-se no encadeamento ininterrupto de requisitos, métricas e procedimentos:

```mermaid
flowchart LR
    F1["<b>Fase 1: Requisitos</b><br/>Stakeholders e<br/>Características Priorizadas"] 
    --> F2["<b>Fase 2: Especificação</b><br/>GQM, Hipóteses H-OP e<br/>Fichas de Métricas"]
    --> F3["<b>Fase 3: Projeto</b><br/>Métodos, Ambientes,<br/>Massa Sintética e Roteiros"]
    --> F4["<b>Fase 4: Execução</b><br/>Dados Brutos, Julgamento<br/>e Ação de Melhoria"]
```

---

## 2. Matriz Completa de Rastreabilidade Operacional

| Stakeholder (Fase 1) | Característica / Subcaracterística (Fase 1) | Questão e Hipótese GQM (Fase 2) | Métrica e Nível Alvo (Fase 2) | Método e Atividade Projetada (Fase 3) | Recursos e Ferramentas (Fase 3) | Evidência / Dado Bruto Previsto (Fase 4) | Ação de Julgamento e Melhoria (Fase 4) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Estudante da UnB** | **Usabilidade** — *Operabilidade* | `Q-OP-01`<br>`H-OP-01` | **`MET-OP-01` (TCH)**<br>Alvo: $TCH \ge 85\%$ | `ATV-OP-05` e `06`<br>Inspeção Heurística de Nielsen nas tarefas $T_1$, $T_2$ e $T_3$ com sessão de consenso. | Google Chrome anônimo (1080p), Checklist padronizado de 10 itens, massa sintética P1. | Folhas de inspeção preenchidas, capturas de tela das fricções e ata de consenso. | Validação de $H\text{-}OP\text{-}01$. Refinamento do layout de créditos e filtros na interface. |
| **Estudante da UnB** | **Usabilidade** — *Apreensibilidade* | `Q-OP-01`<br>`H-OP-01` | **`MET-OP-01b` (ISVH)**<br>Alvo: $N_{\text{cat}} = 0$, $N_{\text{maior}} = 0$, $ISVH \le 5$ | `ATV-OP-05` e `06`<br>Escoragem ponderada de severidades (1 a 4) atribuídas aos itens não conformes. | Escala de Nielsen de 4 níveis, protocolo de desempate conservador, sessão de alinhamento. | Planilha de ponderação com cálculo matemático de $ISVH$ e relatório descritivo. | Validação de $H\text{-}OP\text{-}01$. Inclusão de tooltips e desambiguação de "matérias críticas". |
| **Mantenedores (Crianex)** | **Segurança** — *Integridade da Cadeia de Dependências* | `Q-OP-02`<br>`H-OP-02` | **`MET-OP-02` (DVCD)**<br>Alvo: $N_{\text{crít}} = 0$, $N_{\text{alta}} = 0$, $IRP \le 5$ | `ATV-OP-02`<br>Auditoria estática de composição de software (SCA) nos repositórios. | Node.js, NPM, `testes/analisador_sca_irp.py`, commit `87b5475`. | Arquivos brutos `audit-frontend.json` e `audit-backend.json`, log de extração de CVEs. | Validação de $H\text{-}OP\text{-}02$. Execução de `npm audit fix` ou substituição de dependências desatualizadas. |
| **Estudante da UnB** / **Mantenedores** | **Segurança** — *Confidencialidade* (LGPD) | `Q-OP-02`<br>`H-OP-02` | **`MET-OP-02b` (GED-C)**<br>Alvo: $GED\text{-}C = 0$ chaves sensíveis | `ATV-OP-03`<br>Inspeção visual e estruturada de persistência no navegador (*DevTools Storage*). | Chrome DevTools (*Application > Storage*), massa sintética P1 e P2. | Capturas de tela dos itens em `localStorage`, `sessionStorage` e cookies com análise de conteúdo. | Validação de $H\text{-}OP\text{-}02$. Migração de dados sensíveis para memória volátil ou anonimização imediata. |
| **Mantenedores (Crianex)** | **Segurança** — *Autenticidade e Controle de Acesso* (OWASP A01) | `Q-OP-02`<br>`H-OP-02` | **`MET-OP-02c` (TBR)**<br>Alvo: $TBR = 100\%$ bloqueios (HTTP 401/403) | `ATV-OP-04`<br>Bateria automatizada de 10 requisições negativas contra a rota de planejamento. | Python 3, `requests`, `testes/teste_controle_acesso_tbr.py`, endpoint `/planejamento/gerar-plano`. | Relatório de execução com códigos de status HTTP e corpos de resposta gravados em log. | Validação de $H\text{-}OP\text{-}02$. Inserção de middleware de autenticação nas rotas desprotegidas. |

---

## 3. Justificativa das Escolhas Metodológicas

1. **Inspeção Heurística vs. Testes com Usuários Reais:** A opção pela inspeção heurística interna por avaliadores da equipe atende com rigor às restrições éticas e de cronograma, eliminando riscos de vazamento de dados de terceiros e fornecendo um diagnóstico de conformidade técnica direto.
2. **Abordagem SCA Multi-Módulo:** A auditoria segregada entre `frontend` e `backend` permite isolar se eventuais vulnerabilidades afetam o cliente (SvelteKit) ou o servidor de processamento, orientando diretamente a priorização da ação de melhoria na Fase 4.
3. **Massa de Dados Estruturada:** O uso de perfis sintéticos P1 e P2 cobre desde o uso rotineiro até situações de sobrecarga de pré-requisitos, assegurando que o sistema seja testado em condições extremas de usabilidade sem comprometer nenhum dado pessoal discente.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Criação da matriz de rastreabilidade bidirecional completa da Fase 1 à Fase 4 para métricas operacionais | 14/11/2026 | [6594e5c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/6594e5c2349ee5fc4dc632f07b97bc8191357819) |

