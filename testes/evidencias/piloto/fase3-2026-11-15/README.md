# Piloto da Fase 3 — 15/11

Registros de viabilidade com H0, separados da coleta definitiva. `creditos.json`, `ambiente.json`, `api.json` e `storage-metadados.json` descrevem procedimentos observados. Nenhum arquivo contém credenciais ou valores pessoais do storage/payload.

A SCA inclui inventário com URLs/hash dos 129 scripts estáticos carregados, relatório exportado do Retire.js 6.1.1 e cobertura. Somente caminhos locais do relatório foram reduzidos a nomes de arquivo; o hash do original foi preservado. Os scripts e o relatório original permanecem fora do Git. A amostra não identifica todas as dependências e não avalia o backend.

O relatório reconheceu pdf.js 5.4.624, sem achados reportados para esse componente. Não se calcula IRP global com esse resultado. Storage corresponde a um estado e API a uma comparação positiva/sem Authorization; não são GED-C ou TBR definitivos.
