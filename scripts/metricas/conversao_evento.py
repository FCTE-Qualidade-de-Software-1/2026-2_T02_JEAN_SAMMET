from datetime import datetime

from .modelos import Evento
from .tempo import ler_instante


def extrair_instante(bruto: dict) -> datetime | None:
    for chave in ("created_at", "submitted_at"):
        if bruto.get(chave):
            return ler_instante(bruto[chave])
    autor_do_commit = bruto.get("committer") or {}
    if autor_do_commit.get("date"):
        return ler_instante(autor_do_commit["date"])
    return None


def extrair_ator(bruto: dict) -> dict | None:
    for chave in ("actor", "user", "author"):
        valor = bruto.get(chave)
        if isinstance(valor, dict) and valor.get("login"):
            return valor
    return None


def ator_e_automacao(ator: dict | None) -> bool:
    if ator is None:
        return False
    return ator.get("type") == "Bot" or ator["login"].endswith("[bot]")


def converter_evento(bruto: dict) -> Evento | None:
    tipo = bruto.get("event")
    instante = extrair_instante(bruto)
    if not tipo or instante is None:
        return None
    marco = (bruto.get("milestone") or {}).get("title")
    return Evento(tipo, instante, ator_e_automacao(extrair_ator(bruto)), marco)
