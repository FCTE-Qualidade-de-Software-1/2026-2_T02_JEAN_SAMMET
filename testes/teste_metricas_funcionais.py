"""Testes unitários do processamento das métricas funcionais."""

import json
import unittest
from pathlib import Path

from scripts.metricas_funcionais import processar_registros

ROOT = Path(__file__).resolve().parents[1]
H0 = json.loads((ROOT / "testes/referencias/h0_sanitizado.json").read_text(encoding="utf-8"))


def registro(
    metrica: str,
    conforme: str,
    *,
    disciplina: str = "DISC-TESTE",
    relacao: str = "",
    evidencia: str = "evidencia.png",
):
    return {
        "execucao_id": "FUN-TESTE-01",
        "caso": {
            "MET-FUN-01": "CT-01",
            "MET-FUN-02": "CT-02",
            "MET-FUN-03": "CT-03",
            "MET-FUN-04": "CT-04",
            "MET-FUN-05": "CT-05",
            "MET-FUN-06": "CT-06",
            "MET-FUN-07": "CT-07",
        }.get(metrica, "CT-01"),
        "metrica": metrica,
        "entrada_id": "H0",
        "cenario_id": "C0",
        "disciplina": disciplina,
        "relacao": relacao,
        "fonte_vigencia": "fonte oficial, vigência identificada",
        "estado_entrada": "registrado",
        "semestre_esperado": "1",
        "semestre_observado": "1",
        "conforme": conforme,
        "evidencia": evidencia,
        "observacao": "registro de teste unitário",
    }


def unidades_referencia(metrica: str) -> list[tuple[str, str]]:
    if metrica == "MET-FUN-03":
        return [
            ("disciplina", item["codigo"])
            for item in H0["obrigacoes_pendentes_sigaa"]["disciplinas_obrigatorias_pendentes"]
            if item.get("tipo") == "disciplina_obrigatoria"
        ]
    if metrica == "MET-FUN-04":
        return [("disciplina", item["codigo"]) for item in H0["registros_academicos"]]
    if metrica == "MET-FUN-05":
        equivalencias = (
            H0["equivalencias_obrigatorias_concluidas"]
            + H0["equivalencias_obrigatorias_em_andamento"]
        )
        return [
            ("relacao", f'{item["componente_aproveitado"]}->{item["obrigatoria_destino"]}')
            for item in equivalencias
        ]
    raise ValueError(metrica)


def registros_completos(metrica: str, conforme: str = "1") -> list[dict[str, str]]:
    resultado = []
    for campo, unidade in unidades_referencia(metrica):
        resultado.append(
            registro(
                metrica,
                conforme,
                disciplina=unidade if campo == "disciplina" else "",
                relacao=unidade if campo == "relacao" else "",
            )
        )
    return resultado


