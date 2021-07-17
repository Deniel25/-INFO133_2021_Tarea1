import folium
from pymongo import MongoClient

mongo = MongoClient("localhost")
baseDatos = mongo["fusaSound"]
coleccion = baseDatos["sounds"]
mapaCity = folium.Map(location =[-39.823641, -73.226158], zoom_start = 14)

for i in coleccion.find():
    lat = i["Latitud"]
    long = i["Longitud"]
    date = i["FechaGrabacion"]
    folium.Marker([lat, long], popup = date, tooltip = date).add_to(mapaCity)

#Cambiar direccion de guardado
mapaCity.save("C:\\Users\\XXXXXX\\Desktop\\MONGO\\map.html")

print("Listo")
