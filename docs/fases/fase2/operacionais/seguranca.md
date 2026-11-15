# Métricas de Segurança

Avaliação do armazenamento de dados acadêmicos, da identificação e do acesso aos serviços de *Planejar formatura*. A análise de dependências complementa as verificações do [modelo da Fase 1](../../fase1/modeloDeQualidade.md).

## 1. Questão e hipótese

- **Q-OP-02:** O sistema protege os dados acadêmicos e os serviços examinados contra exposição no cliente, vulnerabilidades conhecidas e acesso não autorizado?
- **H-OP-02:** Dependências vulneráveis, retenção de dados em claro ou falhas de controle de acesso podem comprometer os dados e serviços examinados.

Confidencialidade e autenticidade são as subcaracterísticas em foco. A inspeção de dependências é evidência complementar; não constitui uma subcaracterística adicional.

## 2. Fichas das métricas

### `MET-OP-02` — Índice de Risco Ponderado de Dependências (IRP)

| Campo | Especificação |
|---|---|
| **Característica** | Segurança — evidência complementar de riscos nos componentes. |
| **Questão e hipótese** | `Q-OP-02` e `H-OP-02`, componente dependências. |
| **Definição e unidade** | Soma ponderada dos achados de vulnerabilidade por severidade; unidade: pontos. |
| **Cálculo** | `IRP = 10 × Ncritica + 5 × Nalta + 2 × Nmoderada + Nbaixa`. Cada achado é identificado por componente, versão e aviso GHSA/CVE ou identificador da ferramenta, sem duplicatas dentro da mesma coleta. Não somar totais de ferramentas com coberturas sobrepostas. |
| **Fontes e cobertura** | Retire.js nos scripts públicos do cliente. Quando disponíveis, `npm audit --json` nos manifestos de frontend e backend do commit `87b5475`, com resultados separados. Registrar componentes e versões reconhecidos e a base de vulnerabilidades consultada. |
| **Coleta** | Preservar relatório bruto e inventário. Separar achados de produção e desenvolvimento quando essa distinção for verificável. Contagens agregadas de pacotes do npm não substituem a relação dos achados. |
| **Excelente** | Nenhuma crítica ou alta e `IRP ≤ 5`. |
| **Aceitável** | Fora da faixa Excelente: nenhuma crítica, até duas altas exclusivamente de desenvolvimento e `IRP ≤ 20`. |
| **Crítico** | Demais resultados válidos, incluindo crítica, alta em produção, mais de duas altas ou `IRP > 20`. |
| **Inconclusivo** | Relatório ausente, erro de ferramenta, cobertura não demonstrada ou dados insuficientes para aplicar as faixas. Nunca assumir zero por ausência de arquivo. |

As faixas e os pesos são critérios da equipe. Aplicar as faixas na ordem apresentada. Componentes não examinados, inclusive o backend em uma coleta apenas do cliente, permanecem sem avaliação. Achados de alta severidade sem classificação verificável de produção/desenvolvimento não permitem declarar a faixa Aceitável.

### `MET-OP-02b` — Grau de Exposição de Dados no Cliente (GED-C)

| Campo | Especificação |
|---|---|
| **Característica** | Segurança — confidencialidade. |
| **Questão e hipótese** | `Q-OP-02` e `H-OP-02`, componente armazenamento. |
| **Definição e unidade** | Número de chaves com identificadores ou dados acadêmicos em texto claro nos mecanismos inspecionados; unidade: chaves. |
| **Cálculo** | `GED-C = quantidade de chaves com matrícula, nome, notas, IRA ou histórico em claro`. Cada chave conta uma vez, identificada pelo mecanismo e origem. |
| **Fonte** | DevTools: `localStorage`, `sessionStorage` e cookies após carregar o histórico sintético e gerar o plano. |
| **Coleta** | Registrar estado do fluxo, origem, chaves, conteúdo sintético e evidências. Inspecionar cookies no painel Application; registrar `HttpOnly` e `Secure` separadamente. Essas flags não tornam o conteúdo cifrado. |
| **Conforme** | `GED-C = 0`, com inspeção completa dos mecanismos previstos. |
| **Não conforme** | `GED-C ≥ 1`, com conteúdo e estado do fluxo comprovados. |
| **Inconclusivo** | Fluxo não concluído, mecanismos não inspecionados ou evidência insuficiente. |

O resultado descreve o armazenamento observado; não comprova confidencialidade integral nem conformidade legal.

### `MET-OP-02c` — Taxa de Bloqueio de Requisições Não Autorizadas (TBR)

| Campo | Especificação |
|---|---|
| **Característica** | Segurança — autenticidade e controle de acesso. |
| **Questão e hipótese** | `Q-OP-02` e `H-OP-02`, componente acesso. |
| **Definição e unidade** | Percentual de chamadas negativas válidas bloqueadas com HTTP 401/403; unidade: percentual. |
| **Pré-condições** | Confirmar requisito de proteção, URL, método e payload. Verificar uma chamada positiva autorizada ao mesmo serviço, em ambiente autorizado. A rota `POST /planejamento/gerar-plano` é referência a confirmar, não prova da URL implantada. |
| **Cálculo** | `TBR = (Nbloqueadas / Nvalidas) × 100`. `Nvalidas` inclui chamadas ao serviço validado que permitam observar bloqueio ou execução indevida. Informar também total planejado, válido e inconclusivo. Se `Nvalidas = 0`, não calcular a taxa. |
| **Coleta** | Planejar ao menos dez casos negativos. Registrar data, alvo, status, cabeçalhos relevantes, resposta e comportamento observado. Para testar expiração ou papel insuficiente, usar credenciais de teste que isolem essa condição. |
| **Conforme** | `TBR = 100%`, com toda a bateria prevista concluída e válida. |
| **Não conforme** | Pelo menos uma chamada válida executa ação ou acessa dado que exigia autorização, sem a permissão necessária. Um HTTP 200 isolado não comprova esse acesso. |
| **Inconclusivo** | HTTP 404/405, erro de conexão, HTTP 500 sem evidência de acesso ou outro retorno que não permita avaliar o controle. `TBR = 100%` em apenas parte da bateria não autoriza aprovação global. |
| **Não aplicável** | O requisito documentado permite acesso público ao serviço e não há operação protegida no recorte. Justificar. |

## 3. Resposta à questão e julgamento da hipótese

Aplicar a [regra conjunta](visaoGeral.md#22-regra-de-julgamento-conjunto). Um resultado favorável de storage ou dependências não encerra a avaliação dos demais componentes. Ausência de achados significa apenas que a hipótese não foi corroborada naquele recorte.

## 4. Referências de segurança

As verificações usam OWASP Top 10:2021 como referência: A01 para controle de acesso e A06 para componentes vulneráveis. Os cuidados com dados pessoais seguem os limites do [escopo](../../fase1/escopo.md). As definições e fontes estão nas [referências operacionais](referencias.md); os testes não constituem auditoria de conformidade legal.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Elaboração da especificação de segurança, fichas MET-OP-02, MET-OP-02b e MET-OP-02c e alinhamento com OWASP/LGPD | 16/10 | [3584382](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/3584382ccfb17e27db841b011ce415fa1503cbbc) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Simplificação textual e concisão mantendo coerência com ISO 25010, OWASP e LGPD | 24/10 | [corrente] |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Correção das métricas, faixas e resultados inconclusivos de segurança | 15/11 | [8d625c1](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/8d625c1a87436bf186efb0abffb6682e1916a3d5) |
