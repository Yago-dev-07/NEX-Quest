
# Planejamento do Projeto — NEX Quest

## 1. Identificação do projeto

**Nome:** NEX Quest — A Missão da Inteligência Artificial  
**Disciplina:** Introdução a Algoritmos  
**Linguagem:** Python  
**Biblioteca gráfica:** Pygame  
**Tipo de projeto:** Jogo educativo de perguntas e respostas

### Integrantes

- Yago Teixeira Almeida Nascimento
- Heitor Dornelas Anacleto
- Cauã Guilherme
- Miguel Hayser Gonçalves do Sacramento
- Pedro Teodoro Goulart Santana

## 2. Objetivo do projeto

Desenvolver um jogo educativo e interativo que apresente conceitos, aplicações e cuidados relacionados à Inteligência Artificial.

O jogador acompanha NEX, um pequeno robô que perdeu parte de suas memórias após uma falha no sistema. Para ajudá-lo a recuperar seus conhecimentos, deverá responder a perguntas de múltipla escolha e superar três fases.

Além de proporcionar uma experiência divertida, o jogo busca incentivar o aprendizado sobre a Inteligência Artificial e seu uso responsável.

## 3. Escopo e funcionalidades planejadas

O jogo deverá apresentar:

- Tela inicial com opções para jogar, consultar instruções e sair.
- Personagem NEX, que acompanha a jornada do jogador.
- Três fases, com cinco perguntas em cada uma.
- Quatro alternativas por pergunta, sendo apenas uma correta.
- Sistema de três vidas.
- Pontuação por respostas corretas.
- Bônus por acertos consecutivos.
- Explicações educativas após cada resposta.
- Transição automática entre as fases.
- Telas de vitória e derrota.
- Possibilidade de reiniciar a partida.
- Armazenamento do recorde de pontuação.

O desenvolvimento será realizado com Python e Pygame, utilizando o template disponibilizado pela disciplina.

## 4. Regras do jogo

1. O jogador inicia a partida com três vidas e zero pontos.
2. O jogo possui 15 perguntas, distribuídas igualmente entre três fases.
3. Cada resposta correta acrescenta 100 pontos.
4. Cada resposta incorreta retira uma vida.
5. A cada três acertos consecutivos, o jogador recebe um bônus de 50 pontos.
6. Uma resposta incorreta reinicia a sequência de acertos.
7. Após responder, o jogador recebe um feedback e uma explicação.
8. Ao concluir cinco perguntas, avança para a próxima fase.
9. O jogador vence ao concluir as três fases com pelo menos uma vida.
10. O jogador perde ao ficar sem vidas.

A pontuação máxima prevista é de **1.750 pontos**, considerando 15 respostas corretas e cinco bônus de 50 pontos.

## 5. Organização das fases

### Fase 1 — O Despertar de NEX

Apresentação de conceitos básicos de Inteligência Artificial, permitindo que o jogador conheça o tema e inicie a recuperação das memórias do personagem.

### Fase 2 — Explorando o Mundo

Perguntas relacionadas às aplicações da Inteligência Artificial no cotidiano, demonstrando situações em que essa tecnologia está presente.

### Fase 3 — A Última Memória

Perguntas sobre o uso responsável da Inteligência Artificial, abordando cuidados como privacidade, confiabilidade das informações e verificação de conteúdos.

## 6. Divisão das responsabilidades

| Integrante | Responsabilidades |
|---|---|
| Yago Teixeira Almeida Nascimento | Desenvolvimento das telas inicial, instruções, vitória e derrota, além da navegação e dos botões. |
| Heitor Dornelas Anacleto | Elaboração e organização das perguntas, alternativas, respostas corretas e explicações. |
| Cauã Guilherme | Desenvolvimento das regras de pontuação, vidas, combo e progressão das perguntas e fases. |
| Miguel Hayser Gonçalves do Sacramento | Desenvolvimento da interface visual do quiz, incluindo alternativas, indicadores, feedback e interação. |
| Pedro Teodoro Goulart Santana | Desenvolvimento e integração do personagem NEX, gerenciamento do fluxo principal do jogo, conexão entre os módulos, controle dos estados da partida e apoio à implementação do sistema de recorde. |

A integração dos módulos foi realizada principalmente por Pedro Teodoro, responsável por conectar as funcionalidades desenvolvidas pelos demais integrantes. Os testes, as correções e a documentação foram realizados de forma colaborativa, buscando garantir o funcionamento completo do jogo.

## 7. Etapas de desenvolvimento

