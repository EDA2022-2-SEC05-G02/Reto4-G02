"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import csv
import datetime
import time
from DISClib.ADT import list as lt

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""
#* Configurar el entorno de desarrollo

csv.field_size_limit(2147483647)

# Inicialización del Catálogo de libros

def newController():
    """
    Llama la función para iniciar el Catalogo de Plataformas Digitales
    """
    
    control = {"model" : None}
    control["model"] = model.newAnalyzer()
    
    return control   

# Funciones para la carga de datos

def loadData(control, suffix):
    analyzer = control["model"]
    StopsFile = cf.data_dir + "bus_stops_bcn-utf8" + suffix
    EdgesDataFile = cf.data_dir + "bus_edges_bcn-utf8" + suffix
    inputFileStops = csv.DictReader(open(StopsFile, encoding = 'utf-8'))
    inputFileEdgesData = csv.DictReader(open(EdgesDataFile, encoding= "utf-8"))
   
    for stop in inputFileStops:
        stop = reformStop(stop)

   
    for edge in inputFileEdgesData:
        edge = reformEdge(edge)
        

    return control

# Funciones de ordenamiento

def reformStop(stop):
    pass

def reformEdge(edge):
    pass

# Funciones de consulta sobre el catálogo

#! =^..^=   =^..^=   =^..^=    =^..^=  [Requerimiento 1]  =^..^=    =^..^=    =^..^=    =^..^=


#! =^..^=   =^..^=   =^..^=    =^..^=  [Requerimiento 2]  =^..^=    =^..^=    =^..^=    =^..^=


#! =^..^=   =^..^=   =^..^=    =^..^=  [Requerimiento 3]  =^..^=    =^..^=    =^..^=    =^..^=


#! =^..^=   =^..^=   =^..^=    =^..^=  [Requerimiento 4]  =^..^=    =^..^=    =^..^=    =^..^=


#! =^..^=   =^..^=   =^..^=    =^..^=  [Requerimiento 5]  =^..^=    =^..^=    =^..^=    =^..^=


#! =^..^=   =^..^=   =^..^=    =^..^=  [Requerimiento 6]  =^..^=    =^..^=    =^..^=    =^..^=


#! =^..^=   =^..^=   =^..^=    =^..^=  [Requerimiento 7]  =^..^=    =^..^=    =^..^=    =^..^=


#! =^..^=   =^..^=   =^..^=    =^..^=  [Requerimiento 8]  =^..^=    =^..^=    =^..^=    =^..^=


#* Funciones de Calculo y Analisis

def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def deltaTime(end, start):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
