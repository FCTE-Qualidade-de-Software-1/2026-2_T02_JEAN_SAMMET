# Matriz Geral de Rastreabilidade

Esta página centraliza a **rastreabilidade bidirecional completa** da avaliação **EC-01**, conectando cada elemento da estrutura **GQM** ao processo **SQuaRE** (Fases 1 a 4). Cada identificador da Tabela 1 é um link direto para a definição, o procedimento, a evidência ou a análise correspondente, permitindo percorrer a avaliação tanto da origem para o resultado quanto no sentido inverso.

---

## 1. Arquitetura de rastreabilidade

A Figura 1 apresenta o encadeamento entre os artefatos das quatro fases.

```mermaid
flowchart LR
    F1["Fase 1<br/>Características (ISO 25010)"]
    F2O["Fase 2<br/>Objetivos GQM"]
    F2H["Fase 2<br/>Hipóteses e Questões"]
    F2M["Fase 2<br/>Fichas das 12 Métricas"]
    F3["Fase 3<br/>Casos CT-01–CT-07 e Métodos"]
    F4D["Fase 4<br/>Dados Brutos e Evidências"]
    F4A["Fase 4<br/>Análise, M-01 e Conclusão"]

    F1 <--> F2O
    F2O <--> F2H
    F2H <--> F2M
    F2M <--> F3
    F3 <--> F4D
    F4D <--> F4A
```

*Figura 1 — Fluxo bidirecional entre as Fases 1 e 4. Fonte: elaboração da equipe.*

---

## 2. Matriz única GQM e SQuaRE

A Tabela 1 reúne, em uma única visão, os **dois objetivos**, **três características**, **nove hipóteses**, **nove questões** e **doze métricas** da avaliação.

**Tabela 1 — Matriz geral de rastreabilidade (Fases 1 a 4).**

