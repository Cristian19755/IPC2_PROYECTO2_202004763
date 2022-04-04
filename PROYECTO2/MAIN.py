from lista import Lista as Lista
from xml.dom import minidom
from tkinter import filedialog, Tk

class Main:
    def menu(self):
        print("****Seleccione una opcion****\n   1.Cargar Archivo\n   2.Salir")
        op = input()
        if op == '1':
            raiz = Tk()
            myArchivo = filedialog.askopenfilename(title="Abrir Archivo")
            if myArchivo != None:
                self.archivo = minidom.parse(myArchivo)
                M.leerArchivo()
                print('Archivo Cargado')
                raiz.destroy()
                M.menu2()
            else: 
                print('Archivo no encontrado')
        if op == '2':
            exit()

    def menu2(self):
        print('****Seleccione una misión****\n 1.Mision de Rescate\n 2.Mision de extracción de recursos\n 0.Salir')
        y = int(input())
        if y == 1 :
            print('****Seleccione una ciudad****\n  0. Salir')
            for i in range(0,CNRescue.cantidad_de_datos()):
                nombre = CNRescue.extraer_dato(i)
                opcion = '  '+str(i+1)+'. '+nombre
                print(opcion)
            x=int(input())
            if x == 0:
                exit()
            x= x-1
            z = MisionesRescate.extraer_dato(x)
            for i in range(0, z.cantidad_de_datos()):
                n = z.extraer_dato(i)
                CElegida.insertar_fin(n)
            for i in range (0,UMRecursos.cantidad_de_datos()):
                n = a.extraer_dato(i)
                dato = 'M'
                x = n.extraer_dato(1)-1
                y = n.extraer_dato(2)-1
                M.modificarXY(x,y,dato)
            M.menuRescate()
        elif y == 2:
            print('****Seleccione una ciudad****\n  0. Salir')
            for i in range(0,CNRecursos.cantidad_de_datos()):
                nombre = CNRecursos.extraer_dato(i)
                opcion = '  '+str(i+1)+'. '+nombre
                print(opcion)
            x=int(input())
            if x == 0:
                exit()
            x= x-1
            z = MisionesRecursos.extraer_dato(x)
            a = UMRecursos.extraer_dato(x)
            for i in range(0, z.cantidad_de_datos()):
                n = z.extraer_dato(i)
                CElegida.insertar_fin(n)
            for i in range (0,UMRecursos.cantidad_de_datos()):
                n = a.extraer_dato(i)
                dato = 'M'
                x = n.extraer_dato(1)-1
                y = n.extraer_dato(2)-1
                M.modificarXY(x,y,dato)
            M.menuRecursos()
        elif y == 0:
            exit()

    def menuRecursos(self):
        print('****Seleccione un ChapinFighter****\n  0. Salir')
        for i in range(0,ChapinFighters.cantidad_de_datos()):
            robot = ChapinFighters.extraer_dato(i)
            nombre = robot.extraer_dato(0)
            capacidad = robot.extraer_dato(2)
            opcion = '  '+str(i+1)+'. '+nombre+'    Capacidad: '+str(capacidad)
            print(opcion)
        x=int(input())
        if x == 0:
            exit()
        x= x-1
        z = ChapinFighters.extraer_dato(x)
        for i in range(0,z.cantidad_de_datos()):
            n = z.extraer_dato(i)
            RElegido.insertar_fin(n)

    def menuRescate(self):
        print('****Seleccione un ChapinRescue****\n  0. Salir')
        for i in range(0,ChapinRescues.cantidad_de_datos()):
            robot = ChapinRescues.extraer_dato(i)
            nombre = robot.extraer_dato(0)
            opcion = '  '+str(i+1)+'. '+nombre
            print(opcion)
        x=int(input())
        if x == 0:
            exit()
        x= x-1
        z = ChapinRescues.extraer_dato(x)
        for i in range(0,z.cantidad_de_datos()):
            n = z.extraer_dato(i)
            RElegido.insertar_fin(n)    

    def leerArchivo(self):
        a = self.archivo
        ciudades = a.getElementsByTagName('listaCiudades')
        robots = a.getElementsByTagName('robots')
        
        for elem in ciudades:
            ciudad = elem.getElementsByTagName('ciudad')
            for i in ciudad:
                nombreCiudades = i.getElementsByTagName('nombre')
                filas = i.getElementsByTagName('fila')
                uniMilitar = i.getElementsByTagName('unidadMilitar')
                for j in nombreCiudades:
                    nombreCiudades = j.firstChild.data
                    ciudadesName.insertar_fin(nombreCiudades)
                Filas = Lista()
                for k in filas:
                    filas = k.firstChild.data
                    filas= filas.replace("\n", "")
                    cadena = ''
                    temp = 1
                    for n in filas:
                        n = str(n)
                        if n == "\"" and temp ==0:
                            break
                        if temp == 0:
                            cadena = cadena + n
                        if n == "\"":
                            temp = 0   
                    filas = cadena
                    filas = filas.replace(' ','H')
                    filas = filas.replace("\"", "")
                    Filas.insertar_fin(filas)
                u = Lista()
                for l in uniMilitar:
                    UM = Lista() ###########Lista (atributo)
                    x = l.getAttribute('columna')
                    y = l.getAttribute('fila')
                    capacidad = l.firstChild.data
                    UM.insertar_fin(int(capacidad))
                    UM.insertar_fin(int(x))
                    UM.insertar_fin(int(y))
                    u.insertar_fin(UM)  ##############Lista por ciudad (ciudad)
                unidadesMilitares.insertar_fin(u)   ########Lista de listas (ciudades)
                Matrices.insertar_fin(Filas)
        for elem in robots:
            robot = elem.getElementsByTagName('robot')
            for i in robot:
                nombre = i.getElementsByTagName('nombre')
                robot = Lista()
                for j in nombre:
                    nombre = j.firstChild.data
                    Tipo = j.getAttribute('tipo')     
                robot.insertar_fin(nombre)
                robot.insertar_fin(Tipo)
                if Tipo == 'ChapinRescue':
                    ChapinRescues.insertar_fin(robot)
                elif Tipo == 'ChapinFighter':
                    Capacidad = j.getAttribute('capacidad')
                    robot.insertar_fin(int(Capacidad))
                    ChapinFighters.insertar_fin(robot)
        for x in range(0, Matrices.cantidad_de_datos()):
            y = Matrices.extraer_dato(x)
            r = ciudadesName.extraer_dato(x)
            u = unidadesMilitares.extraer_dato(x)
            z = False
            p = False
            for j in range(0, y.cantidad_de_datos()):
                n = y.extraer_dato(j)
                for i in n:
                    if i == 'C':
                        z = True
                    elif i == 'R':
                        p = True
            if z == True:
                CNRescue.insertar_fin(r)
                MisionesRescate.insertar_fin(y)
                UMRescate.insertar_fin(u)
            if p == True:
                CNRecursos.insertar_fin(r)
                MisionesRecursos.insertar_fin(y)
                UMRecursos.insertar_fin(u)

    def modificarXY(self, x, y, dato):
        MatrizF = Lista()
        Y = CElegida.extraer_dato(y)
        contador = 0
        newY = ''
        for X in Y:
            if x != contador:
                newY = newY + X
            else:
                newY = newY+dato
            contador = contador + 1
        for i in range(0, CElegida.cantidad_de_datos()):
            if i != y:
                r = CElegida.extraer_dato(i)
                MatrizF.insertar_fin(r)
            else:
                MatrizF.insertar_fin(newY)
        while CElegida.cantidad_de_datos() != 0:
            CElegida.DeleteFirst()
        for i in range(0, MatrizF.cantidad_de_datos()):
            r = MatrizF.extraer_dato(i)
            CElegida.insertar_fin(r)
          
CNRescue = Lista()
CNRecursos = Lista()
MisionesRescate = Lista()
MisionesRecursos = Lista()
UMRescate = Lista()
UMRecursos = Lista()
ChapinFighters = Lista()
ChapinRescues = Lista()
CElegida = Lista()
RElegido = Lista()
###################################
ciudadesName= Lista() 
Matrices = Lista()
unidadesMilitares = Lista()


M = Main()
M.menu()
