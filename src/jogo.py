import pygame

from src.quiz import TelaQuiz

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    FPS,
    TITULO_JOGO,
    COR_FUNDO,
    COR_FUNDO_SECUNDARIO,
    COR_PRIMARIA,
    COR_SECUNDARIA,
    COR_TEXTO,
    COR_TEXTO_SECUNDARIO,
    COR_ACERTO,
    COR_ERRO,
    CAMINHO_RECORDE,
)
from src.funcoes import (
    processar_resposta,
    jogador_perdeu,
    jogador_venceu,
    avancar_pergunta,
    avancar_fase,
)
from src.dados import carregar_recorde, atualizar_recorde
from src.perguntas import obter_perguntas_fase, embaralhar_perguntas
from src.botoes import desenhar_botao, verificar_clique
from src.telas import (
    desenhar_texto,
    desenhar_texto_centralizado,
    desenhar_tela_inicial,
    desenhar_tela_instrucoes,
    desenhar_tela_vitoria,
    desenhar_tela_derrota,
)
from src.sprites import (
    criar_nex,
    nex_posicionar,
    nex_falar,
    nex_calar,
    desenhar_nex,
    quebrar_texto,
)

# ---------------------------------------------------------------------------
# Constantes do jogo
# ---------------------------------------------------------------------------
VIDAS_INICIAIS = 3
TOTAL_FASES = 3

# Os estados possíveis do jogo (cada um é uma "tela"):
#   "menu" | "instrucoes" | "quiz" | "vitoria" | "derrota"


# ---------------------------------------------------------------------------
# Lógica da partida (sem desenho: só dados e regras)
# ---------------------------------------------------------------------------
def carregar_fase(numero_fase):
    """Sorteia a ordem das perguntas de uma fase."""
    return embaralhar_perguntas(obter_perguntas_fase(numero_fase))


def criar_partida():
    """Cria o estado inicial de uma partida nova."""
    return {
        "fase": 1,
        "indice": 0,                      # pergunta atual dentro da fase
        "perguntas": carregar_fase(1),
        "pontos": 0,
        "vidas": VIDAS_INICIAIS,
        "combo": 0,                       # acertos seguidos
        "resposta": None,                 # alternativa escolhida (None = ainda não respondeu)
    }


def pergunta_atual(partida):
    """Retorna a pergunta que está sendo exibida."""
    return partida["perguntas"][partida["indice"]]


def registrar_resposta(partida, escolha):
    """Aplica a resposta do jogador (pontos, vidas, combo). Retorna True se acertou."""
    pergunta = pergunta_atual(partida)

    pontos, vidas, combo, acertou = processar_resposta(
        partida["pontos"],
        partida["vidas"],
        partida["combo"],
        escolha,
        pergunta["correta"],
    )

    partida["pontos"] = pontos
    partida["vidas"] = vidas
    partida["combo"] = combo
    partida["resposta"] = escolha

    return acertou


def avancar_partida(partida):
    """Passa para a próxima pergunta/fase. Retorna o próximo estado do jogo."""
    if jogador_perdeu(partida["vidas"]):
        return "derrota"

    partida["indice"] = avancar_pergunta(partida["indice"])
    partida["resposta"] = None

    # Acabaram as perguntas da fase?
    if partida["indice"] >= len(partida["perguntas"]):
        if jogador_venceu(partida["fase"], TOTAL_FASES, partida["vidas"]):
            return "vitoria"

        partida["fase"] = avancar_fase(partida["fase"], TOTAL_FASES)
        partida["perguntas"] = carregar_fase(partida["fase"])
        partida["indice"] = 0

    return "quiz"


# ---------------------------------------------------------------------------
# Estado geral do jogo e transições entre telas
# ---------------------------------------------------------------------------
def criar_fontes():
    """Cria as fontes uma única vez (criar fonte a cada quadro é lento)."""
    return {
        "texto": pygame.font.SysFont("arial", 20),
        "pequena": pygame.font.SysFont("arial", 18),
        "balao": pygame.font.SysFont("arial", 17),
        "pergunta": pygame.font.SysFont("arial", 24, bold=True),
        "botao": pygame.font.SysFont("arial", 22, bold=True),
    }


