from abc import  ABC, abstractmethod
import random




class Personaje:
     def __init__(self, nombre, vida):
         self.nombre = nombre
         self.vida = vida
         self.vivo = True

     def recibir_daño(self, cantidad):
             self.vida -= cantidad
             print(f"{self.nombre} recibe {cantidad} de daño. vida restante: {self.vida}")
             if self.vida <= 0:
                 self.vida = 0
                 self.vivo = False
                 print(f"{self.nombre} ha sido derrotado.")
             else:
                 print(f"{self.nombre} recibió {cantidad} de daño. su vida restante. {self.vida}")

class Jugador :
     def __init__(self, nombre):
         super().__init__(nombre, vida=100)
         self.puntuacion = 0
         self.arma = None


