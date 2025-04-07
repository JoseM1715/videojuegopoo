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
         super().__init__(nombre, vida=100)
         self.nombre: str = nombre
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

     def usar_arma(self):
         pass



class Arma:
    def __init__(self, tipo: str, dano: int, alcance: str):
        self.tipo = tipo
        self.dano = dano
        self.alcance = alcance

    def usar(self):
        print(f"usaste el arma tipo {self.tipo} con daño de {self.dano} y alcance {self.alcance}")



