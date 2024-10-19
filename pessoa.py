from pokemon import *

class pessoa:
    def __init__ (self,nome = None, pokemons=[]):
        if nome :
            self.nome= nome
        else : 
            nome = "Anonimo"
            
        self.pokemons = pokemons
        
    def __str__ (self):
        return self.nome
    
    def mostrar_pokemons (self):
        for pokemon in self.pokemons:
            print(pokemon)
            
            
class Player (pessoa):
    tipo = "Player"
    
class inimigo (pessoa):
    tipo = "Inimigo"
    
    
meu_pokemon = pokemon_Eletrico("pikachu")
meu_pokemon2 = pokemon_Fogo("charmander")

eu = Player(nome ="rafael", pokemons=[meu_pokemon,meu_pokemon2])

print(eu)
eu.mostrar_pokemons()