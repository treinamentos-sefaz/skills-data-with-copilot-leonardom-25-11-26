"""Módulo 4 — Visualização de Dados.

Complete cada função com o apoio do GitHub Copilot. Cada função deve **gerar um
gráfico e salvá-lo** no caminho ``out_path`` (formato PNG). Use ``matplotlib`` e
``seaborn``. Em ambientes sem interface gráfica (CI), mantenha o backend "Agg".

Valide com:  ``python lab/check.py --module viz``
"""
from __future__ import annotations

import matplotlib

matplotlib.use("Agg")  # backend sem interface gráfica (funciona no CI)
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402
import seaborn as sns  # noqa: E402


def plot_rating_distribution(df: pd.DataFrame, out_path: str):
    """Histograma da distribuição da coluna ``rating``. Inclua título e labels em
    português e salve a figura em ``out_path``."""
    # Prompt sugerido: "Crie um histograma da coluna rating com 20 bins, título e
    #  labels em português, e salve a figura em out_path."
    fig, ax = plt.subplots()
    ax.hist(df["rating"].dropna(), bins=20)
    ax.set_title("Distribuição das avaliações")
    ax.set_xlabel("Avaliação")
    ax.set_ylabel("Frequência")
    fig.tight_layout()
    fig.savefig(out_path, format="png")
    plt.close(fig)


def plot_top_varieties(df: pd.DataFrame, out_path: str):
    """Gráfico de barras horizontais com as 10 variedades (``variety``) com maior
    quantidade de vinhos. Salve a figura em ``out_path``."""
    counts = df["variety"].dropna().value_counts().head(10).sort_values(ascending=True)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=counts.values, y=counts.index, ax=ax)
    ax.set_title("10 variedades mais frequentes")
    ax.set_xlabel("Quantidade de vinhos")
    ax.set_ylabel("Variedade")
    fig.tight_layout()
    fig.savefig(out_path, format="png")
    plt.close(fig)


def plot_boxplot_by_variety(df: pd.DataFrame, out_path: str):
    """Boxplot de ``rating`` para as 5 variedades mais frequentes. Salve a figura
    em ``out_path``."""
    top_varieties = df["variety"].dropna().value_counts().head(5).index
    filtered = df[df["variety"].isin(top_varieties)].dropna(subset=["rating"])

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=filtered, x="variety", y="rating", order=top_varieties, ax=ax)
    ax.set_title("Avaliações das 5 variedades mais frequentes")
    ax.set_xlabel("Variedade")
    ax.set_ylabel("Avaliação")
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
    fig.tight_layout()
    fig.savefig(out_path, format="png")
    plt.close(fig)
