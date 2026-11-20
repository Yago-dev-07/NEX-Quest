import math

import pygame

from src.config import (
    LARGURA_TELA,
    COR_FUNDO,
    COR_PRIMARIA,
    COR_SECUNDARIA,
    COR_TEXTO,
    COR_TEXTO_SECUNDARIO,
)
from src.funcoes import limitar_valor


def pegar_sprite(local_arquivo, x, y, width, height, scale=1):
    """Corta um único elemento de uma spritesheet BMP e remove o fundo."""

    # 1. Carrega o BMP e usa .convert() (sem alpha) para otimizar a velocidade
    sheet = pygame.image.load(local_arquivo).convert()

    # 2. Cria uma superfície padrão para o recorte (não precisa de SRCALPHA aqui)
    image = pygame.Surface((width, height))

    # 3. Copia o pedaço da folha BMP para a nossa nova imagem
    image.blit(sheet, (0, 0), (x, y, width, height))

    # 4. CONFIGURAÇÃO DA TRANSPARÊNCIA (O segredo para o BMP)
    # Pegamos a cor do pixel no canto superior esquerdo (0,0) do recorte,
    # assumindo que o fundo do seu sprite começa ali.
    cor_do_fundo = image.get_at((0, 0))

    # Dizemos ao Pygame para ignorar essa cor específica na hora de desenhar
    image.set_colorkey(cor_do_fundo)

    # 5. Aplica o redimensionamento, se houver
    if scale != 1:
        novo_largura = int(width * scale)
        novo_altura = int(height * scale)
        image = pygame.transform.scale(image, (novo_largura, novo_altura))

    return image


# ---------------------------------------------------------------------------
# Personagem NEX
# ---------------------------------------------------------------------------

# Mensagens que o NEX apresenta em cada situação do jogo.
MENSAGENS_NEX = {
    "inicio": "Olá! Preciso da sua ajuda para recuperar minhas memórias!",
    "acerto": "Muito bem! Você recuperou mais uma memória!",
    "erro": "Ops! Essa memória ainda está confusa...",
    "vitoria": "Conseguimos! Todas as minhas memórias foram recuperadas!",
    "derrota": "Ah, não! Precisamos tentar novamente!",
}

# Expressão do rosto que acompanha cada situação.
EXPRESSOES_NEX = {
    "inicio": "neutro",
    "acerto": "feliz",
    "erro": "triste",
    "vitoria": "feliz",
    "derrota": "triste",
}


def _desenhar_nex(tamanho, expressao):
    """Desenha o robô NEX com formas do Pygame e devolve a imagem.

    Todas as medidas são dadas numa grade de 0 a 100 e convertidas para o
    tamanho pedido, assim o NEX pode ser desenhado em qualquer escala.
    """
    unidade = tamanho / 100

    def p(valor):
        return int(valor * unidade)

    def ret(x, y, largura, altura):
        return pygame.Rect(p(x), p(y), p(largura), p(altura))

    imagem = pygame.Surface((tamanho, tamanho), pygame.SRCALPHA)
    espessura = max(2, p(3))

    # Antena
    pygame.draw.line(imagem, COR_TEXTO_SECUNDARIO, (p(50), p(8)), (p(50), p(17)), espessura)
    pygame.draw.circle(imagem, COR_SECUNDARIA, (p(50), p(7)), p(5))

    # Braços, corpo e pés
    pygame.draw.rect(imagem, COR_PRIMARIA, ret(18, 60, 9, 26), border_radius=p(4))
    pygame.draw.rect(imagem, COR_PRIMARIA, ret(73, 60, 9, 26), border_radius=p(4))
    pygame.draw.rect(imagem, COR_SECUNDARIA, ret(30, 58, 40, 34), border_radius=p(8))
    pygame.draw.circle(imagem, COR_PRIMARIA, (p(50), p(75)), p(7))
    pygame.draw.rect(imagem, COR_TEXTO_SECUNDARIO, ret(34, 92, 12, 6), border_radius=p(3))
    pygame.draw.rect(imagem, COR_TEXTO_SECUNDARIO, ret(54, 92, 12, 6), border_radius=p(3))

    # Cabeça com a "tela" do rosto
    pygame.draw.rect(imagem, COR_PRIMARIA, ret(20, 16, 60, 40), border_radius=p(10))
    pygame.draw.rect(imagem, COR_FUNDO, ret(27, 22, 46, 28), border_radius=p(6))

    # Olhos e boca mudam conforme a expressão
    if expressao == "feliz":
        # Olhos em arco (^ ^) e sorriso
        pygame.draw.arc(imagem, COR_PRIMARIA, ret(35, 30, 10, 10), 0, math.pi, espessura)
        pygame.draw.arc(imagem, COR_PRIMARIA, ret(55, 30, 10, 10), 0, math.pi, espessura)
        pygame.draw.arc(imagem, COR_PRIMARIA, ret(44, 36, 12, 10), math.pi, 2 * math.pi, espessura)
    elif expressao == "triste":
        # Olhos menores e boca curvada para baixo
        pygame.draw.circle(imagem, COR_PRIMARIA, (p(40), p(34)), p(4))
        pygame.draw.circle(imagem, COR_PRIMARIA, (p(60), p(34)), p(4))
        pygame.draw.arc(imagem, COR_PRIMARIA, ret(44, 42, 12, 10), 0, math.pi, espessura)
    else:
        # Neutro: olhos redondos e boca reta
        pygame.draw.circle(imagem, COR_PRIMARIA, (p(40), p(34)), p(5))
        pygame.draw.circle(imagem, COR_PRIMARIA, (p(60), p(34)), p(5))
        pygame.draw.line(imagem, COR_PRIMARIA, (p(44), p(43)), (p(56), p(43)), espessura)

    return imagem


