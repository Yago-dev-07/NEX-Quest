
import os

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")

import pygame

from src.sprites import (
    EXPRESSOES_NEX,
    MENSAGENS_NEX,
    criar_nex,
    nex_calar,
    nex_falar,
    nex_posicionar,
    quebrar_texto,
)


def test_criar_nex_tem_tres_expressoes():
    nex = criar_nex(100)

    assert set(nex["imagens"]) == {"neutro", "feliz", "triste"}
    assert nex["imagens"]["feliz"].get_size() == (100, 100)
    assert nex["mensagem"] == ""


def test_todas_as_situacoes_tem_mensagem_e_expressao():
    assert set(MENSAGENS_NEX) == set(EXPRESSOES_NEX)
    assert set(MENSAGENS_NEX) == {"inicio", "acerto", "erro", "vitoria", "derrota"}


def test_nex_falar_e_calar():
    nex = criar_nex(100)

    nex_falar(nex, "erro")
    assert nex["mensagem"] == MENSAGENS_NEX["erro"]
    assert nex["expressao"] == "triste"

    nex_calar(nex)
    assert nex["mensagem"] == ""
    assert nex["expressao"] == "neutro"


def test_nex_posicionar_usa_centro_da_base():
    nex = criar_nex(100)
    nex_posicionar(nex, 200, 500)

    assert nex["rect"].midbottom == (200, 500)


def test_quebrar_texto_respeita_a_largura():
    pygame.font.init()
    fonte = pygame.font.Font(None, 20)
    texto = "Ajude o NEX a recuperar todas as memórias perdidas na falha do sistema"

    linhas = quebrar_texto(texto, fonte, 150)

    assert len(linhas) > 1
    assert " ".join(linhas) == texto
    for linha in linhas:
        assert fonte.size(linha)[0] <= 150