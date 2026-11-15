# Especificação dos Métodos de Avaliação Operacional

Este documento detalha os **métodos de avaliação** selecionados e padronizados na Fase 3 para mensurar as características de **Usabilidade** e **Segurança** da funcionalidade _Planejar formatura_ do No Fluxo UnB, em estrito alinhamento com a **ISO/IEC 25040:2011/2024**, **ISO 9241-11** e diretrizes da **OWASP**.

---

## 1. Métodos de Avaliação de Usabilidade

Para avaliar a usabilidade sem a necessidade de recrutamento de sujeitos externos — mantendo o foco analítico da equipe avaliadora sobre a interface —, o método adotado é a **Inspeção Heurística de Nielsen (1994)** combinada com percursos cognitivos baseados em tarefas de referência.

### 1.1 Processo de Inspeção Heurística Estruturada

O método divide-se em quatro etapas rigorosas:

```mermaid
flowchart TD
    E1["<b>1. Preparação</b><br/>Carregamento de massa sintética e setup isolado"] --> E2["<b>2. Inspeção Individual</b><br/>Cada avaliador percorre as tarefas T1, T2 e T3 independentemente"]
    E2 --> E3["<b>3. Registro de Fricções</b><br/>Pontuação Conforme (1) / Não Conforme (0) e Severidade (1 a 4)"]
    E3 --> E4["<b>4. Sessão de Consenso</b><br/>Debate técnico e unificação das notas finais TCH e ISVH"]
```

1. **Inspeção Individual Independente:** Cada avaliador atua isoladamente, sem comunicação prévia com os demais colegas, executando o percurso das 3 tarefas de referência na interface `/plano-formatura`. Essa independência impede o efeito de ancoragem ou viés de confirmação coletiva.
2. **Avaliação por Heurística:** Cada item do checklist (baseado nas 10 Heurísticas de Nielsen) é inspecionado. Se o sistema atender ao princípio, atribui-se conformidade ($1$). Se violar, registra-se não conformidade ($0$), captura-se a evidência visual e classifica-se a severidade de 1 a 4.
3. **Escala de Severidade Padronizada (Nielsen):**
   - **1 — Cosmético:** Problema estético superficial que não degrada a usabilidade nem atrasa o aluno (ex.: pequeno desalinhamento de margem).
   - **2 — Menor:** Fricção leve; o usuário percebe a inconsistência ou hesita, mas consegue continuar a tarefa sem assistência.
   - **3 — Maior:** Dificulta severamente a realização da tarefa, gerando frustração ou risco iminente de interpretação errônea do plano de formatura.
   - **4 — Catastrófico:** Impede a conclusão da tarefa, trava a interação ou induz o estudante a uma decisão acadêmica gravemente incorreta sem possibilidade de recuperação.
4. **Protocolo da Sessão de Consenso:** Os avaliadores reúnem-se com suas folhas de registro individuais. Para cada item com divergência:
   - Se houver divergência quanto à conformidade ($1$ vs $0$), debate-se a evidência à luz da definição da heurística até obtenção de consenso unânime.
   - Se houver divergência de severidade (ex.: avaliador A atribuiu grau 2 e avaliador B atribuiu grau 3), adota-se a severidade mais conservadora (mais alta) quando houver evidência de barreira operacional para o estudante, registrando a justificativa em ata.

### 1.2 Operacionalização das Tarefas de Referência

| ID | Nome da Tarefa | Ponto de Início e Término | Ações Esperadas do Usuário | Heurísticas Inspecionadas |
| :---: | :--- | :--- | :--- | :---: |
| **$T_1$** | Localizar Previsão de Formatura | Tela inicial do planejamento $\to$ Localização do semestre previsto. | Identificar imediatamente o card que resume o ano/semestre estimado para formatura e os semestres restantes, sem necessidade de rolagem excessiva. | #1, #6, #8 |
| **$T_2$** | Interpretar Matérias Críticas | Tela de grafo/tabela $\to$ Identificação das matérias que travam a formatura. | Identificar visualmente os nós com destaque diferenciado (matérias críticas), entender o porquê do destaque e sua dependência na cadeia de pré-requisitos. | #2, #4, #6, #10 |
| **$T_3$** | Ajustar Limite de Créditos | Painel de controle de créditos $\to$ Recálculo da projeção. | Localizar o seletor de créditos por semestre, alterar o valor (ex.: de 24 para 18 créditos), acionar o recálculo, observar o feedback de processamento e reverter a ação se desejado. | #1, #3, #5, #7, #9 |

