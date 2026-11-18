import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    COR_FUNDO,
    COR_FUNDO_SECUNDARIO,
    COR_PRIMARIA, 
    COR_SECUNDARIA,
    COR_TEXTO_SECUNDARIO,
    COR_ACERTO,
    COR_ERRO
)

from src.botoes import desenhar_botao

def desenhar_texto_centralizado(tela, texto, fonte, cor, y):
    """Desenha um texto centralizado horizontalmente na tela."""

    texto_renderizado = fonte.render(texto, True, cor)

    posicao_texto = texto_renderizado.get_rect(center=(LARGURA_TELA // 2, y))

    tela.blit(texto_renderizado, posicao_texto)

def desenhar_texto(tela, texto, fonte, cor, x, y):
    """Desenha um texto em uma posição específica."""
    texto_renderizado = fonte.render(texto, True, cor)

    tela.blit(texto_renderizado, (x, y))

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

def desenhar_tela_instrucoes(tela):
    """Desenha a tela de instruções e retorna o botão de voltar."""

    tela.fill(COR_FUNDO)

    # Configuração das fontes
    fonte_titulo = pygame.font.SysFont("arial", 42, bold=True)
    fonte_subtitulo = pygame.font.SysFont("arial", 24)
    fonte_texto = pygame.font.SysFont("arial", 20)
    fonte_botao = pygame.font.SysFont("arial", 24, bold=True)

    # Título e subtítulo
    desenhar_texto_centralizado(tela, "COMO JOGAR", fonte_titulo, COR_PRIMARIA, 50)

    desenhar_texto_centralizado(tela, "Conheça as regras da sua missão!", fonte_subtitulo, COR_SECUNDARIA, 100)

    # Painel de instruções
    painel = pygame.Rect(60, 140, LARGURA_TELA - 120, 340)

    pygame.draw.rect(tela, COR_FUNDO_SECUNDARIO, painel, border_radius=15)

    # Lista de instruções
    instrucoes = [
        "Ajude NEX a recuperar suas memórias.",
        "Responda perguntas sobre inteligência artificial.",
        "Complete as três fases do jogo.",
        "Você começa com 3 vidas.",
        "Cada acerto vale 100 pontos.",
        "Cadas erro faz você perder uma vida.",
        "3 acertos consecutivos valem 50 pontos extras.",
        "Utilize o mouse para selecionar as alternativas."
    ]

    # Exibição das instruções
    y = 165

    for instrucao in instrucoes:
        desenhar_texto(tela, instrucao, fonte_texto, COR_TEXTO_SECUNDARIO, 85, y)

        y += 38
    
    # Botão de voltar
    largura_botao = 260
    altura_botao = 55

    x_botao = (LARGURA_TELA - largura_botao) // 2

    botao_voltar = desenhar_botao(tela, "Voltar", x_botao, 510, largura_botao, altura_botao, fonte_botao)

    return {"voltar": botao_voltar}

def desenhar_texto_posicao(tela, texto, fonte, cor, x, y):
    """Desenha um texto centralizado nas coordenadas informadas."""
    
    texto_renderizado = fonte.render(texto, True, cor)

    posicao_texto = texto_renderizado.get_rect(center=(x, y))
    
    tela.blit(texto_renderizado, posicao_texto)

def desenhar_tela_vitoria(tela, pontuacao, vidas):
    """Desenha a tela de vitória e retorna seus botões."""

    tela.fill(COR_FUNDO)

    # Configuração das fontes
    fonte_titulo = pygame.font.SysFont("arial", 46, bold=True)
    fonte_texto = pygame.font.SysFont("arial", 22)
    fonte_resultado = pygame.font.SysFont("arial", 38, bold=True)
    fonte_botao = pygame.font.SysFont("arial", 24, bold=True)

    # Mensagem de vitória
    desenhar_texto_centralizado(tela, "MISSÃO CONCLUÍDA!", fonte_titulo, COR_PRIMARIA, 65)

    desenhar_texto_centralizado(tela, "Parabéns! Você recuperou as memórias de NEX.", fonte_texto, COR_SECUNDARIA, 120)

    # Painel de resultados
    painel = pygame.Rect(100, 170, LARGURA_TELA - 200, 150)

    pygame.draw.rect(tela, COR_FUNDO_SECUNDARIO, painel, border_radius=15)

    # Pontuação final
    desenhar_texto_posicao(tela, "Pontuação final", fonte_texto, COR_TEXTO_SECUNDARIO, 250, 210)

    desenhar_texto_posicao(tela, str(pontuacao), fonte_resultado, COR_PRIMARIA, 250, 270)

    # Vidas restantes
    desenhar_texto_posicao(tela, "Vidas restantes", fonte_texto, COR_TEXTO_SECUNDARIO, 550, 210)

    desenhar_texto_posicao(tela, str(vidas), fonte_resultado, COR_ACERTO, 550, 270)

    # Dimensões dos botões
    largura_botao = 260
    altura_botao = 55

    x_botao = (LARGURA_TELA - largura_botao) // 2

    # Botões
    botao_reiniciar = desenhar_botao(tela, "Jogar novamente", x_botao, 350, largura_botao, altura_botao, fonte_botao)

    botao_menu = desenhar_botao(tela, "Menu inicial", x_botao, 425, largura_botao, altura_botao, fonte_botao)

    botao_sair = desenhar_botao(tela, "Sair", x_botao, 500, largura_botao, altura_botao, fonte_botao)

    return {
        "reiniciar": botao_reiniciar,
        "menu": botao_menu,
        "sair": botao_sair
    }
def desenhar_tela_derrota(tela, pontuacao):
    """Desenha a tela de derrota e retorna seus botões."""

    tela.fill(COR_FUNDO)

    # Configuração das fontes
    fonte_titulo = pygame.font.SysFont("arial", 46, bold=True)
    fonte_texto = pygame.font.SysFont("arial", 22)
    fonte_resultado = pygame.font.SysFont("arial", 38, bold=True)
    fonte_botao = pygame.font.SysFont("arial", 24, bold=True)

    # Mensagem de derrota
    desenhar_texto_centralizado(tela, "MISSÃO INTERROMPIDA!", fonte_titulo, COR_ERRO, 65)

    desenhar_texto_centralizado(tela, "NEX ainda precisa da sua ajuda. Tente novamente!", fonte_texto, COR_SECUNDARIA, 120)

    # Painel de resultados
    painel = pygame.Rect(100, 170, LARGURA_TELA - 200, 150)

    pygame.draw.rect(tela, COR_FUNDO_SECUNDARIO, painel, border_radius=15)
    
    # Pontuação final
    desenhar_texto_posicao(tela, "Pontuação final", fonte_texto, COR_TEXTO_SECUNDARIO, 250, 210)

    desenhar_texto_posicao(tela, str(pontuacao), fonte_resultado, COR_PRIMARIA, 250, 270)

    # Vidas restantes
    desenhar_texto_posicao(tela, "Vidas restantes", fonte_texto, COR_TEXTO_SECUNDARIO, 550, 210)

    desenhar_texto_posicao(tela, "0", fonte_resultado, COR_ERRO, 550, 270)

    # Dimensões dos botões
    largura_botao = 260
    altura_botao = 55

    x_botao = (LARGURA_TELA - largura_botao) // 2

    # Botões
    botao_reiniciar = desenhar_botao(tela, "Tentar novamente", x_botao, 350, largura_botao, altura_botao, fonte_botao)

    botao_menu = desenhar_botao(tela, "Menu inicial", x_botao, 425, largura_botao, altura_botao, fonte_botao)

    botao_sair = desenhar_botao(tela, "Sair", x_botao, 500, largura_botao, altura_botao, fonte_botao)

    return {
        "reiniciar": botao_reiniciar,
        "menu": botao_menu,
        "sair": botao_sair
    }