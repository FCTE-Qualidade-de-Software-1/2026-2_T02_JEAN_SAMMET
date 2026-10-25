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
| **Commit / Instância** | Commit `87b5475` / `no-fluxo.crianex.com` |
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

### 4.1 Comandos de Execução
No commit `87b5475`, executar a auditoria em ambos os módulos:

```bash
# Backend
cd /caminho/para/2025-1-NoFluxoUnB/backend
npm audit --json > audit-backend.json

# Frontend
cd /caminho/para/2025-1-NoFluxoUnB/frontend
npm audit --json > audit-frontend.json
```

### 4.2 Registro de Vulnerabilidades

| Módulo | Crítica (10 pts) | Alta (5 pts) | Moderada (2 pts) | Baixa (1 pt) | $IRP$ | Status (Validação `H-OP-02`) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Backend** (`backend/`) | [preencher] | [preencher] | [preencher] | [preencher] | [cálculo] | [Excelente / Aceitável / Crítico] |
| **Frontend** (`frontend/`) | [preencher] | [preencher] | [preencher] | [preencher] | [cálculo] | [Excelente / Aceitável / Crítico] |
| **Consolidado** | [total] | [total] | [total] | [total] | [total] | **Resultado Global `MET-OP-02`** |

---

## 5. Inspeção de Armazenamento e Acesso — Teste da Hipótese `H-OP-02` (`MET-OP-02b` e `MET-OP-02c`)

### 5.1 Armazenamento no Cliente (`MET-OP-02b`)
1. Autenticar em aba anônima e enviar o histórico sintético para gerar o plano.
2. No DevTools (`F12`), acessar **Application > Storage**.
3. Inspecionar:
   - `Local Storage`: verificar persistência de notas, IRA, matrícula ou disciplinas.
   - `Session Storage`: verificar dados de sessão.
   - `Cookies`: checar presença de flags `HttpOnly` e `Secure`.
4. Contabilizar chaves com dados sensíveis em texto claro ($GED\text{-}C$).

### 5.2 Controle de Acesso a Rotas Protegidas (`MET-OP-02c`)
Disparar chamadas sem token contra o endpoint de planejamento:

```bash
curl -i -X POST "https://no-fluxo.crianex.com/api/planejamento/gerar-plano" \
     -H "Content-Type: application/json" \
     -d '{"matriculaCurricular": "6360/1", "disciplinasConcluidas": []}'
```

Registrar se o retorno foi estritamente **HTTP 401 Unauthorized** ou **HTTP 403 Forbidden** ($TBR = 100\%$).

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Elaboração dos protocolos experimentais de usabilidade, desempenho e manutenibilidade | 16/10 | [f2910c5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f2910c5) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Ajuste do protocolo experimental para Usabilidade e Segurança | 16/10 | [3584382](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/3584382ccfb17e27db841b011ce415fa1503cbbc) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Simplificação textual e concisão mantendo fidelidade ao protocolo experimental ISO 25040 | 24/10 | [b31d87e](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/b31d87e) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Substituição do protocolo com voluntários externos por Inspeção Heurística interna de Nielsen | 25/10 | [8330fa6](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/8330fa6ce8a670d083d8718eada13606616f064c) |

