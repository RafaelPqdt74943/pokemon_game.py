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
            



if __name__ == "__main__":
    
    print("_____________________________________")
    print("Bem vindo ao pokemon RPG de terminal")
    nome=input("qual o seu nome? ")
    player = Player(nome)
    print("Ola {} esse é um número habitado por pokemons, a partir de agora sua missão é se tornar um mestre dos pokemons, capture o máximo de pokemonos que conseguir e lute com seus inimigos".format(player))
    player.mostra_dinheiro()
    if player.pokemons :
        print("já vi que você possui alguns pokemons")
        player.mostrar_pokemons()
    else:
        print("você não tem nenhum pokemon, portanto precis escolher um")
        escolher_pokemon_inicial(player)
        
print(" pronto agora que você já possui um pokemon, enfrente seu rival desde da infanâcia")

gary= inimigo("Gary", pokemons=[ pokemon_Agua("Squirtle", level=1)])
player.batalhar(gary)
    
        
while True :
    print("_________________________")
    print(" o que deseja fazer ?")
    print(" 1-explorar pelo mundão a fora ?")
    print(" 2-lutar com inimigo ?")
    print(" 0-sair do jogo ?")
    escolha = int(input("Sua escolha : "))
    
    if escolha == 0 : 
        print("fechando o jogo")
        break 
    elif escolha == 1 :
        player.explorar()
    elif escolha == 2 : 
        inimigo_aleatorio = inimigo()
        player.batalhar(inimigo_aleatorio)
    else:
        print("escolha invalida!!!!")
    
    
    
    
    
