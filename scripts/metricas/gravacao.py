import json
import os
from pathlib import Path

from .grafico_burndown import desenhar_burndown
from .resultado_marco import ResultadoMarco
from .serializacao import serializar_resultado


def diretorio_do_marco(raiz: Path, numero: int) -> Path:
    return raiz / f"marco-{numero}"


def gravar_marco(resultado: ResultadoMarco, raiz: Path) -> Path:
    destino = diretorio_do_marco(raiz, resultado.marco.numero)
    destino.mkdir(parents=True, exist_ok=True)
    conteudo = json.dumps(serializar_resultado(resultado), ensure_ascii=False, indent=2)
    (destino / "metricas.json").write_text(conteudo + "\n", encoding="utf-8")
    if resultado.burndown:
        desenhar_burndown(resultado.burndown, f"Burndown: {resultado.marco.titulo}", destino / "burndown.png")
    return destino


def prefixo_relativo(raiz: Path, arquivo_painel: Path) -> str:
    return Path(os.path.relpath(raiz, arquivo_painel.parent)).as_posix()


def gravar_painel(texto: str, arquivo_painel: Path) -> None:
    arquivo_painel.parent.mkdir(parents=True, exist_ok=True)
    arquivo_painel.write_text(texto, encoding="utf-8")
