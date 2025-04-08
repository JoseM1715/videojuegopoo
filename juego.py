import random
import time


class Personaje:
     def __init__(self, nombre: str, vida: int):
         self.nombre: str = nombre
         self.vida: int = vida

     def recibir_dano(self, cantidad: int):
         self.vida -= cantidad
         print(f"{self.nombre} recibe {cantidad} de daño. Vida restante: {self.vida}")


     def esta_vivo(self):
        return self.vida > 0


class Jugador(Personaje):
     def __init__(self, nombre):
         super().__init__(nombre, vida=10)
         self.puntos = 0
         self.arma = Arma("Espada", "Corto")
         self.energia = 0


     def atacar(self, enemigo):
         print(f"Atacas a { enemigo.nombre} con {self.arma.nombre}")
         enemigo.recibir_dano(self.arma.dano)
         self.energia += 1
         if self.energia >= 5:
             print("Habilidad especial disponible")

     def habilidad_especial(self, enemigos):
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
    enemigos = [Enemigo("Goomba", 5), Enemigo("Koopa", 6, agresivo= True)]
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
        elif accion == "especial":
            jugador.habilidad_especial(enemigos)
        elif accion == "recoger":
            if recompensas:
                jugador.recoger_recompensa(recompensas.pop(0))
            else:
                print("No hay recompensas disponibles.")
        elif accion == "salir":
            print("Has salido del juego.")
            break
        else:
            print("Acción no válida.")

        if enemigo.esta_vivo():
            enemigo.atacar(jugador)

        nivel += 1
        time.sleep(1)

    if jugador.esta_vivo():
        print("\nHas ganado. Puntuación: ", jugador.puntos)
    else:
        print("\nHas perdido. Fin del juego.")


juego()





