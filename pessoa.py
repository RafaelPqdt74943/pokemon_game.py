import random

from pokemon import *


NOMES = ["Rafael","Gary", "Ash", "doctor Who", "SuperMan", "Homen-aranha", "Charlie", "Boris", " Floresvaldo", "Arthur"
         , "Lancelot", "Matheus", "Nemias"]

POKEMONS = [
    pokemon_Fogo("Charmander"),
    pokemon_Fogo("Charmeleon"),
    pokemon_Fogo("Arcanine"), 
    pokemon_Fogo("Flarion"),
    pokemon_Eletrico("Pikachu"),
    pokemon_Eletrico("Raichu"),
    pokemon_Agua("squirtle"),
    pokemon_Agua("magicarp"),
    pokemon_Agua("Gyarados")
]

class pessoa:
    def __init__ (self,nome = None, pokemons=[], dinheiro = 100):
        if nome :
            self.nome= nome
        else : 
            self.nome = random.choice(NOMES)
            
        self.pokemons = pokemons

        self.dinheiro = dinheiro
        
    def __str__ (self):
        return self.nome
    
    def mostrar_pokemons (self):
        if self.pokemons:
            print("pokemons de {}: ".format(self))   
            for index,pokemon in enumerate(self.pokemons):
                print("{} - {}".format(index,pokemon))
        else : 
            print("{} não tem nenhum pokemon".format(self)) 
            
    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print("{} escolheu {}".format(self,pokemon_escolhido))
            return pokemon_escolhido
        else:
            print("ERRO:esse jogador não possui nenhum pokemon para ser escolhido")

    def mostra_dinheiro(self): 
        print("você possui $ {} em sua conta " .format(self.dinheiro))
           
    def ganhar_dinheiro(self, quantidade):
        self.dinheiro += quantidade
        print("você ganhou {} " .format(quantidade))
        self.mostra_dinheiro()

    def batalhar(self, pessoa):
        print("{} iniciou uma batalha com {}".format(self, pessoa))

        pessoa.mostrar_pokemons()
        pokemon_inimigo = pessoa.escolher_pokemon()
    
        pokemon = self.escolher_pokemon()
        
        if pokemon and pokemon_inimigo :
            while True:
                vitoria=pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print("{} ganhou a batalha".format(self))
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)
                    break
                vitoria_inimiga=pokemon_inimigo.atacar(pokemon)
                if vitoria_inimiga : 
                    print("{} ganhou a batalha".format(pessoa))
                    break
        else:
            print("Essa batalha não pode ocorrer")
            
            
class Player (pessoa):
    tipo = "Player"
    
    def capturar (self, pokemon):
        self.pokemons.append(pokemon)
        print("{} capturou um {}!!".format(self,pokemon))
        
    def escolher_pokemon(self):
        self.mostrar_pokemons()

        if self.pokemons:
                
            while True :
                Escolha = input("Escolha o seu Pokemon : ")
                try:
                    Escolha = int(Escolha)
                    pokemon_escolhido = self.pokemons[Escolha] 
                    print("{} eu escolho você!!!!".format(pokemon_escolhido))  
                    return pokemon_escolhido                  
                except:
                    print("escolha invalida")   
        else:
            print("ERRO:esse jogador não possui nenhum pokemon para ser escolhido")

    def explorar (self) : 
        if random.random() <= 0.3 :
            pokemon = random.choice(POKEMONS)
            print("Um pokemon selvagem apareceu {}".format(pokemon))
            escolha= input("deseja capturar o pokemon s/n?")
            if escolha == "s" :
                if random.random() >= 0.5 :
                    self.capturar(pokemon)
                else:
                    print(" {} fugiu, qu pena!!!!!".format(pokemon))
                
            else : 
                print(" Ok, boa viajem")
        else:
            print("essa exploração não deu em nada")
            return None


        
    
class inimigo (pessoa):
    tipo = "Inimigo"

    def __init__(self, nome=None, pokemons = []):
       if not pokemons :
           for i in range(random.randint(1,6)):
              pokemons.append(random.choice(POKEMONS))

       super().__init__(nome = nome, pokemons= pokemons)


       