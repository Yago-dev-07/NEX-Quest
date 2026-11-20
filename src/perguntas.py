"""
Banco de perguntas do NEX Quest.

Cada pergunta possui:
- fase: número da fase (1, 2 ou 3)
- pergunta: texto exibido ao jogador
- alternativas: lista com quatro opções
- correta: posição da alternativa correta (começa em 0)
- explicacao: texto mostrado depois da resposta
"""

import json
import random
from pathlib import Path


CAMINHO_PERGUNTAS = (
    Path(__file__).resolve().parent.parent / "data" / "perguntas.json"
)


def carregar_perguntas():
    """Carrega todas as perguntas do arquivo JSON."""
    with open(CAMINHO_PERGUNTAS, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def obter_perguntas_fase(numero_fase):
    """Retorna somente as perguntas da fase informada."""
    perguntas = carregar_perguntas()
    perguntas_da_fase = []

    for pergunta in perguntas:
        if pergunta["fase"] == numero_fase:
            perguntas_da_fase.append(pergunta)

    return perguntas_da_fase


def embaralhar_perguntas(perguntas):
    """Retorna uma cópia das perguntas em ordem aleatória."""
    perguntas_embaralhadas = perguntas.copy()
    random.shuffle(perguntas_embaralhadas)
    return perguntas_embaralhadas