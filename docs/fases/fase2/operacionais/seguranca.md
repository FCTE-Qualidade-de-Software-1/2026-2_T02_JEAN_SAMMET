# Métricas de Segurança

Este documento detalha a especificação das perguntas, hipóteses e métricas de **Segurança** para a funcionalidade _Planejar formatura_ do No Fluxo UnB, focando na proteção da privacidade dos dados acadêmicos dos estudantes, no controle de acesso a rotas de serviço e na integridade da cadeia de suprimentos de software.

---

## 1. Característica e Subcaracterísticas Avaliadas

Conforme o [Modelo de Qualidade](../../fase1/modeloDeQualidade.md) fundamentado na norma **ISO/IEC 25010:2011**, a característica de **Segurança** é avaliada por meio de três subcaracterísticas essenciais para a operação do software:

1. **Confidencialidade (_Confidentiality_):** grau em que o software garante que dados acadêmicos e identificadores pessoais dos alunos (matrícula, notas, histórico escolar e reprovações) sejam acessíveis exclusivamente por partes autorizadas, prevenindo exposição indevida no ambiente do cliente (*browser storage*).
2. **Autenticidade e Controle de Acesso (_Authenticity and Access Control_):** grau em que a identidade de usuários ou sessões pode ser comprovada e as requisições a serviços de processamento (`POST /planejamento/gerar-plano`) são estritamente restritas a sujeitos autenticados, rejeitando chamadas anônimas.
3. **Integridade da Cadeia de Dependências (_Software Supply Chain Integrity_):** grau em que os componentes de terceiros e bibliotecas de código aberto que compõem o frontend e backend estão livres de vulnerabilidades conhecidas e exploráveis (CVEs documentadas).

---

## 2. Questão GQM e Hipótese Associada

### Questão GQM: `Q-OP-02`
> **"A funcionalidade de planejamento de formatura resguarda adequadamente a confidencialidade dos dados acadêmicos e restringe o acesso aos seus serviços contra vulnerabilidades conhecidas e chamadas não autenticadas?"**

### Hipótese Operacional: `H-OP-02`
> **Hipótese:** O software manipula históricos acadêmicos com informações pessoais sensíveis no navegador e se comunica com serviços externos e de banco de dados (Supabase); a retenção não volátil de dados de históricos no armazenamento do cliente (`localStorage`) e a existência de bibliotecas desatualizadas na árvore de dependências do npm podem expor o sistema a vulnerabilidades conhecidas de severidade moderada a alta.

---

## 3. Fichas Completas das Métricas de Segurança

### Ficha da Métrica Principal: `MET-OP-02` — Densidade de Vulnerabilidades Conhecidas em Dependências (DVCD)

| Campo | Especificação Metodológica |
| :--- | :--- |
| **Identificador** | `MET-OP-02` |
| **Nome da Métrica** | Densidade de Vulnerabilidades Conhecidas em Dependências (DVCD) |
| **Característica / Subcaracterística** | Segurança — Integridade da Cadeia de Dependências (*Supply Chain Integrity*) |
| **Pergunta GQM Relacionada** | `Q-OP-02`: A funcionalidade de planejamento resguarda o acesso contra vulnerabilidades conhecidas? |
| **1. Definição** | Quantidade absoluta e ponderada de vulnerabilidades de segurança publicamente conhecidas (registradas na base nacional de vulnerabilidades / CVE) presentes na árvore de dependências diretas e transitivas do frontend e do backend, identificadas via Software Composition Analysis (SCA). Unidade: contagem inteira de CVEs por nível de severidade (*Critical*, *High*, *Moderate*, *Low*). |
| **2. Procedimento de Cálculo** | Executa-se a auditoria automatizada de pacotes em ambos os módulos (`frontend/` e `backend/`). O índice de risco ponderado da aplicação ($IRP$) é computado por:<br><br>$$IRP = (10 \times N_{\text{crítica}}) + (5 \times N_{\text{alta}}) + (2 \times N_{\text{moderada}}) + (1 \times N_{\text{baixa}})$$<br>Onde $N_s$ representa o número de vulnerabilidades encontradas no nível de severidade $s$. |
| **3. Fonte dos Dados** | Relatórios automatizados gerados em formato JSON pelo utilitário oficial `npm audit --json` executado sobre os arquivos de manifesto `package.json` e de lockfile `package-lock.json` no commit de referência `87b5475`. |
| **4. Procedimento de Coleta** | 1. Clonar o repositório público no commit delimitado.<br>2. Navegar separadamente aos diretórios `frontend` e `backend`.<br>3. Executar o comando `npm audit --json > audit-report.json`.<br>4. Parsear os relatórios identificando os identificadores GHSA/CVE, pacotes afetados, severidade e disponibilidade de correção sem quebra de API (*breaking changes*). |
| **5. Critérios de Interpretação e Níveis de Julgamento** | - **Nível Excelente:** $N_{\text{crítica}} = 0$, $N_{\text{alta}} = 0$ e $IRP \le 5$. Ausência de vulnerabilidades de alto impacto explorável.<br>- **Nível Aceitável:** $N_{\text{crítica}} = 0$, $N_{\text{alta}} \le 2$ (desde que restritas a dependências de desenvolvimento sem exposição em runtime de produção) e $IRP \le 20$.<br>- **Nível Crítico / Inaceitável:** $N_{\text{crítica}} \ge 1$ ou $N_{\text{alta}} > 2$ em dependências de produção. Indica exposição grave a vetores como execução remota de código (RCE), Prototype Pollution ou negação de serviço via dependência. |

