# Estrutura do Artigo

Estrutura da 1ª versão do artigo (Entrega 1), com o conteúdo de cada seção e a página da GitPage de onde ele vem. O texto completo está em `latex/main.tex`.

---

## Título

Avaliação da Qualidade do Planejamento de Formatura do No Fluxo UnB: Requisitos e Especificação segundo a ISO/IEC 25040

## Autores e afiliação

- Ana Beatriz Souza Araujo, Giovani De Oliveira Teodoro Coelho, Yasmim de Souza Santos, Gabriel Mota Oliveira, Gustavo Gomes Fornaciari e Vitor Lages Nogueira Araújo
- Faculdade de Ciências e Tecnologias em Engenharia (FCTE), Universidade de Brasília (UnB)

## Abstract

## Resumo

- Contexto: estudantes da UnB usam ferramentas web para planejar as disciplinas
- Objeto: fluxo de planejamento de formatura do No Fluxo UnB
- Método: processo da ISO/IEC 25040 (SQuaRE), GQM para as medidas e PSM/CID para a gestão
- Produtos: requisitos da avaliação, modelo de qualidade adaptado da ISO/IEC 25010 (Adequação Funcional, Segurança e Usabilidade) e especificação com 2 objetivos, 9 questões e 12 métricas

---

## 1. Introdução

- Contexto e problema: planos com pré-requisitos ignorados, co-requisitos omitidos, obrigatórias ausentes ou histórico mal interpretado podem atrasar a graduação; o histórico pode conter dados pessoais
- Objeto: envio do histórico, renderização inicial do fluxograma atual e tela "Planejar formatura" (objeto central)
- Objetivo geral e objetivos específicos (i) a (iv); esta versão cobre (i) e (ii), ou seja, as Fases 1 e 2
- Abordagem: ISO/IEC 25040, GQM e PSM/CID
- Links do repositório e da GitPage
- Organização do artigo
- Origem: [Início](../docs/index.md), [Software Escolhido](../docs/fases/fase1/softwareEscolhido.md) e [Métricas Funcionais](../docs/fases/fase2/funcionais/visaoGeral.md)

## 2. Referencial Teórico

Origem: [Visão Geral da Metodologia](../docs/metodologia/visaoGeral.md) e [Referências](../docs/referencias/fase1.md)

### 2.1 Qualidade de produto de software e a família SQuaRE

- Divisões 2500n a 2504n; normas usadas: ISO/IEC 25010, 25020, 25023, 25030 e 25040

### 2.2 Modelo de qualidade da ISO/IEC 25010

- Oito características da edição de 2011
- Adequação Funcional, Segurança e Usabilidade e suas subcaracterísticas
- Edição de 2023 citada; o trabalho adota a de 2011

### 2.3 Processo de avaliação da ISO/IEC 25040

- Cinco atividades, agrupadas em quatro fases na disciplina

### 2.4 Método GQM

- Níveis conceitual, operacional e quantitativo; hipóteses

### 2.5 Medição para gestão de projetos: PSM/CID

- Modelo de informação (ISO/IEC/IEEE 15939), categorias de informação e medidas do CID

## 3. Metodologia de Desenvolvimento do Projeto

Origem: [Metodologia](../docs/metodologia/visaoGeral.md), [Processo](../docs/metodologia/processoSquare.md), [Fluxo de Trabalho](../docs/metodologia/fluxoDeTrabalho.md) e [Gestão do Projeto](../docs/gestaoProjeto/psm-cid.md)

### 3.1 Processo adotado

- Entrega 1 (26/10/2026): Fases 1 e 2; Entrega 2: Fases 3 e 4 e ação de melhoria
- Ciclo por entrega: planejamento, execução, revisão, integração e medições PSM/CID

### 3.2 Organização da equipe, ferramentas e artefatos

- Frentes da Entrega 1 em Issues e Milestone, cada uma com uma dupla
- Branch por tarefa, Pull Request com revisão, MkDocs Material, Mermaid e LaTeX no modelo SBC

### 3.3 Gestão do projeto com PSM/CID

- Origem das medidas: categorias do PSM (McGarry et al., 2001) e medidas do CID (PSM, 2021); limites definidos pela equipe
- Calendário e Progresso: TCT = Nconc / Nplanejado × 100; meta de 100% no prazo; alerta se TCT < 75% a 24 h do prazo
- Recursos e Custos: esforço em horas (Ee, Er), Ve = |Er − Ee| / Ee × 100 e custo equivalente com R$ 50,00/h (valor didático); meta Ve ≤ 10%; alerta se Ve > 20%
- Desempenho do Processo: TC médio de até 2 dias; alerta para Issues abertas sem atividade há mais de 3 dias; eventos que contam como atividade no TSA
- Esforço consolidado por consenso retroativo; scripts do repositório que calculam as medidas a cada publicação
- Resultados do Milestone 1: TCT de 100% (6 de 6), Er de 20,0 h ante 21,0 h estimadas (Ve de 4,76%), custo de R$ 1.000,00 ante R$ 1.050,00, TC médio de 3,0 dias, TSA de 0,0 dia; leitura do burndown
- Quatro decisões de gestão registradas
- Origem: [Calendário e Progresso](../docs/gestaoProjeto/calendario-progresso.md), [Recursos e Custos](../docs/gestaoProjeto/recursos-custos.md), [Desempenho do Processo](../docs/gestaoProjeto/desempenho-processo.md) e [Acompanhamento](../docs/gestaoProjeto/acompanhamento.md)

