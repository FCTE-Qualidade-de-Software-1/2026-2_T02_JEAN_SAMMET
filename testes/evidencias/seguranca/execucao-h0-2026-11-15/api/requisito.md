# Requisito e alcance do teste de acesso

O critério da equipe na Fase 2 exige autenticação para a operação de planejamento examinada com dados acadêmicos da conta. A Fase 3 identificou a rota real e o controle positivo. A coleta usa exclusivamente a conta de teste e o payload válido do próprio H0, sem acessar dados de outra pessoa.

Alvo observado: POST `https://api-nofluxo.crianex.com/planejamento/gerar-plano`. O cliente envia Authorization com token e User-ID; o controle autenticado devolveu 200 e plano estruturado. Cada teste preservou método, payload e User-ID, alterando somente a condição de Authorization. Credenciais e payload acadêmico não são publicados; o hash do payload permite conferir igualdade entre os registros.

O plano identifica dez condições antes desta bateria. REQ-07, REQ-09 e REQ-10 não foram executadas por falta de token expirado com assinatura válida, usuário/papel apropriado e token revogado. Alterar claims e deixar a assinatura inválida não isola essas condições. REQ-04 testa Bearer sem token; um Bearer acompanhado de token válido não seria uma chamada negativa por si só.

Fontes: docs/fases/fase2/operacionais/seguranca.md e docs/fases/fase3/operacionais/metodos.md. A aplicação deste critério não afirma que toda rota pública do produto exija autenticação.
