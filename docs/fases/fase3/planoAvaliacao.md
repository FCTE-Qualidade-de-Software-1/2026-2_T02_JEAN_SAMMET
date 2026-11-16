# Fase 3 — Plano de avaliação

O plano prepara a coleta das sete métricas funcionais e cinco operacionais da [Fase 2](../fase2/funcionais/GQM.md). A coleta completa, o cálculo e o julgamento pertencem à Fase 4. A preparação verifica a viabilidade dos procedimentos e permanece separada dos resultados definitivos.

## 1. Organização

**Tabela 1 — Organização.**

| Parte | Conteúdo |
| --- | --- |
| [Roteiro funcional](funcionais/roteiro.md) | CT-01 a CT-07: entradas, referências, passos e resultados esperados |
| [Fontes curriculares](funcionais/fontes.md) | Matriz 6360/1, regras verificadas e lacunas |
| [Plano operacional](metricasOperacionais.md) | Usabilidade, dependências, armazenamento e acesso |
| [Ambiente e dados](operacionais/ambienteERecursos.md) | Conta de teste, histórico autorizado e cenários planejados |
| [Cronograma de avaliação](cronograma.md) | Datas-alvo, atividades, responsáveis e dependências até 22/11 |
| [Matriz de rastreabilidade](operacionais/rastreabilidade.md) | Necessidades, questões, hipóteses, métricas, metas, procedimentos e registros previstos |

*Fonte: elaboração da equipe, conforme os registros e referências desta página.*

## 2. Registro e decisão

Cada execução identifica caso, entrada, cenário, responsável, data/hora com fuso, ambiente, versão conhecida, regra, resultado esperado, observado, cálculo e evidência. Os modelos ficam em `testes/modelos_coleta/`. Criar uma cópia por execução e preservar os modelos vazios.

- **Conforme/Não conforme:** há regra e dados válidos para aplicar a ficha da Fase 2.
- **Pendente de especificação:** falta regra ou efeito esperado documentado.
- **Inconclusivo:** a coleta ou a evidência não permite julgar.
- **Sem cobertura:** a entrada disponível não permite executar a condição planejada; registrar a lacuna, sem taxa ou aprovação.
- **Não aplicável:** uma regra conhecida não se aplica ao cenário; justificar.

Não usar ausência de dados como zero. Preservar também falhas e repetições, com o motivo. Resultados de entradas, cenários, versões ou ferramentas diferentes são identificados separadamente.

## 3. Prontidão para a coleta

**Fase 3 concluída no escopo de preparação**, com viabilidade básica verificada: H0 aceito, planejamento acessível, cargas 20/24/32 créditos operáveis, base restaurada, ambiente registrado e instrumentos de segurança exercitados. A identificação da versão do servidor permanece desconhecida; o cliente tem inventário de URLs e hashes dos scripts observados.

O prazo é **22/11**. Gabriel executará os testes funcionais; Giovani, os de segurança; Gustavo fará a revisão/consolidação. Gustavo e Gabriel realizarão duas inspeções independentes de usabilidade. O acompanhamento do esforço realizado permanece no [PSM](../../gestaoProjeto/painel.md).

A coleta completa, os percentuais e as respostas GQM ficam na Fase 4. Cada caso exige sua regra, entrada e evidência; dados ou credenciais indisponíveis significam cobertura limitada, sem fabricar casos ou resultados. A SCA fica restrita aos componentes efetivamente reconhecidos; storage exige três estados; TBR exige casos negativos válidos além do controle positivo.

C0–C5 mantêm H0 fixo. As capturas de Gabriel, identificadas pela equipe como H0, foram integradas aos [registros funcionais](../fase4/funcionais/dadosBrutos.md). PDF, identificação, credenciais e planos individuais completos ficam fora do repositório; publicar somente referências e evidências sanitizadas.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Organização do plano integrado e dos critérios de prontidão | 15/11 | [aa0c61f](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/aa0c61fac5e9d2db19adec76fd052a2bb6b04b90) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Padronização da entrada H0 | 15/11 | [f454d2c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f454d2c099e16a6dd593b92420b541a18262b086) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Atualização dos responsáveis e das condições de prontidão | 15/11 | [7a74d9e](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/7a74d9e0809e91d60a36a88559b357bfe171f37e) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Atualização das referências após remoção do cronograma operacional | 15/11 | [f5e77d5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f5e77d5) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Atualização do acesso à matriz integrada de rastreabilidade da Fase 3 | 16/11 | [2c27c5f](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/2c27c5f7e47663e993ffdc4c3abeb0411eac1c3e) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Inclusão do cronograma de avaliação no plano integrado | 16/11 | [6d11323](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/6d113238dd362d70e6f821ff3e4dad670239bf95) |
