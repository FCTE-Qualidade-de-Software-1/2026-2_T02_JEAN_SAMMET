from .configuracao import DATAS_FINAIS_BURNDOWN
from .modelos import Marco
from .tempo import fim_do_dia, fim_do_dia_local, ler_instante


def converter_marco(bruto: dict) -> Marco:
    prazo = fim_do_dia(bruto["due_on"]) if bruto.get("due_on") else None
    prazo_configurado = DATAS_FINAIS_BURNDOWN.get(bruto["number"])
    if prazo_configurado is not None:
        prazo = fim_do_dia_local(prazo_configurado)
    encerrado_em = ler_instante(bruto["closed_at"]) if bruto.get("closed_at") else None
    return Marco(
        numero=bruto["number"],
        titulo=bruto["title"],
        url=bruto["html_url"],
        estado=bruto["state"],
        criado_em=ler_instante(bruto["created_at"]),
        prazo=prazo,
        encerrado_em=encerrado_em,
        descricao=bruto.get("description") or "",
    )


def listar_marcos(cliente, repositorio: str) -> list[Marco]:
    brutos = cliente.listar(f"/repos/{repositorio}/milestones", {"state": "all"})
    return sorted((converter_marco(bruto) for bruto in brutos), key=lambda marco: marco.numero)
