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


class Jugador:
     def __init__(self, nombre):
         self.nombre: str = nombre
         self.vida: int = 100
         self.vivo: bool = True
         self.puntuacion: int = 0
         self.arma = None

     def atacar(self, enemigo):
         if self.arma and self.arma.esta_disponble():
             poder = self.arma.usar()
             print(f"{self.nombre} ata con {self.arma.nombre} y causa {poder} de daño.")
             enemigo.recibir_golpe(poder)
             if not  enemigo.vivo:
                 self.puntuacion += 10
                 print(f"{self.nombre} derrota a {enemigo.nombre} gana 10 puntos. puntuacion total:{self.puntuacion} ")
         else:
             print(f"{self.nombre} no tiene un arma disponible para atacar")

     def usar_arma(self):
         if self.arma and self.arma.esta_disponible():
             dano = self.arma.usar()
             print(f"usaste el arma tipo {self.arma.tipo} con daño de {self.arma.dano} y alcance {self.arma.alcance}")
             return dano
         return print(f"{self.nombre} no se puede usar el arma")


class Arma:
    def __init__(self,nombre, tipo: str, dano: int):
        self.nombre = nombre
        self.tipo = tipo
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






