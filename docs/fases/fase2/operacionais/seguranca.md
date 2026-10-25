# Métricas de Segurança

Especificação de perguntas, hipóteses e métricas de **Segurança** para a funcionalidade _Planejar formatura_ do No Fluxo UnB, focando em privacidade de dados acadêmicos, controle de acesso e dependências de software.

---

## 1. Subcaracterísticas Avaliadas (ISO/IEC 25010)

1. **Confidencialidade (_Confidentiality_):** proteção de dados acadêmicos e identificadores dos alunos (matrícula, notas, histórico), prevenindo exposição indevida no navegador (*browser storage*).
2. **Autenticidade e Controle de Acesso (_Access Control_):** restrição de endpoints de processamento (`POST /planejamento/gerar-plano`) exclusivamente a usuários autenticados, rejeitando chamadas anônimas.
3. **Integridade da Cadeia de Dependências (_Supply Chain Integrity_):** ausência de vulnerabilidades conhecidas (CVEs) em pacotes de terceiros no frontend e backend.

---

## 2. Questão GQM e Hipótese Associada

- **Questão `Q-OP-02`:** A funcionalidade resguarda a confidencialidade dos dados acadêmicos e restringe o acesso aos serviços contra vulnerabilidades conhecidas e chamadas não autenticadas?
- **Hipótese `H-OP-02`:** O processamento no navegador com retenção em `localStorage` e dependências desatualizadas no npm podem expor dados sensíveis e vulnerabilidades de severidade moderada a alta.

---

## 3. Fichas das Métricas de Segurança

### `MET-OP-02` — Densidade de Vulnerabilidades em Dependências (DVCD)

| Campo | Especificação |
| :--- | :--- |
| **Identificador** | `MET-OP-02` |
| **Nome** | Densidade de Vulnerabilidades Conhecidas em Dependências (DVCD) |
| **Característica** | Segurança — Integridade da Cadeia de Dependências |
| **Questão GQM** | `Q-OP-02`: O sistema resguarda o acesso contra vulnerabilidades conhecidas? |
| **Hipótese Relacionada** | **`H-OP-02`**: A presença de dependências desatualizadas no npm expõe o sistema a vulnerabilidades conhecidas. |
| **Definição** | Quantidade e risco ponderado de CVEs conhecidas nas dependências diretas e transitivas (frontend e backend), via Software Composition Analysis (SCA). |
| **Cálculo** | Índice de Risco Ponderado ($IRP$):<br>$$IRP = (10 \times N_{\text{crítica}}) + (5 \times N_{\text{alta}}) + (2 \times N_{\text{moderada}}) + (1 \times N_{\text{baixa}})$$<br>Onde $N_s$ é a quantidade de vulnerabilidades na severidade $s$. |
| **Fonte** | Relatórios gerados por `npm audit --json` nos arquivos `package.json` e `package-lock.json` no commit `87b5475`. |
| **Coleta** | 1. Executar `npm audit --json` separadamente em `frontend/` e `backend/`.<br>2. Extrair identificadores GHSA/CVE, pacotes afetados e severidade.<br>3. Computar o $IRP$ por módulo e consolidado. |
| **Níveis de Julgamento** | - **Excelente:** $N_{\text{crítica}} = 0$, $N_{\text{alta}} = 0$ e $IRP \le 5$ (refuta `H-OP-02`).<br>- **Aceitável:** $N_{\text{crítica}} = 0$, $N_{\text{alta}} \le 2$ (apenas devDependencies) e $IRP \le 20$.<br>- **Crítico:** $N_{\text{crítica}} \ge 1$ ou $N_{\text{alta}} > 2$ em produção (**confirma `H-OP-02`**; risco de RCE, Prototype Pollution, etc.). |

---

### `MET-OP-02b` — Grau de Exposição de Dados no Cliente (GED-C)

