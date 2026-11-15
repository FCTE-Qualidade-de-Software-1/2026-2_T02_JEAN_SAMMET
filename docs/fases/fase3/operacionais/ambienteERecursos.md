# Ambiente e massa de dados

## 1. Ambiente exploratório

| Item | Registro de 15/11 |
|---|---|
| Instância | `https://no-fluxo.crianex.com` |
| Matriz | 6360/1 — 2017.1 |
| Navegador instalado | Google Chrome 157.0.8103.52 |
| Sistema | macOS 27.0.1, arquitetura arm64 |
| Sessão | Conta de teste já autenticada, em perfil normal do Chrome |
| Extensão de automação | Instalada pelo usuário; interferências não foram quantificadas |
| Hardware, viewport e zoom | Ainda não registrados integralmente; conferir antes da coleta formal |
| Versão implantada | Desconhecida; não associar automaticamente ao commit `87b5475` |

Esta ficha descreve a exploração, não uma configuração certificada. Antes da coleta formal, registrar versões, resolução, viewport, zoom, extensões, rede e condições de sessão. Manter as mesmas condições nos cenários pareados; qualquer mudança deve constar no registro.

## 2. Dados para a avaliação

O PDF sintético preparado para o piloto foi rejeitado pelo importador, conforme [evidência do piloto](../piloto.md#4-rejeicao-do-pdf-de-teste). Os dois PDFs de teste foram retirados. O sistema orienta utilizar o histórico gerado pelo SIGAA/UnB.

A entrada prevista passa a ser o **histórico oficial já fornecido e autorizado pelo usuário**, mantido fora do repositório. Publicar apenas verificações e evidências sanitizadas. Os antigos perfis fictícios foram substituídos por H0, o histórico autorizado, e C0–C5, configurações de uso do mesmo histórico. A especificação fica em `testes/cenarios_avaliacao.json`, sem dados pessoais.

## 3. Preparação da entrada

1. Usar o histórico oficial autorizado e conferir os códigos e status reconhecidos pelo sistema, sem versionar o documento.
2. Identificar quais casos funcionais podem ser verificados com esse histórico. Recalcular a lista esperada de pendências a partir da entrada real; não existe denominador fixo para essa entrada.
3. Verificar se existe edição de disciplinas/status suportada pelo produto. Somente se esse recurso for confirmado, executar variações controladas por ele; não preparar novos PDFs sintéticos.
4. Casos que exijam dados indisponíveis permanecem pendentes ou inconclusivos, com a cobertura declarada. Não apresentar as configurações de uso como históricos acadêmicos diferentes.
5. Nas comparações de preferências, manter o histórico fixo, registrar mudanças e verificar a restauração. Sanitizar capturas antes de publicar.

## 4. Ferramentas

Chrome e DevTools para interface, tráfego e storage; Retire.js ou scanner equivalente documentado para cliente; `npm audit` apenas quando os manifestos estiverem disponíveis. Exportar o relatório bruto e o inventário da SCA.

Os instrumentos `testes/analisador_sca_irp.py` e `testes/teste_controle_acesso_tbr.py` foram corrigidos e verificados com testes locais. Ambos apuram relatórios revisados; não executam scanner nem requisições. Usar os modelos `sca.json` e `tbr.json` em `testes/modelos_coleta/`. A cobertura, o relatório bruto e as evidências devem existir antes do cálculo. Dados ausentes produzem Inconclusivo; a TBR exige controle positivo e não interpreta HTTP 405 como acesso indevido. Essas verificações do instrumento não são resultados do No Fluxo.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Especificação de hardware, software, isolamento, massa sintética LGPD e matriz de papéis | 14/11/2026 | [6594e5c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/6594e5c2349ee5fc4dc632f07b97bc8191357819) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Registro do ambiente observado e preparação dos perfis sintéticos | 15/11 | [aa0c61f](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/aa0c61fac5e9d2db19adec76fd052a2bb6b04b90) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Substituição da massa fictícia por entrada autorizada e configurações de uso | 15/11 | [0e38da3](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/0e38da3eac882c62bf7c6f9e1bda97a8b744ef2e) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Padronização da entrada H0 | 15/11 | Não commitado |
