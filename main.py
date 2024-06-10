from typing import Any
import pandas as pd
import folium

# Datos de ejemplo
data : dict[str, list[str | int]] = {
    'Evento': ['Holocausto', 'Genocidio de Ruanda', 'Guerra Civil Española'],
    'Año': [1945, 1994, 1939],
    'Latitud': [52.52, -1.94, 40.42],
    'Longitud': [13.40, 29.87, -3.70],
    'Descripcion': [
        'Genocidio llevado a cabo por el régimen nazi durante la Segunda Guerra Mundial.',
        'Asesinato masivo de tutsis y hutus moderados por parte de los hutus extremistas.',
        'Conflicto armado entre republicanos y nacionalistas en España.'
    ]
}

df : pd.DataFrame = pd.DataFrame(data)

# Crear un mapa
map : Any = folium.Map(location=[20, 0], zoom_start=2)

# Añadir marcadores para cada evento
for i, row in df.iterrows():
    folium.Marker(
        location=[row['Latitud'], row['Longitud']],
        popup=f"{row['Evento']} ({row['Año']}): {row['Descripcion']}",
        icon=folium.Icon(color='red' if row['Año'] < 1950 else 'blue')
    ).add_to(map)

# Guardar el mapa en un archivo HTML
map.save('mapa.html')
