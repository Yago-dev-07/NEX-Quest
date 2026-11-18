import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    COR_FUNDO,
    COR_PRIMARIA, 
    COR_SECUNDARIA,
    COR_TEXTO_SECUNDARIO
)

from src.botoes import desenhar_botao

def desenhar_texto_centralizado(tela, texto, fonte, cor, y):
    """Desenha um texto centralizado horizontalmente na tela."""

    texto_renderizado = fonte.render(texto, True, cor)

    posicao_texto = texto_renderizado.get_rect(center=(LARGURA_TELA // 2, y))

    tela.blit(texto_renderizado, posicao_texto)

def desenhar_tela_inicial(tela):
    """Desenha a tela inicial e retora seus botões."""

    tela.fill(COR_FUNDO)

    # Configurações das fontes
    fonte_titulo = pygame.font.SysFont("arial", 56, bold=True)
    fonte_subtitulo = pygame.font.SysFont("arial", 26)
    fonte_texto = pygame.font.SysFont("arial", 20)
    fonte_botao = pygame.font.SysFont("arial", 24, bold=True)

    # Textos principais
    desenhar_texto_centralizado(tela, "NEX QUEST", fonte_titulo, COR_PRIMARIA, 100)

    desenhar_texto_centralizado(tela, "A Missão da Inteligência Artificial", fonte_subtitulo, COR_SECUNDARIA, 160)

    desenhar_texto_centralizado(tela, "Ajude NEX a recuperar suas memórias!", fonte_texto, COR_TEXTO_SECUNDARIO, 220)

    # Dimensões e posição dos botões
    largura_botao = 260
    altura_botao = 55

    x_botao = (LARGURA_TELA - largura_botao) // 2

    # Botões
    botao_jogar = desenhar_botao(tela, "Jogar", x_botao, 290, largura_botao, altura_botao, fonte_botao)

    botao_instrucoes = desenhar_botao(tela, "Como jogar", x_botao, 365, largura_botao, altura_botao, fonte_botao)

    botao_sair = desenhar_botao(tela, "Sair", x_botao, 440, largura_botao, altura_botao, fonte_botao)

    # Rodapé
    desenhar_texto_centralizado(tela, "Uma aventura pelo universo da inteligência artificial.", fonte_texto, COR_TEXTO_SECUNDARIO, ALTURA_TELA - 35)

    return {
        "jogar": botao_jogar,
        "instrucoes": botao_instrucoes,
        "sair": botao_sair
    }