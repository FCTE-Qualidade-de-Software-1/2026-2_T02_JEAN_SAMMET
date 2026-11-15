# Protocolo de Coleta e Condições de Teste

Protocolo de medição e registro das condições experimentais para as métricas operacionais (**Usabilidade** e **Segurança**) da funcionalidade _Planejar formatura_ do No Fluxo UnB (processo **ISO/IEC 25040**).

---

## 1. Diretrizes de Reprodutibilidade

1. **Dados Sintéticos:** histórico acadêmico fictício sem dados pessoais reais (em conformidade com a LGPD e o [Escopo](../../fase1/escopo.md)).
2. **Isolamento:** testes executados em abas anônimas e sem extensões de navegador ativas.
3. **Registro Auditável:** geração de planilhas de observação, dumps de armazenamento e relatórios JSON de auditoria.

---

## 2. Ficha de Registro de Ambiente

| Parâmetro | Especificação / Valor de Referência |
| :--- | :--- |
| **Data e Horário** | Registrar data e faixa horária (horário de Brasília) |
| **Commit / Instância** | Commit do código/manifesto e URL da instância, registrados separadamente; declarar se a versão implantada for desconhecida |
| **Hardware** | Processador, Memória RAM e Arquitetura |
| **Sistema Operacional** | Linux Ubuntu (22.04 LTS+) / Windows 11 / macOS |
| **Navegador** | Google Chrome (versão estável mais recente, 64 bits) |
| **Resolução** | 1920 × 1080 (Full HD, maximizado) |
| **Rede** | Banda larga fixa (registrar ping e taxas de download/upload) |
| **Avaliador** | [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) |

---

## 3. Protocolo de Inspeção Heurística — Teste da Hipótese `H-OP-01` (`MET-OP-01` e `MET-OP-01b`)

A inspeção é realizada diretamente pela equipe avaliadora, dispensando o recrutamento de voluntários externos. Os avaliadores aplicam o checklist ergonômico de 10 itens baseado nas Heurísticas de Nielsen e consolidam consensualmente os resultados.

### 3.1 Procedimento de Inspeção Interna
1. **Preparação:** Abrir a aplicação No Fluxo UnB no ambiente controlado com o histórico sintético carregado.
2. **Inspeção Individual:** Cada avaliador percorre a tela `/plano-formatura` executando as tarefas de referência ($T_1$: localizar previsão, $T_2$: interpretar críticas, $T_3$: ajustar créditos).
3. **Avaliação por Item:** Para cada um dos 10 itens do checklist, registrar:
   - **Situação:** Conforme (1) ou Não Conforme (0).
   - **Severidade da Violação (se Não Conforme):** 1 (Cosmético), 2 (Menor), 3 (Maior) ou 4 (Catastrófico).
4. **Sessão de Consenso:** Os avaliadores debatem divergências e fecham as pontuações consolidadas da `MET-OP-01` ($TCH$) e `MET-OP-01b` ($ISVH$).

### 3.2 Planilha de Registro de Inspeção Heurística

