"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import threading
from DISClib.ADT import stack
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import list as lt
import folium
import webbrowser
assert cf
from DISClib.ADT import graph as gr
import model
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
#? Funciones Print: Se usan principalmente para ahorrar la escritura de prints

def printchooseCSV():
    print('\nIngrese la representación de los datos que quiere usar: ')
    print(' 1. -small')
    print(' 2. -5pct')
    print(' 3. -10pct')
    print(' 4. -20pct')
    print(' 5. -30pct')
    print(' 6. -50pct')
    print(' 7. -80pct')
    print(' 8. -large')

def printHeader(rqn, msg_rq, msg_answer):
    """
    Imprime en consola los encabezados de cada requerimiento

    Args:
        rqn (_type_):   Numero del requerimiento 
        msg_rq (_type_): Mensaje del requerimiento (Inputs)
        msg_answer (_type_): Mensaje de Respuesta
    """    
    print("\n============= Req No. " + str(rqn) + " Inputs =============")
    print(msg_rq)
    print("\n============= Req No. " + str(rqn) + " Answer =============" )
    print(msg_answer)
    print("------------------------------------------------------------------------")

def printeador(resp0=None,resp1=None,resp2=None,resp3=None,resp4=None):
    [(print(i+"\n")) for i in (resp0,resp1,resp2,resp3,resp4) if i!=None]

def printMenu():
    print("\n------------------------------------------------------------------------")
    print("Bienvenido")
    print("0- Cargar información en el catálogo")
    print("1- Buscar un camino posible entre dos estaciones (G)")
    print("2- Buscar el camino con menos paradas entre dos estaciones (G)")
    print("3- Reconocer los componentes conectados de la Red de rutas de bus (I)")
    print("4- Planear el camino con distancia mínima entre dos puntos geográficos (I)")
    print("5- Informar las estaciones “alcanzables” desde un origen a un número máximo de conexiones (I)")
    print("6- Buscar el camino con mínima distancia entre una estación de origen y un vecindario de destino (G)")
    print("7- Encontrar un posible camino circular desde una estación de origen (G)")
    print("8- Graficar resultados para cada uno de los requerimientos (B)")

#? Funciones Choose: Se usan principalmente para que el usuario escoja un tipo de representacion

def fileChoose():
    """
    
    Da opciones al usuario para que escoja la representación de los datos de su preferencia

    Returns:
        
        El sufijo de la representación de los datos escogida
    """    
    fileChoose = False
    while fileChoose == False:
    
        suffixFileChoose = input('Opción seleccionada: ')
        if int(suffixFileChoose[0]) == 1:
            suffix = '-small'
            print('\nSeleciono el archivo ' + suffix)
            suffix += '.csv'
            fileChoose = True
        elif int(suffixFileChoose[0]) == 2:
            suffix = '-5pct'
            print('\nSeleciono el archivo ' + suffix)
            suffix += '.csv'
            fileChoose = True
        elif int(suffixFileChoose[0]) == 3:
            suffix = '-10pct'
            print('\nSeleciono el archivo ' + suffix)
            suffix += '.csv'
            fileChoose = True
        elif int(suffixFileChoose[0]) == 4:
            suffix = '-20pct'
            print('\nSeleciono el archivo ' + suffix)
            suffix += '.csv'
            fileChoose = True
        elif int(suffixFileChoose[0]) == 5:
            suffix = '-30pct'
            print('\nSeleciono el archivo ' + suffix)
            suffix += '.csv'
            fileChoose = True
        elif int(suffixFileChoose[0]) == 6:
            suffix = '-50pct'
            print('\nSeleciono el archivo ' + suffix)
            suffix += '.csv'
            fileChoose = True
        elif int(suffixFileChoose[0]) == 7:
            suffix = '-80pct'
            print('\nSeleciono el archivo ' + suffix)
            suffix += '.csv'
            fileChoose = True
        elif int(suffixFileChoose[0]) == 8:
            suffix = '-large'
            print('\nSeleciono el archivo ' + suffix)
            suffix += '.csv'
            fileChoose = True    
            
    return suffix

