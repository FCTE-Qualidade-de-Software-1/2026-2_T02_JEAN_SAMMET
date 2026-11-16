# Métodos de avaliação operacional

## 1. Usabilidade — TCH e ISVH

Gustavo e Gabriel percorrem T1–T3 independentemente, com a mesma entrada autorizada e ambiente, e preenchem os dez itens do [checklist da Fase 2](../../fase2/operacionais/usabilidade.md). Para cada violação, registrar descrição, tarefa, severidade 1–4 e evidência. Depois, consolidar em consenso, preservando notas individuais e justificativas de divergência.

`TCH = itens conformes / 10 × 100`. `ISVH = 4 × Ncatastrofico + 3 × Nmaior + 2 × Nmenor + Ncosmetico`. Os limites são os da Fase 2; não atribuir uma nota final a partir de uma única exploração.

## 2. Dependências — IRP

Inspecionar os scripts efetivamente carregados no cliente, com Retire.js e inventário de arquivos/versões. Registrar achados únicos por componente, versão e aviso. Auditar manifestos públicos separadamente, quando disponíveis; não somar coberturas sobrepostas.

`IRP = 10 × Ncritica + 5 × Nalta + 2 × Nmoderada + Nbaixa`. Ausência de relatório, cobertura desconhecida ou erro do scanner gera Inconclusivo. O resultado do cliente não avalia o backend. Separar produção e desenvolvimento quando verificável.

No piloto, Retire.js 6.1.1 processou 129 scripts estáticos carregados e reconheceu pdf.js 5.4.624. Relatório, hashes e cobertura estão em `testes/evidencias/piloto/fase3-2026-11-15/`. Dependências não reconhecidas e backend ficam fora dessa cobertura. Não converter ausência de achados em aprovação global.

## 3. Armazenamento — GED-C

Inspecionar `localStorage`, `sessionStorage` e cookies em três estados: sessão inicial, após carregar o histórico autorizado e após gerar o plano. Registrar origem, mecanismo, chave, tipo de conteúdo e evidência sanitizada. Identificar cada chave pela origem, mecanismo e nome; no consolidado, contar a mesma chave uma vez, mesmo se aparecer em vários estados. Contar apenas chaves com dado pessoal/acadêmico em claro, sem copiar os valores pessoais para a documentação. Verificar flags no painel de cookies, sem publicar seus valores de autenticação.

A viabilidade da leitura dos três mecanismos foi confirmada no piloto, sem exportar valores. O registro atual corresponde a H0 já carregado e plano gerado; os três estados completos ainda serão coletados na Fase 4. A sessão inicial deve declarar se já contém dados persistidos; não presumir armazenamento vazio nem apagar dados ou credenciais para fabricar uma linha de base.

`GED-C = quantidade de chaves com dados em claro`. Uma coleta parcial não pode receber Conforme. As flags de cookie não demonstram criptografia do conteúdo nem conformidade legal.

## 4. Acesso — TBR

O piloto confirmou `POST https://api-nofluxo.crianex.com/planejamento/gerar-plano`: resposta 200 com autenticação e 401 sem Authorization, preservando método, corpo e User-ID. O cliente enviou o token diretamente no cabeçalho, **sem prefixo Bearer**. O corpo contém `curriculo_completo`, `codigos_concluidos`, `semestre_atual` e `limite_creditos`. Metadados em `testes/evidencias/piloto/fase3-2026-11-15/api.json`; valores e credenciais não são publicados. Essa comparação valida o procedimento e não representa a bateria definitiva.

Na coleta formal, observar novamente a chamada real usada ao gerar o plano. Confirmar a operação protegida, domínio, método, payload e chamada positiva autorizada. Somente depois executar os casos negativos, com a conta autorizada. Se a operação exigir dados acadêmicos, restringir o payload ao mínimo necessário já autorizado e não publicar seus valores.

| Caso | Condição | Cuidados para validar o teste |
|---|---|---|
| REQ-01 | Sem Authorization | Preservar método e payload válidos |
| REQ-02 | Authorization vazio | Diferenciar header vazio de ausente |
| REQ-03 | Prefixo inesperado, como Basic | Serviço observado recebe token direto em Authorization |
| REQ-04 | Bearer sem token | Não há credencial JWT; Bearer acompanhado de token válido não é chamada negativa por si só |
| REQ-05 | Token malformado | Registrar resposta, sem reutilizar credencial pessoal |
| REQ-06 | Assinatura inválida | Token de teste com estrutura apropriada |
| REQ-07 | Token expirado | Credencial de teste cuja assinatura seja verificável; assinatura falsa não isola expiração |
| REQ-08 | Token sem assinatura | Aplicável somente ao mecanismo observado |
| REQ-09 | Papel insuficiente | Usuário de teste autenticado sem a permissão necessária |
| REQ-10 | Token revogado | Credencial de teste revogada; se o fluxo não existir, substituir por caso aplicável, antes da coleta |

A bateria acima é proposta. Antes da coleta, confirmar o contrato do mecanismo, incluindo a aceitação de Bearer: o piloto observou token direto, mas não provou que esse seja o único formato aceito. Preparar tokens controlados para REQ-06/07/08/10 e usuário/papel apropriado para REQ-09. Sem essas condições, registrar Sem cobertura/Inconclusivo, sem simular validade ou completar dez casos artificialmente. Credenciais necessárias ainda devem ser preparadas. Não fabricar uma assinatura e apresentar o teste como validação de permissões. Enviar `Origin` em Python, por si só, não testa a aplicação de CORS pelo navegador.

`TBR = bloqueios 401/403 / chamadas negativas válidas × 100`. Informar bateria planejada, válida e inconclusiva. HTTP 404/405, falha de conexão ou HTTP 500 sem prova de acesso não demonstram falha de autenticação. Sem operação protegida no recorte, registrar Não aplicável com fonte. Aplicar os [critérios completos](../../fase2/operacionais/seguranca.md).

---

## Histórico de versão

| Nome do Membro | Contribuição | Data | Commit |
| :--- | :--- | :--- | :--- |
| [Giovani De Oliveira Teodoro Coelho](https://github.com/Gotc2607) | Especificação detalhada dos métodos de Usabilidade (Nielsen) e Segurança (SCA, Storage e Matriz de 10 testes de API) | 14/11/2026 | [6594e5c](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/6594e5c2349ee5fc4dc632f07b97bc8191357819) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Alinhamento dos métodos aos critérios e à validade das coletas | 15/11 | [aa0c61f](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/aa0c61fac5e9d2db19adec76fd052a2bb6b04b90) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Registro da viabilidade de SCA/storage/API e adequação da bateria ao token observado | 15/11 | [7a74d9e](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_JEAN_SAMMET/commit/7a74d9e0809e91d60a36a88559b357bfe171f37e) |
| [Gustavo Fornaciari](https://github.com/GUGOFO) | Adequação do caso sem token à bateria executada | 15/11 | Não commitado |
