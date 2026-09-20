"""Funções de formatação utilizando estilos da biblioteca Rich."""

from rich.console import Console
from rich.style import Style


def _obter_texto(texto, isArquivo):
    """Obtém o texto diretamente ou lê o conteúdo de um arquivo."""

    if isArquivo:
        with open(texto, "r", encoding="utf-8") as arquivo:
            return arquivo.read()

    return texto


def estilo_negrito(texto, isArquivo):
    """Exibe o texto utilizando um estilo em negrito.

    Args:
        texto: Texto a ser exibido ou caminho do arquivo.
        isArquivo: Indica se texto representa um arquivo.
    """

    conteudo = _obter_texto(texto, isArquivo)

    estilo = Style(
        bold=True,
        color="cyan"
    )

    Console().print(
        conteudo,
        style=estilo
    )


def estilo_italico(texto, isArquivo):
    """Exibe o texto utilizando um estilo em itálico.

    Args:
        texto: Texto a ser exibido ou caminho do arquivo.
        isArquivo: Indica se texto representa um arquivo.
    """

    conteudo = _obter_texto(texto, isArquivo)

    estilo = Style(
        italic=True,
        color="magenta"
    )

    Console().print(
        conteudo,
        style=estilo
    )