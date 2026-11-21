import os


def salvar_recorde(caminho_arquivo, pontuacao):
    """Salva a pontuação recorde em arquivo texto."""
    # Garante que a pasta (ex.: data/) exista antes de gravar
    pasta = os.path.dirname(caminho_arquivo)
    if pasta != "":
        os.makedirs(pasta, exist_ok=True)

    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(str(pontuacao))


def carregar_recorde(caminho_arquivo):
    """Carrega o recorde salvo; retorna 0 se não existir valor válido."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()

            if conteudo == "":
                return 0

            return int(conteudo)

    except (FileNotFoundError, ValueError):
        # Arquivo ausente ou com texto que não é número: começa do zero
        return 0


def atualizar_recorde(caminho_arquivo, pontuacao):
    """Salva a pontuação só se ela superar o recorde. Retorna True se superou."""
    if pontuacao > carregar_recorde(caminho_arquivo):
        salvar_recorde(caminho_arquivo, pontuacao)
        return True

    return False