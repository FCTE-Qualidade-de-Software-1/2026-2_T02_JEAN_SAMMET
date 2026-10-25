"""Testes unitários essenciais para os cálculos PSM/CID.

Executar na raiz do repositório:
python3 -m unittest discover -s testes -t . -p 'teste_*.py' -v
"""
import unittest
from datetime import datetime, timedelta, timezone

from scripts.metricas.avaliacao import avaliar_ciclo, avaliar_tct, avaliar_tsa
from scripts.metricas.calculo_burndown import calcular_burndown, contar_restantes, valor_ideal
from scripts.metricas.calculo_ciclo import calcular_ciclo, ResultadoCiclo
from scripts.metricas.calculo_tct import calcular_tct, ResultadoTct
from scripts.metricas.calculo_tsa import calcular_tsa, ultima_atividade, ResultadoTsa
from scripts.metricas.conversao_evento import ator_e_automacao, converter_evento, extrair_instante
from scripts.metricas.estado_issue import esta_aberta_em, concluida_em
from scripts.metricas.formatacao import decimal, percentual, dias, data
from scripts.metricas.linha_de_base import definir_linha_de_base
from scripts.metricas.modelos import Evento, Issue, Marco
from scripts.metricas.tabelas_markdown import escapar, tabela, link_da_issue
from scripts.metricas.tempo import ler_instante, dia_local, dias_entre, sequencia_de_dias

UTC = timezone.utc


def instante(dia: int, hora: int = 12, minuto: int = 0) -> datetime:
    return datetime(2026, 10, dia, hora, minuto, tzinfo=UTC)


def issue(numero: int, aberta: datetime | None = None, fechada: datetime | None = None,
          eventos: tuple[Evento, ...] = (), rotulos: tuple[str, ...] = ()) -> Issue:
    return Issue(
        numero=numero,
        titulo=f"Issue {numero}",
        url=f"https://github.com/exemplo/repo/issues/{numero}",
        aberta_em=aberta or instante(15),
        fechada_em=fechada,
        rotulos=rotulos,
        eventos=eventos,
    )


def marco(criado: datetime | None = None, prazo: datetime | None = None,
          encerrado: datetime | None = None, estado: str = "open") -> Marco:
    return Marco(
        numero=1,
        titulo="Fase 1",
        url="https://github.com/exemplo/repo/milestone/1",
        estado=estado,
        criado_em=criado or instante(15),
        prazo=prazo,
        encerrado_em=encerrado,
    )


class TesteTempoEFormatacao(unittest.TestCase):
    def test_le_instante_com_z_e_converte_para_utc(self):
        valor = ler_instante("2026-10-15T12:00:00Z")
        self.assertEqual(valor, instante(15))
        self.assertEqual(valor.utcoffset(), timedelta(0))

    def test_dia_local_considera_fuso_de_sao_paulo(self):
        self.assertEqual(dia_local(datetime(2026, 10, 25, 2, 0, tzinfo=UTC)).day, 24)

    def test_dias_entre_calcula_fracao_de_dia(self):
        self.assertEqual(dias_entre(instante(15), instante(16, 0)), 0.5)

    def test_sequencia_de_dias_inclui_inicio_e_fim(self):
        from datetime import date
        self.assertEqual(
            sequencia_de_dias(date(2026, 10, 15), date(2026, 10, 17)),
            [date(2026, 10, 15), date(2026, 10, 16), date(2026, 10, 17)],
        )

    def test_formatacao_decimal_usa_virgula(self):
        self.assertEqual(decimal(12.5, 1), "12,5")

    def test_percentual_de_valor_nulo_e_nao_aplicavel(self):
        self.assertEqual(percentual(None), "Não aplicável")

    def test_percentual_formata_duas_casas(self):
        self.assertEqual(percentual(75), "75,00%")

    def test_dias_de_valor_nulo_e_nao_aplicavel(self):
        self.assertEqual(dias(None), "Não aplicável")

    def test_data_sem_instante_informa_ausencia_de_prazo(self):
        self.assertEqual(data(None), "Sem prazo definido")


