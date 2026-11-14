NEX Quest — A Missão da Inteligência Artificial

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

Integrantes do grupo

- Yago Teixeira Almeida Nascimento
- Heitor Dornelas Anacleto
- Cauã Guilherme
- Miguel Hayser Gonçalves do Sacramento

Estrutura do projeto

- "main.py": ponto de entrada da aplicação.
- "src/": código-fonte principal do jogo (loop, regras, sprites e dados).
- "assets/": imagens, fontes e sons.
- "data/": arquivos persistentes (recorde/ranking).
- "tests/": testes unitários com "pytest".
- "docs/": documentação do projeto, incluindo proposta inicial.

Descrição do jogo

NEX Quest é um quiz educativo com elementos de aventura, desenvolvido em Python com Pygame.

O jogador deverá ajudar NEX, um pequeno robô que perdeu parte de suas memórias após uma falha no sistema, a recuperar seus conhecimentos respondendo a perguntas sobre Inteligência Artificial.

O jogo aborda aplicações da IA no cotidiano e seu uso responsável, incluindo confiabilidade das informações, privacidade e verificação de conteúdos.

Objetivo do jogador

Recuperar as memórias de NEX, respondendo corretamente às perguntas e concluindo as três fases do jogo sem perder todas as vidas.

Regras do jogo

- O jogador começa com três vidas.
- Cada pergunta apresenta quatro alternativas, sendo apenas uma correta.
- Respostas corretas aumentam a pontuação e permitem avançar.
- Respostas erradas retiram uma vida.
- Acertos consecutivos geram um bônus de pontuação.
- Após cada resposta, o jogo apresenta uma explicação educativa.

Controles

- Mouse: selecionar alternativas e interagir com os botões.
- Botões da interface: iniciar, continuar e jogar novamente.

Como executar o projeto

git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
pip install -r requirements.txt
python main.py

Como executar os testes

python -m pytest

Checklist mínimo para entrega

- [x] Preencher este README com nome, descrição, regras e controles do jogo.
- [x] Atualizar "docs/proposta.md" com a proposta do grupo.
- [ ] Garantir que o jogo executa com "python main.py".
- [ ] Garantir que os testes passam com "pytest".

## Observações para os alunos

- Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
- Comentem partes importantes da lógica, principalmente regras do jogo.
- Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.
