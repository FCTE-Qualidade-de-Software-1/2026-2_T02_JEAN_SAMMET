from dataclasses import asdict
from datetime import date, datetime

from .resultado_marco import ResultadoMarco


def converter_valor(valor):
    if isinstance(valor, (datetime, date)):
        return valor.isoformat()
    if isinstance(valor, dict):
        return {chave: converter_valor(item) for chave, item in valor.items()}
    if isinstance(valor, (list, tuple)):
        return [converter_valor(item) for item in valor]
    return valor


def serializar_resultado(resultado: ResultadoMarco) -> dict:
    marco = resultado.marco
    return converter_valor(
        {
            "marco": {
                "numero": marco.numero,
                "titulo": marco.titulo,
                "estado": marco.estado,
                "prazo": marco.prazo,
                "encerrado_em": marco.encerrado_em,
            },
            "referencia": resultado.referencia,
            "inicio_da_linha_de_base": resultado.inicio,
            "tct": asdict(resultado.tct),
            "ciclo": asdict(resultado.ciclo),
            "tsa": asdict(resultado.tsa),
            "burndown": [asdict(ponto) for ponto in resultado.burndown],
            "situacoes": {
                "tct": resultado.situacao_tct,
                "ciclo": resultado.situacao_ciclo,
                "tsa": resultado.situacao_tsa,
            },
        }
    )