def criar_jogo():
    """Cria o dicionário que guarda tudo o que o jogo precisa lembrar."""
    jogo = {
        "estado": "menu",
        "rodando": True,
        "partida": None,
        "recorde": carregar_recorde(CAMINHO_RECORDE),
        "novo_recorde": False,
        "nex": criar_nex(130),
        "quiz": None,
        "botoes": {},        # botões da tela atual (preenchido ao desenhar)
    }
    mudar_estado(jogo, "menu")
    return jogo


def mudar_estado(jogo, novo_estado):
    """Troca de tela e ajusta o que o NEX diz nela."""
    jogo["estado"] = novo_estado

    if novo_estado in ("menu", "quiz"):
        nex_falar(jogo["nex"], "inicio")
    elif novo_estado in ("vitoria", "derrota"):
        nex_falar(jogo["nex"], novo_estado)
    else:
        nex_calar(jogo["nex"])


def iniciar_partida(jogo):
    """Começa uma partida nova e vai para o quiz."""
    jogo["partida"] = criar_partida()
    jogo["quiz"] = None
    jogo["novo_recorde"] = False
    mudar_estado(jogo, "quiz")


def finalizar_partida(jogo):
    """Confere se a pontuação virou recorde e salva em arquivo."""
    jogo["novo_recorde"] = atualizar_recorde(CAMINHO_RECORDE, jogo["partida"]["pontos"])
    jogo["recorde"] = carregar_recorde(CAMINHO_RECORDE)


# ---------------------------------------------------------------------------
# Desenho de cada tela
# ---------------------------------------------------------------------------
def desenhar_menu(tela, jogo, fontes):
    jogo["botoes"] = desenhar_tela_inicial(tela)

    desenhar_texto_centralizado(
        tela, f"Recorde: {jogo['recorde']}", fontes["texto"], COR_TEXTO, 262
    )

    nex_posicionar(jogo["nex"], 135, 575)
    desenhar_nex(tela, jogo["nex"], fontes["balao"])


def desenhar_instrucoes(tela, jogo, fontes):
    jogo["botoes"] = desenhar_tela_instrucoes(tela)


def desenhar_resultado(tela, jogo, fontes):
    """Desenha a tela de vitória ou derrota, com recorde e NEX."""
    partida = jogo["partida"]

    if jogo["estado"] == "vitoria":
        jogo["botoes"] = desenhar_tela_vitoria(tela, partida["pontos"], partida["vidas"])
    else:
        jogo["botoes"] = desenhar_tela_derrota(tela, partida["pontos"])

    if jogo["novo_recorde"]:
        texto = f"NOVO RECORDE: {jogo['recorde']}!"
        cor = COR_ACERTO
    else:
        texto = f"Recorde: {jogo['recorde']}"
        cor = COR_TEXTO_SECUNDARIO
    desenhar_texto_centralizado(tela, texto, fontes["texto"], cor, 335)

    nex_posicionar(jogo["nex"], 135, 575)
    desenhar_nex(tela, jogo["nex"], fontes["balao"])

def criar_interface_quiz(tela, jogo):
    """Conecta a interface do Miguel à lógica da partida."""

    partida = jogo["partida"]

    # A interface utiliza 'pontuacao'; a lógica utiliza 'pontos'.
    partida["pontuacao"] = partida["pontos"]

    def responder(estado, pergunta, escolha):
        # Sincroniza o índice da pergunta atual.
        partida["indice"] = jogo["quiz"].indice

        # Utiliza a lógica oficial de pontuação, vidas e combo.
        acertou = registrar_resposta(partida, escolha)

        # Atualiza o valor utilizado pelo Miguel.
        estado["pontuacao"] = partida["pontos"]

        # Atualiza a fala do personagem NEX.
        nex_falar(jogo["nex"], "acerto" if acertou else "erro")

        return acertou
    
    jogo["quiz"] = TelaQuiz(tela, partida["perguntas"], partida, responder)

