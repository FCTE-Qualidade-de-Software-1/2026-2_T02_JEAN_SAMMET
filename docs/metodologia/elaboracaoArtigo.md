# Elaboração do Artigo

Esta página define como a equipe produz o artigo do projeto. A GitPage é a documentação detalhada de cada fase. O artigo é a síntese dessa documentação no formato de publicação científica, e cada seção dele tem uma página de origem na GitPage.

## 1. Formato

O artigo usa o modelo de artigos para conferências da Sociedade Brasileira de Computação (SBC), em LaTeX, sem alterar a formatação do modelo, como pede a premissa 7. Ele é escrito no Overleaf, com uma cópia versionada no repositório na pasta [`Artigo/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/tree/main/Artigo). O texto fica em `Artigo/latex/main.tex`, as referências em `Artigo/latex/referencias.bib` e a estrutura de apoio em `Artigo/templateArtigo.md`.

O artigo tem no máximo 15 páginas, contando referências, apêndices e anexos, mas a tabela de contribuição no apêndice não entra nesse limite (premissas 9 e 13). Ele é escrito em português, com abstract em inglês e resumo em português, e é entregue em PDF no Moodle, identificando o repositório e a release correspondente (premissa 10).

## 2. Estrutura do artigo e origem de cada seção

A versão final, da Entrega 2, cobre as quatro fases do processo. A Entrega 1 trouxe as Fases 1 e 2, e a Entrega 2 acrescentou as Fases 3 e 4 sem apagar o texto anterior. Cada seção tem uma página de origem na GitPage, e a estrutura resumida está em `Artigo/templateArtigo.md`.

A Introdução apresenta o contexto, o problema, o objeto (o fluxo "Planejar formatura"), os quatro objetivos específicos, os links do repositório e da GitPage e a organização do texto, e vem do [Início](../index.md) e de [Software Escolhido](../fases/fase1/softwareEscolhido.md). O Referencial teórico e trabalhos relacionados trata da SQuaRE e das três características da ISO/IEC 25010 avaliadas e compara este trabalho com três avaliações de sistemas acadêmicos, com base nas [Referências](../referencias/fase1.md).

A Metodologia descreve, passo a passo, o processo da ISO/IEC 25040 nas quatro fases, o uso do GQM e as ferramentas, e remete ao repositório para o detalhamento. Ela vem do [Processo de Avaliação](processoSquare.md).

Os Resultados têm uma subseção por fase. A da Fase 1 cobre propósito, partes interessadas, produto, pontos do Motor 2, priorização, modelo adaptado e escopo, a partir das páginas da [Fase 1](../fases/fase1/propositoEStakeholders.md). A da Fase 2 cobre os objetivos, as questões e suas hipóteses, as métricas, o gráfico GQM e os critérios de julgamento, a partir das páginas da Fase 2 ([funcionais](../fases/fase2/funcionais/visaoGeral.md) e [operacionais](../fases/fase2/metricasOperacionais.md)). A da Fase 3 cobre a entrada de teste, os cenários, as regras de referência, os procedimentos, a rodada inicial, o cronograma e a matriz de rastreabilidade, a partir do [Plano Integrado](../fases/fase3/planoAvaliacao.md) e do [Piloto e Prontidão](../fases/fase3/piloto.md).

A subseção da Fase 4 segue a estrutura do GQM. Uma tabela reúne, para cada uma das nove questões, a métrica, o resultado, a meta, a resposta e o julgamento da hipótese associada. O texto percorre primeiro as questões do objetivo funcional (Q-FUN-01 a Q-FUN-07, com H-FUN-01 a H-FUN-07) e depois as do objetivo operacional (Q-OP-01 e Q-OP-02, com H-OP-01 e H-OP-02), incluindo a ação de melhoria M-01. Ela vem da [Rastreabilidade Completa](../fases/fase4/rastreabilidade.md) e das análises [funcional](../fases/fase4/funcionais/analiseResultados.md) e [operacional](../fases/fase4/operacionais/analiseResultados.md).

A Conclusão sintetiza as quatro fases, as respostas às questões e o julgamento das hipóteses, explica por que as características são julgadas separadamente e apresenta os limites, as recomendações e o próximo passo, a partir da [Conclusão da Avaliação](../fases/fase4/conclusao.md). O resumo e o abstract são escritos por último, a partir de todas as seções. Depois vêm a declaração de uso de IA, por integrante, com base em [Uso de IA](../usoDeIA/IA.md); a disponibilidade dos dados, com o link do repositório e a [release](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/releases) e o commit da versão submetida; e, no Apêndice A, a tabela de contribuição com atividades e percentual de esforço somando 100%, com base em [Equipe](../equipe/equipe.md).

## 3. Etapas de produção

Uma seção do artigo só é escrita depois que a fase correspondente foi consolidada na GitPage e passou pelos critérios de [Organização e Fluxo de Trabalho](fluxoDeTrabalho.md). Assim, a GitPage e o artigo não se contradizem. Ao passar o conteúdo para o LaTeX, a equipe resume e justifica as decisões: tabelas completas, como as fichas de métricas, ficam na GitPage, e o artigo apresenta uma tabela-resumo com o link para a página completa.

Toda norma, método ou dado externo citado no texto precisa ter entrada no `referencias.bib`, com edição, ano e data de acesso conferidos antes da entrega. Cada seção é revisada por um integrante diferente de quem a escreveu, seguindo as regras da seção 4. Em seguida, o PDF é compilado no modelo SBC e o total de páginas é conferido sem contar a tabela de contribuição. Por fim, o `main.tex`, o `referencias.bib` e o PDF são enviados ao repositório, e a release da entrega identifica a versão submetida.

## 4. Regras de redação e revisão

As regras abaixo vêm dos critérios de organização, de português e estilo, de uso de IA e de terminologia da disciplina, e são o que o revisor confere em cada seção.

Os nomes das características e subcaracterísticas seguem a ISO/IEC 25010 em português (Adequação Funcional, Segurança e Usabilidade) e são os mesmos definidos no [Modelo de Qualidade](../fases/fase1/modeloDeQualidade.md) e usados nas fichas da Fase 2. O texto usa os termos da ISO/IEC 25040, como requisitante da avaliação, propósito, requisitos de qualidade, medidas de qualidade, critérios de decisão, plano de avaliação e julgamento, e a correspondência com os termos do GQM e do PSM está na [Visão Geral](visaoGeral.md#5-correspondencia-de-termos-entre-gqm-psm-e-square). Conceitos sem ligação com as métricas, o produto ou o contexto do trabalho ficam de fora.

Quanto à organização, a sequência das seções acompanha as fases do processo, e cada fase retoma o que a anterior decidiu. O texto usa referências cruzadas, como "ver Seção 4", "Tabela 2" e "Figura 3", feitas com `\ref`, e o link do repositório aparece na Introdução e em "Disponibilidade dos dados".

Quanto ao português e à padronização, toda figura e tabela tem número, legenda e fonte e é citada no texto antes de aparecer. As citações seguem o estilo `sbc.bst`, a lista de referências é conferida, não há emojis, figurinhas ou ícones, e as frases são diretas, sem jargão genérico.

A declaração de uso de IA informa, por integrante, a ferramenta, a tarefa e como a saída foi conferida ou ajustada, e nenhum trecho gerado por IA entra no artigo sem revisão contra as fontes e os dados do projeto. Por fim, a tabela de contribuição descreve as atividades de cada integrante e o percentual de esforço, com total de 100%.

## 5. Referências

Referências usadas nesta página, conforme [Referências — Fase 1](../referencias/fase1.md), [Referências — Fase 2](../referencias/fase2.md) e [Referências — Gestão de Projeto](../referencias/psm.md).

- BASILI, Victor R.; CALDIERA, Gianluigi; ROMBACH, H. Dieter. **The Goal Question Metric Approach**. *Encyclopedia of Software Engineering*, John Wiley & Sons, v. 2, p. 528-532, 1994. Disponível em: <https://ntrs.nasa.gov/citations/19940026214>.
- INTERNATIONAL ORGANIZATION FOR STANDARDIZATION. **ISO/IEC 25000:2014: Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Guide to SQuaRE**. Genebra: ISO, 2014. Disponível em: [ficha da ISO/IEC 25000:2014](https://www.iso.org/standard/64764.html). Acesso em: 22 nov. 2026.
- INTERNATIONAL ORGANIZATION FOR STANDARDIZATION. **ISO/IEC 25010:2011: Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models**. Genebra: ISO, 2011. Disponível em: [ficha da ISO/IEC 25010:2011](https://www.iso.org/standard/35733.html). Acesso em: 15 nov. 2026.
- INTERNATIONAL ORGANIZATION FOR STANDARDIZATION. **ISO/IEC 25040:2011: Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Evaluation process**. Genebra: ISO, 2011. Disponível em: [ficha da ISO/IEC 25040:2011](https://www.iso.org/standard/35765.html). Acesso em: 15 nov. 2026.
- RAMOS, Cristiane Soares. **FGA0315 — Qualidade de Software 1: Projeto Final da Disciplina e Materiais Didáticos de PSM**. Brasília: Universidade de Brasília, Faculdade do Gama (UnB/FGA), 2º sem. 2026.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Padronização visual e editorial da documentação | 15/11 | [7a74d9e](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/7a74d9e0809e91d60a36a88559b357bfe171f37e) |
| [Yasmim de Souza Santos](https://github.com/eii-yahs) | Inclusão das referências utilizadas na página | 22/11 | Não commitado |
