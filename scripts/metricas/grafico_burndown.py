from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

COR_REAL = "#1f2937"
COR_IDEAL = "#9ca3af"
COR_GRADE = "#e5e7eb"
DIAS_MAXIMOS_NO_EIXO = 8


def separar(pontos, atributo: str):
    selecionados = [(ponto.dia, getattr(ponto, atributo)) for ponto in pontos if getattr(ponto, atributo) is not None]
    return [par[0] for par in selecionados], [par[1] for par in selecionados]


def configurar_eixos(eixo, pontos) -> None:
    passo = max(1, len(pontos) // DIAS_MAXIMOS_NO_EIXO)
    eixo.xaxis.set_major_locator(mdates.DayLocator(interval=passo))
    eixo.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m"))
    eixo.yaxis.set_major_locator(MaxNLocator(integer=True))
    eixo.set_ylim(bottom=0)
    eixo.set_ylabel("Issues restantes")
    eixo.grid(axis="y", color=COR_GRADE, linewidth=0.8)
    eixo.set_axisbelow(True)
    for lado in ("top", "right"):
        eixo.spines[lado].set_visible(False)


def desenhar_burndown(pontos, titulo: str, caminho: Path) -> None:
    figura, eixo = plt.subplots(figsize=(8, 4.2))
    dias_ideais, valores_ideais = separar(pontos, "ideal")
    dias_reais, valores_reais = separar(pontos, "restantes")
    if dias_ideais:
        eixo.plot(dias_ideais, valores_ideais, linestyle="--", color=COR_IDEAL, label="Ideal")
    if dias_reais:
        eixo.plot(dias_reais, valores_reais, marker="o", color=COR_REAL, label="Real", clip_on=False)
    configurar_eixos(eixo, pontos)
    eixo.set_title(titulo, loc="left", fontsize=11)
    eixo.legend(frameon=False)
    figura.savefig(caminho, dpi=160, bbox_inches="tight")
    plt.close(figura)
