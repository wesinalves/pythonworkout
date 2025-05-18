import random
import time

class Gladiador:
 def __init__(self, nome, vida, ataque):
    self.nome = nome
    self.vida = vida
    self.ataque = ataque

 def atacar(self, outro_gladiador):
    dano = random.randint(0, self.ataque)
    outro_gladiador.vida -= dano
    print(f"{self.nome} atacou {outro_gladiador.nome} com {dano} de dano.")

class Arena:
 def __init__(self):
     self.gladiadores = []

 def adicionar_gladiador(self, gladiador):
    self.gladiadores.append(gladiador)

 def iniciar_batalha(self):
    while len(self.gladiadores) > 1:
        gladiador1 = random.choice(self.gladiadores)
        gladiador2 = random.choice(self.gladiadores)
        while gladiador1 == gladiador2:
            gladiador2 = random.choice(self.gladiadores)
        gladiador1.atacar(gladiador2)
        if gladiador2.vida <= 0:
            self.gladiadores.remove(gladiador2)
            print(f"{gladiador2.nome} morreu.")
            time.sleep(1)
            print(f"Vencedor: {gladiador1.nome}")

# Exemplo de uso
arena = Arena()
arena.adicionar_gladiador(Gladiador("Gladiador 1", 100, 20))
arena.adicionar_gladiador(Gladiador("Gladiador 2", 120, 15))
arena.iniciar_batalha()