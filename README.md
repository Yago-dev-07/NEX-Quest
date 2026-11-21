# NEX Quest — A Missão da Inteligência Artificial

Projeto final da disciplina de **Introdução a Algoritmos**, desenvolvido em Python com a biblioteca Pygame.

## Sobre o jogo

NEX Quest é um jogo educativo de perguntas e respostas sobre Inteligência Artificial e seu uso responsável.

Na história, NEX é um pequeno robô que perdeu parte de suas memórias após uma falha no sistema. O jogador deverá ajudá-lo a recuperar seus conhecimentos, respondendo a perguntas e superando três fases.

O jogo apresenta conceitos básicos de IA, aplicações dessa tecnologia no cotidiano e cuidados relacionados à privacidade, à confiabilidade das informações e ao uso responsável.

## Integrantes

- Yago Teixeira Almeida Nascimento
- Heitor Dornelas Anacleto
- Cauã Guilherme
- Miguel Hayser Gonçalves do Sacramento
- Pedro Teodoro Goulart Santana

## Objetivo

Responder às 15 perguntas e concluir as três fases sem perder todas as vidas, ajudando NEX a recuperar suas memórias.

## Regras

- O jogador começa com três vidas.
- Existem três fases, cada uma com cinco perguntas.
- Cada pergunta possui quatro alternativas e uma única resposta correta.
- Cada acerto vale 100 pontos.
- A cada três acertos consecutivos, o jogador recebe 50 pontos extras.
- Cada erro retira uma vida e reinicia o combo.
- Após responder, uma explicação educativa é apresentada.
- O jogador vence ao concluir as três fases com vidas restantes.
- A partida termina em derrota quando todas as vidas são perdidas.
- O jogo armazena o recorde de pontuação.

A pontuação máxima possível é de **1.750 pontos**.

## Fases

### Fase 1 — O Despertar de NEX

Apresenta conceitos básicos de Inteligência Artificial, introduzindo o jogador ao tema.

### Fase 2 — Explorando o Mundo

Aborda aplicações da Inteligência Artificial no cotidiano, mostrando como essa tecnologia está presente em diferentes situações.

### Fase 3 — A Última Memória

Explora questões relacionadas à ética, à privacidade, à confiabilidade e ao uso responsável da Inteligência Artificial.

## Controles

O jogo utiliza o mouse para selecionar alternativas e interagir com os botões das telas.

## Tecnologias utilizadas

- Python
- Pygame
- Pytest
- Git e GitHub

## Requisitos

- Python instalado no computador.
- Dependências listadas no arquivo `requirements.txt`.

## Como instalar e executar

### 1. Obter o projeto

Clone o repositório pelo GitHub ou baixe o código em formato ZIP.

Depois, abra um terminal na pasta principal do projeto, onde estão os arquivos `main.py` e `requirements.txt`.

### 2. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 3. Executar o jogo

```bash
python main.py
```

## Como executar os testes

Na pasta principal do projeto, execute:

```bash
python -m pytest -v
```

Esse comando executa os testes automatizados disponíveis na pasta `tests/`.

## Estrutura do projeto

```text
NEX-Quest/
├── main.py
├── requirements.txt
├── README.md
├── assets/
│   └── imagens/
│       └── spritesheet.bmp
├── data/
│   ├── perguntas.json
│   └── recorde.txt
├── docs/
│   ├── proposta.MD
│   └── planejamento.md
├── src/
│   ├── __init__.py
│   ├── botoes.py
│   ├── config.py
│   ├── dados.py
│   ├── funcoes.py
│   ├── interface.py
│   ├── jogo.py
│   ├── perguntas.py
│   ├── quiz.py
│   ├── sprites.py
│   └── telas.py
└── tests/
    ├── test_dados.py
    ├── test_jogo.py
    ├── test_logica.py
    ├── test_nex.py
    └── test_perguntas.py
```

A estrutura representa os principais arquivos do projeto. Outros arquivos auxiliares podem estar presentes no repositório.

## Organização do desenvolvimento

O desenvolvimento do NEX Quest foi organizado de forma modular, permitindo que os cinco integrantes da equipe trabalhassem em diferentes funcionalidades do jogo.

**Yago Teixeira Almeida Nascimento** ficou responsável pelo desenvolvimento das telas principais, incluindo a tela inicial, as instruções, a vitória e a derrota, além dos botões e da navegação.

**Heitor Dornelas Anacleto** trabalhou na elaboração e organização das perguntas, alternativas, respostas corretas e explicações educativas, distribuindo o conteúdo entre as três fases.

**Cauã Guilherme** desenvolveu as regras relacionadas à pontuação, às vidas, aos combos e à progressão das perguntas e fases, contribuindo para o funcionamento da lógica principal do jogo.

**Miguel Hayser Gonçalves do Sacramento** ficou responsável pela interface visual do quiz, incluindo a apresentação das perguntas, das alternativas, dos indicadores de pontuação e vidas, dos feedbacks e das interações com o jogador.

**Pedro Teodoro Goulart Santana** atuou principalmente no desenvolvimento e na integração do personagem NEX, no gerenciamento do fluxo principal do jogo e na conexão dos módulos desenvolvidos pelos demais integrantes. Também contribuiu para o controle dos estados da partida e para a implementação do sistema de recorde.

Após o desenvolvimento individual das funcionalidades, a equipe realizou a integração, os testes e os ajustes necessários para garantir o funcionamento do jogo.

O controle de versões foi realizado com Git e GitHub, utilizando branches e commits para organizar as alterações.

## Documentação

Informações adicionais estão disponíveis nos arquivos:

- `docs/proposta.MD`: proposta inicial do jogo.
- `docs/planejamento.md`: funcionalidades, responsabilidades, etapas e estratégia de testes.

## Considerações finais

O NEX Quest foi desenvolvido para aplicar conhecimentos de programação e proporcionar uma experiência educativa sobre Inteligência Artificial.

O projeto também envolveu organização de código, trabalho em equipe, integração de funcionalidades, controle de versões e testes para verificar o funcionamento do jogo.

A colaboração entre os cinco integrantes foi fundamental para conectar os diferentes módulos e desenvolver uma aplicação educativa e interativa.
