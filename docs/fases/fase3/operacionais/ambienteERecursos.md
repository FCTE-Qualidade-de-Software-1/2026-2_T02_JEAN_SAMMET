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

## 2. Dados sintéticos

Os perfis em `testes/massa_dados_sintetica.json` são cenários parciais controlados, não históricos completos de alunos do quinto ou sétimo semestre. Foram corrigidos códigos, nomes e totais usando a matriz oficial.

| Perfil | Aprovações | Créditos concluídos | Situação de teste |
|---|---|---|---|
| P1 | FGA0161, FGA0163, FGA0168 e MAT0025 | 18, correspondentes a 270h | Base com Cálculo 1 aprovado; MAT0026 pendente |
| P2 | FGA0161, FGA0163 e FGA0168 | 12, correspondentes a 180h | Cálculo 1 reprovado e Física 1 Experimental em andamento |

As demais disciplinas permanecem pendentes. Dados de identificação são fictícios. O JSON organiza a entrada e as verificações; **não há confirmação de importação direta de JSON pelo No Fluxo**.

## 3. Preparação da entrada

1. Registrar o estado da conta de teste e o perfil escolhido antes de substituir a matriz.
2. No fluxo de envio, verificar se há preenchimento manual. Se houver, inserir apenas os códigos/status do perfil e conferir o resultado. Esse caminho ainda precisa ser validado no piloto.
3. Se apenas PDF for aceito, preparar um histórico totalmente sintético com estrutura compatível e validar sua leitura. Não enviar o JSON renomeado para PDF nem publicar o histórico pessoal.
4. Conferir nomes/códigos, aprovações, reprovações, disciplinas em andamento e totais. Preservar evidência sanitizada da entrada.
5. Usar as mesmas preferências e período nos cenários pareados. Registrar alterações e restaurar a condição inicial ao terminar.

## 4. Ferramentas

Chrome e DevTools para interface, tráfego e storage; Retire.js ou scanner equivalente documentado para cliente; `npm audit` apenas quando os manifestos estiverem disponíveis. Exportar o relatório bruto e o inventário da SCA.

Os scripts existentes `analisador_sca_irp.py` e `teste_controle_acesso_tbr.py` ainda precisam ser adequados aos critérios revisados da Fase 2 antes de sustentar uma coleta: o primeiro aceita relatórios ausentes como zero e o segundo classifica erros HTTP como falhas de acesso. Até a correção, usar apuração manual conferida; não tomar a classificação automática como julgamento válido.

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Especificação de hardware, software, isolamento, massa sintética LGPD e matriz de papéis | 14/11/2026 | [6594e5c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/6594e5c2349ee5fc4dc632f07b97bc8191357819) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Registro do ambiente observado e preparação dos perfis sintéticos | 15/11 | Não commitado |