### 1.3 Equações das Métricas de Usabilidade

* **Taxa de Conformidade Heurística ($TCH$ - `MET-OP-01`):**
  $$TCH = \left( \frac{\sum_{i=1}^{10} C_i}{10} \right) \times 100$$
  Onde $C_i \in \{0, 1\}$ é o resultado consolidado do item $i$ do checklist.

* **Índice de Severidade de Violações Heurísticas ($ISVH$ - `MET-OP-01b`):**
  $$ISVH = (4 \times N_{\text{catastrófico}}) + (3 \times N_{\text{maior}}) + (2 \times N_{\text{menor}}) + (1 \times N_{\text{cosmético}})$$

---

## 2. Métodos de Avaliação de Segurança

A avaliação de segurança adota uma abordagem mista de **Auditoria Estática de Dependências (SCA)**, **Auditoria de Armazenamento Local no Navegador** e **Testes Funcionais Negativos de Controle de Acesso via API**.

```mermaid
flowchart LR
    subgraph MET-OP-02 [Integridade de Dependências]
        SCA["SCA Automatizado<br/>npm audit --json"] --> IRP["Cálculo do IRP Ponderado"]
    end

    subgraph MET-OP-02b [Confidencialidade]
        Storage["Inspeção DevTools<br/>Local / Session / Cookies"] --> GED["Contabilização de Chaves em Claro (GED-C)"]
    end

    subgraph MET-OP-02c [Controle de Acesso]
        API["Bateria de 10 Requisições<br/>POST /planejamento/gerar-plano"] --> TBR["Taxa de Bloqueio 401/403 (TBR)"]
    end
```

### 2.1 Método 1: Software Composition Analysis (SCA) em Caixa-Preta — `MET-OP-02`

Como a avaliação ocorre **sem acesso ao código-fonte interno da aplicação (avaliação estritamente Caixa-Preta)**, a análise de integridade de dependências afere os pacotes JavaScript entregues e executados pelo navegador na rota pública do No Fluxo UnB.

1. **Abordagem Primária (SCA no Cliente / *Fingerprinting* de Dependências):**
   - Utilização da ferramenta de auditoria de dependências cliente recomendada pela OWASP: **Retire.js** (extensão para Chrome e scanner open-source de vulnerabilidades em bibliotecas JavaScript web).
   - Complementarmente, inspeção via Chrome DevTools (*Sources > Network*) dos pacotes e *chunks* servidos (`/_app/immutable/chunks/`), identificando bibliotecas de terceiros (ex.: visualizadores de grafos, utilitários, frameworks) e versões expostas.
2. **Abordagem Complementar (Manifestos Estáticos Públicos):**
   - Caso manifestos estáticos de dependência (`package.json` / `package-lock.json`) estejam acessíveis em repositórios públicos, a execução de `npm audit --json` é feita isoladamente apenas sobre esses manifestos de texto (sem compilação ou execução do backend), sendo processada pelo script `testes/analisador_sca_irp.py`.
3. **Métrica Ponderada ($IRP$):**
   $$IRP = (10 \times N_{\text{crítica}}) + (5 \times N_{\text{alta}}) + (2 \times N_{\text{moderada}}) + (1 \times N_{\text{baixa}})$$
   Onde $N_s$ indica a quantidade de vulnerabilidades conhecidas catalogadas na severidade $s$.

### 2.2 Método 2: Inspeção de Armazenamento no Cliente — `MET-OP-02b`

O método investiga se dados acadêmicos ou identificadores dos estudantes permanecem gravados em texto claro em mecanismos de persistência do navegador, violando as premissas de confidencialidade da ISO/IEC 25010 e da LGPD.