def desenhar_quiz(tela, jogo, fontes):
    """Desenha a interface do quiz."""

    if jogo["quiz"] is None:
        criar_interface_quiz(tela, jogo)

    jogo["quiz"].desenhar()

# ---------------------------------------------------------------------------
# Tratamento de eventos (cliques) de cada tela
# ---------------------------------------------------------------------------
# Cada função devolve True quando o evento foi usado (um botão foi clicado).
def tratar_menu(jogo, evento):
    botoes = jogo["botoes"]

    if verificar_clique(evento, botoes["jogar"]):
        iniciar_partida(jogo)
    elif verificar_clique(evento, botoes["instrucoes"]):
        mudar_estado(jogo, "instrucoes")
    elif verificar_clique(evento, botoes["sair"]):
        jogo["rodando"] = False
    else:
        return False

    return True


def tratar_instrucoes(jogo, evento):
    if verificar_clique(evento, jogo["botoes"]["voltar"]):
        mudar_estado(jogo, "menu")
        return True

    return False


def tratar_quiz(jogo, evento):
    """Processa os eventos da interface definitiva."""

    quiz = jogo["quiz"]

    if quiz is None:
        return False

    # Guarda o estado anterior para detectar alterações.
    indice_anterior = quiz.indice
    modo_anterior = quiz.modo

    # A interface do Miguel processa o clique.
    quiz.tratar_evento(evento)

    # Verifica se a fase terminou.
    if quiz.terminou:
        partida = jogo["partida"]

        # A lógica oficial decide se haverá outra fase,
        # vitória ou derrota.
        partida["indice"] = len(partida["perguntas"]) - 1

        proximo = avancar_partida(partida)

        if proximo == "quiz":
            # Uma nova fase será carregada no próximo desenho.
            jogo["quiz"] = None
            nex_calar(jogo["nex"])

        else:
            finalizar_partida(jogo)
            mudar_estado(jogo, proximo)

        return True

    # Descarta os eventos restantes quando uma resposta
    # ou mudança de pergunta ocorrer.
    return (
        quiz.indice != indice_anterior
        or quiz.modo != modo_anterior
    )


def tratar_resultado(jogo, evento):
    botoes = jogo["botoes"]

    if verificar_clique(evento, botoes["reiniciar"]):
        iniciar_partida(jogo)
    elif verificar_clique(evento, botoes["menu"]):
        mudar_estado(jogo, "menu")
    elif verificar_clique(evento, botoes["sair"]):
        jogo["rodando"] = False
    else:
        return False

    return True


# Qual função desenha / trata cada estado
DESENHAR = {
    "menu": desenhar_menu,
    "instrucoes": desenhar_instrucoes,
    "quiz": desenhar_quiz,
    "vitoria": desenhar_resultado,
    "derrota": desenhar_resultado,
}

TRATAR = {
    "menu": tratar_menu,
    "instrucoes": tratar_instrucoes,
    "quiz": tratar_quiz,
    "vitoria": tratar_resultado,
    "derrota": tratar_resultado,
}


# ---------------------------------------------------------------------------
# Game loop
# ---------------------------------------------------------------------------
def executar_jogo():
    """Executa o loop principal: desenha a tela do estado atual e trata os cliques."""
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    relogio = pygame.time.Clock()
    fontes = criar_fontes()
    jogo = criar_jogo()

    while jogo["rodando"]:
        relogio.tick(FPS)

        # 1. Desenha a tela atual (isso também descobre onde estão os botões)
        DESENHAR[jogo["estado"]](tela, jogo, fontes)

        # 2. Trata os eventos usando os botões que acabaram de ser desenhados
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogo["rodando"] = False
                break

            # Se o clique mudou algo (tela, pergunta...), os botões guardados
            # já estão velhos: descartamos o resto dos eventos deste quadro.
            if TRATAR[jogo["estado"]](jogo, evento):
                break

        # 3. Mostra o quadro pronto
        pygame.display.flip()

    pygame.quit()