class Pokemon :
    def __init__(self, tipo, especie):
        self.tipo =tipo
        self.especie = especie
        
    def __str__ (self):
        return "{} ({})".format(self.especie, self.tipo)
        
        

        

meu_pokemon = Pokemon("fogo", "charmander")

pokemon_meu_amigo = Pokemon("eletrico", "pikachu")


print(meu_pokemon)
print(pokemon_meu_amigo)