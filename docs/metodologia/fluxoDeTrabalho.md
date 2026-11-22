# Organização e Fluxo de Trabalho

Esta página descreve como a equipe organiza o trabalho para executar o processo de avaliação SQuaRE. Ela cobre o ciclo de cada entrega, as convenções do repositório, os critérios de conclusão e o tratamento dos dados da avaliação.

## 1. Ciclo por entrega

Cada entrega da disciplina é um ciclo. O ciclo da Entrega 1 cobre as Fases 1 e 2 da ISO/IEC 25040, e o ciclo da Entrega 2 cobre as Fases 3 e 4. O ciclo é uma adaptação da equipe: ele descreve o trabalho com Issues, Milestones e Pull Requests no GitHub e não segue formalmente Scrum nem Kanban.

O ciclo começa pelo planejamento, quando a equipe abre o Milestone da entrega e uma Issue para cada tarefa, com seus responsáveis. Esse conjunto inicial de Issues é a linha de base do Milestone. Na execução, cada tarefa é desenvolvida em uma branch própria, produzindo as páginas da GitPage, os dados e as seções do artigo. Ao terminar, o autor abre um Pull Request e pede a revisão de outro integrante, que usa os critérios da seção 3. Depois da revisão, o Pull Request é integrado à `main`, e a GitPage é publicada a partir dela.

Ao longo do ciclo, a equipe calcula os indicadores de Calendário e Progresso, Recursos e Custos e Desempenho do Processo, registrados em [Acompanhamento do Projeto](../gestaoProjeto/painel.md). Quando os critérios de decisão do PSM indicam algum problema, a equipe toma a decisão de gestão correspondente, como redistribuir tarefas ou replanejar, e registra isso nas Issues e nas páginas de [Gestão do Projeto](../gestaoProjeto/psm-cid.md). Esse ajuste alimenta o planejamento do ciclo seguinte.

O trabalho de cada entrega é dividido em frentes, cada uma com responsáveis registrados nas Issues. Na Entrega 1, as frentes foram introdução e referencial teórico, GQM, gráfico GQM, gestão PSM/CID, GitPage e versão em LaTeX, como mostra a página de [Acompanhamento do Projeto](../gestaoProjeto/painel.md).

## 2. Convenções do repositório

As branches seguem o padrão `tipo/assunto`, como `fix/caracteristicas`, `GQM/metricas-funcionais` e `docs/arquivo`, com uma branch por tarefa. As mensagens de commit são curtas, no formato `tipo: descrição`, por exemplo `docs: atualizar histórico de versionamento`. Toda alteração entra na `main` por Pull Request, citando a Issue relacionada, e pelo menos um integrante diferente do autor revisa o Pull Request antes do merge.

Toda página da GitPage termina com a tabela "Histórico de versão", que registra autor, contribuição, data e commit. A GitPage fica na pasta `docs/`, feita com MkDocs Material, e o artigo em LaTeX e seus arquivos de apoio ficam na pasta `Artigo/`.

## 3. Critérios de conclusão de uma tarefa

Uma Issue só é fechada quando o produto atende aos critérios de avaliação da disciplina para as Fases 1 e 2 e para a GitPage. Na prática, o conteúdo precisa responder à atividade da ISO/IEC 25040 correspondente, descrita em [Processo de Avaliação](processoSquare.md), e usar a terminologia da ISO/IEC 25010 em português, por exemplo "Adequação Funcional" e não "Funcionalidade". O texto também deve deixar explícita a ligação com a fase anterior, como um objetivo GQM ligado à característica priorizada e ao stakeholder da Fase 1.

Na forma, figuras e tabelas precisam ter numeração, legenda e fonte e ser citadas no texto, as imagens precisam ter texto alternativo e os links internos devem funcionar. As referências usadas devem estar nas páginas de [Referências](../referencias/fase1.md), e não pode haver emojis, figurinhas ou ícones no corpo da página. Por último, o uso de IA na tarefa deve estar declarado em [Uso de IA](../usoDeIA/IA.md), com ferramenta, tarefa e como a saída foi conferida, e a tabela "Histórico de versão" deve estar atualizada.

## 4. Ferramentas e artefatos

