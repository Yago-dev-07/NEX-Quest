import pygame

from src.config import COR_PRIMARIA, COR_SECUNDARIA, COR_FUNDO

def desenhar_botao(tela, texto, x, y, largura, altura, fonte):
    """Desenha um botão interativo e retorna seu retângulo."""

    botao = pygame.Rect(x, y, largura, altura)

    # Verifica a posição do mouse
    posicao_mouse = pygame.mouse.get_pos()

    if botao.collidepoint(posicao_mouse):
        cor = COR_SECUNDARIA
    else:
        cor = COR_PRIMARIA

    # Desenha o botão
    pygame.draw.rect(tela, cor, botao, border_radius=10)

    # Renderiza e centraliza o texto
    texto_renderizado = fonte.render(texto, True, COR_FUNDO)
    posicao_texto = texto_renderizado.get_rect(center=botao.center)

    tela.blit(texto_renderizado, posicao_texto)

    return botao

def verificar_clique(evento, botao):
    """Verifica se o botão foi clicado com o botão esquerdo do mouse."""

    if evento.type == pygame.MOUSEBUTTONDOWN:
        if evento.button == 1:
            if botao.collidepoint(evento.pos):
                return True
    
    return False