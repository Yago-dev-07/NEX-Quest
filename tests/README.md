# Testes automatizados — NEX Quest

Esta pasta contém os testes automatizados do projeto **NEX Quest**, desenvolvidos com o framework Pytest.

Os testes verificam diferentes funcionalidades do jogo, ajudando a identificar erros e garantir que as regras sejam executadas corretamente.

## Arquivos de testes

- `test_dados.py`: verifica o salvamento, o carregamento e a atualização do recorde.
- `test_jogo.py`: verifica o gerenciamento da partida, a progressão das fases e as condições de vitória e derrota.
- `test_logica.py`: verifica as regras de pontuação, vidas, combos e outras funções da lógica.
- `test_nex.py`: verifica funcionalidades relacionadas ao personagem NEX.
- `test_perguntas.py`: verifica o carregamento, a organização e a estrutura das perguntas.

## Como executar os testes

Abra o terminal na pasta principal do projeto e execute:

```bash
python -m pytest -v
```

Para executar somente os testes desta pasta:

```bash
python -m pytest tests/ -v
```

Para executar um arquivo específico, por exemplo:

```bash
python -m pytest tests/test_dados.py -v
```

## Estratégia de testes

Os testes automatizados são utilizados para verificar o comportamento das funções e dos módulos do jogo.

Além deles, também são realizados testes manuais para conferir:

- Navegação entre as telas.
- Seleção das alternativas.
- Exibição das explicações.
- Atualização da pontuação e das vidas.
- Funcionamento dos bônus por acertos consecutivos.
- Transição entre as três fases.
- Telas de vitória e derrota.
- Reinício da partida.
- Persistência do recorde.

## Observação

Os testes devem ser executados após alterações importantes no código, especialmente quando houver modificações na lógica, na interface ou na integração dos módulos.
