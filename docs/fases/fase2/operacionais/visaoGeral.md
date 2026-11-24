# Visão Geral e Estrutura GQM — Métricas Operacionais

Documento introdutório da avaliação de **Métricas Operacionais** da funcionalidade _Planejar formatura_ do No Fluxo UnB, cobrindo **Usabilidade** e **Segurança**.

---

## 1. Contexto e Rastreabilidade com a Fase 1

As métricas operacionais derivam das definições da Fase 1:

- **Partes Interessadas ([Propósito e Stakeholders](../../fase1/propositoEStakeholders.md)):**
  - *Estudantes:* precisam de interface clara para entender a formatura estimada e autonomia para ajustar créditos, com proteção aos seus dados pessoais.
  - *Mantenedores (Crianex):* necessitam de indicadores sobre facilidade de uso e segurança contra vulnerabilidades em dependências ou rotas desprotegidas.
  - *Equipe avaliadora:* requer evidências reprodutíveis para embasar melhorias na Fase 4.
- **Priorização ([Características de Qualidade](../../fase1/caracteristicasDeQualidade.md)):**
  - *Adequação Funcional:* Prioridade 1 (20 pts) — avaliada em [Métricas Funcionais](../funcionais/visaoGeral.md).
  - *Segurança:* Prioridade 2 (15 pts) — Confidencialidade e autenticidade, com inspeção complementar de dependências.
  - *Usabilidade:* Prioridade 3 (12 pts) — Operabilidade e Apreensibilidade.
- **Escopo e Limites ([Escopo](../../fase1/escopo.md)):**
  - Foco na interface SvelteKit (`/plano-formatura`), armazenamento no cliente (`localStorage`), endpoint `POST /planejamento/gerar-plano` e dependências via Retire.js no cliente e, quando disponíveis, manifestos públicos via `npm audit`.
  - Exclui testes invasivos/destrutivos; uso de dados autorizados, com evidências sanitizadas.

---

## 2. Hipóteses Operacionais e Matriz de Validação