### Etapa 1 — Estrutura inicial

- Organizar as pastas e os arquivos do template.
- Configurar o ambiente Python.
- Instalar as dependências.
- Definir as constantes e cores do jogo.

### Etapa 2 — Telas e navegação

- Criar a tela inicial.
- Implementar a tela de instruções.
- Desenvolver as telas de vitória e derrota.
- Criar botões e tratar os eventos do mouse.

### Etapa 3 — Perguntas e regras

- Elaborar as 15 perguntas.
- Organizar as perguntas por fase.
- Implementar pontuação, vidas e combo.
- Desenvolver a lógica de avanço e encerramento da partida.

### Etapa 4 — Interface e personagem

- Desenvolver a interface do quiz.
- Exibir perguntas, alternativas e explicações.
- Implementar os indicadores de progresso.
- Desenvolver o personagem NEX e suas interações.
- Integrar o personagem à experiência do jogador.

### Etapa 5 — Integração

- Desenvolver o gerenciamento principal da partida.
- Conectar as telas, as perguntas e a lógica.
- Integrar a interface do quiz ao jogo principal.
- Integrar o personagem NEX às funcionalidades.
- Implementar o controle dos estados do jogo.
- Verificar a comunicação entre os módulos.
- Implementar o armazenamento do recorde.

### Etapa 6 — Testes e documentação

- Executar testes automatizados com Pytest.
- Testar manualmente as funcionalidades.
- Corrigir problemas encontrados.
- Organizar o repositório.
- Atualizar o README e a documentação.

## 8. Organização dos arquivos

- `main.py`: inicialização do jogo.
- `src/config.py`: configurações e constantes.
- `src/botoes.py`: criação e interação dos botões.
- `src/telas.py`: telas principais e navegação.
- `src/perguntas.py`: carregamento e organização das perguntas.
- `src/funcoes.py`: regras e funções da lógica.
- `src/jogo.py`: gerenciamento da partida e integração dos módulos.
- `src/interface.py`: componentes visuais da interface.
- `src/quiz.py`: interface e interação do quiz.
- `src/sprites.py`: representação e comportamento do personagem NEX.
- `src/dados.py`: leitura e gravação do recorde.
- `data/`: armazenamento das perguntas e dos dados persistentes.
- `assets/`: recursos visuais utilizados pelo jogo.
- `tests/`: testes automatizados.
- `docs/`: proposta e planejamento do projeto.

## 9. Estratégia de testes

Os testes serão realizados em duas modalidades.

**Testes automatizados:** utilização do Pytest para verificar as funções relacionadas às perguntas, à pontuação, às vidas, à progressão das fases, ao personagem e à persistência do recorde.

**Testes manuais:** execução do jogo para verificar a navegação, a seleção das alternativas, a exibição das explicações, os indicadores visuais, a transição entre as fases, as telas finais e o reinício da partida.

Também serão testadas situações específicas, como três respostas incorretas, três acertos consecutivos, conclusão das 15 perguntas e manutenção do recorde após fechar o jogo.

## 10. Controle de versões

O projeto utilizará Git e GitHub para organizar o desenvolvimento.

As alterações serão realizadas em branches específicas, sempre que necessário, e registradas em commits relacionados às funcionalidades implementadas.

Antes da integração à branch principal, os módulos deverão ser testados para reduzir problemas de compatibilidade.

## 11. Critérios de conclusão

O projeto será considerado pronto para entrega quando:

- O jogo iniciar corretamente pelo arquivo `main.py`.
- Todas as telas e os botões funcionarem.
- As 15 perguntas estiverem disponíveis.
- Pontuação, vidas e bônus funcionarem conforme as regras.
- As três fases puderem ser concluídas.
- Vitória, derrota e reinício funcionarem.
- O personagem NEX estiver integrado ao jogo.
- O recorde puder ser armazenado e recuperado.
- Os testes automatizados e manuais forem concluídos.
- O README e os documentos estiverem atualizados.

## 12. Considerações finais

O desenvolvimento do NEX Quest busca aplicar os conhecimentos adquiridos na disciplina de Introdução a Algoritmos, especialmente variáveis, condicionais, laços, listas, dicionários, funções, arquivos e organização modular.

Além da implementação do jogo, o projeto proporciona uma experiência de desenvolvimento em equipe, integração de códigos, controle de versões e testes de software.

A divisão das responsabilidades entre os cinco integrantes permite organizar melhor o trabalho, enquanto a integração das funcionalidades contribui para a construção de uma aplicação completa e funcional.
