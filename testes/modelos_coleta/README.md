# Modelos de coleta

Copiar os modelos para uma pasta identificada por execução em `testes/evidencias/`. Usar `tipo_coleta` para separar piloto e coleta definitiva. Cabeçalhos não são resultados: campos sem medição permanecem vazios, não zero.

- `execucoes.csv`: contexto, esperado/observado, cálculo e julgamento por caso.
- `verificacoes_funcionais.csv`: uma linha por disciplina ou relação examinada.
- `heuristicas.csv`: folhas individuais e consolidação identificadas separadamente.
- `seguranca.csv`: evidências de dependências, storage e acesso; não guardar credenciais.

Datas em ISO 8601 com fuso, por exemplo `2026-11-15T10:00:00-03:00`. Campos com vírgulas devem ser delimitados por aspas. Salvar capturas e relatórios junto da execução e referenciá-los na coluna `evidencia`.

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Criação dos modelos de coleta | 15/11 | Não commitado |
