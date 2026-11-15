# Dados Brutos e Evidências — Métricas Funcionais (Fase 4)

## 1. Origem e escopo dos registros

A avaliação funcional usa o histórico oficial autorizado `H0`, mantido fora do repositório, e a matriz de Engenharia de Software 6360/1 — 2017.1. Os cenários `C0` a `C5` alteram apenas controles oferecidos pelo produto; não criam aprovações, reprovações ou equivalências artificiais. A especificação dos cenários e os passos de cada caso permanecem na [Fase 3 — Roteiro de Avaliação](../../fase3/funcionais/roteiro.md).

A entrada `H0` não foi incluída neste repositório por conter dados acadêmicos pessoais. O arquivo `testes/cenarios_avaliacao.json` registra sua origem e armazenamento externo. A referência curricular sanitizada e versionada está em `testes/referencias/estrutura_6360_1.json`; ela não substitui o histórico do estudante.

## 2. Evidência exploratória disponível

**Registro:** `testes/evidencias/funcionais/observacoes_piloto.csv`  
**Data:** 15/11/2026  
**Evidência visual:** [`docs/fases/fase3/img/controle-creditos.png`](../../fase3/img/controle-creditos.png)

A exploração percorreu o fluxo *Meu Fluxograma → Planejar formatura → Preferências*. Foram observados a matriz 6360/1, o controle de créditos, a alternância entre créditos/horas e o recálculo visual. A documentação do piloto informa 24 créditos/360h como referência e uma captura intermediária em 14 créditos/210h. O plano final não foi gerado a partir das preferências. A captura registra o estado do controle, não a correção de uma saída.

Essa observação é **evidência de prontidão/piloto**, não uma execução formal de `CT-01` a `CT-07`. Ela não entra nos numeradores ou denominadores de `MET-FUN-01` a `MET-FUN-07`.

## 3. Arquivos de coleta formal

| Arquivo | Conteúdo | Estado |
| :--- | :--- | :--- |
| `testes/evidencias/funcionais/execucoes.csv` | Uma linha por execução, incluindo caso, cenário, responsável, data, ambiente, versão, resultado esperado/observado e cálculo. | Cabeçalho inicializado; sem execução formal registrada. |
| `testes/evidencias/funcionais/verificacoes_funcionais.csv` | Uma linha por relação, disciplina, status, equivalência, expectativa ou restrição verificada; `conforme` recebe `1` ou `0` somente com evidência. | Cabeçalho inicializado; sem verificação formal registrada. |
| `testes/evidencias/funcionais/observacoes_piloto.csv` | Observação exploratória limitada do controle de créditos. | Uma observação, fora da coleta métrica. |

Os cabeçalhos de `execucoes.csv` e `verificacoes_funcionais.csv` reproduzem os modelos de `testes/modelos_coleta/`. Para cada registro formal, usar um `execucao_id` único e uma evidência sanitizada com caminho relativo. O campo `fonte_vigencia` deve identificar a regra curricular ou a expectativa de produto usada como referência. Registros sem evidência ou sem regra identificável não devem receber `conforme=1` nem `conforme=0`.

## 4. Referências para a verificação

- **Matriz e obrigatórias:** `testes/referencias/estrutura_6360_1.json`, transcrita da fonte SIGAA/UnB indicada em [Fontes e Regras](../../fase3/funcionais/fontes.md). O recorte contém 39 componentes obrigatórios, 2.580h obrigatórias e limites curriculares por período; não demonstra integralização das cadeias de seletividade ou das optativas.
- **Pré-requisitos:** exemplos conferidos para FGA0211 e MAT0026, com as vigências indicadas na página de fontes.
- **Co-requisitos:** par FGA0072/FGA0074, com a condição de pré-requisito registrada na página de fontes. Ainda é necessário confirmar que o planejador permite selecionar o par.
- **Equivalência:** MAT0138/MAT0026, com cadastro e vigência consultados. A ocorrência dessa equivalência em `H0` não pode ser presumida.
- **Onboarding:** carga sugerida e opções visíveis foram observadas no piloto. O efeito algorítmico de trabalho/estágio e objetivo ainda depende de comportamento esperado identificável.
- **Calendário e oferta:** dependem de evidência oficial para o período efetivamente avaliado; sem essa fonte, a parcela correspondente de `CT-07` fica pendente.

## 5. Lacunas que impedem a coleta definitiva

1. A importação de `H0` não está demonstrada por um registro sanitizado no pacote. O histórico original não deve ser copiado para o Git.
2. O piloto não terminou a geração de um plano com as preferências; assim, não há plano completo para comparar às regras e à lista de pendências.
3. `CT-02` depende de ocorrência de um par aplicável em `H0` ou de seleção explícita suportada pelo produto. Não fabricar a ocorrência.
4. `CT-05` depende de equivalência presente no histórico e de fonte/vigência aplicável; não presumir MAT0138 em `H0` nem transitividade.
5. `CT-06` depende de expectativas documentadas para cada efeito antes da comparação. A mera ausência de alteração no plano não é prova de defeito.
6. `CT-07` precisa de registros de cargas por semestre e, quando aplicável, calendário/oferta do período.

## 6. Procedimento de reprodutibilidade e privacidade

1. Confirmar que a entrada é o histórico oficial autorizado e que foi carregada corretamente. Manter o arquivo original fora do repositório.
2. Registrar commit/versão, data, navegador, ambiente, matriz e cenário; não registrar credenciais ou valores acadêmicos identificáveis.
3. Pré-definir o resultado esperado com referência oficial/documentada antes de observar a saída.
4. Preservar captura ou log sanitizado do plano completo e uma linha por verificação atômica. Restaurar `C0` entre variações.
5. Executar `python3 scripts/metricas_funcionais.py` e transportar os resultados para a [análise e julgamento](analiseResultados.md), mantendo o arquivo bruto original.

## Histórico de versão

| Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Gabriel Mota](https://github.com/Gabro-MO) | Catálogo das evidências funcionais e registro da limitação da coleta 
 | 15/11/2026 | Não commitado |
