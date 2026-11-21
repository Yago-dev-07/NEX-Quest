"""Funções e componentes de desenho da interface do quiz

Este módulo só DESENHA. Ele não decide se a resposta está certa nem altera
pontos/vidas
"""
import pygame

from src import config
from src.config import (
    COR_FUNDO,
    COR_FUNDO_SECUNDARIO,
    COR_PRIMARIA,
    COR_SECUNDARIA,
    COR_TEXTO,
    COR_TEXTO_SECUNDARIO,
    COR_ACERTO,
    COR_ERRO,
)


VIDAS_INICIAIS = getattr(config, "VIDAS_INICIAIS", 3)


def misturar(cor_a, cor_b, t):
    """Mistura duas cores RGB. t=0 devolve cor_a e t=1 devolve cor_b."""
    return tuple(int(a + (b - a) * t) for a, b in zip(cor_a, cor_b))



COR_PAINEL = COR_FUNDO_SECUNDARIO
COR_BOTAO = COR_FUNDO_SECUNDARIO
COR_BOTAO_HOVER = misturar(COR_FUNDO_SECUNDARIO, COR_SECUNDARIA, 0.45)
COR_APAGADA = misturar(COR_FUNDO, COR_FUNDO_SECUNDARIO, 0.5)
COR_TEXTO_APAGADO = misturar(COR_TEXTO_SECUNDARIO, COR_FUNDO, 0.5)


def quebrar_texto(texto, fonte, largura_max):
    """Quebra um texto em linhas que cabem em `largura_max` pixels.

    Args:
        texto: texto completo.
        fonte: pygame.font.Font usada para medir.
        largura_max: largura máxima de cada linha, em pixels.

    Returns:
        Lista de strings (uma por linha).
    """
    linhas, atual = [], ""
    for palavra in texto.split():
        teste = f"{atual} {palavra}".strip()
        if fonte.size(teste)[0] <= largura_max:
            atual = teste
        else:
            if atual:
                linhas.append(atual)
            atual = palavra
    if atual:
        linhas.append(atual)
    return linhas


def desenhar_texto_multilinha(tela, texto, fonte, cor, rect, espacamento=4):
    """Desenha texto com quebra automática dentro de um retângulo."""
    y = rect.y
    for linha in quebrar_texto(texto, fonte, rect.width):
        superficie = fonte.render(linha, True, cor)
        tela.blit(superficie, (rect.x, y))
        y += superficie.get_height() + espacamento


def desenhar_painel(tela, rect, cor=COR_PAINEL, borda=COR_PRIMARIA):
    """Desenha um painel arredondado com borda."""
    pygame.draw.rect(tela, cor, rect, border_radius=12)
    pygame.draw.rect(tela, borda, rect, width=2, border_radius=12)


def desenhar_hud(tela, estado, fonte):
    """Desenha vidas, pontuação, combo e fase no topo da tela.

    Args:
        tela: superfície do Pygame.
        estado: dict com as chaves 'vidas', 'pontuacao', 'combo' e 'fase'.
        fonte: fonte para os textos.
    """
    largura = tela.get_width()
    vidas = estado.get("vidas", VIDAS_INICIAIS)

    
    for i in range(VIDAS_INICIAIS):
        centro = (40 + i * 34, 30)
        if i < vidas:
            pygame.draw.circle(tela, COR_ERRO, centro, 12)
        else:
            pygame.draw.circle(tela, COR_APAGADA, centro, 12, width=2)

    fase = fonte.render(f"Fase {estado.get('fase', 1)}", True, COR_PRIMARIA)
    tela.blit(fase, fase.get_rect(center=(largura // 2, 30)))

    pontos = fonte.render(f"Pontos: {estado.get('pontuacao', 0)}", True, COR_TEXTO)
    tela.blit(pontos, pontos.get_rect(topright=(largura - 40, 10)))

    combo = estado.get("combo", 0)
    cor_combo = COR_ACERTO if combo >= 2 else COR_TEXTO_SECUNDARIO
    texto_combo = fonte.render(f"Combo x{combo}", True, cor_combo)
    tela.blit(texto_combo, texto_combo.get_rect(topright=(largura - 40, 34)))


def desenhar_progresso(tela, respondidas, total, rect, fonte):
    """Desenha a barra de progresso das perguntas."""
    pygame.draw.rect(tela, COR_APAGADA, rect, border_radius=8)
    if total > 0:
        largura = int(rect.width * respondidas / total)
        if largura > 0:
            preenchido = pygame.Rect(rect.x, rect.y, largura, rect.height)
            pygame.draw.rect(tela, COR_PRIMARIA, preenchido, border_radius=8)
    texto = fonte.render(f"{respondidas}/{total}", True, COR_TEXTO)
    tela.blit(texto, texto.get_rect(center=rect.center))


class BotaoQuiz:
    """Botão de alternativa (A, B, C ou D) com estados de feedback.

    Estados possíveis: 'normal', 'hover', 'correta', 'errada', 'apagada'.
    O texto longo é quebrado em até duas linhas automaticamente.
    """

    CORES = {
        "normal": COR_BOTAO,
        "hover": COR_BOTAO_HOVER,
        "correta": COR_ACERTO,
        "errada": COR_ERRO,
        "apagada": COR_APAGADA,
    }
    BORDAS = {
        "normal": COR_PRIMARIA,
        "hover": COR_SECUNDARIA,
        "correta": COR_TEXTO,
        "errada": COR_TEXTO,
        "apagada": COR_FUNDO_SECUNDARIO,
    }

    def __init__(self, rect, texto, letra):
        self.rect = pygame.Rect(rect)
        self.texto = texto
        self.letra = letra
        self.estado = "normal"

    def atualizar_hover(self, pos_mouse):
        """Alterna entre 'normal' e 'hover' conforme a posição do mouse."""
        if self.estado in ("normal", "hover"):
            sobre = self.rect.collidepoint(pos_mouse)
            self.estado = "hover" if sobre else "normal"

    def desenhar(self, tela, fonte):
        """Desenha o botão na tela."""
        pygame.draw.rect(tela, self.CORES[self.estado], self.rect, border_radius=10)
        pygame.draw.rect(tela, self.BORDAS[self.estado], self.rect, width=2, border_radius=10)

        cor_texto = COR_TEXTO_APAGADO if self.estado == "apagada" else COR_TEXTO

        letra = fonte.render(f"{self.letra})", True, cor_texto)
        tela.blit(letra, letra.get_rect(midleft=(self.rect.x + 16, self.rect.centery)))

        x_texto = self.rect.x + 52
        largura_texto = self.rect.right - x_texto - 12
        linhas = quebrar_texto(self.texto, fonte, largura_texto)
        altura_linha = fonte.get_linesize()
        y = self.rect.centery - (altura_linha * len(linhas)) // 2
        for linha in linhas:
            tela.blit(fonte.render(linha, True, cor_texto), (x_texto, y))
            y += altura_linha


def desenhar_explicacao(tela, acertou, explicacao, rect, fonte_titulo, fonte_texto):
    """Desenha o painel de feedback com a explicação educativa."""
    cor = COR_ACERTO if acertou else COR_ERRO
    desenhar_painel(tela, rect, borda=cor)
    titulo = "Correto!" if acertou else "Resposta incorreta"
    tela.blit(fonte_titulo.render(titulo, True, cor), (rect.x + 14, rect.y + 8))
    area = pygame.Rect(rect.x + 14, rect.y + 38, rect.width - 28, rect.height - 44)
    desenhar_texto_multilinha(tela, explicacao, fonte_texto, COR_TEXTO, area, 2)