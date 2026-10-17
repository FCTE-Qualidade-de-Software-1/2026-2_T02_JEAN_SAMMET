# Protocolo de Coleta e Condições de Teste

Este documento estabelece o protocolo formal de coleta, medição e registro das condições experimentais para as métricas operacionais (**Usabilidade** e **Segurança**) da funcionalidade _Planejar formatura_ do No Fluxo UnB, em estrita conformidade com as diretrizes do processo **ISO/IEC 25040**.

---

## 1. Diretrizes Metodológicas de Reprodutibilidade

Para garantir que qualquer avaliador ou mantenedor do software possa reproduzir os testes e verificar os mesmos resultados, a coleta obedece a três princípios fundamentais:

1. **Padronização de Entrada:** Uso exclusivo de históricos sintéticos controlados, sem dados pessoais reais (em conformidade com a LGPD e o [Escopo](../../fase1/escopo.md)).
2. **Isolamento de Variáveis:** Execução dos testes de usabilidade e inspeção em ambientes de navegador sem extensões ativas e em abas anônimas.
3. **Registro Auditável:** Toda sessão de teste gera evidências brutas (gravações de tela, planilhas de observação, dumps de armazenamento e relatórios JSON de auditoria de segurança).

---

## 2. Ficha de Registro de Condições de Teste (Ambiente)

Antes de iniciar qualquer medição, a equipe deve preencher a ficha de ambiente padronizada:

| Parâmetro de Ambiente | Especificação / Valor Padrão para a Avaliação |
| :--- | :--- |
| **Data e Horário da Coleta** | Registrar data e faixa horária (horário de Brasília) |
| **Versão / Commit do Código** | Commit de referência `87b5475` (código público) / Instância `no-fluxo.crianex.com` |
| **Ambiente de Hardware** | CPU (Processador), Memória RAM e Arquitetura do equipamento de teste |
| **Sistema Operacional** | Linux Ubuntu (22.04 LTS ou superior) / Windows 11 / macOS |
| **Navegador e Versão** | Google Chrome (versão estável mais recente, 64 bits) |
| **Resolução de Exibição** | 1920 × 1080 (Full HD) em janela maximizada |
| **Conexão de Rede** | Banda larga fixa (registrar taxa de download/upload e ping médio) |
| **Responsável pela Coleta** | [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) |

---

## 3. Protocolo de Avaliação de Usabilidade (`MET-OP-01` e `MET-OP-01b`)

### 3.1 Recrutamento e Ética
- **Amostra:** Mínimo de 5 estudantes de graduação da UnB com perfis distintos (calouro/iniciante, meio de curso, formando e aluno com reprovações).
- **Termo de Consentimento:** Esclarecer verbalmente ao participante que o objeto de avaliação é o software e a clareza da interface, e nunca as habilidades individuais do estudante. Assegura-se o anonimato das observações.

### 3.2 Roteiro das Tarefas Padronizadas
O avaliador deve apresentar ao participante as seguintes instruções neutras, sem induzir o local onde ele deve clicar:

* **Tarefa T1 (Previsão de Formatura):**
  > _"Imagine que você acabou de importar o seu histórico acadêmico. Por favor, navegue até a tela de planejamento de formatura e me diga em qual semestre o sistema estima que você irá se formar e quantos semestres faltam."_
* **Tarefa T2 (Matérias Críticas):**
  > _"Observando a tela de planejamento, identifique quais matérias foram destacadas pelo sistema como 'críticas' e em qual semestre futuro elas estão planejadas."_
* **Tarefa T3 (Ajuste de Créditos):**
  > _"Suponha que você começou a estagiar e agora deseja cursar no máximo 20 créditos por semestre. Altere essa preferência no sistema e solicite a atualização do planejamento."_

### 3.3 Planilha de Registro de Dados Brutos de Usabilidade

