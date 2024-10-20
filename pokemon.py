class Pokemon :
    def __init__(self, especie, level = 1, nome=None):
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

class pokemon_Eletrico(Pokemon):
    tipo = "eletrico"
    
    
    def atacar(self, pokemon):
        print("{} lançou um raio do trovão em {}".format(self, pokemon))
        
class pokemon_Fogo(Pokemon):
    tipo = "fogo"
    
    
    def atacar(self, pokemon):
        print("{} lançou uma bola de fogo na cabeça de {}".format(self, pokemon))
        

class pokemon_Agua(Pokemon):
    tipo = "agua"
    
    
    def atacar(self, pokemon):
        print("{} lançou umjato de d'águas em {}".format(self, pokemon))
        
        
        

