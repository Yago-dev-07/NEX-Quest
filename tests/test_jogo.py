from src.jogo import (
    VIDAS_INICIAIS,
    avancar_partida,
    criar_partida,
    pergunta_atual,
    registrar_resposta,
)


def responder_certo(partida):
    return registrar_resposta(partida, pergunta_atual(partida)["correta"])


def responder_errado(partida):
    return registrar_resposta(partida, (pergunta_atual(partida)["correta"] + 1) % 4)


def test_criar_partida_valores_iniciais():
    partida = criar_partida()

    assert partida["fase"] == 1
    assert partida["indice"] == 0
    assert partida["pontos"] == 0
    assert partida["vidas"] == VIDAS_INICIAIS
    assert partida["resposta"] is None
    assert len(partida["perguntas"]) == 5


def test_acerto_soma_pontos_e_mantem_vidas():
    partida = criar_partida()

    assert responder_certo(partida) is True
    assert partida["pontos"] == 100
    assert partida["vidas"] == VIDAS_INICIAIS


def test_erro_tira_uma_vida_e_zera_combo():
    partida = criar_partida()
    responder_certo(partida)

    assert responder_errado(partida) is False
    assert partida["vidas"] == VIDAS_INICIAIS - 1
    assert partida["combo"] == 0


def test_avancar_limpa_resposta_e_vai_para_proxima_pergunta():
    partida = criar_partida()
    responder_certo(partida)

    assert avancar_partida(partida) == "quiz"
    assert partida["indice"] == 1
    assert partida["resposta"] is None


def test_fim_da_fase_avanca_para_a_proxima():
    partida = criar_partida()

    for _ in range(5):
        responder_certo(partida)
        proximo = avancar_partida(partida)

    assert proximo == "quiz"
    assert partida["fase"] == 2
    assert partida["indice"] == 0


def test_partida_perfeita_termina_em_vitoria():
    partida = criar_partida()

    for _ in range(15):
        responder_certo(partida)
        proximo = avancar_partida(partida)

    # 15 acertos x 100 + 5 bônus de combo x 50
    assert proximo == "vitoria"
    assert partida["pontos"] == 1750


def test_tres_erros_levam_a_derrota():
    partida = criar_partida()

    for _ in range(3):
        responder_errado(partida)
        proximo = avancar_partida(partida)

    assert partida["vidas"] == 0
    assert proximo == "derrota"