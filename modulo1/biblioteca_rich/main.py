"""Interface de linha de comando para o pacote personalizador."""

import argparse

from personalizador import layout
from personalizador import painel
from personalizador import progresso
from personalizador import estilo


MODULOS = {
    "1": ("layout", layout),
    "2": ("painel", painel),
    "3": ("progresso", progresso),
    "4": ("estilo", estilo),
}


FUNCOES = {
    "layout": {
        "1": ("layout_horizontal", layout.layout_horizontal),
        "2": ("layout_vertical", layout.layout_vertical),
    },
    "painel": {
        "1": ("painel_simples", painel.painel_simples),
        "2": ("painel_destaque", painel.painel_destaque),
    },
    "progresso": {
        "1": ("progresso_simples", progresso.progresso_simples),
        "2": ("progresso_detalhado", progresso.progresso_detalhado),
    },
    "estilo": {
        "1": ("estilo_negrito", estilo.estilo_negrito),
        "2": ("estilo_italico", estilo.estilo_italico),
    },
}


def criar_parser():
    """Cria e configura o parser da interface de linha de comando."""

    parser = argparse.ArgumentParser(
        description="Programa de formatação de textos utilizando a biblioteca Rich."
    )

    parser.add_argument(
        "texto",
        help="Texto que será formatado ou caminho do arquivo."
    )

    parser.add_argument(
        "-a",
        "--arquivo",
        action="store_true",
        help="Indica que o argumento texto é o caminho para um arquivo."
    )

    parser.add_argument(
        "-m",
        "--modulo",
        default="1",
        help=(
            "Escolha o módulo pelo número ou nome. "
            "Opções: 1=layout, 2=painel, "
            "3=progresso, 4=estilo."
        )
    )

    parser.add_argument(
        "-f",
        "--funcao",
        default="1",
        help=(
            "Escolha a função pelo número ou nome. "
            "Para layout: 1=layout_horizontal, 2=layout_vertical; "
            "para painel: 1=painel_simples, 2=painel_destaque; "
            "para progresso: 1=progresso_simples, 2=progresso_detalhado; "
            "para estilo: 1=estilo_negrito, 2=estilo_italico."
        )
    )

    return parser

def encontrar_modulo(valor):
    """Localiza um módulo pelo número ou pelo nome."""

    valor = valor.lower()

    if valor in MODULOS:
        return MODULOS[valor]

    for nome, modulo in MODULOS.values():
        if valor == nome:
            return nome, modulo

    raise ValueError(f"Módulo inválido: {valor}")


def encontrar_funcao(nome_modulo, valor):
    """Localiza uma função pelo número ou pelo nome."""

    valor = valor.lower()

    funcoes = FUNCOES[nome_modulo]

    if valor in funcoes:
        return funcoes[valor][1]

    for nome, funcao in funcoes.values():
        if valor == nome:
            return funcao

    raise ValueError(
        f"Função inválida: {valor} para o módulo {nome_modulo}"
    )
def main():
    """Executa a interface de linha de comando do programa."""

    parser = criar_parser()
    args = parser.parse_args()

    try:
        nome_modulo, modulo = encontrar_modulo(args.modulo)
        funcao = encontrar_funcao(nome_modulo, args.funcao)

        funcao(args.texto, args.arquivo)

    except ValueError as erro:
        parser.error(str(erro))


if __name__ == "__main__":
    main()