| Item (#) | Heurística Avaliada | Tarefa | Conforme? (1/0) | Severidade (1–4) | Problema Identificado / Evidência `H-OP-01` |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **01** | Visibilidade do estado | $T_3$ | [1 / 0] | [— / 1–4] | [Feedback visual ao alterar créditos] |
| **02** | Correspondência com o mundo real | $T_2$ | [1 / 0] | [— / 1–4] | [Clareza da expressão "matérias críticas"] |
| **03** | Controle e liberdade do usuário | $T_3$ | [1 / 0] | [— / 1–4] | [Facilidade para desfazer ou resetar] |
| **04** | Consistência e padrões | $T_1, T_2$ | [1 / 0] | [— / 1–4] | [Padrão de cores e formas dos nós] |
| **05** | Prevenção de erros | $T_3$ | [1 / 0] | [— / 1–4] | [Validação de limites no input de créditos] |
| **06** | Reconhecimento em vez de memorização | $T_1$ | [1 / 0] | [— / 1–4] | [Destaque visual do card de formatura] |
| **07** | Flexibilidade e eficiência de uso | $T_1, T_2$ | [1 / 0] | [— / 1–4] | [Zoom, arrasto e atalhos de visualização] |
| **08** | Design estético e minimalista | $T_1, T_2$ | [1 / 0] | [— / 1–4] | [Poluição visual e nós sobrepostos] |
| **09** | Auxílio no diagnóstico e correção de erros | $T_3$ | [1 / 0] | [— / 1–4] | [Alertas de incompatibilidade curricular] |
| **10** | Ajuda e documentação | $T_2$ | [1 / 0] | [— / 1–4] | [Tooltips explicativos sobre regras do plano] |
| **Consolidado** | **Taxa $TCH$ e Índice $ISVH$** | — | **[Total]/10** | **Soma $ISVH$** | **Status: [Excelente / Aceitável / Crítico]** |

---

## 4. Protocolo de Auditoria de Dependências — Teste da Hipótese `H-OP-02` (`MET-OP-02`)

### 4.1 Método e cobertura

1. No cliente, usar Retire.js nos scripts carregados pela aplicação. Preservar os arquivos ou seu inventário com URLs e hashes, versão da ferramenta, base consultada e saída integral.
2. Quando disponíveis, auditar os manifestos públicos do commit de referência separadamente:

```bash
# Executar no diretório do módulo, com package.json e lockfile disponíveis.
npm audit --json > audit-modulo.json
```

3. Registrar achados por componente, versão, aviso e severidade, sem duplicatas. Separar produção/desenvolvimento quando verificável. Não somar resultados sobrepostos de npm e Retire.js.
4. Calcular o IRP conforme a [ficha de segurança](seguranca.md). Arquivo ausente ou erro da ferramenta gera Inconclusivo, nunca zero.

Retire.js cobre as bibliotecas reconhecidas no cliente; não substitui a auditoria dos manifestos de frontend e backend. Essa alternativa reduz a cobertura originalmente prevista. Registrar a mudança e deixar explícitos os componentes não examinados, sem extrapolar um resultado favorável para todo o produto.

### 4.2 Registro da coleta

| Campo | Registro obrigatório |
|---|---|
| Alvo e versão | URL/data da instância ou commit do manifesto |
| Ferramenta e base | Nome, versão, comando e data da base de vulnerabilidades |
| Cobertura | Arquivos, componentes e versões reconhecidos; partes não examinadas |
| Achados | Componente, versão, aviso, severidade e produção/desenvolvimento |
| Evidência e resultado | Caminho do relatório bruto, contagens por severidade, IRP e classificação |

## 5. Armazenamento e acesso (`MET-OP-02b` e `MET-OP-02c`)

### 5.1 Armazenamento no cliente

1. Em sessão limpa, carregar o histórico sintético e gerar o plano; autenticar se o fluxo exigir.
2. Inspecionar `localStorage`, `sessionStorage` e cookies em **DevTools > Application**.
3. Registrar chaves e valores sintéticos com evidências. Verificar `HttpOnly` e `Secure` no painel de cookies; não usar `document.cookie` para concluir sobre cookies HttpOnly.
4. Contar as chaves com dados pessoais ou acadêmicos em claro. Se o fluxo ou a inspeção estiver incompleto, registrar Inconclusivo.

### 5.2 Controle de acesso

1. Confirmar o requisito de proteção e obter URL, método e payload a partir do fluxo normal. Validar uma chamada positiva autorizada no mesmo serviço.
2. Em ambiente autorizado, executar os casos negativos da Fase 3 e registrar respostas e comportamento. Usar credenciais de teste adequadas para isolar expiração e permissões.
3. Classificar cada caso: bloqueio 401/403, acesso indevido comprovado ou Inconclusivo. Erros 404/405, de conexão ou de servidor não demonstram falha de autenticação.
4. Calcular TBR apenas com casos válidos; informar casos planejados, válidos e inconclusivos. Só aprovar com toda a bateria concluída e válida.

As regras completas estão na [ficha da TBR](seguranca.md#met-op-02c-taxa-de-bloqueio-de-requisicoes-nao-autorizadas-tbr). Registrar Não aplicável se o requisito permitir acesso público e não houver operação protegida no recorte.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Elaboração dos protocolos experimentais de usabilidade, desempenho e manutenibilidade | 16/10 | [f2910c5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f2910c5) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Ajuste do protocolo experimental para Usabilidade e Segurança | 16/10 | [3584382](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/3584382ccfb17e27db841b011ce415fa1503cbbc) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Simplificação textual e concisão mantendo fidelidade ao protocolo experimental ISO 25040 | 24/10 | [b31d87e](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/b31d87e) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Substituição do protocolo com voluntários externos por Inspeção Heurística interna de Nielsen | 25/10 | [8330fa6](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/8330fa6ce8a670d083d8718eada13606616f064c) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Alinhamento da cobertura SCA e da validade dos testes de acesso | 15/11 | Não commitado |