| ID Part. | Perfil Acadêmico | T1: Previsão Formatura | T2: Matérias Críticas | T3: Ajuste de Créditos | Tempo Total Sessão | Comentários e Hesitações Observadas |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **P01** | Concluinte | [1 = Autônomo / 0 = Ajuda ou Falha] | [1 / 0] | [1 / 0] | __ min | [Relato descritivo de dúvidas] |
| **P02** | Meio de curso | [1 / 0] | [1 / 0] | [1 / 0] | __ min | [...] |
| **P03** | Reprovações no fluxo | [1 / 0] | [1 / 0] | [1 / 0] | __ min | [...] |
| **P04** | Iniciante (2º semestre) | [1 / 0] | [1 / 0] | [1 / 0] | __ min | [...] |
| **P05** | Formando | [1 / 0] | [1 / 0] | [1 / 0] | __ min | [...] |

---

## 4. Protocolo de Auditoria de Vulnerabilidades em Dependências (`MET-OP-02`)

### 4.1 Comandos de Execução
No terminal da máquina de testes, clonar o repositório público no commit delimitado (`87b5475`) e executar a auditoria em ambos os módulos:

```bash
# 1. Auditoria no módulo Backend
cd /caminho/para/2025-1-NoFluxoUnB/backend
npm audit --json > audit-backend.json

# 2. Auditoria no módulo Frontend
cd /caminho/para/2025-1-NoFluxoUnB/frontend
npm audit --json > audit-frontend.json
```

### 4.2 Tabela de Registro de Vulnerabilidades de Dependências

| Módulo Avaliado | Crítica (10 pts) | Alta (5 pts) | Moderada (2 pts) | Baixa (1 pt) | Índice de Risco Ponderado ($IRP$) | Status de Julgamento |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Backend** (`backend/`) | [preencher] | [preencher] | [preencher] | [preencher] | [cálculo] | [Excelente / Aceitável / Crítico] |
| **Frontend** (`frontend/`) | [preencher] | [preencher] | [preencher] | [preencher] | [cálculo] | [Excelente / Aceitável / Crítico] |
| **Consolidado Geral** | [total] | [total] | [total] | [total] | [total] | **Resultado Global `MET-OP-02`** |

---

## 5. Protocolo de Inspeção de Armazenamento e Controle de Acesso (`MET-OP-02b` e `MET-OP-02c`)

### 5.1 Inspeção de Armazenamento do Cliente (`MET-OP-02b`)
1. Abrir o navegador em modo de navegação anônima sem extensões.
2. Autenticar na aplicação e realizar o fluxo completo de upload de histórico acadêmico sintético e geração do plano.
3. Abrir o DevTools (`F12`), acessar a aba **Application** (ou **Storage** no Firefox).
4. Inspecionar:
   - `Local Storage`: verificar se existem chaves com objetos serializados contendo notas, IRA, matrícula ou matérias cursadas.
   - `Session Storage`: verificar os artefatos voláteis criados durante a sessão.
   - `Cookies`: checar se cookies de sessão possuem as diretivas de proteção `HttpOnly` e `Secure`.
5. Salvar a árvore de chaves inspecionadas e registrar a contagem de chaves com dados em texto claro ($GED\text{-}C$).

### 5.2 Validação de Controle de Acesso a Rotas Protegidas (`MET-OP-02c`)
Executar no terminal 10 requisições simuladas sem token de autorização contra o endpoint de geração de planejamento:

```bash
# Teste de chamada não autenticada ao endpoint de planejamento
curl -i -X POST "https://no-fluxo.crianex.com/api/planejamento/gerar-plano" \
     -H "Content-Type: application/json" \
     -d '{"matriculaCurricular": "6360/1", "disciplinasConcluidas": []}'
```

Registrar na planilha de teste se a resposta retornada foi estritamente **HTTP 401 Unauthorized** ou **HTTP 403 Forbidden** (Taxa de Bloqueio $TBR = 100\%$).

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Elaboração dos protocolos experimentais de usabilidade, desempenho e manutenibilidade | 16/10 | [f2910c5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f2910c5) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Ajuste do protocolo experimental para Usabilidade e Segurança | 16/10 | [91b3fa1](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/91b3fa1) |
