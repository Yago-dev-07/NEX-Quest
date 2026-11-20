from src import perguntas


def test_carregar_perguntas():
    """Verifica se as perguntas são carregadas."""
    resultado = perguntas.carregar_perguntas()

    assert len(resultado) == 15


def test_quantidade_por_fase():
    """Verifica se cada fase possui cinco perguntas."""
    for fase in range(1, 4):
        resultado = perguntas.obter_perguntas_fase(fase)
        assert len(resultado) == 5


def test_alternativas_e_resposta_correta():
    """Verifica as alternativas e a posição da resposta correta."""
    todas = perguntas.carregar_perguntas()

    for pergunta in todas:
        assert len(pergunta["alternativas"]) == 4
        assert 0 <= pergunta["correta"] < 4


def test_explicacoes():
    """Verifica se todas as perguntas possuem explicação."""
    todas = perguntas.carregar_perguntas()

    for pergunta in todas:
        assert pergunta["explicacao"] != ""


def test_embaralhar_perguntas():
    """Verifica se o embaralhamento não altera a lista original."""
    originais = perguntas.carregar_perguntas()
    resultado = perguntas.embaralhar_perguntas(originais)

    assert len(resultado) == len(originais)
    assert resultado is not originais
    assert originais == perguntas.carregar_perguntas()