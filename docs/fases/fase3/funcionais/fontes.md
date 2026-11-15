# Referências para os testes funcionais

## 1. Matriz de referência

Foi conferida a estrutura **6360/1 — 2017.1**, no [SIGAA público](https://sigaa.unb.br/sigaa/public/curso/curriculo.jsf?id=414924&lc=pt_BR), em 15/11. Na lista, escolher 6360/1 e **Visualizar Estrutura Curricular**. A matriz estar inativa para novos ingressos não invalida seu uso como recorte da avaliação.

| Regra | Valor conferido |
|---|---|
| Carga total mínima | 3.480h |
| Obrigatórias | 2.580h, distribuídas em 39 componentes |
| Optativas mínimas | 900h |
| Limites por período | Mínimo de 240h e máximo de 480h |
| Componentes eletivos | Máximo de 360h |

A relação foi conferida com a matriz e com o histórico oficial autorizado H0. A transcrição curricular `testes/referencias/estrutura_6360_1.json` foi recuperada do histórico Git incluído no pacote, a partir da referência `origin/feat/op-fase3`; a entrada H0 sanitizada está em `testes/referencias/h0_sanitizado.json` e seus dados brutos em `testes/evidencias/funcionais/`. O histórico original não deve ser versionado.

## 2. Regras consultadas no SIGAA

Nos detalhes da matriz, abrir o nível e selecionar **Visualizar Detalhes do Componente**. O endereço do resumo depende da sessão; usar o código abaixo para repetir a consulta.

| Componente | Regra observada | Uso no teste |
|---|---|---|
| FGA0211 — Redes | Exige FGA0170; pré-requisito ativo desde 01/08/2019. | CT-01 e comparação de status em CT-04 |
| FGA0009 → FGA0011 — TCC 1/2 | A sequência aparece no fluxo do produto: FGA0009 no semestre 9 e FGA0011 no semestre 10. A relação e sua vigência não constam entre as regras formais transcritas no JSON curricular. | CT-01; observação do avaliador, com ressalva de fonte oficial pendente |
| FGA0206 — Engenharia de Produto de Software | O avaliador relata que a disciplina e o pré-requisito alternativo `FGA0242 OU FGA0171` foram deixados de fora do plano. A regra do pré-requisito não está entre as regras formalmente transcritas neste pacote. | CT-03; a omissão de FGA0206 entra no denominador das 14 obrigatórias; o pré-requisito não é contado como outra obrigatória sem confirmação da matriz |
| MAT0026 — Cálculo 2 | Exige MAT0025 ou MAT0024; expressão ativa desde 07/11/2021. | Contexto histórico de CT-01; MAT0025 está aprovada e MAT0026 também consta como aprovada em H0. |
| FGA0072/FGA0074 — Eletrônica Digital 2 | Co-requisito recíproco; ambas optativas. Pré-requisito: `ENE0277 OU (FGA0073 E FGA0071)`, regra de co-requisito ativa desde 01/08/2019. | CT-02. H0 contém FGA0071 e FGA0073 aprovadas, mas não contém FGA0072 nem FGA0074. |
| MAT0138/MAT0026 | A matriz/cadastro consultado registra MAT0138 como equivalência de MAT0026, com as vigências documentadas no cadastro. | É referência curricular geral; MAT0138 não aparece em H0, portanto não deve ser simulada como ocorrência nesta avaliação. |

## 3. Equivalências efetivamente registradas em H0

O próprio histórico SIGAA lista explicitamente cinco declarações `Cumpriu`, com a obrigatória de destino e a disciplina cursada. Essas relações são evidência direta do estado acadêmico esperado para CT-05.

| Obrigatória satisfeita | Componente cursado | Período | Situação no H0 | Evidência |
|---|---|---:|---|---|
| FGA0147 — Estrutura de Dados e Algoritmos | FGA0146 — Estruturas de Dados 1 | 2025.2 | Aprovado | `Cumpriu FGA0147 através de FGA0146` |
| FGA0184 — Gestão da Produção e Qualidade | FGA0307 — Gestão da Produção e Qualidade | 2025.2 | Aprovado | `Cumpriu FGA0184 através de FGA0307` |
| FGA0138 — Métodos de Desenvolvimento de Software | FGA0312 — Métodos de Desenvolvimento de Software | 2025.2 | Aprovado | `Cumpriu FGA0138 através de FGA0312` |
| FGA0172 — Requisitos de Software | FGA0313 — Requisitos de Software | 2026.1 | Aprovado | `Cumpriu FGA0172 através de FGA0313` |
| FGA0238 — Testes de Software | FGA0314 — Testes de Software | 2026.1 | Aprovado | `Cumpriu FGA0238 através de FGA0314` |

H0 também contém FGA0303 → FGA0150 e FGA0315 → FGA0278 com marcador de equivalente a obrigatório, mas ambos estão `MATRICULADO` em 2026.2. O próprio quadro de obrigatórias pendentes mantém FGA0150 e FGA0278 como pendentes. Essas duas relações não devem ser tratadas como equivalências concluídas.

## 4. Obrigatórias pendentes e estado de H0

O quadro do histórico lista 14 disciplinas obrigatórias pendentes, totalizando 1.050h, compatível com o quadro-resumo de carga horária obrigatória pendente. Duas cadeias de seletividade (60h cada) e ENADE concluinte (0h) aparecem separadamente; não integram o denominador de disciplinas de `MET-FUN-03`.

A linha de base inclui 41 registros de componentes curriculares: 33 aprovados, 7 matriculados e 1 trancado. O item FGA0060 está `TRANCADO`; não deve ser interpretado como aprovação. Os sete itens `MATRICULADO` não equivalem a aprovação acadêmica concluída.

## 5. Limitações e rastreabilidade

- **Co-requisitos:** a regra FGA0072/FGA0074 está documentada, e os pré-requisitos alternativos FGA0073/FGA0071 estão aprovados em H0. A execução de 15/11/2026 confirmou que o planejador permitiu a alocação do par; a captura mostra as disciplinas em semestres diferentes, resultando em violação.
- **Equivalências:** cinco conclusões e duas equivalências em andamento estão presentes em H0. O teste mede o comportamento do produto ao interpretar esses dados; a declaração do SIGAA é referência do resultado esperado, não evidência de que o produto os importou corretamente.
- **Oferta e calendário:** registrar o período efetivo da coleta e a oferta oficial. Sem essa fonte, a parte correspondente de CT-07 fica pendente.
- **Onboarding:** a interface mostra carga sugerida e opções de trabalho/estágio e objetivo; o efeito algorítmico exato de trabalho/estágio e velocidade é inconclusivo.
- **Optativas:** conferir apenas as selecionadas para o cenário. As demais ficam fora da cobertura declarada.

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
|---|---|---|---|
| [Gabriel Mota](https://github.com/Gabro-MO) | Vinculação das regras às equivalências e pendências observadas em H0 | 15/11/2026 | Não commitado |
