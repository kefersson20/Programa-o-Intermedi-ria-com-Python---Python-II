"""Funções que utilizam barras de progresso da biblioteca Rich."""

import time

from rich.console import Console
from rich.progress import (
    Progress,
    BarColumn,
    TextColumn,
    TimeRemainingColumn
)


def _obter_texto(texto, isArquivo):
    """Obtém o texto diretamente ou lê o conteúdo de um arquivo."""

    if isArquivo:
        with open(texto, "r", encoding="utf-8") as arquivo:
            return arquivo.read()

    return texto


def progresso_simples(texto, isArquivo):
    """Exibe uma barra de progresso antes de mostrar o texto.

    Args:
        texto: Texto a ser exibido ou caminho do arquivo.
        isArquivo: Indica se texto representa um arquivo.
    """

    conteudo = _obter_texto(texto, isArquivo)

    console = Console()

    with Progress() as progress:

        tarefa = progress.add_task(
            "Processando...",
            total=100
        )

        while not progress.finished:
            progress.update(
                tarefa,
                advance=10
            )

            time.sleep(0.05)

    console.print(conteudo)


def progresso_detalhado(texto, isArquivo):
    """Exibe uma barra de progresso personalizada antes do texto.

    Args:
        texto: Texto a ser exibido ou caminho do arquivo.
        isArquivo: Indica se texto representa um arquivo.
    """

    conteudo = _obter_texto(texto, isArquivo)

    console = Console()

    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("{task.percentage:>3.0f}%"),
        TimeRemainingColumn()
    ) as progress:

        tarefa = progress.add_task(
            "Preparando texto...",
            total=100
        )

        while not progress.finished:
            progress.update(
                tarefa,
                advance=10
            )

            time.sleep(0.05)

    console.print(conteudo)