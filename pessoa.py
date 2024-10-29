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
    def __init__ (self,nome = None, pokemons=[]):
        if nome :
            self.nome= nome
        else : 
            self.nome = random.choice(NOMES)
            
        self.pokemons = pokemons
        
    def __str__ (self):
        return self.nome
    
    def mostrar_pokemons (self):
        if self.pokemons:
            print("pokemons de {}: ".format(self))   
            for pokemon in self.pokemons:
                print(pokemon)
        else : 
            print("{} não tem nenhum pokemon".format(self))
            
            
class Player (pessoa):
    tipo = "Player"
    
    def capturar (self, pokemon):
        self.pokemons.append(pokemon)
        print("{} capturou um {}!!".format(self,pokemon))
        
    
class inimigo (pessoa):
    tipo = "Inimigo"

    def __init__(self, nome=None, pokemons = []):
       if not pokemons :
           for i in range(random.randint(1,6)):
              pokemons.append(random.choice(POKEMONS))

       super().__init__(nome = nome, pokemons= pokemons)


