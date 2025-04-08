from abc import  ABC, abstractmethod
import random


class Personaje:
     def __init__(self, nombre: str, vida: int, vivo: bool, velocidad: int):
         self.nombre: str = nombre
         self.vida: int = vida
         self.vivo: bool = True
         self.velocidad: int = velocidad

     def recibir_golpe(self, cantidad: int):
             self.vida -= cantidad
             print(f"{self.nombre} recibe {cantidad} de daño. vida restante: {self.vida}")
             if self.vida <= 0:
                 self.vivo = False
                 print(f"{self.nombre} ha sido derrotado.")


class Jugador(Personaje):
     def __init__(self, nombre):
         super.__init__(nombre, vida=100)
         self.puntos = 0
         self.arma = Arma("Espada", "Corto")
         self.energia = 0


     def atacar(self, enemigo):
         print(f"Atacas a { enemigo.nombre} con {self.arma.nombre}")
         enemigo.recibir_golpe(self.arma.golpe)
         self.energia += 1
         if self.energia >5:
             print("Habilidad especial disponible")

     def habilidad_especial(self,enemigos):
         if self.energia >= 5:
             print("Usas tu HABILIDAD ESPECIAL: ando de choque")
             for enemigo in enemigos:
                 enemigo.recibir_golpe(3)
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
        self.tipo = tipo
        self.dano = dano

    def mejorar(self):
        self.dano += 2
        print(f"¡Tu arma {self.nombre} ha sido mejorada! Daño: {self.dano}")