| Campo | Especificação |
| :--- | :--- |
| **Identificador** | `MET-OP-02b` |
| **Nome** | Grau de Exposição de Dados Pessoais no Cliente (GED-C) |
| **Característica** | Segurança — Confidencialidade |
| **Questão GQM** | `Q-OP-02`: O sistema resguarda a confidencialidade dos dados acadêmicos? |
| **Hipótese Relacionada** | **`H-OP-02`**: A retenção não volátil de dados de histórico em `localStorage` expõe dados acadêmicos a vazamento local. |
| **Definição** | Quantidade de dados pessoais identificáveis (matrícula, IRA, notas, reprovações) armazenados em texto claro em mecanismos de persistência do navegador (`localStorage`, `sessionStorage` ou cookies sem flag `HttpOnly`). |
| **Cálculo** | $$GED\text{-}C = \sum_{k \in S_{\text{storage}}} \mathbb{I}(\text{contém\_dado\_sensível\_em\_claro}(k))$$<br>Onde $\mathbb{I}$ assume 1 se a chave persistida contiver dado sensível desprotegido e 0 caso contrário. |
| **Fonte** | Painel DevTools (*Application > Storage*) após fluxo de upload de histórico e geração do plano. |
| **Coleta** | 1. Autenticar em aba anônima e enviar histórico sintético.<br>2. Gerar o planejamento de formatura.<br>3. Inspecionar `Local Storage`, `Session Storage` e `Cookies`.<br>4. Contabilizar chaves com dados acadêmicos brutos em texto claro. |
| **Níveis de Julgamento** | - **Conforme (Desejável):** $GED\text{-}C = 0$ (refuta `H-OP-02`; dados acadêmicos não persistem em texto claro).<br>- **Não Conforme (Crítico):** $GED\text{-}C \ge 1$ (**confirma `H-OP-02`**; histórico ou matrícula em texto claro no `localStorage`, violando a LGPD). |

---

### `MET-OP-02c` — Taxa de Bloqueio em Rotas Não Autenticadas (TBR)

| Campo | Especificação |
| :--- | :--- |
| **Identificador** | `MET-OP-02c` |
| **Nome** | Taxa de Bloqueio de Requisições Não Autenticadas (TBR) |
| **Característica** | Segurança — Autenticidade e Controle de Acesso |
| **Questão GQM** | `Q-OP-02`: As chamadas aos serviços de planejamento restringem o acesso não autorizado? |
| **Hipótese Relacionada** | **`H-OP-02`**: Falhas de autenticação em endpoints protegidos permitem chamadas anônimas que consomem serviços indevidamente. |
| **Definição** | Percentual de requisições de teste sem credencial válida enviadas ao endpoint `POST /planejamento/gerar-plano` que são bloqueadas com HTTP 401 ou 403. |
| **Cálculo** | $$TBR = \left( \frac{N_{\text{bloqueios\_corretos}}}{N_{\text{requisicoes\_teste\_invalidas}}} \right) \times 100$$ |
| **Fonte** | Respostas HTTP obtidas em testes não destrutivos via `curl` ou Postman ($N \ge 10$ variações de headers). |
| **Coleta** | 1. Enviar requisições variando: (a) sem header `Authorization`, (b) token malformado, (c) token expirado e (d) assinatura inválida.<br>2. Registrar códigos de status e corpos de resposta. |
| **Níveis de Julgamento** | - **Conforme (Mandatório):** $TBR = 100\%$ (todas as chamadas sem autorização são rejeitadas com 401/403; refuta vulnerabilidade de rota).<br>- **Crítico (Falha Grave):** $TBR < 100\%$ (rota processa payload ou retorna 200/500 sem autenticação; **confirma `H-OP-02`** e violação OWASP A01). |

---

## 4. Alinhamento com OWASP Top 10 e LGPD

1. **OWASP Top 10 (2021):**
   - **A01 — Broken Access Control:** validado por `MET-OP-02c` para impedir chamadas anônimas aos serviços de planejamento.
   - **A06 — Vulnerable and Outdated Components:** coberto por `MET-OP-02` via auditoria de pacotes npm.
2. **LGPD (Lei nº 13.709/2018):**
   - **Segurança e Prevenção (Art. 6º, VII e VIII):** endereçado por `MET-OP-02b`, mitigando riscos de vazamento de dados acadêmicos em computadores compartilhados.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Elaboração da especificação de segurança, fichas MET-OP-02, MET-OP-02b e MET-OP-02c e alinhamento com OWASP/LGPD | 16/10 | [3584382](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/3584382ccfb17e27db841b011ce415fa1503cbbc) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Simplificação textual e concisão mantendo coerência com ISO 25010, OWASP e LGPD | 24/10 | [corrente] |

