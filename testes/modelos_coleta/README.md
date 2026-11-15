# Modelos de coleta

Copiar os modelos para uma pasta identificada por execução em `testes/evidencias/`. Usar `tipo_coleta` para separar piloto e coleta definitiva. Usar `entrada_id = H0` e `cenario_id = C0` a `C5` para distinguir o histórico da configuração aplicada. Cabeçalhos não são resultados: campos sem medição permanecem vazios, não zero.

- `execucoes.csv`: contexto, esperado/observado, cálculo e julgamento por caso.
- `verificacoes_funcionais.csv`: uma linha por disciplina ou relação examinada.
- `heuristicas.csv`: folhas individuais e consolidação identificadas separadamente.
- `seguranca.csv`: evidências de dependências, storage e acesso; não guardar credenciais.

Datas em ISO 8601 com fuso, por exemplo `2026-11-15T10:00:00-03:00`. Campos com vírgulas devem ser delimitados por aspas. Salvar capturas e relatórios junto da execução e referenciá-los na coluna `evidencia`.

## Apuração dos instrumentos de segurança

Copiar `sca.json` ou `tbr.json` para a pasta da execução e preencher a partir de evidências revisadas. Caminhos são relativos à pasta do relatório. Executar, a partir da raiz do repositório:

```bash
python3 testes/analisador_sca_irp.py caminho/execucao/sca.json
python3 testes/teste_controle_acesso_tbr.py caminho/execucao/tbr.json
```

Os comandos apenas apuram registros, não executam scanner ou chamadas HTTP; imprimem JSON e retornam código 2 para Inconclusivo. Não sobrescrevem evidências anteriores. Os modelos vazios devem resultar em Inconclusivo.

- **SCA:** informar ferramenta/base, cobertura, arquivo bruto, inventário (`componente`, `versao`) e achados (`componente`, `versao`, `aviso`, `severidade`, `ambiente`). Severidades: `critical`, `high`, `moderate`, `low`; ambiente: `producao`, `desenvolvimento` ou `desconhecido`. A chave componente/versão/aviso remove duplicatas; divergências impedem julgamento. Adaptar o formato bruto do scanner mediante revisão, preservando o original; contagens npm agregadas não substituem achados.
- **TBR:** validar alvo/método/payload, fonte do requisito e controle positivo. Em `casos`, registrar `id`, `status_http`, `condicao_validada`, `evidencia` e, se houver, `execucao_indevida_comprovada`. Cada evidência deve mostrar a condição isolada e o comportamento; os indicadores booleanos são conclusões da revisão, não provas por si só. Casos não executados ou erros permanecem inconclusivos. Não preencher tokens ou credenciais.

Verificar os instrumentos localmente com `python3 -m unittest testes.teste_instrumentos_seguranca`. Fixtures de teste não constituem resultados do No Fluxo.

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Criação dos modelos de coleta | 15/11 | [aa0c61f](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/aa0c61fac5e9d2db19adec76fd052a2bb6b04b90) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Instruções dos instrumentos e modelos de segurança | 15/11 | [0e38da3](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/0e38da3eac882c62bf7c6f9e1bda97a8b744ef2e) |
