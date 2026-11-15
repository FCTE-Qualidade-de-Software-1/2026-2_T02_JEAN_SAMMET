# Execução e Conclusão da Avaliação — Métricas Funcionais (Fase 4)

> **Estado da avaliação: coleta formal pendente.** O piloto documentado em 15/11/2026 não concluiu a geração de um plano pelas preferências. O histórico oficial autorizado `H0` é mantido fora do repositório e não está presente neste pacote. Assim, não há base para calcular as sete métricas funcionais nem para confirmar/refutar as hipóteses. A observação exploratória disponível está preservada como evidência de piloto, sem ser contabilizada como teste funcional.

Esta página centraliza a execução e a conclusão da avaliação de **Adequação Funcional** da funcionalidade *Planejar formatura* do No Fluxo UnB, seguindo o objetivo, as métricas e as regras de julgamento definidos na [Fase 2 — GQM](../fase2/funcionais/GQM.md) e os casos do [roteiro funcional da Fase 3](../fase3/funcionais/roteiro.md).

## 1. Navegação pelas páginas da Fase 4

| Seção / Página | Conteúdo | Métricas |
| :--- | :--- | :---: |
| [Dados brutos e evidências](funcionais/dadosBrutos.md) | Fontes, registros do piloto, arquivos de coleta, lacunas e regras de preservação. | Todas |
| [Análise dos resultados e julgamento](funcionais/analiseResultados.md) | Fórmulas, cobertura, comparação com as metas da Fase 2, validação das hipóteses e respostas formais às questões GQM. | Todas |

## 2. Quadro de situação das métricas

| Métrica | Nome | Caso | Valor obtido | Situação nesta versão |
| :---: | :--- | :---: | :---: | :---: |
| `MET-FUN-01` | Violações de pré-requisitos (TVP) | `CT-01` | Não calculável | **Pendente de execução** |
| `MET-FUN-02` | Violações de co-requisitos (TVC) | `CT-02` | Não calculável | **Pendente de execução** |
| `MET-FUN-03` | Cobertura de obrigatórias pendentes (CDO) | `CT-03` | Não calculável | **Pendente de execução** |
| `MET-FUN-04` | Divergências no tratamento do histórico (TDH) | `CT-04` | Não calculável | **Pendente de execução** |
| `MET-FUN-05` | Aplicação incorreta de equivalências (TAE) | `CT-05` | Não calculável | **Pendente de execução** |
| `MET-FUN-06` | Conformidade das opções do onboarding (COO) | `CT-06` | Não calculável | **Pendente de especificação e execução** |
| `MET-FUN-07` | Violações de restrições semestrais (TVS) | `CT-07` | Não calculável | **Pendente de execução** |

**Não calculável não significa 0%.** Nenhuma linha formal foi registrada em `verificacoes_funcionais.csv`; portanto, os denominadores válidos são inexistentes. A métrica `MET-FUN-06` também depende de expectativas verificáveis para os efeitos de cada opção do onboarding. A consulta às regras curriculares oficiais não substitui a comparação entre histórico, plano esperado e plano efetivamente gerado.

## 3. Síntese do estado da avaliação

1. **Planejamento e fontes:** a matriz 6360/1 — 2017.1, exemplos de pré-requisito, co-requisito e equivalência e limites curriculares estão documentados na Fase 3. Esses registros definem referências, mas não comprovam como o motor tratou o histórico.
2. **Evidência parcial:** o piloto observou controles de preferência e recálculo visual. A captura preservada mostra um estado intermediário de 14 créditos/210h; ela não comprova a saída final, a cobertura de disciplinas ou a conformidade de uma regra curricular.
3. **Coleta formal:** os arquivos de execução e verificação foram preparados, mas permanecem sem linhas de teste. Não foi possível inferir numeradores e denominadores para `CT-01` a `CT-07`.
4. **Conclusão:** a adequação funcional ainda não pode ser classificada como Conforme ou Não conforme. As respostas formais às questões GQM e os motivos de pendência estão na [análise dos resultados](funcionais/analiseResultados.md).

## 4. Processamento reproduzível

Após preencher os registros sanitizados, processar a coleta com:

```bash
python3 scripts/metricas_funcionais.py
```

Para usar outro arquivo:

```bash
python3 scripts/metricas_funcionais.py --csv caminho/para/verificacoes_funcionais.csv
```

O script calcula as taxas de falha ou cobertura segundo a direção de cada métrica, apresenta a contagem válida e a cobertura, julga `MET-FUN-07` separadamente por tipo de restrição e consolida as respostas de `Q-FUN-01` a `Q-FUN-07`. Denominador zero gera pendência, nunca conformidade.

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Gabriel Mota](https://github.com/Gabro-MO) | Consolidação da execução e do julgamento das métricas funcionais na Fase 4, com rastreabilidade dos dados ainda pendentes | 15/11/2026 | Não commitado |