---

### Ficha da Métrica Complementar: `MET-OP-02b` — Grau de Exposição de Dados Pessoais no Cliente (GED-C)

| Campo | Especificação Metodológica |
| :--- | :--- |
| **Identificador** | `MET-OP-02b` |
| **Nome da Métrica** | Grau de Exposição de Dados Pessoais no Cliente (GED-C) |
| **Característica / Subcaracterística** | Segurança — Confidencialidade (*Confidentiality*) |
| **Pergunta GQM Relacionada** | `Q-OP-02`: A funcionalidade de planejamento resguarda adequadamente a confidencialidade dos dados acadêmicos? |
| **1. Definição** | Mede a presença e persistência indevida de dados pessoais identificáveis (PII) e informações acadêmicas confidenciais (número de matrícula, nome do estudante, IRA, histórico de notas e reprovações) armazenados em texto claro em mecanismos de persistência do navegador (`localStorage`, `sessionStorage` ou cookies desprovidos da flag `HttpOnly`). Unidade: contagem de chaves/atributos sensíveis retidos sem criptografia. |
| **2. Procedimento de Cálculo** | $$GED\text{-}C = \sum_{k \in S_{\text{armazenamento}}} \mathbb{I}(\text{contém\_dado\_sensível\_em\_claro}(k))$$<br>Onde $S_{\text{armazenamento}}$ é o conjunto de todas as chaves persistidas no navegador após o fluxo completo de upload de histórico e geração do plano, e $\mathbb{I}$ é a função indicadora que assume valor 1 caso o valor contenha PII desprotegida e 0 caso contrário. |
| **3. Fonte dos Dados** | Inspeção via console de desenvolvimento do navegador (painel *Application* do Chrome DevTools / Storage do Firefox Developer Edition) após a execução do fluxo padrão de uso com histórico sintético. |
| **4. Procedimento de Coleta** | 1. Iniciar sessão em aba anônima e autenticar no No Fluxo UnB.<br>2. Realizar o upload do histórico acadêmico sintético e gerar o planejamento curricular.<br>3. Acessar *DevTools > Application > Storage* e inspecionar os namespaces `Local Storage`, `Session Storage` e `Cookies`.<br>4. Inspecionar o conteúdo de cada chave serializada e verificar se constam dados acadêmicos brutos persistidos além do token de autenticação de sessão. |
| **5. Critérios de Interpretação e Níveis de Julgamento** | - **Nível Conforme (Desejável):** $GED\text{-}C = 0$. Nenhum dado acadêmico sensível (notas, matrícula, histórico completo) permanece persistido em texto claro no armazenamento permanente do cliente; apenas tokens temporários ou preferências de interface são retidos.<br>- **Nível Não Conforme (Crítico):** $GED\text{-}C \ge 1$. Existência de histórico acadêmico ou matrícula retida em texto claro no `localStorage`, violando princípios de minimização de dados e segurança da informação previstos na LGPD. |