Formuladas a partir das limitações levantadas na Fase 1 ([Software Escolhido](../../fase1/softwareEscolhido.md#8-limitacoes-conhecidas)):

**Tabela 1 — Hipóteses Operacionais e Matriz de Validação.**

| ID | Característica | Hipótese Documentada | Questão GQM | Métricas de Teste | Critério de Validação da Hipótese |
| :---: | :--- | :--- | :---: | :--- | :--- |
| **H-OP-01** | Usabilidade | A interface apresenta violações heurísticas relevantes nas tarefas avaliadas. | [`Q-OP-01`](#32-questoes-de-medicao-nivel-operacional) | [TCH](usabilidade.md#met-op-01-taxa-de-conformidade-heuristica-tch) e [ISVH](usabilidade.md#met-op-01b-indice-de-severidade-de-violacoes-heuristicas-isvh) | Confirmada no recorte se `TCH < 85%` ou houver violação maior/catastrófica; caso contrário, não corroborada, com coleta completa. |
| **H-OP-02** | Segurança | Dependências vulneráveis, retenção de dados em claro ou falhas de controle de acesso podem comprometer os dados e serviços examinados. | [`Q-OP-02`](#32-questoes-de-medicao-nivel-operacional) | [IRP](seguranca.md#met-op-02-indice-de-risco-ponderado-de-dependencias-irp), [GED-C](seguranca.md#met-op-02b-grau-de-exposicao-de-dados-no-cliente-ged-c) e [TBR](seguranca.md#met-op-02c-taxa-de-bloqueio-de-requisicoes-nao-autorizadas-tbr) | Julgar os componentes separadamente e aplicar a regra conjunta abaixo. |

*Fonte: elaboração da equipe, conforme os registros e referências desta página.*

### 2.1 Qualidade dos dados

Dados ausentes, erros de coleta e testes que não alcançam o serviço esperado são inconclusivos. Itens sem requisito aplicável recebem Não aplicável, com justificativa. Nenhum desses estados equivale a aprovação.

### 2.2 Regra de julgamento conjunto

**Tabela 2 — Regra de julgamento conjunto.**

| Questão | Regra de resposta |
| --- | --- |
| **Q-OP-01** | Classificar TCH e ISVH pelas fichas e adotar o pior nível. Usar Inconclusivo se a coleta não cumprir o protocolo. H-OP-01 pode ser confirmada mesmo no nível Aceitável, pois seu limiar é mais exigente. |
| **Q-OP-02** | Há ressalva de segurança se algum componente estiver fora da meta; indicar qual. Só responder favoravelmente quando todos os componentes aplicáveis tiverem dados válidos e atenderem às metas: IRP Excelente, GED-C Conforme e TBR Conforme. Se houver componentes inconclusivos, a resposta global permanece parcial. |

*Fonte: elaboração da equipe, conforme os registros e referências desta página.*

H-OP-02 é confirmada no componente com IRP válido acima de 5 ou classificado Crítico, GED-C não conforme ou acesso indevido comprovado. Os demais componentes continuam com seus próprios estados. Sem esses achados e com cobertura completa, registrar **não corroborada no escopo avaliado**; com lacunas, registrar **inconclusiva**. Não usar uma medida favorável para refutar toda a hipótese.

---

## 3. Estrutura GQM (Goal-Question-Metric)

### 3.1 Objetivo Geral de Medição (Nível Conceitual)

**Tabela 3 — Objetivo Geral de Medição (Nível Conceitual).**

| Elemento GQM | Especificação Formal |
| :--- | :--- |
| **Objeto** | A funcionalidade _Planejar formatura_ (interface web, armazenamento cliente e dependências) do No Fluxo UnB. |
| **Propósito** | **Avaliar** |
| **Foco de Qualidade** | **Usabilidade** e **Segurança** (ISO/IEC 25010). |
| **Ponto de Vista** | **equipe de desenvolvedores**. |
| **Contexto** | Ambiente web desktop controlado, currículo de Engenharia de Software da FGA/UnB, histórico oficial autorizado e inspeção dos componentes disponíveis. |
| **Questões associadas** | [`Q-OP-01` (Usabilidade) e `Q-OP-02` (Segurança)](#32-questoes-de-medicao-nivel-operacional) |
| **Características associadas** | [Usabilidade e Segurança (Fase 1)](../../fase1/modeloDeQualidade.md) |
| **Matriz de rastreabilidade** | [Matriz Geral](../../../rastreabilidade.md) |

*Fonte: elaboração da equipe, conforme os registros e referências desta página.*

### 3.2 Questões de Medição (Nível Operacional)

| Objetivo associado | Questão | Enunciado | Hipótese associada | Métricas associadas |
| :---: | :---: | :--- | :---: | :--- |
| [`OBJ-OP`](#31-objetivo-geral-de-medicao-nivel-conceitual) | `Q-OP-01` | A interface da tela de planejamento atende às heurísticas ergonômicas de usabilidade essenciais para operação e apreensão autônoma? | [`H-OP-01`](#2-hipoteses-operacionais-e-matriz-de-validacao) | [`MET-OP-01` (TCH)](usabilidade.md#met-op-01-taxa-de-conformidade-heuristica-tch) · [`MET-OP-01b` (ISVH)](usabilidade.md#met-op-01b-indice-de-severidade-de-violacoes-heuristicas-isvh) |
| [`OBJ-OP`](#31-objetivo-geral-de-medicao-nivel-conceitual) | `Q-OP-02` | O sistema protege os dados acadêmicos e os serviços examinados contra exposição no cliente, vulnerabilidades conhecidas e acesso não autorizado? | [`H-OP-02`](#2-hipoteses-operacionais-e-matriz-de-validacao) | [`MET-OP-02` (IRP)](seguranca.md#met-op-02-indice-de-risco-ponderado-de-dependencias-irp) · [`MET-OP-02b` (GED-C)](seguranca.md#met-op-02b-grau-de-exposicao-de-dados-no-cliente-ged-c) · [`MET-OP-02c` (TBR)](seguranca.md#met-op-02c-taxa-de-bloqueio-de-requisicoes-nao-autorizadas-tbr) |

### 3.3 Árvore GQM com Hipóteses Operacionais

A Figura 1 apresenta o diagrama desta seção.

```mermaid
graph TD
    Goal["Objetivo GQM Operacional:<br/>Avaliar Usabilidade e Segurança da funcionalidade Planejar Formatura"]

    Goal --> H1["<b>Hipótese H-OP-01</b>:<br/>Violações heurísticas comprometem a operabilidade e a apreensão"]
    Goal --> H2["<b>Hipótese H-OP-02</b>:<br/>Dependências, armazenamento e acesso podem comprometer dados e serviços"]

    H1 --> Q1["Q-OP-01: A interface atende às heurísticas ergonômicas de usabilidade?"]
    H2 --> Q2["Q-OP-02: O sistema resguarda a confidencialidade e restringe o acesso contra vulnerabilidades?"]

    Q1 --> M1["MET-OP-01: Taxa de Conformidade Heurística (TCH)<br/><i>Usabilidade / Operabilidade</i>"]
    Q1 --> M1b["MET-OP-01b: Índice de Severidade de Violações Heurísticas (ISVH)<br/><i>Usabilidade / Apreensibilidade</i>"]

    Q2 --> M2["MET-OP-02: Índice de Risco Ponderado de Dependências (IRP)<br/><i>Segurança / Evidência complementar</i>"]
    Q2 --> M2b["MET-OP-02b: Grau de Exposição de Dados no Cliente (GED-C)<br/><i>Segurança / Confidencialidade</i>"]
    Q2 --> M2c["MET-OP-02c: Taxa de Bloqueio em Rotas Não Autenticadas (TBR)<br/><i>Segurança / Controle de Acesso</i>"]
```

*Figura 1 — Árvore GQM com Hipóteses Operacionais. Fonte: elaboração da equipe, conforme as referências desta página.*

---

## 4. Organização das Páginas Operacionais

**Tabela 4 — Organização das Páginas Operacionais.**

| Seção / Página | Foco e Conteúdo Principal | Hipótese | Métricas |
| :--- | :--- | :---: | :---: |
| **[1. Métricas de Usabilidade](usabilidade.md)** | Checklist heurístico (Nielsen), tarefas de referência (`T1`, `T2` e `T3`), operabilidade e apreensibilidade. | `H-OP-01` | `MET-OP-01`<br>`MET-OP-01b` |
| **[2. Métricas de Segurança](seguranca.md)** | Auditoria SCA, persistência no cliente, controle de acesso e referências OWASP e proteção de dados. | `H-OP-02` | `MET-OP-02`<br>`MET-OP-02b`<br>`MET-OP-02c` |
| **[3. Protocolo de Coleta e Teste](protocolo.md)** | Roteiro de inspeção heurística da equipe, fichas de ambiente, storage e SCA. | `H-OP-01`<br>`H-OP-02` | Todas |
| **[4. Referências](referencias.md)** | Referências metodológicas, normas técnicas (ISO/IEC e ISO 9241), OWASP e LGPD. | — | Todas |

*Fonte: elaboração da equipe, conforme os registros e referências desta página.*

---

## 5. Integração com as Métricas Funcionais

A avaliação adota abordagem holística, cruzando dados operacionais e funcionais ([Métricas Funcionais](../funcionais/visaoGeral.md)):

A Figura 2 apresenta o diagrama desta seção.

```mermaid
graph LR
    OP["Métricas Operacionais<br/>Usabilidade e Segurança"] <-->|"Validação Cruzada"| FN["Métricas Funcionais<br/>Regras Curriculares e Algoritmo"]
    OP --> DEC["Decisões de Melhoria (Fase 4)<br/>Interface intuitiva, dados seguros e planos válidos"]
    FN --> DEC
```

*Figura 2 — Integração com as Métricas Funcionais. Fonte: elaboração da equipe, conforme as referências desta página.*

- **Usabilidade × Adequação Funcional:** Interface intuitiva não compensa planos curriculares incorretos; da mesma forma, um plano correto não tem utilidade se a interface for incompreensível.
- **Segurança × Confiabilidade:** Relacionar achados de dependências e acesso aos riscos do fluxo, sem inferir confiabilidade ou conformidade legal apenas dessas medidas.

## 6. Referências

Referências usadas nesta página, conforme [Referências — Fase 2](../../../referencias/fase2.md) e [Referências — Fase 3](../../../referencias/fase3.md).

- BASILI, Victor R.; CALDIERA, Gianluigi; ROMBACH, H. Dieter. **The Goal Question Metric Approach**. *Encyclopedia of Software Engineering*, John Wiley & Sons, v. 2, p. 528-532, 1994. Disponível em: <https://ntrs.nasa.gov/citations/19940026214>.
- BRASIL. **Lei nº 13.709, de 14 de agosto de 2018**. Lei Geral de Proteção de Dados Pessoais (LGPD). Diário Oficial da União: seção 1, Brasília, DF, p. 59, 15 ago. 2018.
- INTERNATIONAL ORGANIZATION FOR STANDARDIZATION. **ISO 9241-11:2018**: Ergonomics of human-system interaction — Part 11: Usability: Definitions and concepts. Genebra: ISO, 2018.
- INTERNATIONAL ORGANIZATION FOR STANDARDIZATION. **ISO/IEC 25010:2011**: Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models. Genebra: ISO, 2011.
- NIELSEN, Jakob. **10 Usability Heuristics for User Interface Design**. Nielsen Norman Group, 1994. Disponível em: <https://www.nngroup.com/articles/ten-usability-heuristics/>.
- NIELSEN, Jakob. **Severity Ratings for Usability Problems**. Nielsen Norman Group, 1995. Disponível em: <https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/>. Acesso em: 14 nov. 2026.
- NPM, INC. **npm-audit**: documentation and command-line security auditing for Node.js packages. npm Docs, 2026. Disponível em: <https://docs.npmjs.com/cli/commands/npm-audit>.
- OWASP FOUNDATION. **OWASP Top 10: 2021** — The Ten Most Critical Web Application Security Risks. OWASP, 2021. Disponível em: <https://owasp.org/Top10/>.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Elaboração da visão geral, modelo GQM operacional, hipóteses e matriz de rastreabilidade | 16/10 | [b4e71a0](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/b4e71a0) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Remoção de referências a divisões internas de pessoas e padronização documental | 16/10 | [81912ba](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/81912bac5e02d7429e2d05446544ec9636891f5e) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Ajuste da estrutura GQM operacional para Usabilidade e Segurança | 16/10 | [3584382](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/3584382ccfb17e27db841b011ce415fa1503cbbc) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Simplificação textual e concisão mantendo coerência com GQM e ISO 25010 | 24/10 | [b31d87e](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/b31d87e) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Atualização de Usabilidade para Avaliação Heurística de Nielsen (TCH e ISVH) e inclusão na árvore GQM | 25/10 | [8330fa6](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/8330fa6ce8a670d083d8718eada13606616f064c) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Alinhamento das hipóteses e das regras de julgamento conjunto | 15/11 | [8d625c1](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/8d625c1a87436bf186efb0abffb6682e1916a3d5) |
| [Yasmim de Souza Santos](https://github.com/eii-yahs) | Inclusão das referências utilizadas na página | 22/11 | Não commitado |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Inclusão de links bidirecionais de rastreabilidade no objetivo e tabela de questões operacionais | 23/11 | [0b37cf6](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/0b37cf68e64f7e1d9021604848841415f141a2ae) |