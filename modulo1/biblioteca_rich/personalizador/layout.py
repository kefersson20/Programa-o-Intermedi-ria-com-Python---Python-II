"""Funções de formatação utilizando o recurso Layout da biblioteca Rich."""

from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel


def _obter_texto(texto, isArquivo):
    """Obtém o texto diretamente ou lê o conteúdo de um arquivo."""

    if isArquivo:
        with open(texto, "r", encoding="utf-8") as arquivo:
            return arquivo.read()

    return texto


def layout_horizontal(texto, isArquivo):
    """Exibe o texto utilizando um Layout dividido horizontalmente.

    Args:
        texto: Texto a ser exibido ou caminho do arquivo.
        isArquivo: Indica se texto representa um arquivo.
    """

    conteudo = _obter_texto(texto, isArquivo)

    layout = Layout()

    layout.split_row(
        Layout(Panel("Biblioteca Rich")),
        Layout(Panel(conteudo))
    )

    Console().print(layout)


def layout_vertical(texto, isArquivo):
    """Exibe o texto utilizando um Layout dividido verticalmente.

    Args:
        texto: Texto a ser exibido ou caminho do arquivo.
        isArquivo: Indica se texto representa um arquivo.
    """

    conteudo = _obter_texto(texto, isArquivo)

    layout = Layout()

    layout.split_column(
        Layout(Panel("Biblioteca Rich")),
        Layout(Panel(conteudo))
    )

    Console().print(layout)