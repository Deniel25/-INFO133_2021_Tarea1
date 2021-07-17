from bson.binary import Binary
from bson import ObjectId
import pymongo, gridfs
from gridfs import GridFS
from pymongo import MongoClient

mongo = MongoClient("localhost")
baseDatos = mongo["fusaSound"]
coleccion = baseDatos["sonidos"]


modelFile = "wilhelm.wav"
with open(modelFile, "rb") as f:
    encoded = Binary(f.read())
coleccion.insert_one({"NombreAudio": modelFile, "archivo": encoded,
                      "description": "Wilhelm Scream",
                      "FechaArchivo": "30/06/2021"})

modelFile = "yoda.wav"
with open(modelFile, "rb") as f:
    encoded = Binary(f.read())
coleccion.insert_one({"NombreAudio": modelFile, "archivo": encoded,
                      "description": "Yoda Death",
                      "FechaArchivo": "01/07/2021"})

modelFile = "rickroll.wav"
with open(modelFile, "rb") as f:
    encoded = Binary(f.read())
coleccion.insert_one({"NombreAudio": modelFile, "archivo": encoded,
                      "description": "Rick Roll",
                      "FechaArchivo": "02/07/2021"})

modelFile = "tiger.wav"
with open(modelFile, "rb") as f:
    encoded = Binary(f.read())
coleccion.insert_one({"NombreAudio": modelFile, "archivo": encoded,
                      "description": "Tiger Roar",
                      "FechaArchivo": "03/07/2021"})
