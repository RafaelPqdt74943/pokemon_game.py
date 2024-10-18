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

class pokemon_eletrico(Pokemon):
    def atacar(self, pokemon):
        print("{} lançou um raio do trovão em {}".format(self, pokemon))
    def dar_choque(self, pokemon):
        print("{} Deu choque em {}".format(self, pokemon))
        
        
meu_pokemon = pokemon_eletrico("eletrico", "Pikachu")
pokemon_amigo = Pokemon("fogo", "charmander")

meu_pokemon.dar_choque(pokemon_amigo)
pokemon_amigo.atacar(meu_pokemon)

