"""Regressões de validade dos instrumentos; não acessam rede nem o site."""
import copy
import tempfile
import unittest
from pathlib import Path
from testes import analisador_sca_irp as sca
from testes import teste_controle_acesso_tbr as tbr


class Instrumentos(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base=Path(self.temp.name)
        (self.base/'evidencia.txt').write_text('Fixture de teste local; não é coleta do produto.')
        self.sca={'cobertura_confirmada':True,'escopo':'cliente sintético','ferramenta':'fixture',
                  'base_vulnerabilidades':'fixture-v1','relatorio_bruto':'evidencia.txt',
                  'inventario':[{'componente':'lib','versao':'1'}],'achados':[]}
        self.tbr={'protecao_exigida':True,'fonte_requisito':'evidencia.txt',
                  'url':'https://example.invalid/teste','metodo':'POST','payload_validado':True,
                  'controle_positivo':{'status_http':200,'operacao_confirmada':True,'evidencia':'evidencia.txt'},
                  'casos_planejados':[f'REQ-{i:02}' for i in range(1,11)],
                  'casos':[{'id':f'REQ-{i:02}','status_http':401,'condicao_validada':True,
                            'evidencia':'evidencia.txt'} for i in range(1,11)]}

    def achado(self,severidade,ambiente='producao'):
        return {'componente':'lib','versao':'1','aviso':'AVISO-1','severidade':severidade,'ambiente':ambiente}

    def test_ausencia_nao_vira_zero(self):
        self.assertIsNone(sca.analisar({},self.base)['irp'])
        self.sca['relatorio_bruto']='ausente.json'
        self.assertEqual(sca.analisar(self.sca,self.base)['status'],'Inconclusivo')

    def test_zero_exige_inventario(self):
        self.assertEqual(sca.analisar(self.sca,self.base)['status'],'Excelente')
        self.sca['inventario']=[]
        self.assertIsNone(sca.analisar(self.sca,self.base)['irp'])

    def test_alta_producao_dev_desconhecida(self):
        for ambiente,esperado in [('producao','Crítico'),('desenvolvimento','Aceitável'),('desconhecido','Inconclusivo')]:
            with self.subTest(ambiente=ambiente):
                self.sca['achados']=[self.achado('high',ambiente)]
                self.assertEqual(sca.analisar(self.sca,self.base)['status'],esperado)

    def test_deduplicacao(self):
        a=self.achado('moderate');self.sca['achados']=[a,copy.deepcopy(a)]
        self.assertEqual(sca.analisar(self.sca,self.base)['irp'],2)
        self.sca['achados'][1]['severidade']='high'
        self.assertIsNone(sca.analisar(self.sca,self.base)['irp'])

    def test_irp_acima_20_sem_alta_e_critico(self):
        self.sca['achados']=[dict(self.achado('moderate'),aviso=f'A-{i}') for i in range(11)]
        self.assertEqual(sca.analisar(self.sca,self.base)['status'],'Crítico')

    def test_tbr_controle_positivo_obrigatorio(self):
        self.tbr['controle_positivo']['status_http']=405
        self.assertIsNone(tbr.analisar(self.tbr,self.base)['tbr'])

    def test_tbr_bateria_completa(self):
        resultado=tbr.analisar(self.tbr,self.base)
        self.assertEqual((resultado['status'],resultado['tbr']),('Conforme',100))

    def test_tbr_405_nao_e_acesso(self):
        self.tbr['casos'][0]['status_http']=405
        resultado=tbr.analisar(self.tbr,self.base)
        self.assertEqual((resultado['status'],resultado['validos'],resultado['inconclusivos']),('Inconclusivo',9,1))

    def test_tbr_200_sem_prova_nao_e_acesso(self):
        self.tbr['casos'][0]['status_http']=200
        self.assertEqual(tbr.analisar(self.tbr,self.base)['status'],'Inconclusivo')
        self.tbr['casos'][0]['execucao_indevida_comprovada']=True
        self.assertEqual(tbr.analisar(self.tbr,self.base)['status'],'Não conforme (Crítico)')

    def test_tbr_condicao_expiracao_ou_papel_nao_isolada(self):
        self.tbr['casos'][6]['condicao_validada']=False
        self.assertEqual(tbr.analisar(self.tbr,self.base)['validos'],9)

    def test_tbr_caso_duplicado_ou_fonte_ausente(self):
        self.tbr['casos'].append(copy.deepcopy(self.tbr['casos'][0]))
        self.assertIsNone(tbr.analisar(self.tbr,self.base)['tbr'])
        self.tbr['casos'].pop();self.tbr['fonte_requisito']='ausente'
        self.assertIsNone(tbr.analisar(self.tbr,self.base)['tbr'])


if __name__=='__main__':unittest.main()
