# Registro de consolidação de CT-05 — 7/7 equivalências

**Data:** 15/11/2026  
**Métrica:** `MET-FUN-05` — TAE (Aplicação incorreta de equivalências)  
**Critério de fechamento informado pelo avaliador:** contabilizar as sete relações de equivalência registradas em H0 como corretamente tratadas pelo produto.

## Classificação consolidada

Para o fechamento solicitado, as sete relações de H0 foram lançadas como conformes (`conforme=1`) no arquivo `testes/evidencias/funcionais/verificacoes_funcionais.csv`. Isso corresponde a `NEI=0`, `NRE=7` e `TAE=(0/7)×100=0%`.

A classificação respeita a diferença de status existente no H0:

- **Cinco relações concluídas:** as disciplinas de origem estão `APROVADO` e o SIGAA declara que as obrigatórias de destino foram cumpridas.
- **Duas relações em andamento:** as disciplinas de origem estão `MATRICULADO`; são contabilizadas como corretamente tratadas somente quando não são interpretadas como equivalências já concluídas e as obrigatórias de destino permanecem pendentes.

## Alcance das capturas e rastreabilidade

A captura `CT-05-Equivalencias.png` apresenta diretamente FGA0147 e FGA0172 como reconhecidas/concluídas, sem duplicação e sem permanência da obrigatória original na lista de pendências, conforme a análise do avaliador.

As outras cinco relações não aparecem individualmente nessa captura. Suas classificações `conforme=1` registram a decisão de consolidação explicitamente solicitada pelo avaliador; **este registro documenta essa decisão, mas não substitui capturas individuais nem deve ser descrito como prova visual independente das cinco relações**.

Assim, o resultado numérico de CT-05 fica fechado como **7/7 corretas (TAE=0%)**, com essa ressalva de rastreabilidade preservada na documentação.
