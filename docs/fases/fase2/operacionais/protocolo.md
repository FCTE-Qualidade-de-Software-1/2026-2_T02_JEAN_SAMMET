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

## 3. Protocolo de Usabilidade — Teste da Hipótese `H-OP-01` (`MET-OP-01` e `MET-OP-01b`)

A coleta investiga se a densidade de nós e painéis gera hesitação ou demanda auxílio para encontrar a formatura estimada e matérias críticas (`H-OP-01`).

### 3.1 Amostra e Ética
- **Amostra:** Mínimo de 5 estudantes da UnB em diferentes fases do curso (calouro, meio, formando e aluno com reprovações).
- **Consentimento:** Informar que a avaliação recai sobre a interface do software, garantindo sigilo e anonimato.

### 3.2 Roteiro das Tarefas
- **T1 (Previsão de Formatura):**
  > _"Navegue até a tela de planejamento de formatura e informe o semestre estimado de formatura e quantos semestres restam."_
- **T2 (Matérias Críticas):**
  > _"Na tela de planejamento, identifique quais matérias são destacadas como 'críticas' e em qual semestre futuro estão alocadas."_
- **T3 (Ajuste de Créditos):**
  > _"Altere o limite para 20 créditos por semestre e solicite a atualização do planejamento."_

### 3.3 Planilha de Registro de Usabilidade

| ID | Perfil | T1 (Previsão) | T2 (Críticas) | T3 (Créditos) | Tempo Total | Observações e Hesitações (Evidência `H-OP-01`) |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **P01** | Concluinte | [1 = Autônomo / 0 = Ajuda ou Falha] | [1 / 0] | [1 / 0] | __ min | [Relato de dúvidas] |
| **P02** | Meio de curso | [1 / 0] | [1 / 0] | [1 / 0] | __ min | [...] |
| **P03** | Reprovações | [1 / 0] | [1 / 0] | [1 / 0] | __ min | [...] |
| **P04** | Iniciante (2º sem.) | [1 / 0] | [1 / 0] | [1 / 0] | __ min | [...] |
| **P05** | Formando | [1 / 0] | [1 / 0] | [1 / 0] | __ min | [...] |

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
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Simplificação textual e concisão mantendo fidelidade ao protocolo experimental ISO 25040 | 24/10 | [corrente] |

