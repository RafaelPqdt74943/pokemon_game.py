import random  # Importa a biblioteca random para gerar valores aleatórios

from pokemon import *  # Importa todos os elementos do módulo pokemon

# Lista de nomes possíveis para personagens
NOMES = ["Rafael", "Gary", "Ash", "doctor Who", "SuperMan", "Homen-aranha", "Charlie", "Boris", "Floresvaldo", "Arthur", 
         "Lancelot", "Matheus", "Nemias"]

# Lista de instâncias de Pokémon de diferentes tipos
POKEMONS = [
    pokemon_Fogo("Charmander"),
    pokemon_Fogo("Charmeleon"),
    pokemon_Fogo("Arcanine"),
    pokemon_Fogo("Flarion"),
    pokemon_Eletrico("Pikachu"),
    pokemon_Eletrico("Raichu"),
    pokemon_Agua("Squirtle"),
    pokemon_Agua("Magikarp"),
    pokemon_Agua("Gyarados")
]

# Define a classe 'pessoa', que serve como base para personagens no jogo
class pessoa:
    # Inicializa o objeto pessoa com nome, pokémons e dinheiro
    def __init__(self, nome=None, pokemons=[], dinheiro=100):
        # Define o nome da pessoa aleatoriamente, caso não seja passado um nome
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons  # Lista de Pokémons do jogador
        self.dinheiro = dinheiro  # Dinheiro disponível

    # Representação em string da pessoa (retorna o nome)
    def __str__(self):
        return self.nome

    # Mostra todos os pokémons da pessoa
    def mostrar_pokemons(self):
        if self.pokemons:
            print("Pokémons de {}: ".format(self))
            for index, pokemon in enumerate(self.pokemons):
                print("{} - {}".format(index, pokemon))
        else:
            print("{} não tem nenhum Pokémon".format(self))

    # Escolhe um Pokémon aleatório do jogador para batalhar
    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print("{} escolheu {}".format(self, pokemon_escolhido))
            return pokemon_escolhido
        else:
            print("ERRO: Esse jogador não possui nenhum Pokémon para ser escolhido")

    # Mostra o valor de dinheiro disponível
    def mostra_dinheiro(self):
        print("Você possui $ {} em sua conta".format(self.dinheiro))

    # Adiciona uma quantia de dinheiro à conta
    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print("Você ganhou {} ".format(quantidade))
        self.mostra_dinheiro()

    # Função que gerencia uma batalha entre dois personagens
    def batalhar(self, pessoa):
        print("{} iniciou uma batalha com {}".format(self, pessoa))

        pessoa.mostrar_pokemons()  # Mostra os Pokémons do oponente
        pokemon_inimigo = pessoa.escolher_pokemon()  # Escolhe um Pokémon do oponente

        pokemon = self.escolher_pokemon()  # Escolhe um Pokémon do próprio jogador

        # Loop da batalha, continua até um dos Pokémons vencer
        if pokemon and pokemon_inimigo:
            while True:
                vitoria = pokemon.atacar(pokemon_inimigo)  # Tenta um ataque
                if vitoria:
                    print("{} ganhou a batalha".format(self))
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)  # Ganha dinheiro
                    break

                vitoria_inimiga = pokemon_inimigo.atacar(pokemon)  # Oponente tenta um ataque
                if vitoria_inimiga:
                    print("{} ganhou a batalha".format(pessoa))
                    break
        else:
            print("Essa batalha não pode ocorrer")

# Define a classe 'Player', que é um tipo específico de pessoa
class Player(pessoa):
    tipo = "Player"  # Define o tipo de personagem como Player

    # Método para capturar um novo Pokémon
    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print("{} capturou um {}!!".format(self, pokemon))

    # Escolhe um Pokémon baseado na escolha do usuário
    def escolher_pokemon(self):
        self.mostrar_pokemons()

        if self.pokemons:
            while True:
                escolha = input("Escolha o seu Pokémon: ")
                try:
                    escolha = int(escolha)
                    pokemon_escolhido = self.pokemons[escolha]
                    print("{} eu escolho você!!!!".format(pokemon_escolhido))
                    return pokemon_escolhido
                except:
                    print("Escolha inválida")
        else:
            print("ERRO: Esse jogador não possui nenhum Pokémon para ser escolhido")

    # Exploração que possibilita encontrar e capturar um Pokémon
    def explorar(self):
        if random.random() <= 0.3:  # 30% de chance de encontrar um Pokémon
            pokemon = random.choice(POKEMONS)
            print("Um Pokémon selvagem apareceu: {}".format(pokemon))
            escolha = input("Deseja capturar o Pokémon? (s/n): ")
            if escolha == "s":
                if random.random() >= 0.5:  # 50% de chance de capturar o Pokémon
                    self.capturar(pokemon)
                else:
                    print("O {} fugiu, que pena!".format(pokemon))
            else:
                print("Ok, boa viagem")
        else:
            print("Essa exploração não deu em nada")
            return None

# Define a classe 'inimigo', outro tipo específico de pessoa
class inimigo(pessoa):
    tipo = "Inimigo"  # Define o tipo de personagem como Inimigo

    # Inicializa um inimigo com Pokémons aleatórios, caso nenhum seja fornecido
    def __init__(self, nome=None, pokemons=None):
        if not pokemons:
            pokemons_aleatorios = []
            for i in range(random.randint(1, 6)):  # Gera de 1 a 6 Pokémons aleatórios
                pokemons_aleatorios.append(random.choice(POKEMONS))
            super().__init__(nome=nome, pokemons=pokemons_aleatorios)
        else:
            super().__init__(nome=nome, pokemons=pokemons)
