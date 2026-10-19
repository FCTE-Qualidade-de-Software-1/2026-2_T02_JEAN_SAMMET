# Elaboração do Artigo

Esta página define como a equipe produz o artigo do projeto. A GitPage é a documentação detalhada de cada fase. O artigo é a síntese dessa documentação no formato de publicação científica, e cada seção dele tem uma página de origem na GitPage.

## 1. Formato

O artigo usa o modelo de artigos para conferências da Sociedade Brasileira de Computação (SBC), em LaTeX, sem alterar a formatação do modelo, como pede a premissa 7. Ele é escrito no Overleaf, com uma cópia versionada no repositório na pasta [`Artigo/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/tree/main/Artigo). O texto fica em `Artigo/latex/main.tex`, as referências em `Artigo/latex/referencias.bib` e a estrutura de apoio em `Artigo/templateArtigo.md`.

O artigo tem no máximo 15 páginas, contando referências, apêndices e anexos, mas a tabela de contribuição no apêndice não entra nesse limite (premissas 9 e 13). Ele é escrito em português, com abstract em inglês e resumo em português, e é entregue em PDF no Moodle, identificando o repositório e a release correspondente (premissa 10).

## 2. Estrutura do artigo e origem de cada seção

A 1ª versão, da Entrega 1, segue os produtos exigidos: Introdução, Referencial teórico, Metodologia de desenvolvimento do projeto, Fase 1 e Fase 2. Cada seção tem uma página de origem na GitPage e uma referência SQuaRE principal.

A Introdução apresenta o contexto, o problema, o objeto (o fluxo "Planejar formatura"), os objetivos, o link do repositório e a organização do texto, e vem do [Início](../index.md) e de [Software Escolhido](../fases/fase1/softwareEscolhido.md). O Referencial teórico trata da SQuaRE, da ISO/IEC 25010, do processo da ISO/IEC 25040, do GQM e do PSM/CID, com base na [Visão Geral da Metodologia](visaoGeral.md) e nas [Referências](../referencias/fase1.md), citando principalmente a ISO/IEC 25000, a ISO/IEC 25010, a ISO/IEC 25040 e a ISO/IEC/IEEE 15939.

A seção de Metodologia de desenvolvimento do projeto descreve o processo adotado, a organização da equipe, a gestão com PSM/CID e a rastreabilidade e ética. Ela vem desta seção da GitPage ([Visão Geral](visaoGeral.md), [Processo](processoSquare.md) e [Fluxo de Trabalho](fluxoDeTrabalho.md)) e de [Gestão do Projeto](../gestaoProjeto/psm-cid.md).

A seção da Fase 1 cobre propósito, stakeholders, tipo de produto, modelo adaptado, priorização, escopo e ODS, a partir das páginas da [Fase 1](../fases/fase1/propositoEStakeholders.md), com base na ISO/IEC 25010, na ISO/IEC 25030 e na ISO/IEC 25040. A seção da Fase 2 cobre a ligação com a Fase 1, os objetivos, as questões e hipóteses, as métricas, os níveis de pontuação, os critérios de julgamento e o gráfico GQM, a partir das páginas da Fase 2 ([funcionais](../fases/fase2/funcionais/visaoGeral.md) e [operacionais](../fases/fase2/metricasOperacionais.md)), com base no GQM, na ISO/IEC 25023 e na ISO/IEC 25040.

As Considerações parciais sintetizam a Entrega 1 e apontam os próximos passos das Fases 3 e 4, apoiadas no estado atual descrito em [Processo de Avaliação](processoSquare.md). O resumo e o abstract são escritos por último, a partir de todas as seções. Depois vêm a declaração de uso de IA, por integrante, com base em [Uso de IA](../usoDeIA/IA.md); a disponibilidade dos dados, com o link do repositório e a [release](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/releases) e o commit da versão submetida; e, no Apêndice A, a tabela de contribuição com atividades e percentual de esforço somando 100%, com base em [Equipe](../equipe/equipe.md).

Na 2ª versão, da Entrega 2, as seções de Fase 1 e Fase 2 são condensadas na metodologia, e entram as seções de Resultados (Fases 3 e 4, com a ação de melhoria) e de Conclusão.

## 3. Etapas de produção

Uma seção do artigo só é escrita depois que a fase correspondente foi consolidada na GitPage e passou pelos critérios de [Organização e Fluxo de Trabalho](fluxoDeTrabalho.md). Assim, a GitPage e o artigo não se contradizem. Ao passar o conteúdo para o LaTeX, a equipe resume e justifica as decisões: tabelas completas, como as fichas de métricas, ficam na GitPage, e o artigo apresenta uma tabela-resumo com o link para a página completa.

Toda norma, método ou dado externo citado no texto precisa ter entrada no `referencias.bib`, com edição, ano e data de acesso conferidos antes da entrega. Cada seção é revisada por um integrante diferente de quem a escreveu, seguindo as regras da seção 4. Em seguida, o PDF é compilado no modelo SBC e o total de páginas é conferido sem contar a tabela de contribuição. Por fim, o `main.tex`, o `referencias.bib` e o PDF são enviados ao repositório, e a release da entrega identifica a versão submetida.

## 4. Regras de redação e revisão

As regras abaixo vêm dos critérios de organização, de português e estilo, de uso de IA e de terminologia da disciplina, e são o que o revisor confere em cada seção.

Os nomes das características e subcaracterísticas seguem a ISO/IEC 25010 em português (Adequação Funcional, Segurança e Usabilidade) e são os mesmos definidos no [Modelo de Qualidade](../fases/fase1/modeloDeQualidade.md) e usados nas fichas da Fase 2. O texto usa os termos da ISO/IEC 25040, como requisitante da avaliação, propósito, requisitos de qualidade, medidas de qualidade, critérios de decisão, plano de avaliação e julgamento, e a correspondência com os termos do GQM e do PSM está na [Visão Geral](visaoGeral.md#5-correspondencia-de-termos-entre-gqm-psm-e-square). Conceitos sem ligação com as métricas, o produto ou o contexto do trabalho ficam de fora.

Quanto à organização, a sequência das seções acompanha as fases do processo, e cada fase retoma o que a anterior decidiu. O texto usa referências cruzadas, como "ver Seção 4", "Tabela 2" e "Figura 3", feitas com `\ref`, e o link do repositório aparece na Introdução e em "Disponibilidade dos dados".

Quanto ao português e à padronização, toda figura e tabela tem número, legenda e fonte e é citada no texto antes de aparecer. As citações seguem o estilo `sbc.bst`, a lista de referências é conferida, não há emojis, figurinhas ou ícones, e as frases são diretas, sem jargão genérico.

A declaração de uso de IA informa, por integrante, a ferramenta, a tarefa e como a saída foi conferida ou ajustada, e nenhum trecho gerado por IA entra no artigo sem revisão contra as fontes e os dados do projeto. Por fim, a tabela de contribuição descreve as atividades de cada integrante e o percentual de esforço, com total de 100%.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Yasmim de Souza Santos](https://github.com/eii-yahs) | Criação da página de elaboração do artigo | 18/10/2026 | [Preencher]() |
