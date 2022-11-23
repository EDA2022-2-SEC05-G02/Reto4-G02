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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as ss
from tabulate import tabulate
import datetime 
import time
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.ADT import minpq as pq
from DISClib.ADT import stack as st
from DISClib.ADT import graph as gr
from DISClib.ADT import indexminpq as ipq
import folium
from folium.plugins import MarkerCluster
import math
assert cf


#para intalar harvesine ejecutar en consola:               pip install haversine
from haversine import haversine, Unit



"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newAnalyzer():
    """
    Se crea el analizador de los datos del reto
    
    """    
    
    analyzer = {"DiGraph": None,
                "Graph": None,
                "id->Coordenadas HASH": None,
                "id->District_Name HASH":None,
                "id->Neighborhood_Name HASH":None,
                "Arcos LIST": None,
                "Vertices LIST": None}
    
    #Tiene el cálculo exacto para el tamaño sumando el total de busstops + transbordos
    analyzer["diGraph"] = gr.newGraph(datastructure="ADJ_LIST", directed=True, size=5011, comparefunction=compareStopIds)
    analyzer["graph"] = gr.newGraph(datastructure="ADJ_LIST", directed=False, size=5011, comparefunction=compareStopIds)

    #Tiene el número de elementos preciso, es decir, el número primo más cercano al producto del total de bustops x 4
    analyzer["id->Coordenadas HASH"] = mp.newMap(numelements=18593, maptype='PROBING', loadfactor=0.5, comparefunction=compareMapID)
    analyzer["id->District_Name HASH"] = mp.newMap(numelements=18593, maptype='PROBING', loadfactor=0.5, comparefunction=compareMapID)
    analyzer["id->Neighborhood_Name HASH"] = mp.newMap(numelements=18593, maptype='PROBING', loadfactor=0.5, comparefunction=compareMapID)

    #analyzer["Arcos LIST"] = lt.newList(datastructure='ARRAY_LIST', cmpfunction= ?????????? va a ser una lista literal solo de los pesos de los vértices? o que?)
    #analyzer["Vertices LIST"] = lt.newList(datastructure='ARRAY_LIST', cmpfunction= ?????? va a ser lit de solo los identificadores? pa que? toca preguntar)

    return analyzer

# Funciones para agregar informacion al catalogo

def addCoordenadasToHASH(stop, analyzer):
    map = analyzer["id->Coordenadas HASH"]
    longitude = stop["Longitude"]
    latitude = stop["Latitude"]
    id = stop["id"]

    mp.put(map, id, (latitude, longitude))

def addVertexToGraph(stop, graph, analyzer):
    id = stop["id"]
    graph = analyzer[graph]

    gr.insertVertex(graph=graph, vertex=id)

def addEdgesToDigraph(edge, graph, analyzer):
    graph = analyzer[graph]
    bus = edge["Bus_Stop"][4:7]
    vertexA = edge["Code"] + "-" + bus
    vertexB = edge["Code_Destiny"] + "-" + bus
    coorA = getValueFast(analyzer["id->Coordenadas HASH"], vertexA)
    coorB = getValueFast(analyzer["id->Coordenadas HASH"], vertexB)
    weight = haversine(coorA, coorB)

    gr.addEdge(graph, vertexA, vertexB, weight)
    gr.addEdge(graph, vertexB, vertexA, weight)

def addEdgesToGraph(edge, graph, analyzer):
    graph = analyzer[graph]
    bus = edge["Bus_Stop"][4:7]
    vertexA = edge["Code"] + "-" + bus
    vertexB = edge["Code_Destiny"] + "-" + bus
    coorA = getValueFast(analyzer["id->Coordenadas HASH"], vertexA)
    coorB = getValueFast(analyzer["id->Coordenadas HASH"], vertexB)
    weight = haversine(coorA, coorB)

    gr.addEdge(graph, vertexA, vertexB, weight)
    

# Funciones para creacion de datos

# Funciones de consulta

#! =^..^=   =^..^=   =^..^=    =^..^=  [Requerimiento 1]  =^..^=    =^..^=    =^..^=    =^..^=

#! =^..^=   =^..^=   =^..^=    =^..^=  [Requerimiento 2]  =^..^=    =^..^=    =^..^=    =^..^=

#! =^..^=   =^..^=   =^..^=    =^..^=  [Requerimiento 3]  =^..^=    =^..^=    =^..^=    =^..^=

#! =^..^=   =^..^=   =^..^=    =^..^=  [Requerimiento 4]  =^..^=    =^..^=    =^..^=    =^..^=

#! =^..^=   =^..^=   =^..^=    =^..^=  [Requerimiento 5]  =^..^=    =^..^=    =^..^=    =^..^=

#! =^..^=   =^..^=   =^..^=    =^..^=  [Requerimiento 6]  =^..^=    =^..^=    =^..^=    =^..^=

#! =^..^=   =^..^=   =^..^=    =^..^=  [Requerimiento 7]  =^..^=    =^..^=    =^..^=    =^..^=

#! =^..^=   =^..^=   =^..^=    =^..^=  [Requerimiento 8]  =^..^=    =^..^=    =^..^=    =^..^=



# Funciones utilizadas para comparar elementos 

def compareStopIds(stop, keyvaluestop):
    stopcode = keyvaluestop['key']
    if (stop == stopcode):
        return 0
    elif (stop > stopcode):
        return 1
    else:
        return -1
    
def compareMapID(id, entry):
    idEntry = me.getKey(entry)
    if (id == idEntry):
        return 0
    elif (id > idEntry):
        return 1
    else:
        return -1

# Funciones de ordenamiento
    

#Funciones útiles
    
def getValueFast(map, key):

    entry = mp.get(map, key)

    value = me.getValue(entry)

    return value
    
def printVerteces(graph, analyzer):
    graph = analyzer[graph]
    list = gr.vertices(graph)
    for vertex in lt.iterator(list):
        print(vertex)