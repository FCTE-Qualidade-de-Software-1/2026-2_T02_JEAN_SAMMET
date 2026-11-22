# Especificação da avaliação — Métricas funcionais

A avaliação usa o método **Goal-Question-Metric (GQM)** para verificar a adequação funcional de *Planejar formatura*, com foco no Motor 2. Os critérios e métricas estão detalhados em [GQM](GQM.md), e os cenários de coleta em [Protocolo de testes](testes.md).

O objetivo é identificar planos que contrariem regras curriculares, omitam disciplinas ou interpretem incorretamente o histórico e as opções informadas. Os resultados apoiam estudantes, coordenação acadêmica, equipe responsável pelo produto e avaliadores. Como o plano é uma estimativa e o No Fluxo UnB não é ferramenta oficial da UnB, a avaliação **não garante a formatura**.

## 1. Escopo e referência

**Tabela 1 — Escopo e referência.**

| Item | Definição |
| --- | --- |
| **Objeto** | Motor 2, em `backend/src/services/plano_formatura.service.ts`, chamado por `POST /planejamento/gerar-plano`. |
| **Versão** | Commit de referência `87b5475`, conforme documentação da Fase 1. |
| **Matriz prioritária** | Engenharia de Software da FGA/UnB, identificada como `6360/1` ou `2017.1` e descrita como inativa no sistema observado. Confirmar a matriz aplicável antes da coleta. |
| **Dados** | Históricos sintéticos ou dados autorizados e anonimizados. |
| **Entradas** | Histórico e status das disciplinas, matriz, pré/co-requisitos, equivalências, oferta de turmas e opções do onboarding. |
| **Saídas** | Disciplinas e semestres planejados, pendências/críticas, previsão de formatura e informações de integralização exibidas. |
| **Validade** | Conclusões limitadas aos cenários, dados, matriz, ambiente e versão registrados; o commit não comprova equivalência com a versão em produção. |

*Fonte: elaboração da equipe, conforme os registros e referências desta página.*

## 2. Hipóteses a verificar

Os itens a seguir são hipóteses registradas na Fase 1, não defeitos confirmados.

**Tabela 2 — Hipóteses a verificar.**

| Hipótese | Risco e verificação | Referência |
| --- | --- | --- |
| Trabalho/estágio e objetivo do onboarding podem não influenciar a seleção de disciplinas. | Confirmar o comportamento documentado antes de classificar uma diferença ou ausência de efeito como falha. | `MET-FUN-06` / `CT-06` |
| Disciplinas em andamento podem ser tratadas como aprovadas para semestres futuros. | Conferir a regra documentada e registrar o efeito no plano. | `MET-FUN-04` / `CT-04` |
| Uma lista vazia de disciplinas não alocadas pode coexistir com obrigatórias omitidas. | Comparar o plano com a lista completa de obrigatórias pendentes. | `MET-FUN-03` / `CT-03` |
| Uma disciplina pode ser alocada sem a co-requisitada. | Conferir os pares e a regra de satisfação oficial. | `MET-FUN-02` / `CT-02` |
| Equivalências podem ser expandidas em uma passagem e sem considerar a vigência. | Testar apenas relações e vigências respaldadas por fonte oficial. | `MET-FUN-05` / `CT-05` |
| Falha na consulta do período letivo pode levar à estimativa pela data do sistema. | Comparar o semestre usado com o calendário oficial. | `MET-FUN-07` / `CT-07` |

*Fonte: elaboração da equipe, conforme os registros e referências desta página.*

## 3. Referências

Referências usadas nesta página, conforme [Referências — Fase 2](../../../referencias/fase2.md).

- BASILI, Victor R.; CALDIERA, Gianluigi; ROMBACH, H. Dieter. **The Goal Question Metric Approach**. *Encyclopedia of Software Engineering*, John Wiley & Sons, v. 2, p. 528-532, 1994. Disponível em: <https://ntrs.nasa.gov/citations/19940026214>.
- NOFLUXO UNB. **2025-1-NoFluxoUnB**: serviço de planejamento de formatura (`backend/src/services/plano_formatura.service.ts` — Motor 2). GitHub, 2026. Commit de referência `87b5475`. Disponível em: <https://github.com/unb-mds/2025-1-NoFluxoUnB>.
- UNIVERSIDADE DE BRASÍLIA (UnB). **Projeto Pedagógico do Curso de Bacharelado em Engenharia de Software**. Faculdade UnB Gama (FGA). Matriz Curricular 6360/1 (Fluxo 2017.1), pré-requisitos, co-requisitos e regras de integralização curricular. Brasília: UnB/FGA, 2017.

---

## Histórico de versão

| Membro | Contribuição | Data | Commit |
|---|---|---|---|
| [Gabriel Mota](https://github.com/Gabro-MO) | Perguntas GQM, fichas de métricas e cenários iniciais. | 16/10 | [9306147](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/9306147e05a3017e02f9bedaf2c75a8287ef1c8b) |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Revisão do foco GQM e dos papéis da equipe. | 16/10 | [81912ba](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/81912bac5e02d7429e2d05446544ec9636891f5e) |
| [Gabriel Mota](https://github.com/Gabro-MO) | Divisão do documento em páginas. | 16/10 | [e60f42c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/e60f42cea76bd6f39f2c6069ecdbce438b4e941a) |
| [Yasmim de Souza Santos](https://github.com/eii-yahs) | Inclusão das referências utilizadas na página | 22/11 | Não commitado |