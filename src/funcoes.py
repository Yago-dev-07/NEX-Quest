def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos à pontuação atual."""
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    """Reduz a vida atual com base no dano recebido."""
    return max(0, vida_atual - dano)


def jogador_perdeu(vidas):
    """Indica se o jogador ficou sem vidas."""
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro do intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_colisao(retangulo_1, retangulo_2):
    """Verifica sobreposição entre dois retângulos do Pygame."""
    return retangulo_1.colliderect(retangulo_2)


def verificar_resposta(resposta_escolhida, resposta_correta):
    """Retorna True somente quando as respostas forem iguais."""
    return resposta_escolhida == resposta_correta


def atualizar_combo(combo_atual, acertou):
    """Mantém o combo após acertos ou reinicia após um erro."""
    if acertou:
        return combo_atual + 1
    return 0


def calcular_bonus_combo(combo_atual):
    """Concede 50 pontos a cada sequência de três acertos."""
    if combo_atual > 0 and combo_atual % 3 == 0:
        return 50
    return 0


def calcular_pontos_resposta(pontos_atual, combo_atual, acertou):
    """Calcula pontos e o novo combo após uma resposta."""
    novo_combo = atualizar_combo(combo_atual, acertou)

    if not acertou:
        return pontos_atual, novo_combo

    pontos_ganhos = 100
    pontos_ganhos += calcular_bonus_combo(novo_combo)
    return calcular_pontos(pontos_atual, pontos_ganhos), novo_combo


def processar_resposta(pontos, vidas, combo, resposta_escolhida, resposta_correta):
    """Atualiza pontuação, vidas e combo de uma resposta."""
    acertou = verificar_resposta(resposta_escolhida, resposta_correta)
    novos_pontos, novo_combo = calcular_pontos_resposta(pontos, combo, acertou)

    if acertou:
        novas_vidas = vidas
    else:
        novas_vidas = tomar_dano(vidas, 1)

    return novos_pontos, novas_vidas, novo_combo, acertou


def jogador_venceu(fase_atual, total_fases=3, vidas=None):
    """Indica se todas as fases foram concluídas e há vidas disponíveis."""
    concluiu_fases = fase_atual >= total_fases
    if vidas is None:
        return concluiu_fases
    return concluiu_fases and vidas > 0


def avancar_pergunta(indice_atual):
    """Avança o índice da pergunta atual."""
    return indice_atual + 1


def avancar_fase(fase_atual, total_fases=3):
    """Avança uma fase sem ultrapassar o total configurado."""
    return limitar_valor(fase_atual + 1, 1, total_fases)