import playsound
from pymongo import MongoClient

mongo = MongoClient("localhost")
baseDatos = mongo["fusaSound"]
coleccion = baseDatos["sonidos"]
b = True

while(b):
    date = input("Hoola\nIngrese la fecha de grabacion de su archivo: ")
    for i in coleccion.find():
        if(i["FechaArchivo"] == date):
            name = i["NombreAudio"]

    nA = name
    name = "output" + name
    data = coleccion.find_one({"FechaArchivo": date})
        
    with open(name, "wb") as f:
        f.write(data["archivo"])

    print("Reproduciendo:",nA)
    playsound.playsound(name)
    print("Fin")


    ans = input("Reproducir otro? (S/N): ")
    if(ans == "N" or ans == "n"):
        print("Chaoo")
        b = False


