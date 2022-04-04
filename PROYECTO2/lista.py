from nodo import node

class Lista: 
    def __init__(self):
        self.root = None

    def insertar_inicio(self, data):
        self.root = node(data=data, siguiente=self.root) 
 
    def insertar_fin(self, dato): 

        if self.root is None: 
            self.root = node(data=dato) 
            return 
        auxRoot = self.root
        while auxRoot.siguiente: 
            auxRoot = auxRoot.siguiente
        auxRoot.siguiente = node(data=dato)
    
    def imprimir_lista( self ):
        nodeAux = self.root 
        while nodeAux != None:
            print(nodeAux.data)
            nodeAux = nodeAux.siguiente

    def extraer_dato(self, x):
        auxRoot = self.root
        for i in range(0,x):
            auxRoot = auxRoot.siguiente
        return auxRoot.data

    def __str__(self):
        Cadena = "["
        auxRoot = self.root
        for i in range(self.cantidad_de_datos()):
            Cadena += '\''+str(auxRoot.data)+'\''
            if i != self.cantidad_de_datos()-1:
                    Cadena += str(", ")
            auxRoot = auxRoot.siguiente
        Cadena +="]"
        return Cadena

    def cantidad_de_datos(self):
        nodeAux = self.root 
        contador= 0
        while nodeAux != None:
            contador = contador+1
            nodeAux = nodeAux.siguiente
        return contador
    
    def DeleteFirst(self):
        self.root = self.root.siguiente
