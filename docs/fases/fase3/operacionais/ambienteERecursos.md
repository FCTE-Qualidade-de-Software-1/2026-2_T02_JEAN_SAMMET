# Ambiente e massa de dados

## 1. Ambiente exploratório

**Tabela 1 — Ambiente exploratório.**

| Item | Registro de 15/11 |
| --- | --- |
| Instância | `https://no-fluxo.crianex.com` |
| Matriz | 6360/1 — 2017.1 |
| Navegador instalado | Google Chrome 157.0.8103.52 |
| Sistema | macOS 27.0.1, arquitetura arm64 |
| Sessão | Conta de teste já autenticada, em perfil normal do Chrome |
| Extensão de automação | ChatGPT conectada ao Chrome; acesso à aba e inspeção técnica validados |
| Hardware | Apple M5, 16 GB de memória; modelo Mac17,3 |
| Viewport e zoom | 1470 × 779 CSS px; zoom 100%; DPR 2 |
| Tela reportada | 1470 × 956 CSS px; não confundir com resolução física do painel |
| Rede reportada | Online; effectiveType 4g, RTT estimado 100 ms e downlink estimado 10 Mb/s; não é teste de velocidade |
| Identificação do cliente | Inventário de 129 scripts estáticos com URL e SHA-256 no piloto |
| Versão do servidor | Não identificada; não associar automaticamente a um commit |

*Fonte: elaboração da equipe, conforme os registros e referências desta página.*

Esta ficha registra as condições observadas no piloto. Cada avaliador deve registrar seu próprio ambiente antes da coleta formal. Manter as mesmas condições nos cenários pareados; qualquer mudança deve constar no registro.

## 2. Dados para a avaliação

O PDF sintético preparado para o piloto foi rejeitado pelo importador, conforme a [captura de rejeição](../img/rejeicao-pdf-teste.png). Os dois PDFs de teste foram retirados. O sistema orienta utilizar o histórico gerado pelo SIGAA/UnB.

A entrada prevista passa a ser o **histórico oficial já fornecido e autorizado pelo usuário**, mantido fora do repositório. Publicar apenas verificações e evidências sanitizadas. Os antigos perfis fictícios foram substituídos por H0, o histórico autorizado, e C0–C5, configurações de uso do mesmo histórico. A especificação fica em `testes/cenarios_avaliacao.json`, sem dados pessoais.

## 3. Preparação da entrada

1. Usar o histórico oficial autorizado e conferir os códigos e status reconhecidos pelo sistema, sem versionar o documento.
2. Identificar quais casos funcionais podem ser verificados com esse histórico. Conferir a importação contra a referência sanitizada de H0: 44 registros acadêmicos, 15 obrigatórias pendentes e 8 relações de equivalência (6 concluídas e 2 em andamento). Esses universos são específicos de H0; não são resultados medidos no produto.
3. Aplicar C0–C5 mantendo H0 fixo e alterando somente as configurações previstas no roteiro. Edição de disciplinas/status fica fora desses cenários; só poderá integrar uma ampliação documentada após confirmar suporte no produto.
4. Casos que exijam dados indisponíveis permanecem pendentes ou inconclusivos, com a cobertura declarada. Não apresentar as configurações de uso como históricos acadêmicos diferentes.
5. Nas comparações de preferências, manter o histórico fixo, registrar mudanças e verificar a restauração. Sanitizar capturas antes de publicar.

O histórico oficial foi aceito no piloto. Os arquivos de referência e os modelos permanecem separados dos resultados de execução.

## 4. Ferramentas

Chrome/extensão e inspeção técnica para interface, tráfego e storage; Retire.js 6.1.1 validado sobre 129 scripts estáticos carregados no cliente; `npm audit` apenas quando os manifestos estiverem disponíveis. Exportar o relatório e o inventário da SCA. O piloto reconheceu pdf.js 5.4.624; a cobertura não corresponde a todas as dependências. Os registros sanitizados estão em `testes/evidencias/piloto/fase3-2026-11-15/`.

Os instrumentos `testes/analisador_sca_irp.py` e `testes/teste_controle_acesso_tbr.py` foram corrigidos e verificados com testes locais. Ambos apuram relatórios revisados; não executam scanner nem requisições. Usar os modelos `sca.json` e `tbr.json` em `testes/modelos_coleta/`. A cobertura, o relatório bruto e as evidências devem existir antes do cálculo. Dados ausentes produzem Inconclusivo; a TBR exige controle positivo e não interpreta HTTP 405 como acesso indevido. Essas verificações do instrumento não são resultados do No Fluxo.

## 5. Referências

Referências usadas nesta página, conforme [Referências — Fase 1](../../../referencias/fase1.md), [Referências — Fase 2](../../../referencias/fase2.md) e [Referências — Fase 3](../../../referencias/fase3.md).

- NO FLUXO UNB. **No Fluxo UnB**. Crianex, [s. d.]. Disponível em: [aplicação No Fluxo UnB](https://no-fluxo.crianex.com). Acesso em: 15 out. 2026.
- NPM, INC. **npm-audit**: documentation and command-line security auditing for Node.js packages. npm Docs, 2026. Disponível em: <https://docs.npmjs.com/cli/commands/npm-audit>.
- UNIVERSIDADE DE BRASÍLIA. **SIGAA — Estruturas curriculares de Engenharia de Software**, matriz 6360/1 — 2017.1. [Consulta pública](https://sigaa.unb.br/sigaa/public/curso/curriculo.jsf?id=414924&lc=pt_BR). Acesso em: 15 nov. 2026. Nos detalhes, consultar os componentes FGA0211, MAT0026 e IFD0173 e seus históricos de vigência.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Especificação de hardware, software, isolamento, massa sintética LGPD e matriz de papéis | 14/11 | [6594e5c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/6594e5c2349ee5fc4dc632f07b97bc8191357819) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Registro do ambiente observado e preparação dos perfis sintéticos | 15/11 | [aa0c61f](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/aa0c61fac5e9d2db19adec76fd052a2bb6b04b90) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Substituição da massa fictícia por entrada autorizada e configurações de uso | 15/11 | [0e38da3](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/0e38da3eac882c62bf7c6f9e1bda97a8b744ef2e) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Padronização da entrada H0 | 15/11 | [f454d2c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f454d2c099e16a6dd593b92420b541a18262b086) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Consolidação do preparo com H0, piloto e rastreabilidade das evidências | 15/11 | [7a74d9e](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/7a74d9e0809e91d60a36a88559b357bfe171f37e) |
| [Yasmim de Souza Santos](https://github.com/eii-yahs) | Inclusão das referências utilizadas na página | 22/11 | Não commitado |