### 3.4 Rastreabilidade dos dados e aspectos éticos

- Dados versionados no repositório; históricos sintéticos ou autorizados
- Usabilidade por inspeção heurística da própria equipe, sem participantes externos
- Verificações de segurança não invasivas e não destrutivas

## 4. Fase 1 - Estabelecimento dos Requisitos da Avaliação

Origem: páginas da [Fase 1](../docs/fases/fase1/propositoEStakeholders.md)

### 4.1 Propósito da avaliação e uso pretendido

- Três decisões apoiadas: divergências funcionais, problemas observáveis de acesso ou exposição de dados e dificuldades de uso
- A avaliação não certifica o software

### 4.2 Requisitante e partes interessadas

- Tabela de partes interessadas: estudantes, mantenedores, Profa. Cristiane Ramos e equipe avaliadora
- Três perfis de estudante como cenários

### 4.3 Tipo de produto e descrição do software

- Aplicação web; estrutura do repositório no commit 87b5475; Motor 2 e rota `POST /planejamento/gerar-plano`
- Figura da tela "Planejar formatura" e diagrama de contexto (Figura 4 de [Software Escolhido](../docs/fases/fase1/softwareEscolhido.md))
- O que é e o que não é possível concluir com o recorte

### 4.4 Modelo de qualidade adaptado

- ISO/IEC 25010:2011 restrita a Adequação Funcional (completude e correção funcional), Usabilidade (apreensibilidade e operabilidade) e Segurança (confidencialidade e autenticidade)
- Figura do modelo em árvore
- Origem: [Modelo de Qualidade](../docs/fases/fase1/modeloDeQualidade.md)

### 4.5 Seleção e priorização das características

- Matriz impacto × risco (notas de 1 a 5): Adequação Funcional 20, Segurança 15, Usabilidade 12, Eficiência de desempenho 9, Confiabilidade 8, Compatibilidade 4, Manutenibilidade 3
- Justificativas das selecionadas e trade-offs das não selecionadas
- Origem: [Características de Qualidade](../docs/fases/fase1/caracteristicasDeQualidade.md)

### 4.6 Escopo, profundidade e objetos de avaliação

- Três etapas do fluxo; objeto de cada característica
- Exclusões e suas justificativas
- Limites de validade dos resultados
- Origem: [Escopo](../docs/fases/fase1/escopo.md)

### 4.7 Relação com os ODS

- ODS 4, Meta 4.3 e indicador 4.3.1 (não mensurável pela avaliação), Meta 4.4 apenas contextual
- Indicadores internos do produto
- Origem: [ODS](../docs/fases/fase1/ODS.md)

## 5. Fase 2 - Especificação da Avaliação

Origem: [Métricas Funcionais](../docs/fases/fase2/funcionais/visaoGeral.md) e [Métricas Operacionais](../docs/fases/fase2/metricasOperacionais.md)

### 5.1 Rastreabilidade entre as Fases 1 e 2

- Objetivo funcional: Adequação Funcional (prioridade 1)
- Objetivo operacional: Segurança (prioridade 2) e Usabilidade (prioridade 3)
- Necessidades das partes interessadas
- Objetos: Motor 2 (`plano_formatura.service.ts`), commit 87b5475, matriz 6360/1 (2017.1); interface `/plano-formatura`, armazenamento no navegador, rota e dependências

### 5.2 Objetivos de medição - nível conceitual

- Tabela com objeto, propósito, foco, ponto de vista e contexto dos dois objetivos
- Enunciado completo do objetivo funcional

### 5.3 Questões e hipóteses - nível operacional

- Q-FUN-01 a Q-FUN-07 com as hipóteses funcionais documentadas
- Q-OP-01 (H-OP-01) e Q-OP-02 (H-OP-02)

### 5.4 Métricas - nível quantitativo

- MET-FUN-01 a MET-FUN-07 (TVP, TVC, CDO, TDH, TAE, COO e TVS)
- MET-OP-01 (TCH), MET-OP-01b (ISVH), MET-OP-02 (DVCD/IRP), MET-OP-02b (GED-C) e MET-OP-02c (TBR)
- Coleta: casos de teste CT-01 a CT-07; inspeção heurística de Nielsen com tarefas T1 a T3 e checklist de 10 itens; `npm audit`, inspeção do armazenamento do navegador e requisições sem credencial
- Alinhamento com OWASP Top 10 (A01 e A06) e LGPD

### 5.5 Níveis de pontuação e critérios de julgamento

- Metas funcionais e classificação das execuções (conforme, não conforme, não aplicável ou pendente de especificação)
- Níveis das métricas operacionais (excelente, aceitável e crítico)
- Critérios de confirmação de H-OP-01 e H-OP-02

### 5.6 Gráfico GQM

- Dois objetivos, nove questões e doze métricas

## 6. Considerações Parciais

- Síntese da Entrega 1
- Próximos passos: plano de avaliação (Fase 3) e execução, julgamento, ação de melhoria e relatório (Fase 4)
- Origem: [Processo de Avaliação](../docs/metodologia/processoSquare.md)

---

## Declaração de Uso de Inteligência Artificial

- Um registro por integrante, com ferramenta, tarefa e como a saída foi conferida
- Origem: [Uso de IA](../docs/usoDeIA/IA.md)

## Disponibilidade dos Dados

- Link do repositório

## Referências

- Arquivo `latex/referencias.bib`

## Apêndice A - Tabela de Contribuição

- Integrante, matrícula, atividades realizadas e percentual de esforço
- Origem: [Equipe](../docs/equipe/equipe.md)
