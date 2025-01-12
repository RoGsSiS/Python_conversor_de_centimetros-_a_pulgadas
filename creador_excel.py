
import pandas as pd

# Dataframe en la información básica con el nombre de las piezas y centímetros para poder armar el excel

data = {
    "Piezas" : ["Pata", "Tablero", "Puerta", "Estante", "Panel Lateral"],
    "Centimetros": [40,120,60,30,180]
}

df = pd.DataFrame(data)

# Guardar el DataFRame en un archivo Excel

df.to_excel("muebles_medidas.xlsx", index=False)