# Piloto e verificação de prontidão

## 1. Entrada e fluxo verificados em 15/11

O histórico oficial **H0** foi enviado manualmente por Gustavo à conta de teste. A tela mostrou **Processamento concluído**, matriz 6360/1 e semestre 2026.2. O resumo apresentou 39 obrigatórias, 24 concluídas, 15 pendentes e 2.130h/3.480h integralizadas, compatíveis com a referência sanitizada. Esses totais não substituem a conferência individual dos 44 registros e das 8 equivalências na Fase 4.

![Importação do histórico oficial concluída](img/importacao-h0.png)

*Figura 1 — Resumo de H0 aceito. Fonte: No Fluxo, 15/11. Recorte sem identificação, índices acadêmicos ou nome do arquivo.*

O fluxo **Visualizar fluxograma → Planejar formatura → Preferências** foi acessado; o assistente de três etapas e o plano gerado ficaram observáveis. Foram aceitas as configurações **24 créditos/360h**, **20/300h** e **32/480h**, com recálculo. A base foi restaurada para **24/360h**, sem indicador de recálculo pendente. Isso confirma a operação dos controles, sem julgar a correção de todas as alocações.

![Carga menor verificada no piloto](img/creditos-20.jpg)

*Figura 2 — Controle em 20 créditos/300h após o recálculo. Fonte: No Fluxo, 15/11.*

![Carga maior verificada no piloto](img/creditos-32.jpg)

*Figura 3 — Controle em 32 créditos/480h após o recálculo. Fonte: No Fluxo, 15/11.*

![Carga-base restaurada](img/creditos-24.jpg)

*Figura 4 — Controle restaurado para 24 créditos/360h. Fonte: No Fluxo, 15/11.*

## 2. Condições para encerrar o preparo

| Frente | Verificação do piloto | Encaminhamento para a Fase 4 |
|---|---|---|
| Entrada e planejamento | H0 aceito; plano e controles acessíveis; C1/C2 aceitos e base restaurada | Gabriel confere CT-01 a CT-07 por unidade e registra cobertura. |
| Usabilidade | Tarefas e checklist disponíveis; dupla Gustavo/Gabriel definida | Alinhar severidade e realizar duas inspeções independentes antes do consenso. |
| Ambiente | Viewport, zoom, hardware, sessão e estimativas de rede registrados | Cada avaliador registra seu ambiente; a versão do servidor permanece desconhecida. |
| SCA | Retire.js 6.1.1 executado sobre 129 scripts estáticos carregados; pdf.js 5.4.624 reconhecido | Giovani registra cobertura e limitações. O reconhecimento de um componente não cobre todas as dependências nem o backend. |
| Storage | Acesso a localStorage, sessionStorage e cookies confirmado; somente metadados exportados | Giovani coleta os três estados e classifica as chaves sem publicar valores pessoais. |
| API | POST real do planejamento retornou 200; mesma chamada sem Authorization retornou 401 | Giovani repete o controle e executa somente casos cujas pré-condições estejam atendidas. A bateria completa ainda não foi coletada. |

**Fase 3 concluída no escopo de preparação:** procedimentos, recursos, responsáveis e viabilidade básica verificados. A conclusão não significa aprovação das métricas nem cobertura integral dos casos. Condições ausentes permanecem Sem cobertura/Inconclusivo na Fase 4; não preencher resultados automaticamente.

O prazo é **22/11**. As **23h** continuam como estimativa de planejamento e as **7h** informadas por Gustavo como esforço realizado parcial no PSM. Não foram acrescentadas horas reais sem novo apontamento.

## 3. Evidências e limites

Os registros sanitizados do piloto ficam em `testes/evidencias/piloto/fase3-2026-11-15/`: ambiente, créditos, API, metadados de storage, inventário dos scripts, cobertura e relatório do scanner. PDF, tokens, payload acadêmico e valores de armazenamento não foram incluídos nos arquivos versionados.

A chamada observada é `POST https://api-nofluxo.crianex.com/planejamento/gerar-plano`, com token direto em Authorization, sem prefixo Bearer. O corpo possui `curriculo_completo`, `codigos_concluidos`, `semestre_atual` e `limite_creditos`. A verificação sem Authorization preservou método, corpo e User-ID. Não se calculou TBR a partir desse único teste.

O scanner foi validado conforme sua [documentação oficial](https://github.com/RetireJS/retire.js/blob/master/node/README.md). Seu relatório reconheceu pdf.js 5.4.624 sem achados reportados para esse componente. Isso não equivale a IRP global igual a zero: dependências não reconhecidas, outros fluxos e backend não estão cobertos.

C0–C5 mantêm H0 fixo. A seleção do par de optativas de CT-02 deve ser confirmada antes de sua coleta; se indisponível, registrar Sem cobertura. As regras oficiais estão em [Fontes e regras](funcionais/fontes.md). Interpretações de carga sugerida, oferta/calendário e políticas sem fonte não serão convertidas em defeitos.

As falhas anteriores de controle do Chrome foram superadas pela conexão da extensão. As capturas recuperadas de Gabriel permanecem em [Execução anterior](../fase4/funcionais/execucaoAnterior.md), separadas dos resultados de H0.

## 4. Rejeição do PDF de teste

O PDF sintético enviado no teste relatado por Gustavo foi rejeitado. O importador exige o histórico oficial gerado pelo SIGAA/UnB. Os arquivos sintéticos foram retirados; H0 foi aceito e é a entrada adotada.

![Rejeição do PDF de teste](img/rejeicao-pdf-teste.png)

*Figura 5 — Captura fornecida por Gustavo, 15/11. Comprova a rejeição dessa entrada, sem gerar nota para as métricas.*

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Registro da exploração do fluxo e das pendências do piloto sintético | 15/11 | [aa0c61f](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/aa0c61fac5e9d2db19adec76fd052a2bb6b04b90) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Padronização da entrada H0 | 15/11 | [f454d2c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f454d2c099e16a6dd593b92420b541a18262b086) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Registro do piloto com H0, responsáveis e condições restantes de prontidão | 15/11 | [f454d2c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/f454d2c099e16a6dd593b92420b541a18262b086) |