class TesteConversaoDeEventos(unittest.TestCase):
    def test_extrai_created_at(self):
        valor = extrair_instante({"created_at": "2026-10-15T12:00:00Z"})
        self.assertEqual(valor, instante(15))

    def test_extrai_submitted_at_quando_created_at_nao_existe(self):
        valor = extrair_instante({"submitted_at": "2026-10-16T12:00:00Z"})
        self.assertEqual(valor, instante(16))

    def test_extrai_data_do_committer(self):
        valor = extrair_instante({"committer": {"date": "2026-10-17T12:00:00Z"}})
        self.assertEqual(valor, instante(17))

    def test_identifica_ator_bot(self):
        self.assertTrue(ator_e_automacao({"type": "Bot", "login": "actions"}))
        self.assertTrue(ator_e_automacao({"type": "User", "login": "renovate[bot]"}))

    def test_nao_identifica_pessoa_como_bot(self):
        self.assertFalse(ator_e_automacao({"type": "User", "login": "ana"}))
        self.assertFalse(ator_e_automacao(None))

    def test_evento_sem_tipo_ou_data_e_ignorado(self):
        self.assertIsNone(converter_evento({"event": "commented"}))
        self.assertIsNone(converter_evento({"created_at": "2026-10-15T12:00:00Z"}))

    def test_converte_evento_e_marco(self):
        evento = converter_evento({
            "event": "milestoned",
            "created_at": "2026-10-15T12:00:00Z",
            "milestone": {"title": "Fase 1"},
            "actor": {"login": "ana", "type": "User"},
        })
        self.assertIsNotNone(evento)
        self.assertEqual(evento.tipo, "milestoned")
        self.assertEqual(evento.marco, "Fase 1")
        self.assertFalse(evento.automacao)


class TesteLinhaDeBase(unittest.TestCase):
    def test_sem_issues_produz_linha_de_base_vazia(self):
        resultado = definir_linha_de_base(marco(), [], 48)
        self.assertIsNone(resultado.inicio)
        self.assertEqual(resultado.planejadas, ())
        self.assertEqual(resultado.adicionadas, ())

    def test_issue_na_janela_de_48_horas_e_planejada(self):
        m = marco(criado=instante(14))
        a = issue(1, aberta=instante(15))
        b = issue(2, aberta=instante(17))
        c = issue(3, aberta=instante(18, 13))
        resultado = definir_linha_de_base(m, [a, b, c], 48)
        self.assertEqual([x.numero for x in resultado.planejadas], [1, 2])
        self.assertEqual([x.numero for x in resultado.adicionadas], [3])

    def test_evento_de_entrada_no_marco_prevalece_sobre_abertura(self):
        m = marco(criado=instante(14))
        a = issue(1, aberta=instante(14), eventos=(Evento("milestoned", instante(16), False, "Fase 1"),))
        resultado = definir_linha_de_base(m, [a], 48)
        self.assertEqual(resultado.inicio, instante(16))


class TesteEstadoEIndicadores(unittest.TestCase):
    def test_issue_sem_historico_fica_aberta_antes_da_data_de_fechamento(self):
        a = issue(1, fechada=instante(17))
        self.assertTrue(esta_aberta_em(a, instante(16)))
        self.assertFalse(esta_aberta_em(a, instante(18)))

    def test_issue_fechada_no_historico_e_concluida(self):
        a = issue(1, eventos=(Evento("closed", instante(17), False, None),))
        self.assertFalse(esta_aberta_em(a, instante(18)))
        self.assertEqual(concluida_em(a, instante(18)), instante(17))

    def test_issue_reaberta_no_historico_volta_a_ficar_aberta(self):
        a = issue(1, eventos=(Evento("closed", instante(16), False, None), Evento("reopened", instante(17), False, None)))
        self.assertTrue(esta_aberta_em(a, instante(18)))
        self.assertIsNone(concluida_em(a, instante(18)))

    def test_tct_calcula_percentual_das_issues_planejadas_concluidas(self):
        planejadas = (issue(1, fechada=instante(16)), issue(2, fechada=instante(17)), issue(3))
        resultado = calcular_tct(planejadas, (), instante(18))
        self.assertEqual(resultado.planejadas, 3)
        self.assertEqual(resultado.concluidas, 2)
        self.assertAlmostEqual(resultado.tct, 200 / 3)

    def test_tct_sem_planejadas_e_nulo(self):
        resultado = calcular_tct((), (), instante(18))
        self.assertIsNone(resultado.tct)

    def test_tempo_de_ciclo_considera_somente_issues_concluidas(self):
        a = issue(1, aberta=instante(15), fechada=instante(17))
        b = issue(2, aberta=instante(15))
        resultado = calcular_ciclo((a, b), instante(18))
        self.assertEqual(len(resultado.itens), 1)
        self.assertAlmostEqual(resultado.media_dias, 2.0)

    def test_tempo_de_ciclo_sem_conclusoes_e_nulo(self):
        resultado = calcular_ciclo((issue(1),), instante(18))
        self.assertIsNone(resultado.media_dias)

    def test_tsa_considera_apenas_issues_abertas(self):
        abertas = issue(1, aberta=instante(15))
        fechada = issue(2, aberta=instante(15), fechada=instante(17))
        resultado = calcular_tsa((abertas, fechada), instante(18), 2)
        self.assertEqual([x.numero for x in resultado.itens], [1])
        self.assertEqual(resultado.itens[0].dias, 3.0)
        self.assertTrue(resultado.itens[0].acima_do_limite)

    def test_tsa_ignora_atividade_de_bot_e_evento_futuro(self):
        a = issue(1, aberta=instante(15), eventos=(
            Evento("commented", instante(16), True, None),
            Evento("commented", instante(19), False, None),
        ))
        self.assertEqual(ultima_atividade(a, instante(18)), instante(15))


