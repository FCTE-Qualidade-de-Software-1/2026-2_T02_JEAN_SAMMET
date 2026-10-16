# Protocolo de Coleta e Condições de Teste

Este documento estabelece o protocolo formal de coleta, medição e registro das condições experimentais para as métricas operacionais (**Usabilidade**, **Desempenho** e **Manutenibilidade**) da funcionalidade _Planejar formatura_ do No Fluxo UnB, em estrita conformidade com as diretrizes do processo **ISO/IEC 25040**.

---

## 1. Diretrizes Metodológicas de Reprodutibilidade

Para garantir que qualquer avaliador ou mantenedor do software possa reproduzir os testes e verificar os mesmos resultados, a coleta obedece a três princípios fundamentais:

1. **Padronização de Entrada:** Uso exclusivo de históricos sintéticos controlados, sem dados pessoais reais (em conformidade com a LGPD e o [Escopo](../../fase1/escopo.md)).
2. **Isolamento de Variáveis:** Execução dos testes em ambientes de navegador sem extensões ativas e com parâmetros de rede conhecidos.
3. **Registro Auditável:** Toda sessão de teste gera evidências brutas (gravações de tela, logs de rede e relatórios HTML de cobertura).

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

## 4. Protocolo de Medição de Desempenho (`MET-OP-02` e `MET-OP-02b`)

### 4.1 Preparação do Ambiente
1. Abrir o Google Chrome em modo de navegação anônima para desativar qualquer extensão que possa interferir no DOM ou no tráfego de rede.
2. Abrir o DevTools (`F12`), selecionar a aba **Network** e marcar a opção **Disable cache**.
3. Autenticar com a conta de testes e carregar o histórico sintético padrão de Engenharia de Software (aluno com aproximadamente 50% de integralização).

### 4.2 Procedimento Experimental (10 Repetições)
1. Clicar no botão de acionamento do planejamento.
2. Registrar o tempo da requisição `POST /planejamento/gerar-plano` na coluna *Time* da aba Network ($T_{\text{backend}}$).
3. Na aba **Performance**, verificar o término da pintura visual completa dos componentes do grafo no DOM ($T_{\text{total}}$).
4. Subtrair $T_{\text{total}} - T_{\text{backend}}$ para obter o tempo de renderização do cliente ($T_{\text{frontend}}$).
5. **Aguardar 10 segundos** antes de disparar a próxima repetição para respeitar o limite de 120 requisições por minuto por IP da infraestrutura.
6. Repetir o procedimento até completar 10 execuções válidas.

### 4.3 Tabela de Coleta dos Tempos de Desempenho

| Execução | $T_{\text{backend}}$ (ms) | $T_{\text{frontend}}$ (ms) | Tempo Total $TGRP$ (ms) | Status HTTP | Observações |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **R01** | | | | 200 OK | Execução inicial |
| **R02** | | | | 200 OK | |
| **R03** | | | | 200 OK | |
| **R04** | | | | 200 OK | |
| **R05** | | | | 200 OK | |
| **R06** | | | | 200 OK | |
| **R07** | | | | 200 OK | |
| **R08** | | | | 200 OK | |
| **R09** | | | | 200 OK | |
| **R10** | | | | 200 OK | |
| **Mediana ($\tilde{T}$)** | | | | — | **Indicador Central (`MET-OP-02`)** |
| **P95 / Máx ($T_{\max}$)** | | | | — | **Pior cenário observado** |
| **Desvio Padrão ($s$)** | | | | — | **Estabilidade temporal** |

---

## 5. Protocolo de Instrumentação de Manutenibilidade (`MET-OP-03` e `MET-OP-03b`)

### 5.1 Comandos de Execução
No terminal da máquina de testes, executar:

```bash
# 1. Acessar o subdiretório do backend no commit 87b5475
cd /caminho/para/2025-1-NoFluxoUnB/backend

# 2. Assegurar dependências instaladas (Node 20.x)
npm install

# 3. Executar a suíte de testes com cobertura isolada no serviço do Motor 2
npm run test -- --coverage --collectCoverageFrom="src/services/plano_formatura.service.ts"
```

### 5.2 Tabela de Registro da Cobertura de Código

| Componente Instrumentado | Total de Linhas | Linhas Cobertas | % Linhas (`MET-OP-03b`) | Total de Branches | Branches Cobertos | % Branches (`MET-OP-03`) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `src/services/plano_formatura.service.ts` | [preencher] | [preencher] | [%] | [preencher] | [preencher] | [%] |

### 5.3 Evidência Comprobatória
- Salvar a captura de tela do terminal com o relatório em texto tabular gerado.
- Exportar o arquivo HTML gerado pelo Istanbul/c8 em `coverage/lcov-report/src/services/plano_formatura.service.ts.html` para inspeção visual detalhada das linhas não cobertas.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Elaboração dos protocolos experimentais de usabilidade, desempenho e manutenibilidade | 16/10 | [f2910c5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f2910c5) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Remoção de referências a divisões internas de pessoas e padronização documental | 16/10 | [81912ba](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/81912bac5e02d7429e2d05446544ec9636891f5e) |
