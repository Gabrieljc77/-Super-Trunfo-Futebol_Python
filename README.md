
Super Trunfo de Futebol em Python

Jogo de Super Trunfo desenvolvido em Python, executado diretamente pelo terminal, no qual clubes de futebol são representados por cartas com atributos de Ataque, Meio-campo e Defesa.

O projeto permite partidas em Single Player, contra o computador, e em Multiplayer local, com dois jogadores. A cada rodada, um atributo é escolhido e os valores das cartas são comparados. O vencedor recebe a carta do adversário e, em caso de empate, as cartas ficam acumuladas em um monte de espera até que uma rodada posterior defina quem ficará com elas.

📌 Sobre o projeto

Este projeto foi desenvolvido com o objetivo de praticar conceitos fundamentais da linguagem Python por meio da implementação da lógica de um jogo de cartas.

Durante a execução, o programa:

• cria o baralho com os clubes e seus atributos;
• embaralha as cartas aleatoriamente;
• distribui as cartas entre os jogadores;
• permite selecionar o modo de jogo;
• apresenta a carta do jogador da vez;
• permite escolher o atributo da rodada;
• compara os valores das duas cartas;
• transfere as cartas de acordo com o resultado;
• armazena cartas empatadas em um monte de espera;
• exibe a quantidade de cartas de cada jogador;
• determina o vencedor quando um dos jogadores fica sem cartas.

🎮 Modos de jogo

Single Player

O Jogador 1 é controlado pelo usuário e o Jogador 2 é controlado pelo computador.

Quando chega a vez do computador, o atributo da rodada é escolhido aleatoriamente entre:

1. Ataque
2. Meio-campo
3. Defesa

Multiplayer

Dois jogadores participam localmente utilizando o mesmo terminal.

O jogador que estiver com a vez escolhe o atributo que será utilizado na comparação da rodada.

🃏 Clubes disponíveis

|Clube           |Ataque|Meio-campo|Defesa|
|----------------|-----:|---------:|-----:|
|Flamengo        |80    |77        |77    |
|Palmeiras       |79    |77        |78    |
|Corinthians     |76    |75        |74    |
|São Paulo       |76    |75        |74    |
|Atlético Mineiro|77    |76        |76    |
|Botafogo        |76    |76        |75    |
|Fluminense      |75    |76        |74    |
|Grêmio          |75    |74        |74    |

⚙️ Como funciona

No início de cada partida, o programa utiliza random.shuffle() para embaralhar o baralho e distribui as cartas alternadamente entre os dois jogadores.

Em cada rodada:

1. O programa mostra a quantidade de cartas de cada jogador.
2. É informado qual jogador possui a vez.
3. O jogador escolhe um atributo da sua carta.
4. Os valores desse atributo nas duas cartas são comparados.
5. O jogador com o maior valor vence a rodada.
6. A carta do adversário é adicionada à mão do vencedor.
7. O vencedor da rodada passa a escolher o atributo da próxima rodada.

Empates

Quando os dois clubes possuem o mesmo valor no atributo escolhido, as duas cartas são retiradas temporariamente das mãos e colocadas em um monte de espera.

Na próxima rodada que possuir um vencedor, todas as cartas acumuladas nesse monte são entregues ao vencedor juntamente com a carta conquistada naquela rodada.

🛠️ Tecnologias utilizadas

• Python 3 — linguagem utilizada no desenvolvimento do projeto.
• random — módulo da biblioteca padrão do Python utilizado para embaralhar as cartas e realizar escolhas aleatórias do computador.

> O projeto não necessita de bibliotecas externas ou instalação de dependências adicionais.

🧠 Conceitos de programação aplicados

• Funções
• Listas
• Índices
• Estruturas condicionais
• Estruturas de repetição
• Entrada e saída de dados
• Validação de opções
• Manipulação de listas
• Modularização do código
• Biblioteca padrão do Python
• Lógica de turnos
• Regras de jogo

📂 Estrutura do projeto

```text
Super-Trunfo/
├── Super_Trunfo.py
└── README.md
```

▶️ Como executar

Pré-requisito

Tenha o Python 3 instalado.

Para verificar:

```bash
python --version
```

ou:

```bash
python3 --version
```

Executando

Clone o repositório:

```bash
git clone URL-DO-SEU-REPOSITORIO
```

Entre na pasta:

```bash
cd Super-Trunfo
```

Execute:

```bash
python Super_Trunfo.py
```

ou:

```bash
python3 Super_Trunfo.py
```

🕹️ Menu principal

```text
1 - Single Player
2 - Multiplayer
3 - Sair
```

Durante a partida:

```text
1 - Ataque
2 - Meio-campo
3 - Defesa
```

🧩 Principais funções

|Função               |Responsabilidade                          |
|---------------------|------------------------------------------|
|`criar_gabarito()`   |Define os nomes dos atributos das cartas. |
|`criar_baralho()`    |Cria os clubes e seus valores.            |
|`exibir_topo()`      |Exibe os dados da carta atual.            |
|`valida_escolha()`   |Valida opções entre 1 e 3.                |
|`distribuir_cartas()`|Embaralha e distribui as cartas.          |
|`escolher_atributo()`|Recebe o atributo escolhido.              |
|`comparar_cartas()`  |Compara as cartas e identifica o vencedor.|
|`atualizar_maos()`   |Transfere a carta do perdedor.            |
|`guardar_empate()`   |Guarda cartas empatadas.                  |
|`entregar_monte()`   |Entrega o monte acumulado ao vencedor.    |
|`mostrar_placar()`   |Mostra a quantidade de cartas.            |
|`jogar()`            |Controla a partida.                       |
|`menu()`             |Controla o menu principal.                |

🚀 Possíveis melhorias futuras

• adicionar mais clubes;
• incluir novos atributos;
• criar níveis de dificuldade;
• desenvolver uma interface gráfica;
• adicionar pontuação e histórico de partidas;
• permitir personalização das cartas;
• salvar estatísticas;
• melhorar o tratamento de entradas inválidas;
• adicionar testes automatizados;
• aplicar programação orientada a objetos.

👥 Autores

Projeto desenvolvido por:

• Gabriel Jardim
• Gabriel Alonso
• Nicolas Gabriel

📄 Licença

Este projeto foi desenvolvido para fins de estudo e aprendizado. Caso seja utilizada uma licença específica futuramente, recomenda-se adicionar um arquivo LICENSE ao repositório.