def criar_nex(tamanho=130):
    """Cria o NEX (um dicionário, no mesmo estilo do template).

    As três expressões são desenhadas uma única vez aqui; depois o jogo só
    escolhe qual delas mostrar.
    """
    imagens = {}
    for expressao in ("neutro", "feliz", "triste"):
        imagens[expressao] = _desenhar_nex(tamanho, expressao)

    return {
        "imagens": imagens,
        "rect": pygame.Rect(0, 0, tamanho, tamanho),
        "expressao": "neutro",
        "mensagem": "",
    }


def nex_posicionar(nex, x, y):
    """Posiciona o NEX pelo centro da base (x = meio, y = chão)."""
    nex["rect"].midbottom = (x, y)


def nex_falar(nex, situacao):
    """Faz o NEX dizer a mensagem da situação ("inicio", "acerto", ...)."""
    nex["mensagem"] = MENSAGENS_NEX[situacao]
    nex["expressao"] = EXPRESSOES_NEX[situacao]


def nex_calar(nex):
    """Tira o balão de fala e volta o NEX para a expressão neutra."""
    nex["mensagem"] = ""
    nex["expressao"] = "neutro"


def quebrar_texto(texto, fonte, largura_maxima):
    """Divide um texto em linhas que cabem na largura informada."""
    linhas = []
    linha_atual = ""

    for palavra in texto.split():
        if linha_atual == "":
            tentativa = palavra
        else:
            tentativa = linha_atual + " " + palavra

        if fonte.size(tentativa)[0] <= largura_maxima:
            linha_atual = tentativa
        else:
            if linha_atual != "":
                linhas.append(linha_atual)
            linha_atual = palavra

    if linha_atual != "":
        linhas.append(linha_atual)

    return linhas


def _desenhar_balao(tela, texto, fonte, nex_rect, largura=210):
    """Desenha o balão de fala acima do NEX."""
    margem = 10
    linhas = quebrar_texto(texto, fonte, largura - 2 * margem)
    altura_linha = fonte.get_linesize()
    altura = len(linhas) * altura_linha + 2 * margem

    # Mantém o balão inteiro dentro da tela
    x = limitar_valor(nex_rect.centerx - largura // 2, 10, LARGURA_TELA - largura - 10)
    y = nex_rect.top - altura - 14
    balao = pygame.Rect(x, y, largura, altura)

    pygame.draw.rect(tela, COR_TEXTO, balao, border_radius=12)

    # Pontinha do balão apontando para o NEX
    ponta_x = limitar_valor(nex_rect.centerx, balao.left + 20, balao.right - 20)
    pygame.draw.polygon(tela, COR_TEXTO, [
        (ponta_x - 8, balao.bottom - 1),
        (ponta_x + 8, balao.bottom - 1),
        (ponta_x, balao.bottom + 10),
    ])

    for i, linha in enumerate(linhas):
        texto_renderizado = fonte.render(linha, True, COR_FUNDO)
        tela.blit(texto_renderizado, (balao.x + margem, balao.y + margem + i * altura_linha))


def desenhar_nex(tela, nex, fonte):
    """Desenha o NEX e, se ele estiver falando, o balão com a mensagem."""
    tela.blit(nex["imagens"][nex["expressao"]], nex["rect"])

    if nex["mensagem"] != "":
        _desenhar_balao(tela, nex["mensagem"], fonte, nex["rect"])