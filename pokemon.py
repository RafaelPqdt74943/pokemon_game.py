import random

class Pokemon :
    def __init__(self, especie, level = None, nome=None):
        self.especie = especie

        if level:
            self.level = level
        else:
            self.level = random.randint(1,100) 
        
        if nome: 
            self.nome = nome
        else : 
            self.nome = especie
        self.ataque = self.level * 5
        self.vida = self.level * 10
        
    def __str__ (self):
        return "{} ({})".format(self.nome, self.level)
    
    def atacar(self,pokemon):
        pokemon.vida = pokemon.vida - self.ataque
        print("{} perdeu {} pontos de vida".format( pokemon,self.ataque))
        
        if pokemon.vida <= 0 :
            print("{} foi derrotado".format(pokemon))
            return True
        else : 
            return False

class pokemon_Eletrico(Pokemon):
    tipo = "eletrico"
    
    
    def atacar(self, pokemon):
        print("{} lançou um raio do trovão em {}".format(self, pokemon))
        return super().atacar(pokemon)
        
class pokemon_Fogo(Pokemon):
    tipo = "fogo"
    
    
    def atacar(self, pokemon):      
        print("{} lançou uma bola de fogo na cabeça de {}".format(self, pokemon))
        return super().atacar(pokemon)
        

class pokemon_Agua(Pokemon):
    tipo = "agua"
    
    
    def atacar(self, pokemon):        
        print("{} lançou umjato de d'águas em {}".format(self, pokemon))
        return super().atacar(pokemon)
        
        
        

