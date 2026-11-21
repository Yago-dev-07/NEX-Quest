from src.dados import (
    salvar_recorde,
    carregar_recorde,
    atualizar_recorde
)


def test_salvar_recorde(tmp_path):
    """Verifica se o recorde é salvo corretamente."""

    caminho = tmp_path / "recorde.txt"

    salvar_recorde(caminho, 500)

    assert carregar_recorde(caminho) == 500


def test_carregar_recorde_inexistente(tmp_path):
    """Verifica o retorno quando o arquivo não existe."""

    caminho = tmp_path / "recorde.txt"

    assert carregar_recorde(caminho) == 0


def test_atualizar_recorde_maior(tmp_path):
    """Verifica se uma pontuação maior atualiza o recorde."""

    caminho = tmp_path / "recorde.txt"

    salvar_recorde(caminho, 300)

    resultado = atualizar_recorde(caminho, 600)

    assert resultado is True
    assert carregar_recorde(caminho) == 600


def test_atualizar_recorde_menor(tmp_path):
    """Verifica se uma pontuação menor mantém o recorde."""

    caminho = tmp_path / "recorde.txt"

    salvar_recorde(caminho, 800)

    resultado = atualizar_recorde(caminho, 400)

    assert resultado is False
    assert carregar_recorde(caminho) == 800


def test_carregar_recorde_invalido(tmp_path):
    """Verifica o comportamento com conteúdo inválido."""

    caminho = tmp_path / "recorde.txt"

    caminho.write_text("pontuacao invalida", encoding="utf-8")

    assert carregar_recorde(caminho) == 0