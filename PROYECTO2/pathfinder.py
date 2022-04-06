from re import X
from tkinter import Y
from lista import Lista

class celda:
    def __init__(self, x = None, y = None):
        self.x = x 
        self.y = y
        self.G = 0
        self.H = 0
        self.F = self.H+self.G
        self.padre = None
        self.adyacentes = Lista()

class generarcamino:
    def __init__(self):
        self.openset = Lista()
        self.closedset = Lista()
        self.fin = False

    def heuristica(self, x0, y0, xf, yf):
        x = abs(xf-x0)
        y = abs(yf-y0)
        H = x+y
        return H

    def eliminarDato(self, posicion):
        blank = Lista()
        for i in range(0, self.openset.cantidad_de_datos()):
            if i != posicion:
                x = self.openset.extraer_dato(i)
                blank.insertar_fin(x)
        while self.openset.cantidad_de_datos() != 0:
            self.openset.DeleteFirst()
        for i in range(0, blank.cantidad_de_datos()):
            x = blank.extraer_dato(i)
            self.openset.insertar_fin(x)
  

