"""Funções de formatação utilizando os painéis da biblioteca Rich."""

from rich.console import Console
from rich.panel import Panel


def _obter_texto(texto, isArquivo):
    """Obtém o texto diretamente ou lê o conteúdo de um arquivo."""

    if isArquivo:
        with open(texto, "r", encoding="utf-8") as arquivo:
            return arquivo.read()

    return texto


def painel_simples(texto, isArquivo):
    """Exibe o texto dentro de um painel simples.

    Args:
        texto: Texto a ser exibido ou caminho do arquivo.
        isArquivo: Indica se texto representa um arquivo.
    """

    conteudo = _obter_texto(texto, isArquivo)

    painel = Panel(
        conteudo,
        title="Biblioteca Rich",
        border_style="blue"
    )

    Console().print(painel)


def painel_destaque(texto, isArquivo):
    """Exibe o texto dentro de um painel destacado.

    Args:
        texto: Texto a ser exibido ou caminho do arquivo.
        isArquivo: Indica se texto representa um arquivo.
    """

    conteudo = _obter_texto(texto, isArquivo)

    painel = Panel(
        conteudo,
        title="DESTAQUE",
        subtitle="Rich",
        border_style="green",
        padding=(1, 2)
    )

    Console().print(painel)