catalog = None

"""
Menu principal
"""
def thread_cycle():
    while True:
        printMenu()
        inputs = input('\nSeleccione una opción para continuar\n')
        if int(inputs) == 0:
            print("Cargando información de los archivos ....")
            control = controller.newController()
            printchooseCSV()
            suffix = fileChoose()
            control, totalRutas, area, longMin, longMax,  latMin, latMax, table = controller.loadData(control, suffix)
            respuesta = controller.mostrarCarga(control)
            print("\nEl total de rutas de bus disponibles es: " + str(totalRutas))
            print(respuesta)
            # print("TOTAL VERTICES MAP:" + str(gr.numVertices(control["model"]["DiGraph"])))
            print(f"El rango del área rectangular de Barcelona que cubre la red de buses es: '{area}'\nLongitud Mínima: {longMin}\nLongitud Máxima: {longMax}\nLatitud Mínima: {latMin}\nLatitud Máxima: {latMax}\n")
            print("Las primeras cinco y últimas cinco estaciones registradas en el grafo son las siguientes: ")
            print(table)
            # for x in lt.iterator(control["model"]["listPerTransbordo"]):
            #     print(x)
            # print("="*20)
            # for x in lt.iterator(control["model"]["listPerNOTTransbordo"]):
            #     print(x)


        elif int(inputs) == 1:
            estacionOrigen = input("¿Cúal es la estación de origen?: ")
            estacionDestino = input("¿Cúal es la estación de destino?: ")
            # model.printVerteces("DiGraph", control["model"])
            # model.printEdges("DiGraph", control["model"])

        elif int(inputs) == 2:

            #!  DATOS TENTATIVOS QUE SIRVEN
            # estacionOrigen = "0036-109"
            # estacionDestino = "0058-D40"
            estacionOrigen = input("¿Cúal es la estación de origen?: ")
            estacionDestino = input("¿Cúal es la estación de destino?: ")
            totalStops, pathList, totalTransbordos = controller.buscarCaminoOptimoEntreDosEstaciones(control,estacionOrigen,estacionDestino)
            resp1 = ("El total de estaciones que contiene el camino solución es (Sin contar Transbordos): "+str(totalStops-totalTransbordos))
            resp2 = ("El total de transbordos de ruta que debe realizar el usuario es: "+str(totalTransbordos))
                #! ESTO ESTA MAL, AUN NO ME DA XD
            resp0,resp3 = controller.distancias(control,pathList)
            resp0 = ("La distancia total que toma el camino entre la estación origen y la estación destino es: "+str(round(resp0,2))+"Km")
            printeador(resp0,resp1,resp2,resp3)
        elif int(inputs) == 3:
                #NO HAY ENTRADAS POR PARÁMETRO
            pass

        elif int(inputs) == 4:
            localizaciónOrigen = input("¿Cúal es la localización de origen?: ")
            localizaciónDestino = input("¿Cúal es la localización de destino?: ")

            pass

        elif int(inputs) == 5:
            estacionOrigen = input("¿Cúal es el identificador de la estación origen? (Code-IdBus): ")
            numeroConexiones = int(input("¿Cúal es el número de conexiones permitidas?: "))
            pass

        elif int(inputs) == 6:
            estacionOrigen = input("¿Cúal es el identificador de la estación origen? (Code-IdBus): ")
            neighborhoodDestino = input("¿Cúal es el identificador del vecindario: ")
            pass

        elif int(inputs) == 7:
            estacionOrigen = input("¿Cúal es el identificador de la estación origen? (Code-IdBus): ")
            pass

        elif int(inputs) == 8:
            controller.printkeys(control)

        elif int(inputs) == 9:
            print("VOY A PROBAR COSAS")

        else:
            sys.exit(0)
    sys.exit(0)

if __name__ == "__main__":
    threading.stack_size(67108864)  # 64MB stack
    sys.setrecursionlimit(2 ** 20)
    thread = threading.Thread(target=thread_cycle)
    thread.start()



#Primera entrega – Reto 4#