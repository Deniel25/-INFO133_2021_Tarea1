import pymongo, gridfs
from pymongo import MongoClient

mongo = MongoClient("localhost")
baseDatos = mongo["fusaSound"]
coleccion = baseDatos["sounds"]
coleccion.delete_many([])

Archivos = [{"IDAarchivo" : 0,
            "FechaGrabacion" : "30/06/2021",
            "Ciudad" : "Valdivia",
            "DuracionArchivo" : 2 ,
            "FormatoArchivo" : ".wav" ,
            "Latitud" : "-39.83346303002122" ,
            "Longitud" : "-73.24529916977669" ,
            "Exterior" : "interior" ,
            "Usuario" : { "RUT" : "19.941.933-1" ,
                          "Nombre" : "Daniel" ,
                          "Apellido" : "Díaz"
                          },
            "Segmentos" : [{ "ID_segmento" : 1,
                             "FormatoSegmento" : ".wav" ,
                             "DuracionSegmento" : 2 ,
                             "Inicio" : 0,
                             "Fin" : 2,
                             "Etiquetas" : [ {
                                 "NombreFuente" : "wilhelm" ,
                                 "Descripcion" : "AAAAUU",
                                 "IDAnalizador" : 1}]
                             }
                           ]
            },
            
    {"IDAarchivo" : 1,
            "FechaGrabacion" : "01/07/2021",
            "Ciudad" : "Valdivia",
            "DuracionArchivo" : 3 ,
            "FormatoArchivo" : ".wav" ,
            "Latitud" : "-39.816129505751064" ,
            "Longitud" : "-73.24234009393798" ,
            "Exterior" : "interior" ,
            "Usuario" : { "RUT" : "19.941.933-1" ,
                          "Nombre" : "Daniel" ,
                          "Apellido" : "Díaz"
                          },
            "Segmentos" : [{ "ID_segmento" : 1,
                             "FormatoSegmento" : ".wav" ,
                             "DuracionSegmento" : 3 ,
                             "Inicio" : 0,
                             "Fin" : 3,
                             "Etiquetas" : [ {
                                 "NombreFuente" : "yoda" ,
                                 "Descripcion" : "Yoda Death",
                                 "IDAnalizador" : 1}]
                             }
                           ]
        },

    {"IDAarchivo" : 2,
            "FechaGrabacion" : "02/07/2021",
            "Ciudad" : "Valdivia",
            "DuracionArchivo" : 20 ,
            "FormatoArchivo" : ".wav" ,
            "Latitud" : "-39.81518084244701" ,
            "Longitud" : "-73.23927480170632" ,
            "Exterior" : "interior" ,
            "Usuario" : { "RUT" : "19.941.933-1" ,
                          "Nombre" : "Daniel" ,
                          "Apellido" : "Díaz"
                          },
            "Segmentos" : [{ "ID_segmento" : 1,
                             "FormatoSegmento" : ".wav" ,
                             "DuracionSegmento" : 20 ,
                             "Inicio" : 0,
                             "Fin" : 20,
                             "Etiquetas" : [ {
                                 "NombreFuente" : "tiger" ,
                                 "Descripcion" : "Roar",
                                 "IDAnalizador" : 1}]
                             }
                           ]
            },
            
    {"IDAarchivo" : 3,
            "FechaGrabacion" : "03/07/2021",
            "Ciudad" : "Valdivia",
            "DuracionArchivo" : 7 ,
            "FormatoArchivo" : ".wav" ,
            "Latitud" : "-39.81209355750812" ,
            "Longitud" : "-73.25050101755464" ,
            "Exterior" : "interior" ,
            "Usuario" : { "RUT" : "19.941.933-1" ,
                          "Nombre" : "Daniel" ,
                          "Apellido" : "Díaz"
                          },
            "Segmentos" : [{ "ID_segmento" : 1,
                             "FormatoSegmento" : ".wav" ,
                             "DuracionSegmento" : 7 ,
                             "Inicio" : 0,
                             "Fin" : 7,
                             "Etiquetas" : [ {
                                 "NombreFuente" : "rickroll" ,
                                 "Descripcion" : "Never gonna give you up",
                                 "IDAnalizador" : 1}]
                             }
                           ]
            }]

coleccion.insert_many(Archivos)
