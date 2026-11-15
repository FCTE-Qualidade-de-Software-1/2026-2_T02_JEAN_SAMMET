"""Verifica integridade, consistência e minimização de dados da entrada H0."""
import csv
import json
import unittest
from io import StringIO
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
H0_JSON = ROOT / "testes/referencias/h0_sanitizado.json"
H0_CSV = ROOT / "testes/evidencias/funcionais/h0_registros.csv"
PEND = ROOT / "testes/evidencias/funcionais/h0_obrigacoes_pendentes.csv"
EQUIV = ROOT / "testes/evidencias/funcionais/h0_equivalencias.csv"
ESTRUTURA = ROOT / "testes/referencias/estrutura_6360_1.json"


class TesteH0Sanitizado(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.h0 = json.loads(H0_JSON.read_text(encoding="utf-8"))

    def test_entrada_e_matriz_estao_identificadas_sem_identificador_pessoal(self):
        self.assertEqual(self.h0["entrada_id"], "H0")
        self.assertEqual(self.h0["vinculo_academico"]["matriz"], "6360/1")
        self.assertFalse(self.h0["privacidade"]["identificadores_pessoais_incluidos"])
        forbidden_keys = {"nome_discente", "matricula", "cpf", "data_nascimento", "documento", "codigo_autenticacao", "ira", "mp"}
        self.assertFalse(forbidden_keys.intersection(self.h0.keys()))

    def test_quantidade_e_status_dos_registros_estao_consistentes(self):
        rows = list(csv.DictReader(StringIO(H0_CSV.read_text(encoding="utf-8-sig"))))
        summary = self.h0["resumo_registros"]
        self.assertEqual(len(rows), 41)
        self.assertEqual(summary["componentes_curriculares_com_status"], 41)
        self.assertEqual(summary["aprovados"], 33)
        self.assertEqual(summary["matriculados"], 7)
        self.assertEqual(summary["trancados"], 1)
        self.assertEqual(sum(r["status_historico"] == "APROVADO" for r in rows), 33)
        self.assertEqual(sum(r["status_historico"] == "MATRICULADO" for r in rows), 7)
        self.assertEqual(sum(r["status_historico"] == "TRANCADO" for r in rows), 1)

    def test_pendencias_tem_14_disciplinas_mais_dois_requisitos_separados(self):
        rows = list(csv.DictReader(StringIO(PEND.read_text(encoding="utf-8-sig"))))
        self.assertEqual(len(rows), 17)
        self.assertEqual(sum(r["tipo_obrigacao"] == "disciplina_obrigatoria" for r in rows), 14)
        self.assertEqual(sum(r["tipo_obrigacao"] == "cadeia_de_seletividade" for r in rows), 2)
        self.assertEqual(sum(r["tipo_obrigacao"] == "requisito_nao_curricular" for r in rows), 1)
        self.assertEqual(sum(int(r["carga_horaria_h"]) for r in rows if r["tipo_obrigacao"] == "disciplina_obrigatoria"), 1050)

    def test_obrigatorias_pendentes_sao_da_matriz_e_batem_com_o_resumo(self):
        estrutura = json.loads(ESTRUTURA.read_text(encoding="utf-8"))
        codigos_matriz = {item["codigo"] for item in estrutura["obrigatorias"]}
        rows = list(csv.DictReader(StringIO(PEND.read_text(encoding="utf-8-sig"))))
        pendentes = [row for row in rows if row["tipo_obrigacao"] == "disciplina_obrigatoria"]
        self.assertEqual(len(pendentes), 14)
        self.assertTrue({row["codigo"] for row in pendentes}.issubset(codigos_matriz))
        soma_horas = sum(int(row["carga_horaria_h"]) for row in pendentes)
        self.assertEqual(soma_horas, self.h0["resumo_carga_horaria"]["obrigatorias"]["pendente_h"])

    def test_equivalencias_separam_concluidas_de_matriculadas(self):
        rows = list(csv.DictReader(StringIO(EQUIV.read_text(encoding="utf-8-sig"))))
        self.assertEqual(len(rows), 7)
        self.assertEqual(sum(r["classificacao"] == "equivalencia concluida" for r in rows), 5)
        self.assertEqual(sum(r["classificacao"] == "equivalencia em andamento; não cumprida" for r in rows), 2)

    def test_estrutura_nao_armazena_campos_de_identificacao_pessoal(self):
        campos_sensiveis = {
            "nome_discente", "matricula", "cpf", "data_nascimento",
            "numero_documento", "documento", "codigo_autenticacao",
            "ira", "mp", "local_nascimento", "nacionalidade",
        }

        def percorrer_chaves(valor):
            if isinstance(valor, dict):
                for chave, conteudo in valor.items():
                    yield chave
                    yield from percorrer_chaves(conteudo)
            elif isinstance(valor, list):
                for item in valor:
                    yield from percorrer_chaves(item)

        chaves = {str(chave).strip().lower() for chave in percorrer_chaves(self.h0)}
        self.assertFalse(campos_sensiveis.intersection(chaves))
        self.assertEqual(
            self.h0["origem"]["arquivo_fonte_original"],
            "Arquivo original não versionado por conter dados pessoais.",
        )

    def test_csvs_contem_somente_colunas_academicas_necessarias(self):
        colunas_permitidas = {
            H0_CSV: {
                "entrada_id", "codigo_disciplina", "nome_disciplina", "periodo_letivo",
                "carga_horaria_h", "status_historico", "marcador_sigaa",
                "significado_marcador", "pagina_origem",
            },
            PEND: {
                "entrada_id", "tipo_obrigacao", "codigo", "nome", "carga_horaria_h",
                "situacao_na_entrada", "pagina_origem", "observacao",
            },
            EQUIV: {
                "entrada_id", "obrigatoria_destino", "nome_destino", "componente_aproveitado",
                "nome_aproveitado", "carga_horaria_h", "status_historico", "periodo_letivo",
                "classificacao", "evidencia_sigaa",
            },
        }
        for caminho, permitidas in colunas_permitidas.items():
            with caminho.open(encoding="utf-8-sig", newline="") as arquivo:
                leitor = csv.DictReader(arquivo)
                self.assertEqual(set(leitor.fieldnames or []), permitidas)


if __name__ == "__main__":
    unittest.main()
