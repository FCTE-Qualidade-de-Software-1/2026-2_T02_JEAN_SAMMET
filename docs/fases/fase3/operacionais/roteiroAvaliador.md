# Roteiro Operacional Passo a Passo para o Avaliador

Este documento estabelece as **instruções passo a passo, detalhadas e repetíveis**, que cada avaliador deve seguir durante a execução experimental na Fase 4. A padronização estrita deste roteiro garante a ausência de ambiguidades operacionais e a confiabilidade dos dados obtidos, conforme preconiza a norma **ISO/IEC 25040:2011/2024**.

---

## 1. Roteiro de Inspeção Heurística (Usabilidade)

Destinado aos avaliadores de usabilidade para coleta das métricas `MET-OP-01` ($TCH$) e `MET-OP-01b` ($ISVH$).

### 1.1 Etapa 1: Preparação do Ambiente Individual
1. Feche todas as instâncias abertas do Google Chrome.
2. Abra uma **nova janela anônima** (`Ctrl + Shift + N` no Linux/Windows ou `Cmd + Shift + N` no macOS).
3. Verifique se o zoom do navegador está configurado em **100%** (`Ctrl + 0`).
4. Maximize a janela na resolução de 1920 × 1080.
5. Acesse a aplicação No Fluxo UnB no commit congelado `87b5475` (ou na instância `no-fluxo.crianex.com`).
6. Carregue o perfil sintético **P1** ([Massa de Dados Sintética](ambienteERecursos.md#22-perfis-sinteticos-de-teste)).

### 1.2 Etapa 2: Execução das Tarefas de Referência
O avaliador deve navegar pela rota `/plano-formatura` e executar ordenadamente as tarefas abaixo, observando atentamente a interação e as respostas visuais do sistema:

- **Execução da Tarefa $T_1$ (Localizar Previsão de Formatura):**
  - Direcione a atenção para a localização da estimativa de formatura.
  - Observe se o ano e semestre de formatura estão evidentes de imediato ou se demandam cálculo mental e contagem manual de períodos (Heurística #6 e #8).
  - Verifique se o estado atual do plano é exibido com clareza (Heurística #1).

- **Execução da Tarefa $T_2$ (Interpretar Matérias Críticas):**
  - Localize a indicação de matérias críticas (disciplinas que limitam o avanço curricular).
  - Avalie se a expressão "matérias críticas" é compreensível e contextualizada (Heurística #2).
  - Verifique se a diferenciação cromática e geométrica desses nós é consistente com o restante da interface (Heurística #4).
  - Tente acessar documentações ou legendas explicativas sobre as matérias críticas (Heurística #10).

- **Execução da Tarefa $T_3$ (Ajustar Limite de Créditos):**
  - Localize o controle de créditos por semestre.
  - Altere o limite padrão de créditos (ex.: reduza para 18 créditos).
  - Observe se o sistema fornece feedback visual claro durante o recálculo do fluxo (Heurística #1).
  - Tente inserir valores inválidos (ex.: créditos negativos ou acima de 40) e verifique se há prevenção de erros (Heurística #5).
  - Avalie a facilidade para reverter a alteração ou resetar o planejamento para a configuração original (Heurística #3).

### 1.3 Etapa 3: Preenchimento Individual do Checklist
Para cada um dos 10 itens da tabela abaixo, preencha:
- **Conformidade:** Digite **1** se a interface atende satisfatoriamente; digite **0** se houver violação ergonômica.
- **Severidade (se 0):** Atribua **1** (Cosmético), **2** (Menor), **3** (Maior) ou **4** (Catastrófico).
- **Descrição da Evidência:** Descreva textualmente o comportamento inadequado e tire uma captura de tela da falha.

| # | Heurística de Nielsen | Pergunta Guia do Checklist | Conforme? (1/0) | Severidade (1 a 4) | Evidência / Descrição da Fricção |
| :---: | :--- | :--- | :---: | :---: | :--- |
| **01** | Visibilidade do estado (#1) | O sistema indica claramente quando está recalculando a projeção de formatura? | [ ] | [ ] | |
| **02** | Correspondência (#2) | A terminologia acadêmica ("matérias críticas", "créditos") é intuitiva para o discente? | [ ] | [ ] | |
| **03** | Controle e liberdade (#3) | É fácil desfazer um ajuste de créditos ou retornar ao plano anterior com um clique? | [ ] | [ ] | |
| **04** | Consistência (#4) | Os nós e semestres mantêm o mesmo padrão de cores e tipografia em toda a tela? | [ ] | [ ] | |
| **05** | Prevenção de erros (#5) | O sistema impede valores incoerentes de créditos e avisa sobre quebra de pré-requisitos? | [ ] | [ ] | |
| **06** | Reconhecimento (#6) | O semestre de formatura é identificado de relance, sem memorização ou contagem manual? | [ ] | [ ] | |
| **07** | Flexibilidade e eficiência (#7) | Há ferramentas ágeis de visualização do grafo (zoom suave, arrasto rápido, visualização resumida)? | [ ] | [ ] | |
| **08** | Design minimalista (#8) | O layout é limpo, livre de poluição visual, linhas emaranhadas ou sobreposição de cards? | [ ] | [ ] | |
| **09** | Diagnóstico de erros (#9) | Mensagens de incompatibilidade curricular explicam com clareza o problema e a solução? | [ ] | [ ] | |
| **10** | Ajuda e documentação (#10) | Existem tooltips, legendas explicativas ou guias contextuais sobre as regras do plano? | [ ] | [ ] | |

### 1.4 Etapa 4: Sessão de Consenso e Desempate
1. Reúna os avaliadores com suas tabelas individuais preenchidas.
2. Identifique itens divergentes (ex.: um avaliador marcou 1 e outro marcou 0).
3. Reexamine a interface em conjunto e determine o veredito por unanimidade.
4. Caso haja divergência de severidade, registre em ata o motivo da escolha final (adotando a regra conservadora em caso de barreira real para o aluno).
5. Calcule as métricas $TCH$ e $ISVH$ na planilha consolidada.

---

## 2. Roteiro de Auditoria de Segurança

Destinado ao auditor técnico para coleta das métricas `MET-OP-02` ($DVCD$ / $IRP$), `MET-OP-02b` ($GED\text{-}C$) e `MET-OP-02c` ($TBR$).

### 2.1 Coleta de `MET-OP-02` (Auditoria de Dependências em Caixa-Preta)

Como a avaliação é realizada **sem acesso ao código-fonte interno da aplicação**, a análise de vulnerabilidades de dependências é executada de forma não invasiva no cliente (SCA Caixa-Preta) sobre as bibliotecas JavaScript entregues pelo servidor:

1. **Varredura via Extensão Retire.js (Recomendada):**
   - Instale a extensão oficial de código aberto **Retire.js** na Google Chrome Web Store.
   - Acesse a aplicação na rota pública `https://no-fluxo.crianex.com/plano-formatura`.
   - Abra o DevTools (`F12`) e acesse a aba **Retire.js**.
   - A ferramenta varre automaticamente todos os scripts e bibliotecas carregados pelo navegador, identificando nomes, versões e CVEs conhecidas catalogadas na National Vulnerability Database (NVD).
   - Tire capturas de tela das bibliotecas detectadas e exporte os dados.
2. **Inspeção Manual de Chunks SvelteKit (Via DevTools):**
   - No DevTools (`F12`), abra a aba **Sources** ou **Network** e filtre por arquivos `.js`.
   - Inspecione os cabeçalhos dos arquivos em `/_app/immutable/chunks/` para identificar menções e metadados de dependências de terceiros.
3. **Alternativa via Manifestos Públicos (se disponíveis):**
   - Caso os arquivos públicos `package.json` e `package-lock.json` sejam obtidos isoladamente, execute `npm audit --json` em diretório isolado e processe pelo script:
     ```bash
     python3 testes/analisador_sca_irp.py
     ```
4. **Cálculo do $IRP$:** Registre as vulnerabilidades encontradas por severidade e aplique a ponderação do $IRP$.

### 2.2 Coleta de `MET-OP-02b` (Inspeção de Armazenamento Local no Navegador)
1. Abra uma janela anônima limpa no Google Chrome.
2. Pressione `F12` para abrir o DevTools e selecione a aba **Application**.
3. No menu lateral esquerdo, expanda **Storage**.
4. Realize a importação do histórico sintético e gere a projeção de formatura na tela `/plano-formatura`.
5. Clique sequencialmente em:
   - **Local Storage:** Selecione a origem `https://no-fluxo.crianex.com` (ou `http://localhost:5173`).
   - **Session Storage:** Selecione a mesma origem.
   - **Cookies:** Selecione a mesma origem.
6. Para cada item listado no painel:
   - Analise os nomes das chaves e os valores JSON armazenados.
   - Verifique a existência de menções, notas brutas, IRA, matrícula ou nome de estudante em texto claro.
   - Verifique nos Cookies se as flags `HttpOnly` e `Secure` estão marcadas como ativas.
7. Tire um print da tela do DevTools comprovando a inspeção.
8. Contabilize o número total de violações identificadas ($GED\text{-}C$).

### 2.3 Coleta de `MET-OP-02c` (Bateria de Testes Negativos de Controle de Acesso)
1. Certifique-se de que o Python 3 e a biblioteca `requests` estão instalados.
2. Execute o script automatizado contendo a suíte das 10 requisições negativas:
   ```bash
   python3 testes/teste_controle_acesso_tbr.py
   ```
3. O script executará ordenadamente os 10 casos de teste contra o endpoint `/planejamento/gerar-plano`:
   - REQ-01: Sem header `Authorization`
   - REQ-02: Header `Authorization` vazio
   - REQ-03: Esquema `Basic`
   - REQ-04: Esquema `Bearer` vazio
   - REQ-05: Token com string aleatória
   - REQ-06: JWT com assinatura manipulada
   - REQ-07: JWT com tempo expirado
   - REQ-08: JWT com algoritmo `none`
   - REQ-09: Token de perfil não autorizado
   - REQ-10: Requisição com origem cruzada suspeita
4. O script exibirá o status HTTP retornado por cada chamada (esperado: 401 ou 403), computará a taxa $TBR$ e salvará o log em `testes/evidencias/seguranca/api/resultado_tbr.log`.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Elaboração do roteiro passo a passo do avaliador para Usabilidade e Segurança | 14/11/2026 | [6594e5c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/6594e5c2349ee5fc4dc632f07b97bc8191357819) |