class TesteBurndownERegrasDeAvaliacao(unittest.TestCase):
    def test_valor_ideal_comeca_no_total_e_termina_em_zero(self):
        self.assertEqual(valor_ideal(6, 0, 3), 6)
        self.assertEqual(valor_ideal(6, 3, 3), 0)

    def test_valor_ideal_sem_duracao_e_nulo(self):
        self.assertIsNone(valor_ideal(6, 1, None))

    def test_burndown_vazio_quando_nao_existe_linha_de_base(self):
        self.assertEqual(calcular_burndown((), None, instante(20), instante(18)), ())

    def test_burndown_gera_pontos_dia_a_dia(self):
        a = issue(1, aberta=instante(15), fechada=instante(16))
        b = issue(2, aberta=instante(15))
        resultado = calcular_burndown((a, b), instante(15), instante(17, 23), instante(17, 20))
        self.assertGreaterEqual(len(resultado), 3)
        self.assertEqual(resultado[0].restantes, 2)
        self.assertEqual(resultado[-1].restantes, 1)

    def test_avaliacao_tct_nao_aplicavel(self):
        self.assertEqual(avaliar_tct(ResultadoTct(0, 0, 0, 0, None), None, instante(18)),
                         "Não aplicável (não há Issues planejadas)")

    def test_avaliacao_tct_meta_atingida(self):
        resultado = ResultadoTct(2, 2, 0, 0, 100.0)
        self.assertEqual(avaliar_tct(resultado, instante(20), instante(18)), "Meta atingida")

    def test_avaliacao_tct_alerta_quando_abaixo_de_75_porcento_a_24_horas(self):
        prazo = instante(19)
        resultado = ResultadoTct(4, 2, 0, 0, 50.0)
        self.assertIn("Alerta de atraso", avaliar_tct(resultado, prazo, instante(18)))

    def test_avaliacao_ciclo_dentro_e_acima_da_meta(self):
        self.assertIn("Dentro da meta", avaliar_ciclo(ResultadoCiclo((), 2.0)))
        self.assertIn("Acima da meta", avaliar_ciclo(ResultadoCiclo((), 2.1)))

    def test_avaliacao_tsa_sem_issues_abertas(self):
        self.assertEqual(avaliar_tsa(ResultadoTsa((), None)), "Não aplicável (nenhuma Issue aberta)")


class TesteTabelasMarkdown(unittest.TestCase):
    def test_escapa_pipe_em_celula(self):
        self.assertEqual(escapar("a|b"), "a\\|b")

    def test_gera_tabela_markdown(self):
        texto = tabela(["Nome", "Estado"], [["Tarefa", "Concluída"]])
        self.assertIn("| Nome | Estado |", texto)
        self.assertIn("| :--- | :--- |", texto)
        self.assertIn("| Tarefa | Concluída |", texto)

    def test_gera_link_da_issue(self):
        self.assertEqual(link_da_issue(7, "https://exemplo.test/7"), "[#7](https://exemplo.test/7)")


if __name__ == "__main__":
    unittest.main()