---

### Ficha da Métrica Complementar: `MET-OP-02c` — Taxa de Bloqueio de Requisições Não Autenticadas (TBR)

| Campo | Especificação Metodológica |
| :--- | :--- |
| **Identificador** | `MET-OP-02c` |
| **Nome da Métrica** | Taxa de Bloqueio de Requisições Não Autenticadas (TBR) |
| **Característica / Subcaracterística** | Segurança — Autenticidade e Controle de Acesso (*Access Control*) |
| **Pergunta GQM Relacionada** | `Q-OP-02`: As chamadas aos serviços de planejamento restringem adequadamente o acesso não autorizado? |
| **1. Definição** | Percentual de requisições de teste enviadas aos endpoints protegidos da funcionalidade de planejamento (`POST /planejamento/gerar-plano` e rotas correlatas de persistência) sem credencial de autenticação (cabeçalho `Authorization: Bearer <token>` ausente ou com token JWT inválido/expirado) que são terminantemente rejeitadas pelo backend com status HTTP 401 (*Unauthorized*) ou 403 (*Forbidden*). Unidade: percentual (%). |
| **2. Procedimento de Cálculo** | $$TBR = \left( \frac{N_{\text{bloqueios\_corretos}}}{N_{\text{requisicoes\_teste\_invalidas}}} \right) \times 100$$<br>Onde:<br>- $N_{\text{bloqueios\_corretos}}$: total de tentativas que retornaram status HTTP 401 ou 403 sem processamento do payload.<br>- $N_{\text{requisicoes\_teste\_invalidas}}$: total de requisições enviadas nos cenários de teste não autorizados (amostra de controle com $N \ge 10$ variações de headers). |
| **3. Fonte dos Dados** | Logs de respostas HTTP obtidos via requisições de teste controladas e não destrutivas executadas via `curl` ou Postman contra o endpoint da API. |
| **4. Procedimento de Coleta** | 1. Formular payload padrão de planejamento de formatura.<br>2. Disparar chamadas variando os cenários: (a) ausência completa de header `Authorization`, (b) header com token malformado, (c) token expirado e (d) token assinado com chave espúria.<br>3. Registrar o status HTTP retornado e a presença ou ausência de dados de resposta. |
| **5. Critérios de Interpretação e Níveis de Julgamento** | - **Nível Conforme (Mandatório):** $TBR = 100\%$. Todas as requisições não autenticadas ou inválidas são bloqueadas imediatamente, impedindo consumo indevido de processamento do algoritmo do Motor 2.<br>- **Nível Crítico (Falha Grave):** $TBR < 100\%$. Qualquer cenário em que a rota processe os dados ou retorne código HTTP 200/500 sem autenticação válida é considerado vulnerabilidade crítica de controle de acesso (Broken Access Control - OWASP Top 10). |

---

## 4. Alinhamento com Padrões de Segurança da Informação e LGPD

A avaliação de segurança orienta-se por normas consagradas:

1. **OWASP Top 10 (2021):**
   - **A01:2021 — Broken Access Control:** coberto pela métrica `MET-OP-02c`, prevenindo que endpoints que exigem contexto de estudante autenticado possam ser acionados arbitrariamente.
   - **A06:2021 — Vulnerable and Outdated Components:** coberto pela métrica `MET-OP-02`, verificando se a árvore de pacotes de terceiros introduz brechas exploráveis.
2. **Lei Geral de Proteção de Dados (Lei nº 13.709/2018 - LGPD):**
   - **Princípio da Segurança e da Prevenção (Art. 6º, incisos VII e VIII):** coberto pela métrica `MET-OP-02b`, mitigando o risco de que computadores de uso compartilhado em laboratórios da UnB retenham históricos e notas de estudantes anteriores em caches locais do navegador.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Elaboração da especificação de segurança, fichas MET-OP-02, MET-OP-02b e MET-OP-02c e alinhamento com OWASP/LGPD | 16/10 | [3584382](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/3584382ccfb17e27db841b011ce415fa1503cbbc) |
