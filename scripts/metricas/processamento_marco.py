from datetime import datetime

from .avaliacao import avaliar_ciclo, avaliar_tct, avaliar_tsa
from .calculo_burndown import calcular_burndown
from .calculo_ciclo import calcular_ciclo
from .calculo_tct import calcular_tct
from .calculo_tsa import calcular_tsa
from .configuracao import JANELA_LINHA_DE_BASE_HORAS, LIMITE_TSA_DIAS
from .leitura_issues import listar_issues
from .linha_de_base import definir_linha_de_base
from .modelos import Marco
from .referencia import referencia_do_marco
from .resultado_marco import ResultadoMarco


def processar_marco(cliente, repositorio: str, marco: Marco, agora: datetime) -> ResultadoMarco:
    issues = listar_issues(cliente, repositorio, marco)
    referencia = referencia_do_marco(marco, agora)
    base = definir_linha_de_base(marco, issues, JANELA_LINHA_DE_BASE_HORAS)
    tct = calcular_tct(base.planejadas, base.adicionadas, referencia)
    ciclo = calcular_ciclo(issues, referencia)
    tsa = calcular_tsa(issues, referencia, LIMITE_TSA_DIAS)
    burndown = calcular_burndown(base.planejadas, base.inicio, marco.prazo, referencia)
    return ResultadoMarco(
        marco=marco,
        referencia=referencia,
        inicio=base.inicio,
        issues=tuple(issues),
        tct=tct,
        ciclo=ciclo,
        tsa=tsa,
        burndown=burndown,
        situacao_tct=avaliar_tct(tct, marco.prazo, referencia),
        situacao_ciclo=avaliar_ciclo(ciclo),
        situacao_tsa=avaliar_tsa(tsa),
    )
