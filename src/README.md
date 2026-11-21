# Código-fonte — NEX Quest

Esta pasta contém os módulos Python responsáveis pelo funcionamento do jogo **NEX Quest — A Missão da Inteligência Artificial**.

## Organização dos arquivos

- `__init__.py`: identifica a pasta `src` como um pacote Python.
- `botoes.py`: contém funções para desenhar botões e identificar cliques.
- `config.py`: armazena constantes e configurações do jogo.
- `dados.py`: realiza a leitura, gravação e atualização do recorde.
- `funcoes.py`: implementa as regras de pontuação, vidas e combos.
- `interface.py`: contém componentes visuais utilizados na interface do quiz.
- `jogo.py`: gerencia o fluxo principal da partida, os estados do jogo e a integração dos módulos.
- `perguntas.py`: carrega e organiza as perguntas de cada fase.
- `quiz.py`: controla a apresentação das perguntas, as alternativas e a interação com o jogador.
- `sprites.py`: contém funcionalidades relacionadas ao personagem NEX.
- `telas.py`: implementa as telas principais, como menu, instruções, vitória e derrota.

## Organização modular

O código foi dividido em módulos para facilitar o desenvolvimento, a manutenção e a integração das funcionalidades.

Cada arquivo possui uma responsabilidade específica, permitindo que diferentes integrantes trabalhem no projeto de maneira organizada.

## Execução

Para iniciar o jogo, abra o terminal na pasta principal do projeto e execute:

```bash
python main.py
```

O arquivo `main.py` é responsável por iniciar a aplicação, utilizando os módulos presentes nesta pasta.

## Testes

Os testes automatizados estão disponíveis na pasta `tests/`.

Para executá-los:

```bash
python -m pytest -v
```

