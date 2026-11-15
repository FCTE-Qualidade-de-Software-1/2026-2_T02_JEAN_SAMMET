# Piloto e verificação de prontidão

## 1. Inspeção exploratória de 15/11

Foi acessada a conta de teste disponibilizada pelo usuário no Chrome, em `no-fluxo.crianex.com`. O fluxo observado foi **Meu Fluxograma → Planejar formatura → Preferências**, percorrendo as três etapas sem concluir a geração de um novo plano pelas preferências.

| Item | Observação | Efeito no plano de avaliação |
|---|---|---|
| Matriz | 6360/1 — 2017.1 identificada na interface. | Usar a mesma referência curricular nos casos. |
| Planejamento | Previsão, semestres restantes, matérias críticas e disciplinas em curso/futuras estão disponíveis. | Há informações observáveis para T1/T2 e para registrar a saída funcional. |
| Créditos | Exibidos controle deslizante, campo numérico e alternância Créditos/Horas; 24 créditos aparecem como 360h. | Conferir entrada, valor convertido e recálculo em CT-06/CT-07 e T3. Foi observado recálculo, mas a restauração visual ainda não foi validada com captura consistente. |
| Preferências | Trabalho/estágio; opções de 4/6/8 matérias, aproximadamente 240/360/480h; velocidade/equilíbrio; interesses opcionais. | Executar cenários pareados, alterando apenas um campo. Não inventar o efeito algorítmico de cada escolha. |
| Optativas | Existe aviso sobre horas reservadas sem disciplinas escolhidas. | Registrar reservas separadas da cobertura de obrigatórias. |
| Regras oficiais | Foram consultados os detalhes de FGA0211, MAT0026 e IFD0173 no SIGAA público. | Exemplos fundamentam o roteiro; não representam todas as relações da matriz. |

A sessão continha dados pessoais fornecidos para referência. Nenhum histórico pessoal, token, plano individual ou resultado acadêmico foi incluído nos arquivos do projeto. A única captura publicada dessa sessão foi recortada para mostrar somente o controle de créditos. Esta inspeção não produz notas TCH/ISVH, indicadores de segurança ou resultados funcionais definitivos.

## 2. Verificações de prontidão

| Verificação | Situação | Condição para prosseguir |
|---|---|---|
| PDF sintético | Rejeitado no teste relatado pelo usuário | Arquivos retirados; usar histórico oficial autorizado. Evidência na seção 4. |
| CT-01 e registro do plano | Pendente | Conferir relações disponíveis no histórico autorizado. Aplicar C0 e declarar as relações efetivamente cobertas; C1–C5 alteram apenas configurações do mesmo histórico. |
| Mudança e reversão de créditos | Parcial | Alteração e recálculo observados; a leitura de acessibilidade voltou a 24, mas a captura ficou defasada. Repetir a verificação visual antes da coleta formal. |
| Storage | Pendente | Inspecionar os estados antes/depois de carregar o histórico autorizado e gerar o plano. |
| SCA | Pendente | Confirmar scanner, relatório bruto e inventário dos componentes reconhecidos. |
| API | Pendente | Identificar URL, método, requisito e chamada positiva válida antes da bateria negativa. |

Durante a exploração, a automação do Chrome perdeu acesso ao conteúdo da página após recarregar. Não foi possível atribuir a causa ao site; essa interrupção não conta como falha do produto. A rota da API permanece não confirmada. O retorno posteriormente fornecido pelo usuário exige um histórico gerado pelo SIGAA/UnB. O código de referência também não pôde ser recuperado publicamente nesta consulta.

O plano está preparado para revisão, mas o piloto completo ainda não foi concluído. Os registros anteriores da Fase 4 precisam ser reavaliados pelos critérios corrigidos da Fase 2; não devem preencher automaticamente estas pendências.

## 3. Complemento do preparo

- **Fontes:** confirmado o par FGA0072/FGA0074 e a carga/equivalência de MAT0138. Capturas em [Fontes e regras](funcionais/fontes.md).
- **Entrada:** o PDF sintético foi rejeitado no teste relatado pelo usuário; os arquivos foram retirados. O histórico oficial autorizado H0 passa a ser a entrada, com cenários C0–C5 definidos no roteiro; os perfis fictícios foram removidos.
- **Instrumentos:** onze testes locais verificam ausência de relatório, duplicatas, altas em produção/desenvolvimento, controle positivo, HTTP 405 e cobertura parcial. Nenhum desses testes envia chamadas ao No Fluxo.
- **Limitação da sessão:** após a navegação, a barra de endereço e o conteúdo acessível divergiram; houve falha de captura e perda de janela durante a tentativa de avançar no reenvio. A importação não foi concluída nem houve confirmação de substituição do histórico. Não atribuir essa interrupção ao produto.
- **Acesso separado:** uma sessão nova no navegador de apoio redirecionou para login. Ela não compartilha a autenticação do Chrome e não foi usada para criar conta ou transferir credenciais.

![Controle de créditos observado durante a exploração](img/controle-creditos.png)

*Figura 1 — Recorte do controle em um estado intermediário: 14 créditos/210h. Fonte: No Fluxo, 15/11. A imagem documenta o instrumento de entrada; não comprova o resultado correto do plano nem a restauração final. Dados acadêmicos e identificação ficaram fora do recorte.*

**Situação:** preparação documental e instrumentos revisados; liberação da coleta ainda condicionada ao piloto com histórico oficial autorizado, inspeção de storage/SCA e validação da chamada da API. Responsáveis e datas da equipe continuam como proposta, não como aceite confirmado.

## 4. Rejeição do PDF de teste

Em 15/11, o usuário informou que o PDF sintético enviado foi rejeitado e forneceu a captura abaixo. A mensagem orienta baixar e enviar o histórico gerado no SIGAA/UnB. Os PDFs sintéticos foram retirados do projeto e dos entregáveis locais.

![Mensagem de rejeição do PDF de teste pelo No Fluxo](img/rejeicao-pdf-teste.png)

*Figura 2 — Rejeição da entrada preparada para o piloto. Fonte: captura fornecida por Gustavo, 15/11. A captura não identifica qual dos arquivos preparados foi enviado.*

O retorno comprova que o arquivo enviado não foi aceito. Não demonstra falha do planejamento nem impossibilidade de toda entrada sintética. Para este trabalho, o caminho dos PDFs sintéticos foi descartado. Usar o histórico oficial já autorizado e declarar os cenários sem entrada viável; editar disciplinas somente se houver recurso suportado pelo sistema. Esta evidência não gera nota para as doze métricas.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Registro da exploração do fluxo e das pendências do piloto sintético | 15/11 | [aa0c61f](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/aa0c61fac5e9d2db19adec76fd052a2bb6b04b90) |