| Característica (Fase 1) | Objetivo (Fase 2) | Hipótese (Fase 2) | Questão (Fase 2) | Métrica (Fase 2) | Procedimento (Fase 3) | Evidência (Fase 4) | Resultado da Métrica (Fase 4) | Resposta GQM e Ação (Fase 4) |
| :--- | :---: | :---: | :---: | :--- | :---: | :---: | :--- | :--- |
| [Adequação Funcional](fases/fase1/modeloDeQualidade.md) | [`OBJ-FUN`](fases/fase2/funcionais/GQM.md#1-objetivo-da-avaliacao) | [`H-FUN-01`](fases/fase2/funcionais/GQM.md#3-hipoteses-perguntas-e-metricas) | [`Q-FUN-01`](fases/fase2/funcionais/GQM.md#3-hipoteses-perguntas-e-metricas) | [`MET-FUN-01` (TVP)](fases/fase2/funcionais/GQM.md#met-fun-01-violacoes-de-pre-requisitos) | [`CT-01`](fases/fase3/funcionais/roteiro.md#ct-01-pre-requisitos-met-fun-01) | [Dados `CT-01`](fases/fase4/funcionais/dadosBrutos.md#ct-01-pre-requisitos) | [0,00% (Conforme)](fases/fase4/funcionais/analiseResultados.md#1-metricas-e-cobertura) | [Resposta `Q-FUN-01`](fases/fase4/funcionais/analiseResultados.md#q-fun-01-o-plano-respeita-os-pre-requisitos-oficiais) · [Fechamento](fases/fase4/rastreabilidade.md#q-fun-01-pre-requisitos) |
| [Adequação Funcional](fases/fase1/modeloDeQualidade.md) | [`OBJ-FUN`](fases/fase2/funcionais/GQM.md#1-objetivo-da-avaliacao) | [`H-FUN-02`](fases/fase2/funcionais/GQM.md#3-hipoteses-perguntas-e-metricas) | [`Q-FUN-02`](fases/fase2/funcionais/GQM.md#3-hipoteses-perguntas-e-metricas) | [`MET-FUN-02` (TVC)](fases/fase2/funcionais/GQM.md#met-fun-02-violacoes-de-co-requisitos) | [`CT-02`](fases/fase3/funcionais/roteiro.md#ct-02-co-requisitos-met-fun-02) | [Dados `CT-02`](fases/fase4/funcionais/dadosBrutos.md#ct-02-co-requisitos) | [0,00% (Conforme)](fases/fase4/funcionais/analiseResultados.md#1-metricas-e-cobertura) | [Resposta `Q-FUN-02`](fases/fase4/funcionais/analiseResultados.md#q-fun-02-o-plano-respeita-os-co-requisitos-oficiais) · [Fechamento](fases/fase4/rastreabilidade.md#q-fun-02-co-requisitos) |
| [Adequação Funcional](fases/fase1/modeloDeQualidade.md) | [`OBJ-FUN`](fases/fase2/funcionais/GQM.md#1-objetivo-da-avaliacao) | [`H-FUN-03`](fases/fase2/funcionais/GQM.md#3-hipoteses-perguntas-e-metricas) | [`Q-FUN-03`](fases/fase2/funcionais/GQM.md#3-hipoteses-perguntas-e-metricas) | [`MET-FUN-03` (CDO)](fases/fase2/funcionais/GQM.md#met-fun-03-cobertura-de-disciplinas-obrigatorias-pendentes) | [`CT-03`](fases/fase3/funcionais/roteiro.md#ct-03-obrigatorias-pendentes-met-fun-03) | [Dados `CT-03`](fases/fase4/funcionais/dadosBrutos.md#ct-03-obrigatorias-pendentes) | [93,33% (Não conforme)](fases/fase4/funcionais/analiseResultados.md#1-metricas-e-cobertura) | [Resposta `Q-FUN-03`](fases/fase4/funcionais/analiseResultados.md#q-fun-03-todas-as-disciplinas-obrigatorias-pendentes-aplicaveis-sao-contempladas) · [Rec. Alta](fases/fase4/conclusao.md#3-recomendacoes-finais) |
| [Adequação Funcional](fases/fase1/modeloDeQualidade.md) | [`OBJ-FUN`](fases/fase2/funcionais/GQM.md#1-objetivo-da-avaliacao) | [`H-FUN-04`](fases/fase2/funcionais/GQM.md#3-hipoteses-perguntas-e-metricas) | [`Q-FUN-04`](fases/fase2/funcionais/GQM.md#3-hipoteses-perguntas-e-metricas) | [`MET-FUN-04` (TDH)](fases/fase2/funcionais/GQM.md#met-fun-04-divergencias-no-tratamento-do-historico) | [`CT-04`](fases/fase3/funcionais/roteiro.md#ct-04-tratamento-do-historico-met-fun-04) | [Dados `CT-04`](fases/fase4/funcionais/dadosBrutos.md#ct-04-tratamento-do-historico) | [0,00% (Conforme)](fases/fase4/funcionais/analiseResultados.md#1-metricas-e-cobertura) | [Resposta `Q-FUN-04`](fases/fase4/funcionais/analiseResultados.md#q-fun-04-o-historico-e-os-status-sao-interpretados-conforme-as-regras-documentadas) · [Fechamento](fases/fase4/rastreabilidade.md#q-fun-04-interpretacao-do-historico) |
| [Adequação Funcional](fases/fase1/modeloDeQualidade.md) | [`OBJ-FUN`](fases/fase2/funcionais/GQM.md#1-objetivo-da-avaliacao) | [`H-FUN-05`](fases/fase2/funcionais/GQM.md#3-hipoteses-perguntas-e-metricas) | [`Q-FUN-05`](fases/fase2/funcionais/GQM.md#3-hipoteses-perguntas-e-metricas) | [`MET-FUN-05` (TAE)](fases/fase2/funcionais/GQM.md#met-fun-05-aplicacao-incorreta-de-equivalencias) | [`CT-05`](fases/fase3/funcionais/roteiro.md#ct-05-equivalencias-met-fun-05-apoio-a-met-fun-03) | [Dados `CT-05`](fases/fase4/funcionais/dadosBrutos.md#ct-05-equivalencias) | [0,00% (Conforme)](fases/fase4/funcionais/analiseResultados.md#1-metricas-e-cobertura) | [Resposta `Q-FUN-05`](fases/fase4/funcionais/analiseResultados.md#q-fun-05-as-equivalencias-respeitam-a-fonte-curricular-e-sua-vigencia) · [Fechamento](fases/fase4/rastreabilidade.md#q-fun-05-equivalencias) |
| [Adequação Funcional](fases/fase1/modeloDeQualidade.md) | [`OBJ-FUN`](fases/fase2/funcionais/GQM.md#1-objetivo-da-avaliacao) | [`H-FUN-06`](fases/fase2/funcionais/GQM.md#3-hipoteses-perguntas-e-metricas) | [`Q-FUN-06`](fases/fase2/funcionais/GQM.md#3-hipoteses-perguntas-e-metricas) | [`MET-FUN-06` (COO)](fases/fase2/funcionais/GQM.md#met-fun-06-conformidade-das-opcoes-do-onboarding) | [`CT-06`](fases/fase3/funcionais/roteiro.md#ct-06-onboarding-met-fun-06) | [Dados `CT-06`](fases/fase4/funcionais/dadosBrutos.md#ct-06-onboarding) | [71,43% (Não conforme)](fases/fase4/funcionais/analiseResultados.md#1-metricas-e-cobertura) | [Resposta `Q-FUN-06`](fases/fase4/funcionais/analiseResultados.md#q-fun-06-o-onboarding-produz-o-comportamento-documentado-ou-prometido) · [Rec. Média](fases/fase4/conclusao.md#3-recomendacoes-finais) |
| [Adequação Funcional](fases/fase1/modeloDeQualidade.md) | [`OBJ-FUN`](fases/fase2/funcionais/GQM.md#1-objetivo-da-avaliacao) | [`H-FUN-07`](fases/fase2/funcionais/GQM.md#3-hipoteses-perguntas-e-metricas) | [`Q-FUN-07`](fases/fase2/funcionais/GQM.md#3-hipoteses-perguntas-e-metricas) | [`MET-FUN-07` (TVS)](fases/fase2/funcionais/GQM.md#met-fun-07-violacoes-de-restricoes-semestrais) | [`CT-07`](fases/fase3/funcionais/roteiro.md#ct-07-restricoes-semestrais-met-fun-07) | [Dados `CT-07`](fases/fase4/funcionais/dadosBrutos.md#ct-07-restricoes-semestrais) | [0% / 10% / 33,33%](fases/fase4/funcionais/analiseResultados.md#1-metricas-e-cobertura) | [Resposta `Q-FUN-07`](fases/fase4/funcionais/analiseResultados.md#q-fun-07-o-plano-respeita-oferta-semestre-inicial-e-limites-de-carga-verificaveis) · [Rec. Alta](fases/fase4/conclusao.md#3-recomendacoes-finais) |
| [Usabilidade](fases/fase1/modeloDeQualidade.md) | [`OBJ-OP`](fases/fase2/operacionais/visaoGeral.md#31-objetivo-geral-de-medicao-nivel-conceitual) | [`H-OP-01`](fases/fase2/operacionais/visaoGeral.md#2-hipoteses-operacionais-e-matriz-de-validacao) | [`Q-OP-01`](fases/fase2/operacionais/visaoGeral.md#32-questoes-de-medicao-nivel-operacional) | [`MET-OP-01` (TCH)](fases/fase2/operacionais/usabilidade.md#met-op-01-taxa-de-conformidade-heuristica-tch) | [Inspeção `T1–T3`](fases/fase3/operacionais/metodos.md#1-usabilidade-tch-e-isvh) | [Dados Usab.](fases/fase4/operacionais/dadosBrutos.md#2-usabilidade) | [80% → 100% (M-01)](fases/fase4/operacionais/analiseResultados.md#11-tch-taxa-de-conformidade-heuristica) | [Resposta `Q-OP-01`](fases/fase4/operacionais/analiseResultados.md#q-op-01-a-interface-da-tela-de-planejamento-atende-as-heuristicas-ergonomicas-de-usabilidade-essenciais-para-operacao-e-apreensao-autonoma) · [Melhoria `M-01`](fases/fase4/operacionais/acaoMelhoria.md) |
| [Usabilidade](fases/fase1/modeloDeQualidade.md) | [`OBJ-OP`](fases/fase2/operacionais/visaoGeral.md#31-objetivo-geral-de-medicao-nivel-conceitual) | [`H-OP-01`](fases/fase2/operacionais/visaoGeral.md#2-hipoteses-operacionais-e-matriz-de-validacao) | [`Q-OP-01`](fases/fase2/operacionais/visaoGeral.md#32-questoes-de-medicao-nivel-operacional) | [`MET-OP-01b` (ISVH)](fases/fase2/operacionais/usabilidade.md#met-op-01b-indice-de-severidade-de-violacoes-heuristicas-isvh) | [Inspeção `T1–T3`](fases/fase3/operacionais/metodos.md#1-usabilidade-tch-e-isvh) | [Dados Usab.](fases/fase4/operacionais/dadosBrutos.md#2-usabilidade) | [4 → 0 pts (M-01)](fases/fase4/operacionais/analiseResultados.md#12-isvh-indice-de-severidade-de-violacoes-heuristicas) | [Resposta `Q-OP-01`](fases/fase4/operacionais/analiseResultados.md#q-op-01-a-interface-da-tela-de-planejamento-atende-as-heuristicas-ergonomicas-de-usabilidade-essenciais-para-operacao-e-apreensao-autonoma) · [Melhoria `M-01`](fases/fase4/operacionais/acaoMelhoria.md) |
| [Segurança](fases/fase1/modeloDeQualidade.md) | [`OBJ-OP`](fases/fase2/operacionais/visaoGeral.md#31-objetivo-geral-de-medicao-nivel-conceitual) | [`H-OP-02`](fases/fase2/operacionais/visaoGeral.md#2-hipoteses-operacionais-e-matriz-de-validacao) | [`Q-OP-02`](fases/fase2/operacionais/visaoGeral.md#32-questoes-de-medicao-nivel-operacional) | [`MET-OP-02` (IRP)](fases/fase2/operacionais/seguranca.md#met-op-02-indice-de-risco-ponderado-de-dependencias-irp) | [Dependências `INV-01`](fases/fase3/operacionais/metodos.md#2-dependencias-irp) | [Dados `INV-01`](fases/fase4/operacionais/dadosBrutos.md#3-dependencias-inventario-inv-01) | [3 pts (Excelente)](fases/fase4/operacionais/analiseResultados.md#21-irp-indice-de-risco-ponderado-de-dependencias) | [Resposta `Q-OP-02`](fases/fase4/operacionais/analiseResultados.md#q-op-02-o-sistema-protege-os-dados-academicos-e-os-servicos-examinados-contra-exposicao-no-cliente-vulnerabilidades-conhecidas-e-acesso-nao-autorizado) · [Rec. Média](fases/fase4/conclusao.md#3-recomendacoes-finais) |
| [Segurança](fases/fase1/modeloDeQualidade.md) | [`OBJ-OP`](fases/fase2/operacionais/visaoGeral.md#31-objetivo-geral-de-medicao-nivel-conceitual) | [`H-OP-02`](fases/fase2/operacionais/visaoGeral.md#2-hipoteses-operacionais-e-matriz-de-validacao) | [`Q-OP-02`](fases/fase2/operacionais/visaoGeral.md#32-questoes-de-medicao-nivel-operacional) | [`MET-OP-02b` (GED-C)](fases/fase2/operacionais/seguranca.md#met-op-02b-grau-de-exposicao-de-dados-no-cliente-ged-c) | [Storage `E0–E2`](fases/fase3/operacionais/metodos.md#3-armazenamento-ged-c) | [Dados Storage](fases/fase4/operacionais/dadosBrutos.md#4-armazenamento-ged-c) | [3 chaves (Não conforme)](fases/fase4/operacionais/analiseResultados.md#22-ged-c-grau-de-exposicao-de-dados-no-cliente) | [Resposta `Q-OP-02`](fases/fase4/operacionais/analiseResultados.md#q-op-02-o-sistema-protege-os-dados-academicos-e-os-servicos-examinados-contra-exposicao-no-cliente-vulnerabilidades-conhecidas-e-acesso-nao-autorizado) · [Rec. Alta](fases/fase4/conclusao.md#3-recomendacoes-finais) |
| [Segurança](fases/fase1/modeloDeQualidade.md) | [`OBJ-OP`](fases/fase2/operacionais/visaoGeral.md#31-objetivo-geral-de-medicao-nivel-conceitual) | [`H-OP-02`](fases/fase2/operacionais/visaoGeral.md#2-hipoteses-operacionais-e-matriz-de-validacao) | [`Q-OP-02`](fases/fase2/operacionais/visaoGeral.md#32-questoes-de-medicao-nivel-operacional) | [`MET-OP-02c` (TBR)](fases/fase2/operacionais/seguranca.md#met-op-02c-taxa-de-bloqueio-de-requisicoes-nao-autorizadas-tbr) | [Controle de Acesso](fases/fase3/operacionais/metodos.md#4-acesso-tbr) | [Dados API](fases/fase4/operacionais/dadosBrutos.md#5-controle-de-acesso-bateria-de-dez-condicoes) | [100% (Conforme)](fases/fase4/operacionais/analiseResultados.md#23-tbr-taxa-de-bloqueio-de-requisicoes-nao-autorizadas) | [Resposta `Q-OP-02`](fases/fase4/operacionais/analiseResultados.md#q-op-02-o-sistema-protege-os-dados-academicos-e-os-servicos-examinados-contra-exposicao-no-cliente-vulnerabilidades-conhecidas-e-acesso-nao-autorizado) · [Fechamento](fases/fase4/rastreabilidade.md#q-op-02-seguranca) |

*Fonte: elaboração da equipe, consolidando a estrutura GQM (Fase 2) e o processo SQuaRE (Fases 1 a 4).*

---

## 3. Artefatos transversais por fase

A Tabela 2 reúne os documentos estruturantes que dão suporte ao conjunto das 12 métricas.

**Tabela 2 — Artefatos transversais da avaliação.**

| Fase | Artefatos principais |
| :--- | :--- |
| **Fase 1 — Requisitos** | [Propósito e Stakeholders](fases/fase1/propositoEStakeholders.md) · [Software Escolhido](fases/fase1/softwareEscolhido.md) · [Modelo de Qualidade](fases/fase1/modeloDeQualidade.md) · [Características e Priorização](fases/fase1/caracteristicasDeQualidade.md) · [Escopo](fases/fase1/escopo.md) |
| **Fase 2 — Especificação (GQM)** | [GQM Funcional](fases/fase2/funcionais/GQM.md) · [GQM Operacional](fases/fase2/operacionais/visaoGeral.md) · [Fichas de Usabilidade](fases/fase2/operacionais/usabilidade.md) · [Fichas de Segurança](fases/fase2/operacionais/seguranca.md) |
| **Fase 3 — Projeto da Avaliação** | [Plano Integrado](fases/fase3/planoAvaliacao.md) · [Piloto e Prontidão](fases/fase3/piloto.md) · [Cronograma](fases/fase3/cronograma.md) · [Planejamento e Cobertura](fases/fase3/operacionais/rastreabilidade.md) · [Fontes e Regras](fases/fase3/funcionais/fontes.md) · [Roteiro do Avaliador](fases/fase3/operacionais/roteiroAvaliador.md) |
| **Fase 4 — Execução e Conclusão** | [Conclusão da Avaliação](fases/fase4/conclusao.md) · [Consolidação das Respostas](fases/fase4/rastreabilidade.md) · [Consolidado Funcional](fases/fase4/metricasFuncionais.md) · [Consolidado Operacional](fases/fase4/metricasOperacionais.md) · [Ação de Melhoria M-01](fases/fase4/operacionais/acaoMelhoria.md) · [Protótipo Interativo](https://gotc2607.github.io/Prot-tipo-JEAN-SAMMET/) |

*Fonte: elaboração da equipe.*

---

## 4. Referências

- BASILI, Victor R.; CALDIERA, Gianluigi; ROMBACH, H. Dieter. **The Goal Question Metric Approach**. *Encyclopedia of Software Engineering*, John Wiley & Sons, v. 2, p. 528-532, 1994. Disponível em: <https://ntrs.nasa.gov/citations/19940026214>.
- INTERNATIONAL ORGANIZATION FOR STANDARDIZATION. **ISO/IEC 25010:2011**: Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models. Genebra: ISO, 2011.
- INTERNATIONAL ORGANIZATION FOR STANDARDIZATION. **ISO/IEC 25040:2011**: Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Evaluation process. Genebra: ISO, 2011.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Criação da Matriz Geral de Rastreabilidade unificada para toda a estrutura GQM e SQuaRE | 23/11 | [0b37cf6](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/0b37cf68e64f7e1d9021604848841415f141a2ae) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Inclusão do link do protótipo interativo nos artefatos transversais da Fase 4 | 23/11 | [0ac2041](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/0ac2041a2ea30b37f9e4afc2ade46f5a1564c37b) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Separação explícita de colunas com links diretos para os resultados das 12 métricas e respostas das 9 questões GQM | 24/11 | [8f30292](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/8f302921912ed18ed6f6a18507c2bbab654f3366) |

