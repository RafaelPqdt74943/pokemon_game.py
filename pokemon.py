class Pokemon :
    def __init__(self, tipo, especie, level = 1, nome=None):
        self.tipo =tipo
        self.especie = especie
        self.level = level
        
        if nome: 
            self.nome = nome
        else : 
            self.nome = especie
        
    def __str__ (self):
        return "{} ({})".format(self.nome, self.level)
    
    def atacar(self,pokemon):
        print("{} atacou {}".format(self, pokemon))
        
        

        

meu_pokemon = Pokemon("fogo", "charmander", nome="tunico")

pokemon_meu_amigo = Pokemon("eletrico", "pikachu")

meu_pokemon.atacar(pokemon_meu_amigo)

pokemon_meu_amigo.atacar(meu_pokemon)

#print(meu_pokemon)
#print(pokemon_meu_amigo)

print(meu_pokemon)
print(pokemon_meu_amigo)

