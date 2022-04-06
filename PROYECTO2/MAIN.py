from lista import Lista as Lista
from xml.dom import minidom
from tkinter import filedialog, Tk
import generarMapa

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
            a = UMRescate.extraer_dato(x)
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
        M.pathfindinRecurso()
        M.graficarCiudad('recursos')

    def pathfinder(self, x0, y0, xf, yf):
        openset = Lista()
        closedset = Lista()
        celda = Lista()
        camino = False
        if M.posicionxy(x0, y0) == 'E' or M.posicionxy(x0, y0) == 'E':
            celda.insertar_fin(x0)
            celda.insertar_fin(y0)
            openset.insertar_fin(celda)
            celda = Lista()

    def posicionxy(self, x, y):
        if y < CElegida.cantidad_de_datos() :
            Y = CElegida.extraer_dato(y)
            contador = 0
            newY = ''
            for X in Y:
                if x != contador:
                    newY = newY 
                else:
                    newY = X
                contador = contador + 1   
            return newY 
        else: 
            return '*'

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
        M.pathfindingRescue()
        M.graficarCiudad('rescate')  

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

    def pathfindingRescue(self):
        openSet = Lista()
        celdaIN = Lista()
        celdaOUT = Lista()
        contador = 0
        for i in range(0,CElegida.cantidad_de_datos()):
            x = CElegida.extraer_dato(i)
            for j in x:
                if j == 'E' or j == 'e':
                    celda = Lista()
                    celda.insertar_fin(contador)
                    celda.insertar_fin(i)
                    celdaIN.insertar_fin(celda)
                contador = contador + 1
            contador = 0
            
        if celdaIN.cantidad_de_datos() != 1:
            print('****Seleccione un punto de partida****\n  0. Salir')
            for i in range(0,celdaIN.cantidad_de_datos()):
                x = celdaIN.extraer_dato(i).extraer_dato(0)
                y = celdaIN.extraer_dato(i).extraer_dato(1)
                opcion = '\n  '+str(i+1)+'. '+str(x)+', '+str(y)
                print(opcion)
            m =int(input())-1
        else:
            m = 0
        
        for i in range(0,CElegida.cantidad_de_datos()):
            x = CElegida.extraer_dato(i)
            for j in x:
                if j == 'C' or j == 'c':
                    celda = Lista()
                    celda.insertar_fin(contador)
                    celda.insertar_fin(i)
                    celdaOUT.insertar_fin(celda)
                    print(celdaOUT)
                contador = contador + 1
            contador = 0
            
        if celdaOUT.cantidad_de_datos() != 1:
            print('****Seleccione una unidad civil****\n  0. Salir')
            for i in range(0,celdaOUT.cantidad_de_datos()):
                x = celdaOUT.extraer_dato(i).extraer_dato(0)
                y = celdaOUT.extraer_dato(i).extraer_dato(1)
                opcion = '\n  '+str(i+1)+'. '+str(x)+', '+str(y)
                print(opcion)
            n =int(input())-1
        else:
            n = 0

        for i in range(0, celdaOUT.cantidad_de_datos()):
            if i != n:
                M.modificarXY(celdaOUT.extraer_dato(i).extraer_dato(0),celdaOUT.extraer_dato(i).extraer_dato(1), 'H') 

        Terminado = False
        inicio = celdaIN.extraer_dato(m)
        final = celdaOUT.extraer_dato(n)
        openSet.insertar_fin(inicio)

        while Terminado == False:
            if openSet.cantidad_de_datos() != 0:
                arriba = Lista()
                abajo = Lista()
                izquierda= Lista()
                derecha = Lista()
                celda = openSet.extraer_dato(0)
                arribay = celda.extraer_dato(1)-1
                arribax = celda.extraer_dato(0)
                abajoy = celda.extraer_dato(1)+1
                abajox = celda.extraer_dato(0)
                izquierdax = celda.extraer_dato(0)-1
                izquierday = celda.extraer_dato(1)
                derechax = celda.extraer_dato(0)+1
                derechay = celda.extraer_dato(1)
                if arribay > 0:
                    arribaxy = M.posicionxy(arribax, arribay)
                    if arribaxy != '*' and arribaxy != 'M' and arribaxy!='A':
                        arriba.insertar_fin(arribax)
                        arriba.insertar_fin(arribay)
                        openSet.insertar_fin(arriba)
                else:
                    arribaxy = None
                if abajoy > 0:
                    abajoxy = M.posicionxy(abajox, abajoy)
                    if abajoxy != '*' and abajoxy != 'M' and abajoxy != 'A':
                        abajo.insertar_fin(abajox)
                        abajo.insertar_fin(abajoy)
                        openSet.insertar_fin(abajo)
                else: 
                    abajoxy = None
                if derechax > 0:
                    derechaxy = M.posicionxy(derechax, derechay)
                    if derechaxy != '*' and derechaxy != 'M' and derechaxy != 'A':
                        derecha.insertar_fin(derechax)
                        derecha.insertar_fin(derechay)
                        openSet.insertar_fin(derecha)
                else: 
                    derechaxy = None
                if izquierdax > 0:
                    izquierdaxy = M.posicionxy(izquierdax, izquierday)
                    if izquierdaxy != '*' and izquierdaxy != 'M' and izquierdaxy != 'A':
                        izquierda.insertar_fin(izquierdax)
                        izquierda.insertar_fin(izquierday)
                        openSet.insertar_fin(izquierda)
                else:
                    izquierdaxy = None
                if arribaxy == '*' or arribaxy == 'M' or arribaxy == 'A':
                    if abajoxy == '*' or abajoxy == 'M' or abajoxy == 'A':
                        if izquierdaxy == '*' or izquierdaxy == 'M' or izquierdaxy == 'A':
                            if derechaxy == '*' or derechaxy == 'M' or derechaxy == 'A':
                                M.modificarXY(celda.extraer_dato(0),celda.extraer_dato(1),'*')
                            else:
                                M.modificarXY(celda.extraer_dato(0),celda.extraer_dato(1),'A')
                        else:
                            M.modificarXY(celda.extraer_dato(0),celda.extraer_dato(1),'A')
                    else:
                        M.modificarXY(celda.extraer_dato(0),celda.extraer_dato(1),'A')
                else:
                    M.modificarXY(celda.extraer_dato(0),celda.extraer_dato(1),'A')
                if arribax == final.extraer_dato(0) and arribay == final.extraer_dato(1) :
                    Terminado = True
                    XYF.insertar_fin(arribax)
                    XYF.insertar_fin(arribay)
                elif abajox == final.extraer_dato(0) and abajoy == final.extraer_dato(1) :
                    Terminado = True
                    XYF.insertar_fin(abajox)
                    XYF.insertar_fin(abajoy)
                elif izquierdax == final.extraer_dato(0) and izquierday == final.extraer_dato(1) : 
                    Terminado = True
                    XYF.insertar_fin(izquierdax)
                    XYF.insertar_fin(izquierday)
                elif derechax == final.extraer_dato(0) and derechay == final.extraer_dato(1):
                    Terminado = True
                    XYF.insertar_fin(derechax)
                    XYF.insertar_fin(derechay)
                openSet.DeleteFirst()
            else:
                print('La mision es imposible')
                Terminado = True
                exit()
            x = inicio.extraer_dato(0)
            y = inicio.extraer_dato(1)
            M.modificarXY(x,y,'E')
            for i in range(0, celdaOUT.cantidad_de_datos()):
                M.modificarXY(celdaOUT.extraer_dato(i).extraer_dato(0),celdaOUT.extraer_dato(i).extraer_dato(1), 'C') 

    def pathfindinRecurso(self):
        openSet = Lista()
        celdaIN = Lista()
        celdaOUT = Lista()
        contador = 0
        for i in range(0,CElegida.cantidad_de_datos()):
            x = CElegida.extraer_dato(i)
            for j in x:
                if j == 'E' or j == 'e':
                    celda = Lista()
                    celda.insertar_fin(contador)
                    celda.insertar_fin(i)
                    celdaIN.insertar_fin(celda)
                contador = contador + 1
            contador = 0
            
        if celdaIN.cantidad_de_datos() != 1:
            print('****Seleccione un punto de partida****\n  0. Salir')
            for i in range(0,celdaIN.cantidad_de_datos()):
                x = celdaIN.extraer_dato(i).extraer_dato(0)
                y = celdaIN.extraer_dato(i).extraer_dato(1)
                opcion = '\n  '+str(i+1)+'. '+str(x)+', '+str(y)
                print(opcion)
            m =int(input())-1
        else:
            m = 0
        for i in range(0,CElegida.cantidad_de_datos()):
            x = CElegida.extraer_dato(i)
            for j in x:
                if j == 'R' or j == 'r':
                    celda = Lista()
                    celda.insertar_fin(contador)
                    celda.insertar_fin(i)
                    celdaOUT.insertar_fin(celda)
                contador = contador + 1
            contador = 0
            
        if celdaOUT.cantidad_de_datos() != 1:
            print('****Seleccione una unidad de recursos****\n  0. Salir')
            for i in range(0,celdaOUT.cantidad_de_datos()):
                x = celdaOUT.extraer_dato(i).extraer_dato(0)
                y = celdaOUT.extraer_dato(i).extraer_dato(1)
                opcion = '\n  '+str(i+1)+'. '+str(x)+', '+str(y)
                print(opcion)
            n =int(input())-1
        else:
            n = 0

        for i in range(0, celdaOUT.cantidad_de_datos()):
            if i != n:
                M.modificarXY(celdaOUT.extraer_dato(i).extraer_dato(0),celdaOUT.extraer_dato(i).extraer_dato(1), 'H')
                k = M.posicionxy(celdaOUT.extraer_dato(i).extraer_dato(0),celdaOUT.extraer_dato(i).extraer_dato(1))
                print(k)
        Terminado = False
        inicio = celdaIN.extraer_dato(m)
        openSet.insertar_fin(inicio)
        while Terminado == False:
            if openSet.cantidad_de_datos() != 0:
                arriba = Lista()
                abajo = Lista()
                izquierda= Lista()
                derecha = Lista()
                celda = openSet.extraer_dato(0)
                arribay = celda.extraer_dato(1)-1
                arribax = celda.extraer_dato(0)
                abajoy = celda.extraer_dato(1)+1
                abajox = celda.extraer_dato(0)
                izquierdax = celda.extraer_dato(0)-1
                izquierday = celda.extraer_dato(1)
                derechax = celda.extraer_dato(0)+1
                derechay = celda.extraer_dato(1)
                if arribay > 0:
                    arribaxy = M.posicionxy(arribax, arribay)
                    if arribaxy != '*' and arribaxy != 'M' and arribaxy!='A':
                        arriba.insertar_fin(arribax)
                        arriba.insertar_fin(arribay)
                        openSet.insertar_fin(arriba)
                else:
                    arribaxy = None
                if abajoy > 0:
                    abajoxy = M.posicionxy(abajox, abajoy)
                    if abajoxy != '*' and abajoxy != 'M' and abajoxy != 'A':
                        abajo.insertar_fin(abajox)
                        abajo.insertar_fin(abajoy)
                        openSet.insertar_fin(abajo)
                else:
                    abajoxy = None
                if derechax > 0:
                    derechaxy = M.posicionxy(derechax, derechay)
                    if derechaxy != '*' and derechaxy != 'M' and derechaxy != 'A':
                        derecha.insertar_fin(derechax)
                        derecha.insertar_fin(derechay)
                        openSet.insertar_fin(derecha)
                else:
                    derechaxy = None
                if izquierdax > 0:
                    izquierdaxy = M.posicionxy(izquierdax, izquierday)
                    if izquierdaxy != '*' and izquierdaxy != 'M' and izquierdaxy != 'A':
                        izquierda.insertar_fin(izquierdax)
                        izquierda.insertar_fin(izquierday)
                        openSet.insertar_fin(izquierda)
                else:
                    izquierdaxy = None
                if arribaxy == '*' or arribaxy == 'M' or arribaxy == 'A':
                    if abajoxy == '*' or abajoxy == 'M' or abajoxy == 'A':
                        if izquierdaxy == '*' or izquierdaxy == 'M' or izquierdaxy == 'A':
                            if derechaxy == '*' or derechaxy == 'M' or derechaxy == 'A':
                                M.modificarXY(celda.extraer_dato(0),celda.extraer_dato(1),' ')
                            else:
                                M.modificarXY(celda.extraer_dato(0),celda.extraer_dato(1),'A')
                        else:
                            M.modificarXY(celda.extraer_dato(0),celda.extraer_dato(1),'A')
                    else:
                        M.modificarXY(celda.extraer_dato(0),celda.extraer_dato(1),'A')
                else:
                    M.modificarXY(celda.extraer_dato(0),celda.extraer_dato(1),'A')
                if arribaxy == 'R' :
                    Terminado = True
                    XYF.insertar_fin(arribax)
                    XYF.insertar_fin(arribay)
                elif abajoxy == 'R' :
                    Terminado = True
                    XYF.insertar_fin(abajox)
                    XYF.insertar_fin(abajoy)
                elif izquierdaxy == 'R': 
                    Terminado = True
                    XYF.insertar_fin(izquierdax)
                    XYF.insertar_fin(izquierday)
                elif derechaxy == 'R':
                    Terminado = True
                    XYF.insertar_fin(derechax)
                    XYF.insertar_fin(derechay)
                openSet.DeleteFirst()
            else:
                print('La mision es imposible')
                Terminado = True
                exit()
            x = inicio.extraer_dato(0)
            y = inicio.extraer_dato(1)
            M.modificarXY(x,y,'E')
            for i in range(0, celdaOUT.cantidad_de_datos()):
                M.modificarXY(celdaOUT.extraer_dato(i).extraer_dato(0),celdaOUT.extraer_dato(i).extraer_dato(1), 'R')

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
    
    def graficarCiudad(self, mision):
        cells = ''
        rows = ''
        celdaNT='''<TD BGCOLOR="BLACK">       </TD>'''
        celdaT='''<TD BGCOLOR="WHITE">       </TD>'''
        celdaE='''<TD BGCOLOR="GREEN">       </TD>'''
        CeldaUM='''<TD BGCOLOR="RED">       </TD>'''
        celdaUC='''<TD BGCOLOR="BLUE">       </TD>'''
        celdaR='''<TD BGCOLOR="GRAY">       </TD>'''
        celdaA = '''<TD BGCOLOR="YELLOW">       </TD>'''
        nombre = 'MISIONCHAPINWARRIORS'
        descripcion = ''
        CapacidadF = ''
        for i in range(0,RElegido.cantidad_de_datos()):
            CapacidadF = RElegido.extraer_dato(i)
        if mision == 'rescate':
            descripcion = descripcion + 'Tipo de mision: Rescate\nUnidad Civil Rescatada: '+str(XYF.extraer_dato(0)+1)+', '+str(XYF.extraer_dato(1)+1)+'\nRobot Utilizado: '+ RElegido.extraer_dato(0)+')'
        elif mision == 'recursos':
            descripcion = descripcion + 'Tipo de mision: Extracción de recursos\nRecurso Extraido: '+'\nRobot Utilizado: '+str(XYF.extraer_dato(0)+1)+', '+str(XYF.extraer_dato(1)+1)+'\nRobot Utilizado: '+ str(RElegido.extraer_dato(0))+','+str(RElegido.extraer_dato(0))+'\nCapacidad de combate inicial '+str(RElegido.extraer_dato(2))+', Capacidad de combate final '+ str(CapacidadF)+')'
        

        for fila in range(0,CElegida.cantidad_de_datos()):
            cadena = CElegida.extraer_dato(fila)
            for letra in cadena:
                if letra =='h' or letra=='H':
                    cells = cells + celdaT
                elif letra =='*':
                    cells = cells + celdaNT
                elif letra == 'E' or letra == 'e':
                    cells = cells + celdaE
                elif letra == 'M' or letra == 'm':
                    cells = cells + CeldaUM
                elif letra == 'C' or letra == 'c':
                    cells = cells + celdaUC
                elif letra == 'R' or letra == 'r':
                    cells = cells + celdaR
                elif letra == 'A' :
                    cells = cells + celdaA
            rows = rows + '''<TR>''' + cells +'''</TR>'''
            cells = ''
        generarMapa.graficar.grafica(rows, nombre, descripcion)

XYF = Lista()
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
