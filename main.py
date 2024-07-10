import pandas as pd
import folium
import json

# Datos de ejemplo
with open("data.json", 'r') as file:
    data : dict = json.load(file)

df : pd.DataFrame = pd.DataFrame(data)

# Crear un mapa
map : folium.Map = folium.Map(location=[20, 0], zoom_start=2)

# Añadir marcadores para cada evento
for i, row in df.iterrows():
    folium.Marker(
        location=[row['Latitud'], row['Longitud']],
        popup=f"{row['Evento']} ({row['Año']}): {row['Descripcion']}",
        icon=folium.Icon(color='red' if row['Año'] < 1950 else 'blue')
    ).add_to(map)

# Guardar el mapa en un archivo HTML
map.save('index.html')