O GitHub é usado para planejamento, execução e revisão, por meio de Issues, Milestones e Pull Requests, e é também a fonte dos dados do PSM/CID. A GitPage é feita com MkDocs Material e publicada automaticamente no GitHub Pages, via GitHub Actions, a cada push na `main`. Os diagramas, como o modelo de qualidade, as árvores GQM e o processo, são feitos em Mermaid e versionados junto com o texto. O artigo é escrito e compilado em LaTeX com o modelo da SBC, no Overleaf. Para a coleta de dados de segurança, a equipe usa o `npm audit` e as ferramentas de desenvolvedor do navegador, conforme o [Protocolo operacional](../fases/fase2/operacionais/protocolo.md).

## 5. Rastreabilidade dos dados e aspectos éticos

As premissas 4, 5 e 6 do trabalho e a atividade de conclusão da ISO/IEC 25040, que trata do destino dos dados da avaliação, orientam a forma como a equipe lida com os dados.

Dados brutos, planilhas de consolidação, procedimentos de cálculo e atas de reunião ficam versionados no repositório, para que todo número do artigo possa ser conferido. Cada arquivo de dados identifica a métrica (`MET-FUN-xx` ou `MET-OP-xx`), a data, o ambiente e a versão do software avaliado. Os testes funcionais usam históricos sintéticos ou autorizados, conforme o [Escopo](../fases/fase1/escopo.md).

Testes de usabilidade e entrevistas só são gravados com consentimento. Os participantes são identificados por códigos, como P01, e as condições de acesso às gravações são definidas antes da coleta. Na segurança, a equipe faz apenas verificações não invasivas, sem tentar explorar vulnerabilidades no sistema em produção.

## 6. Referências

Referências usadas nesta página, conforme [Referências — Fase 1](../referencias/fase1.md), [Referências — Fase 2](../referencias/fase2.md), [Referências — Fase 3](../referencias/fase3.md) e [Referências — Gestão de Projeto](../referencias/psm.md).

- INTERNATIONAL ORGANIZATION FOR STANDARDIZATION. **ISO/IEC 25000:2014: Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Guide to SQuaRE**. Genebra: ISO, 2014. Disponível em: [ficha da ISO/IEC 25000:2014](https://www.iso.org/standard/64764.html). Acesso em: 22 nov. 2026.
- INTERNATIONAL ORGANIZATION FOR STANDARDIZATION. **ISO/IEC 25010:2011: Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models**. Genebra: ISO, 2011. Disponível em: [ficha da ISO/IEC 25010:2011](https://www.iso.org/standard/35733.html). Acesso em: 15 nov. 2026.
- INTERNATIONAL ORGANIZATION FOR STANDARDIZATION. **ISO/IEC 25040:2011: Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Evaluation process**. Genebra: ISO, 2011. Disponível em: [ficha da ISO/IEC 25040:2011](https://www.iso.org/standard/35765.html). Acesso em: 15 nov. 2026.
- McGARRY, John et al. **Practical Software Measurement: Objective Information for Decision Makers**. Boston: Addison-Wesley, 2001.
- NPM, INC. **npm-audit**: documentation and command-line security auditing for Node.js packages. npm Docs, 2026. Disponível em: <https://docs.npmjs.com/cli/commands/npm-audit>.
- PRACTICAL SOFTWARE AND SYSTEMS MEASUREMENT (PSM); NDIA; INCOSE. **Practical Software and Systems Measurement: Continuous Iterative Development (CID) Measurement Framework**. Version 2.1. [S.l.]: PSM Working Group, 2021. Parts 1–3.
- RAMOS, Cristiane Soares. **FGA0315 — Qualidade de Software 1: Projeto Final da Disciplina e Materiais Didáticos de PSM**. Brasília: Universidade de Brasília, Faculdade do Gama (UnB/FGA), 2º sem. 2026.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Padronização visual e editorial da documentação | 15/11 | [7a74d9e](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/7a74d9e0809e91d60a36a88559b357bfe171f37e) |
| [Yasmim de Souza Santos](https://github.com/eii-yahs) | Inclusão das referências utilizadas na página | 22/11 | Não commitado |
