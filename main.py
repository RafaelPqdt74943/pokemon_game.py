from pokemon import *
from pessoa import *

def escolher_pokemon_inicial (player):
    print(" Olá {} você poderá esolher agora o pokemon que irá lhe acompanhar nessa jornada!!!".format(player))
    
    Pikachu = pokemon_Eletrico("Pikachu", level=1)
    Charmander = pokemon_Fogo("Charmander", level=1)
    Squirtle = pokemon_Agua("Squirtle", level=1)
    
    print("Você possui 3 escolhas ")
    print ( "1-", Pikachu)
    print ( "2-", Charmander)
    print ( "3-", Squirtle)
    
    while True :
        Escolha = input("Escolha o seu Pokemon : ")
        
        if Escolha == "1" : 
            player.capturar(Pikachu)
            break
        elif Escolha == "2":
            player.capturar(Charmander)
            break
        elif Escolha == "3":
            player.capturar(Squirtle)
            break
        else:
            print("Escolha invalida!!")
            
player = Player("Rafael")
player.mostra_dinheiro()
player.capturar(pokemon_Fogo("Charmander", level=1))

#inimigo1= inimigo("gary", pokemons=[pokemon_Agua("Squirtle", level=1)])

#player.batalhar(inimigo1)

player.explorar()

player.mostrar_pokemons()
