from src.funcoes import (
    avancar_fase,
    avancar_pergunta,
    calcular_bonus_combo,
    calcular_pontos,
    calcular_pontos_resposta,
    jogador_perdeu,
    jogador_venceu,
    limitar_valor,
    processar_resposta,
    tomar_dano,
    atualizar_combo,
    verificar_resposta,
)


def test_calcular_pontos():
    """Deve somar corretamente os pontos atuais com os pontos ganhos."""
    assert calcular_pontos(10, 5) == 15


def test_jogador_perdeu_com_zero_vidas():
    """Deve indicar derrota quando o total de vidas chega a zero."""
    assert jogador_perdeu(0) is True


def test_jogador_nao_perdeu_com_vidas():
    """Nao deve indicar derrota quando o jogador ainda tem vidas."""
    assert jogador_perdeu(3) is False


def test_limitar_valor_abaixo_do_minimo():
    """Deve retornar o limite minimo quando o valor informado for menor."""
    assert limitar_valor(-5, 0, 100) == 0


def test_limitar_valor_acima_do_maximo():
    """Deve retornar o limite maximo quando o valor informado for maior."""
    assert limitar_valor(150, 0, 100) == 100


def test_limitar_valor_dentro_do_intervalo():
    """Deve manter o valor original quando ele ja estiver no intervalo."""
    assert limitar_valor(50, 0, 100) == 50


def test_verificar_resposta_correta():
    assert verificar_resposta(2, 2) is True


def test_verificar_resposta_incorreta():
    assert verificar_resposta(1, 3) is False


def test_tomar_dano_nao_deixa_vidas_negativas():
    assert tomar_dano(1, 2) == 0


def test_acertos_aumentam_combo():
    assert atualizar_combo(2, True) == 3


def test_erro_reinicia_combo():
    assert atualizar_combo(3, False) == 0


def test_bonus_apenas_em_tres_acertos_consecutivos():
    assert calcular_bonus_combo(2) == 0
    assert calcular_bonus_combo(3) == 50
    assert calcular_bonus_combo(6) == 50


def test_acerto_adiciona_cem_pontos():
    pontos, combo = calcular_pontos_resposta(100, 0, True)
    assert pontos == 200
    assert combo == 1


def test_terceiro_acerto_adiciona_bonus():
    pontos, combo = calcular_pontos_resposta(200, 2, True)
    assert pontos == 350
    assert combo == 3


def test_processar_resposta_incorreta():
    pontos, vidas, combo, acertou = processar_resposta(100, 3, 2, 1, 2)
    assert pontos == 100
    assert vidas == 2
    assert combo == 0
    assert acertou is False


def test_processar_resposta_correta():
    pontos, vidas, combo, acertou = processar_resposta(100, 3, 2, 2, 2)
    assert pontos == 250
    assert vidas == 3
    assert combo == 3
    assert acertou is True


def test_jogador_venceu_ao_concluir_todas_as_fases():
    assert jogador_venceu(3, 3, 1) is True


def test_jogador_nao_vence_sem_vidas():
    assert jogador_venceu(3, 3, 0) is False


def test_avancar_pergunta():
    assert avancar_pergunta(4) == 5


def test_avancar_fase():
    assert avancar_fase(1, 3) == 2
    assert avancar_fase(3, 3) == 3