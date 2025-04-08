from abc import  ABC, abstractmethod
import random


class Personaje:
     def __init__(self, nombre: str, vida: int, vivo: bool, velocidad: int):
         self.nombre: str = nombre
         self.vida: int = vida
         self.vivo: bool = True
         self.velocidad: int = velocidad

     def recibir_dano(self, cantidad: int):
             self.vida -= cantidad
             print(f"{self.nombre} recibe {cantidad} de daño. vida restante: {self.vida}")
             if self.vida <= 0:
                 self.vivo = False
                 print(f"{self.nombre} ha sido derrotado.")


class Jugador(Personaje):
     def __init__(self, nombre):
         super().__init__(nombre, vida=100)
         self.puntos = 0
         self.arma = Arma("Espada", "Corto")
         self.energia = 0


     def atacar(self, enemigo):
         print(f"Atacas a { enemigo.nombre} con {self.arma.nombre}")
         enemigo.recibir_dano(self.arma.dano)
         self.energia += 1
         if self.energia >5:
             print("Habilidad especial disponible")

     def habilidad_especial(self,enemigos):
         if self.energia >= 5:
             print("Usas tu HABILIDAD ESPECIAL: ando de choque")
             for enemigo in enemigos:
                 enemigo.recibir_dano(3)
                 self.energia = 0
            else:
                print("Aun no tienes suficiente energia")

     def recoger_recompensa(self, recompensa):
         print(f"Has recogido: {recompensa}")
         if recompensa == "gema":
             self.arma.mejorar()
         elif recompensa == "moneda":
             self.puntos += 10
             print(f"Puntos actuales: {self.puntos}")



class Arma:
    def __init__(self,nombre, tipo: str, dano: int):
        self.nombre = nombre
        self.tipo = tipo # corto o largo alcance
        self.dano = dano

    def mejorar(self):
        self.dano += 2
        print(f"¡Tu arma {self.nombre} ha sido mejorada! Daño: {self.dano}")

class Enemigo(Personaje):
    def __init__(self, nombre, vida, agresivo=False):
        super().__init__(nombre, vida)
        self.agresivo = agresivo

    def atacar(self, jugador):
        dano = 1 if not self.agresivo else 2
        print(f"{self.nombre} ataca con fuerza {dano}!")
        jugador.recibir_dano(dano)



def juego():
    jugador = Jugador("Heroe")
    enemigos = [Enemigo("Gomba", 5), Enemigo("Koopa", 6, agresivo= True)]
    recompensas = ["moneda", "gema"]

    nivel = 1
    while jugador.esta_vivo() and enemigos:
        print(f"\n--- Nivel {nivel} ---")
        enemigo = enemigos[0]
        accion = input("¿Qué quieres hacer (atacar / especial / recoger / salir): ").lower()

        if accion == "atacar":
            jugador.atacar(enemigo)

            if not enemigo.esta_vivo():
                print(f"{enemigo.nombre} ha sido derrotado.")
                enemigos.pop(0)




