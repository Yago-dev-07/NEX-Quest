
import pygame

from src import interface as ui
from src.botoes import desenhar_botao, verificar_clique
from src.config import COR_FUNDO


class TelaQuiz:
    """Controla a tela de perguntas de uma fase."""

    def __init__(self, tela, perguntas, estado, responder):
        """
        Args:
            tela: superfície principal do Pygame.
            perguntas: lista de perguntas da fase (já embaralhada, se quiser).
            estado: dict com vidas, pontuacao, combo e fase.
            responder: função (estado, pergunta, escolha) -> bool.
        """
        if not perguntas:
            raise ValueError("TelaQuiz precisa de pelo menos uma pergunta.")

        self.tela = tela
        self.perguntas = perguntas
        self.estado = estado
        self.responder = responder

        self.indice = 0
        self.modo = "perguntando" 
        self.acertou = None
        self.terminou = False
        self.rect_proximo = None  

        self.fonte_hud = pygame.font.Font(None, 26)
        self.fonte_pergunta = pygame.font.Font(None, 32)
        self.fonte_alt = pygame.font.Font(None, 24)
        self.fonte_exp = pygame.font.Font(None, 22)

        self.botoes = []
        self._montar_botoes()

    @property
    def resultado(self):
        """'derrota' se acabaram as vidas, senão 'fase_concluida'.

        Só faz sentido depois que `terminou` for True.
        """
        if self.estado.get("vidas", 1) <= 0:
            return "derrota"
        return "fase_concluida"

    #construção 
    def _montar_botoes(self):
        """Cria os botões das alternativas da pergunta atual."""
        largura = self.tela.get_width()
        pergunta = self.perguntas[self.indice]
        self.botoes = []
        for i, texto in enumerate(pergunta["alternativas"]):
            rect = (40, 212 + i * 60, largura - 80, 52)
            self.botoes.append(ui.BotaoQuiz(rect, texto, "ABCD"[i]))

    #eventos 
    def tratar_evento(self, evento):
        """Processa movimento e cliques do mouse."""
        if evento.type == pygame.MOUSEMOTION and self.modo == "perguntando":
            for botao in self.botoes:
                botao.atualizar_hover(evento.pos)

        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if self.modo == "perguntando":
                for i, botao in enumerate(self.botoes):
                    if botao.rect.collidepoint(evento.pos):
                        self._escolher(i)
                        break
            elif self.rect_proximo and verificar_clique(evento, self.rect_proximo):
                self._avancar()

    def _escolher(self, escolha):
        """Registra a resposta e prepara o feedback visual."""
        pergunta = self.perguntas[self.indice]
        self.acertou = bool(self.responder(self.estado, pergunta, escolha))
        correta = pergunta["correta"]

        for i, botao in enumerate(self.botoes):
            if i == correta:
                botao.estado = "correta"
            elif i == escolha:
                botao.estado = "errada"
            else:
                botao.estado = "apagada"

        self.modo = "feedback"
        self.rect_proximo = None

    def _ultima_pergunta(self):
        """True se não há mais perguntas ou se o jogador ficou sem vidas."""
        sem_vidas = self.estado.get("vidas", 1) <= 0
        return sem_vidas or self.indice + 1 >= len(self.perguntas)

    def _avancar(self):
        """Vai para a próxima pergunta ou encerra a fase."""
        self.rect_proximo = None
        if self._ultima_pergunta():
            self.terminou = True
            return
        self.indice += 1
        self.modo = "perguntando"
        self.acertou = None
        self._montar_botoes()

    #desenho
    def desenhar(self):
        """Desenha a tela inteira do quiz."""
        largura = self.tela.get_width()
        altura = self.tela.get_height()
        self.tela.fill(COR_FUNDO)

        ui.desenhar_hud(self.tela, self.estado, self.fonte_hud)

        respondidas = self.indice + (1 if self.modo == "feedback" else 0)
        barra = pygame.Rect(40, 62, largura - 80, 18)
        ui.desenhar_progresso(self.tela, respondidas, len(self.perguntas), barra, self.fonte_exp)

        painel = pygame.Rect(40, 92, largura - 80, 108)
        ui.desenhar_painel(self.tela, painel)
        texto = self.perguntas[self.indice]["pergunta"]
        ui.desenhar_texto_multilinha(
            self.tela, texto, self.fonte_pergunta, ui.COR_TEXTO, painel.inflate(-28, -24)
        )

        for botao in self.botoes:
            botao.desenhar(self.tela, self.fonte_alt)

        if self.modo == "feedback":
            explicacao = self.perguntas[self.indice].get("explicacao", "")
            painel_exp = pygame.Rect(40, 452, largura - 250, altura - 452 - 12)
            ui.desenhar_explicacao(
                self.tela, self.acertou, explicacao, painel_exp, self.fonte_hud, self.fonte_exp
            )
            rotulo = "Finalizar" if self._ultima_pergunta() else "Próxima"
            y_botao = painel_exp.y + (painel_exp.height - 40) // 2
            self.rect_proximo = desenhar_botao(
                self.tela, rotulo, largura - 190, y_botao, 150, 40, self.fonte_hud
            )

def _demo():
    import sys

    from src.config import LARGURA_TELA, ALTURA_TELA, FPS, TITULO_JOGO
    from src.funcoes import calcular_pontos, tomar_dano
    from src.perguntas import obter_perguntas_fase, embaralhar_perguntas

    fase = int(sys.argv[1]) if len(sys.argv) > 1 else 1

    pygame.init()
    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(f"{TITULO_JOGO} - demo do quiz")
    relogio = pygame.time.Clock()

    estado = {"vidas": 3, "pontuacao": 0, "combo": 0, "fase": fase}

    def responder_provisorio(estado, pergunta, escolha):
        """PROVISÓRIO: substituir pela função oficial do Cauã (funcoes.py)."""
        acertou = escolha == pergunta["correta"]
        if acertou:
            estado["combo"] += 1
            estado["pontuacao"] = calcular_pontos(estado["pontuacao"], 100)
            if estado["combo"] % 3 == 0:
                estado["pontuacao"] = calcular_pontos(estado["pontuacao"], 50)
        else:
            estado["vidas"] = tomar_dano(estado["vidas"], 1)
            estado["combo"] = 0
        return acertou

    perguntas = embaralhar_perguntas(obter_perguntas_fase(fase))
    quiz = TelaQuiz(tela, perguntas, estado, responder_provisorio)

    rodando = True
    while rodando and not quiz.terminou:
        relogio.tick(FPS)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            quiz.tratar_evento(evento)
        quiz.desenhar()
        pygame.display.flip()

    if quiz.terminou:
        print("Resultado:", quiz.resultado, "| Pontos:", estado["pontuacao"])
    pygame.quit()


if __name__ == "__main__":
    _demo()