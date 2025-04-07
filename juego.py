from abc import  ABC, abstractmethod
import random


class Personaje:
     def __init__(self, nombre, vida):
         self.nombre = nombre
         self.vida = vida
         self.vivo = True

     def recibir_golpe(self, cantidad):
             self.vida -= cantidad
             print(f"{self.nombre} recibe {cantidad} de daño. vida restante: {self.vida}")
             if self.vida <= 0:
                 self.vivo = False
                 print(f"{self.nombre} ha sido derrotado.")


class Jugador :
     def __init__(self, nombre):
         super().__init__(nombre, vida=100)
         self.puntuacion = 0
         self.arma = None
     def atacar(self, enemigo):
         if self.arma and self.arma.esta_disponble():
             poder = self.arma.usar()
             print(f"{self.nombre} ata con {self.arma.nombre} y causa {poder} de daño.")
             enemigo.recibir_golpe(poder)
             if not  enemigo.vivo:
                 self.puntuacion += 10
                 print(f"{self.nombre} derrota a {enemigo.nombre} gana 10 puntos. puntacion total:{self.puntuacion} ")


