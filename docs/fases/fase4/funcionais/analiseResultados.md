# Análise dos Resultados — Métricas Funcionais

Aplicar o [GQM da Fase 2](../../fase2/funcionais/GQM.md) às comparações registradas conforme o [roteiro da Fase 3](../../fase3/funcionais/roteiro.md). H0 é a única entrada acadêmica da avaliação.

## 1. Estado das métricas

| Métrica | Universo de referência | Situação |
|---|---|---|
| TVP — pré-requisitos | Relações pertinentes, com regra identificada | Pendente de execução |
| TVC — co-requisitos | Relações dirigidas do par selecionado | Pendente de execução |
| CDO — obrigatórias | 15 disciplinas pendentes | Pendente de execução |
| TDH — histórico | 44 registros por código/período | Pendente de execução |
| TAE — equivalências | Oito relações: seis concluídas e duas em andamento | Pendente de execução |
| COO — onboarding | Expectativas especificadas e testadas | Pendente de execução/especificação |
| TVS — restrições | Verificações por tipo de restrição | Pendente de execução |

Não há percentual final sem resultado observado. O histórico define o universo esperado; a quantidade atendida ou violada vem da comparação com o produto.

## 2. Julgamento

Questões e hipóteses GQM permanecem sem conclusão definitiva. Registrar evidências, cobertura e limitações antes de classificar. Relação ausente, regra não especificada e falha de coleta têm causas distintas; nenhuma autoriza preencher zero automaticamente.

CT-04 preserva ocorrências da mesma disciplina em períodos diferentes. CT-05 separa aproveitamentos concluídos de matrículas em equivalente. CT-06/07 distinguem carga sugerida, limite obrigatório e máximo curricular.

## 3. Reprocessamento

```bash
python3 scripts/metricas_funcionais.py
python3 -m unittest testes.teste_metricas_funcionais testes.teste_h0_sanitizado
```

Testes locais validam instrumentos e base, não a qualidade do No Fluxo.

---

## Histórico de versão

| Membro | Contribuição | Data | Commit |
|---|---|---|---|
| Gabriel Mota | Consolidação das observações CT-01 a CT-07, cálculo e respostas GQM | 15/11 | [1bc6aca](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/1bc6acac9640bf2f81bd53039c24ab5507f88b92) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Padronização da avaliação pelo histórico oficial H0 | 15/11 | Não commitado |
