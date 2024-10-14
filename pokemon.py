class Pokemon :
    def __init__(self, tipo, especie):
        self.tipo =tipo
        self.especie = especie
        
    def __str__ (self):
        return "{} ({})".format(self.especie, self.tipo)
    
    def atacar(self,pokemon):
        print("{} atacou {}".format(self, pokemon))
        
        

        

meu_pokemon = Pokemon("fogo", "charmander")

pokemon_meu_amigo = Pokemon("eletrico", "pikachu")

meu_pokemon.atacar(pokemon_meu_amigo)

pokemon_meu_amigo.atacar(meu_pokemon)

#print(meu_pokemon)
#print(pokemon_meu_amigo)