class TestProcessamentoMetricasFuncionais(unittest.TestCase):
    def test_denominador_ausente_nao_vira_zero_porcento(self):
        resultado = processar_registros([])
        metrica = resultado["metricas"]["MET-FUN-01"]
        self.assertIsNone(metrica["valor_percentual"])
        self.assertIsNone(metrica["numerador"])
        self.assertEqual(metrica["denominador"], 0)
        self.assertEqual(metrica["status"], "Pendente de execução")
        self.assertEqual(resultado["questoes"]["Q-FUN-01"]["status"], "Pendente — cobertura/execução incompleta")

    def test_metricas_com_universo_h0_exibem_denominador_conhecido_sem_resultado(self):
        resultado = processar_registros([])
        self.assertEqual(resultado["metricas"]["MET-FUN-03"]["denominador"], 14)
        self.assertEqual(resultado["metricas"]["MET-FUN-04"]["denominador"], 41)
        self.assertEqual(resultado["metricas"]["MET-FUN-05"]["denominador"], 7)
        for metric_id in ("MET-FUN-03", "MET-FUN-04", "MET-FUN-05"):
            item = resultado["metricas"][metric_id]
            self.assertIsNone(item["valor_percentual"])
            self.assertIsNone(item["numerador"])
            self.assertTrue(item["status"].startswith("Pendente"))

    def test_metrica_de_violacao_conta_apenas_nao_conformidades(self):
        resultado = processar_registros([
            registro("MET-FUN-01", "1"),
            registro("MET-FUN-01", "0"),
        ])
        metrica = resultado["metricas"]["MET-FUN-01"]
        self.assertEqual(metrica["numerador"], 1)
        self.assertEqual(metrica["denominador"], 2)
        self.assertEqual(metrica["valor_percentual"], 50.0)
        self.assertEqual(metrica["status"], "Não conforme")

    def test_cobertura_usa_as_14_obrigatorias_de_h0_e_nao_o_tamanho_da_amostra(self):
        registros = registros_completos("MET-FUN-03")
        registros[0]["conforme"] = "0"
        metrica = processar_registros(registros)["metricas"]["MET-FUN-03"]
        self.assertEqual(metrica["numerador"], 13)
        self.assertEqual(metrica["denominador"], 14)
        self.assertAlmostEqual(metrica["valor_percentual"], 13 / 14 * 100, places=4)
        self.assertEqual(metrica["status"], "Não conforme")

    def test_cobertura_incompleta_nao_gera_percentual_inflado(self):
        registros = registros_completos("MET-FUN-03")[:-1]
        metrica = processar_registros(registros)["metricas"]["MET-FUN-03"]
        self.assertIsNone(metrica["numerador"])
        self.assertEqual(metrica["denominador"], 14)
        self.assertEqual(metrica["verificacoes_validas"], 13)
        self.assertIsNone(metrica["valor_percentual"])
        self.assertEqual(metrica["status"], "Pendente — cobertura 13/14")

    def test_unidade_duplicada_impede_fechar_a_metrica(self):
        registros = registros_completos("MET-FUN-03")
        registros.append(dict(registros[0]))
        metrica = processar_registros(registros)["metricas"]["MET-FUN-03"]
        self.assertIsNone(metrica["valor_percentual"])
        self.assertEqual(metrica["denominador"], 14)
        self.assertEqual(metrica["status"], "Pendente — cobertura 13/14")

    def test_metricas_rejeitam_entrada_ou_ct_diferente_do_protocolo(self):
        linha = registro("MET-FUN-03", "1", disciplina="FGA0150")
        linha["caso"] = "CT-01"
        resultado = processar_registros([linha])
        metrica = resultado["metricas"]["MET-FUN-03"]
        self.assertEqual(metrica["verificacoes_validas"], 0)
        self.assertEqual(metrica["denominador"], 14)
        self.assertTrue(any("deve estar associado a CT-03" in aviso for aviso in resultado["avisos"]))

    def test_status_do_historico_exige_comparacao_de_todos_os_41_registros(self):
        registros = registros_completos("MET-FUN-04")
        metrica = processar_registros(registros)["metricas"]["MET-FUN-04"]
        self.assertEqual(metrica["numerador"], 0)
        self.assertEqual(metrica["denominador"], 41)
        self.assertEqual(metrica["valor_percentual"], 0.0)
        self.assertEqual(metrica["status"], "Conforme")

    def test_equivalencias_exigem_as_sete_relacoes_do_h0(self):
        registros = registros_completos("MET-FUN-05")
        registros[0]["conforme"] = "0"
        metrica = processar_registros(registros)["metricas"]["MET-FUN-05"]
        self.assertEqual(metrica["numerador"], 1)
        self.assertEqual(metrica["denominador"], 7)
        self.assertAlmostEqual(metrica["valor_percentual"], 100 / 7, places=4)
        self.assertEqual(metrica["status"], "Não conforme")

    def test_questao_com_duas_metricas_so_e_favoravel_com_cobertura_integral(self):
        resultado = processar_registros(
            registros_completos("MET-FUN-03") + registros_completos("MET-FUN-05")
        )
        self.assertEqual(resultado["questoes"]["Q-FUN-03"]["status"], "Conforme")

        resultado_parcial = processar_registros(
            registros_completos("MET-FUN-03") + registros_completos("MET-FUN-05")[:-1]
        )
        self.assertEqual(
            resultado_parcial["questoes"]["Q-FUN-03"]["status"],
            "Pendente — cobertura/execução incompleta",
        )

    def test_questao_com_falha_e_cobertura_incompleta_nao_fica_favoravel(self):
        registros = registros_completos("MET-FUN-03")[:-1]
        registros[0]["conforme"] = "0"
        resultado = processar_registros(registros)
        self.assertEqual(resultado["questoes"]["Q-FUN-03"]["status"], "Não conforme — resultado parcial")

    def test_questao_informa_resultado_parcial_quando_ha_falha_e_unidades_pendentes(self):
        registros = registros_completos("MET-FUN-04")[:-1]
        registros[0]["conforme"] = "0"
        resultado = processar_registros(registros)
        self.assertEqual(
            resultado["questoes"]["Q-FUN-04"]["status"],
            "Não conforme — resultado parcial",
        )

    def test_cobertura_parcial_nao_gera_resposta_favoravel_completa(self):
        resultado = processar_registros([
            registro("MET-FUN-01", "1"),
            registro("MET-FUN-01", "PENDENTE"),
        ])
        self.assertEqual(resultado["metricas"]["MET-FUN-01"]["status"], "Conforme — cobertura parcial")
        self.assertEqual(resultado["questoes"]["Q-FUN-01"]["status"], "Conforme — cobertura parcial")

    def test_falha_de_coleta_e_inconclusiva(self):
        resultado = processar_registros([registro("MET-FUN-01", "INCONCLUSIVO")])
        self.assertTrue(resultado["metricas"]["MET-FUN-01"]["status"].startswith("Inconclusivo"))
        self.assertEqual(resultado["questoes"]["Q-FUN-01"]["status"], "Inconclusivo")

    def test_nao_aplicavel_exige_registro_explicito(self):
        resultado = processar_registros([registro("MET-FUN-02", "NA")])
        self.assertTrue(resultado["metricas"]["MET-FUN-02"]["status"].startswith("Não aplicável"))
        self.assertTrue(resultado["questoes"]["Q-FUN-02"]["status"].startswith("Não aplicável"))

    def test_restricoes_semestrais_sao_julgadas_por_tipo(self):
        resultado = processar_registros([
            registro("MET-FUN-07", "1", relacao="limite de carga"),
            registro("MET-FUN-07", "0", relacao="oferta"),
        ])
        metrica = resultado["metricas"]["MET-FUN-07"]
        self.assertEqual(set(metrica["por_tipo"]), {"limite de carga", "oferta"})
        self.assertEqual(metrica["por_tipo"]["limite de carga"]["status"], "Conforme")
        self.assertEqual(metrica["por_tipo"]["oferta"]["status"], "Não conforme")
        self.assertEqual(metrica["status"], "Não conforme")

    def test_registro_sem_evidencia_nao_compoe_denominador(self):
        resultado = processar_registros([registro("MET-FUN-01", "0", evidencia="")])
        metrica = resultado["metricas"]["MET-FUN-01"]
        self.assertEqual(metrica["denominador"], 0)
        self.assertTrue(any("sem evidencia" in aviso.lower() for aviso in resultado["avisos"]))


if __name__ == "__main__":
    unittest.main()
