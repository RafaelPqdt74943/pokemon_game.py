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
    
    
eu= Player("rafael")
pokemon_selvagem = pokemon_Fogo("charmander")

print("antes de capturar")
eu.mostrar_pokemons()

eu.capturar(pokemon_selvagem)

eu.mostrar_pokemons()