1. **Procedimento:** 
   - Inicializar aba anônima do navegador.
   - Conduzir o fluxo completo de carregamento do histórico acadêmico sintético e geração do planejamento.
   - Abrir o Chrome DevTools (`F12` ou `Ctrl + Shift + I`) e navegar até a aba **Application > Storage**.
2. **Varredura Estruturada:**
   - **Local Storage (`window.localStorage`):** Inspecionar o valor de todas as chaves persistidas.
   - **Session Storage (`window.sessionStorage`):** Verificar dados transitórios da sessão.
   - **Cookies (`document.cookie`):** Verificar a existência de cookies de sessão e a presença obrigatória das flags `HttpOnly` e `Secure`.
3. **Critério de Contabilização de Violação ($GED\text{-}C$):**
   Uma chave é marcada como violação ($\mathbb{I} = 1$) se contiver, sem criptografia forte ou ofuscação unidirecional, qualquer um dos seguintes dados:
   - Número de matrícula do estudante.
   - Nome completo ou CPF.
   - Relação de notas brutas, menções (ex.: SS, MS, MM, MI, II, SR) ou IRA.
   - Histórico bruto de reprovações.

### 2.3 Método 3: Bateria de Testes Negativos de Controle de Acesso — `MET-OP-02c`

O método valida se o endpoint sensível de geração e processamento do plano curricular (`POST /planejamento/gerar-plano` ou equivalente da API) possui autenticação e autorização robustas, rejeitando chamadas não autorizadas conforme a diretriz **OWASP A01:2021 (Broken Access Control)**.

Para conferir significância estatística e cobertura padronizada, foram projetadas **10 requisições negativas controladas**:

| Caso (#) | Categoria do Teste | Configuração do Cabeçalho `Authorization` | Descrição do Teste Negativo | Status Esperado |
| :---: | :--- | :--- | :--- | :---: |
| **REQ-01** | Ausência Total | *Cabeçalho ausente* | Disparo direto de requisição POST sem nenhum cabeçalho de autenticação. | 401 Unauthorized |
| **REQ-02** | Cabeçalho Vazio | `Authorization: ""` | Cabeçalho presente com string vazia. | 401 Unauthorized |
| **REQ-03** | Esquema Inválido | `Authorization: Basic abc123xyz` | Envio de esquema Basic em vez de Bearer token. | 401 Unauthorized |
| **REQ-04** | Bearer Sem Token | `Authorization: Bearer ` | Palavra-chave Bearer sem nenhum token anexado. | 401 Unauthorized |
| **REQ-05** | Token Malformado | `Authorization: Bearer token_aleatorio_invalido_123` | String alfanumérica que não respeita a estrutura JWT (três partes separadas por ponto). | 401 Unauthorized |
| **REQ-06** | JWT com Assinatura Inválida | `Authorization: Bearer eyJhbGci...violada` | Token JWT válido estruturalmente, mas com assinatura criptográfica adulterada. | 401 Unauthorized |
| **REQ-07** | JWT Expirado | `Authorization: Bearer eyJhbGci...exp_passado` | Token JWT cuja claim `exp` possui timestamp anterior ao momento da requisição. | 401 Unauthorized |
| **REQ-08** | JWT sem Assinatura (`alg: none`) | `Authorization: Bearer eyJhbGciOiJub25l...` | Tentativa clássica de bypass alterando o algoritmo do cabeçalho para `none`. | 401 Unauthorized |
| **REQ-09** | Token com Papel Insuficiente | `Authorization: Bearer <token_visitante>` | Token com credenciais de convidado/visitante tentando acessar rota de processamento restrito. | 403 Forbidden |
| **REQ-10** | Origem Falsificada (Cross-Origin) | `Authorization: ""` com `Origin: https://site-malicioso.com` | Requisição sem token simulando origem cruzada não permitida pela política CORS. | 401 ou 403 |

* **Cálculo da Taxa de Bloqueio ($TBR$):**
  $$TBR = \left( \frac{N_{\text{respostas\_401\_ou\_403}}}{10} \right) \times 100$$

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Especificação detalhada dos métodos de Usabilidade (Nielsen) e Segurança (SCA, Storage e Matriz de 10 testes de API) | 14/11/2026 | [6594e5c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/6594e5c2349ee5fc4dc632f07b97bc8191357819) |

