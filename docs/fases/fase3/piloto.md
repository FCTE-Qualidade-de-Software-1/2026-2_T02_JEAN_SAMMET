# Piloto e verificação de prontidão

## 1. Inspeção exploratória de 15/11

Foi acessada a conta de teste disponibilizada pelo usuário no Chrome, em `no-fluxo.crianex.com`. O fluxo observado foi **Meu Fluxograma → Planejar formatura → Preferências**, percorrendo as três etapas sem concluir a geração de um novo plano pelas preferências.

| Item | Observação | Efeito no plano de avaliação |
|---|---|---|
| Matriz | 6360/1 — 2017.1 identificada na interface. | Usar a mesma referência curricular nos casos. |
| Planejamento | Previsão, semestres restantes, matérias críticas e disciplinas em curso/futuras estão disponíveis. | Há informações observáveis para T1/T2 e para registrar a saída funcional. |
| Créditos | Exibidos controle deslizante, campo numérico e alternância Créditos/Horas; 24 créditos aparecem como 360h. | Conferir entrada, valor convertido e recálculo em CT-06/CT-07 e T3. A alteração e reversão ainda não foram validadas. |
| Preferências | Trabalho/estágio; opções de 4/6/8 matérias, aproximadamente 240/360/480h; velocidade/equilíbrio; interesses opcionais. | Executar cenários pareados, alterando apenas um campo. Não inventar o efeito algorítmico de cada escolha. |
| Optativas | Existe aviso sobre horas reservadas sem disciplinas escolhidas. | Registrar reservas separadas da cobertura de obrigatórias. |
| Regras oficiais | Foram consultados os detalhes de FGA0211, MAT0026 e IFD0173 no SIGAA público. | Exemplos fundamentam o roteiro; não representam todas as relações da matriz. |

A sessão continha dados pessoais fornecidos para referência. Nenhum histórico pessoal, token, captura dessa sessão ou resultado acadêmico individual foi incluído nos arquivos do projeto. Esta inspeção não produz notas TCH/ISVH, indicadores de segurança ou resultados funcionais definitivos.

## 2. Piloto ainda necessário com dados sintéticos

| Verificação | Situação | Condição para prosseguir |
|---|---|---|
| Importação/preenchimento de P1 | Pendente | Confirmar modo aceito, carregar os códigos e conferir status sem usar histórico pessoal. |
| CT-01 e registro do plano | Pendente | Executar P1/P2 e salvar evidências suficientes para conferir a ordem de MAT0026. |
| Mudança e reversão de créditos | Pendente | Registrar valor anterior, alteração, recálculo e retorno ao valor inicial. |
| Storage | Pendente | Inspecionar estado antes/depois de carregar massa e gerar plano. |
| SCA | Pendente | Confirmar scanner, relatório bruto e inventário dos componentes reconhecidos. |
| API | Pendente | Identificar URL, método, requisito e chamada positiva válida antes da bateria negativa. |

Durante a exploração, a automação do Chrome perdeu acesso ao conteúdo da página após recarregar. Não foi possível atribuir a causa ao site; essa interrupção não conta como falha do produto. A rota da API e o formato real de importação permanecem não confirmados. O código de referência também não pôde ser recuperado publicamente nesta consulta.

O plano está preparado para revisão, mas o piloto completo ainda não foi concluído. Os registros anteriores da Fase 4 precisam ser reavaliados pelos critérios corrigidos da Fase 2; não devem preencher automaticamente estas pendências.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Registro da exploração do fluxo e das pendências do piloto sintético | 15/11 | [aa0c61f](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/aa0c61fac5e9d2db19adec76fd052a2bb6b04b90) |
