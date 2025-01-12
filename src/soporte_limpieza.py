
import pandas as pd
def convertir_comas_a_puntos(valor):
    """
    Convierte comas en puntos y devuelve el número como float.
    Si el valor no es válido, devuelve NaN.
    """
    try:
        return float(valor.replace(",", "."))
    except (ValueError):
        return np.nan
    




def exctraccion_csv(lisat_de_directorios):
    """
    crea un diccionario a partir de los archivos csv
    """
    diccionario_dfs = {}
    for i in lisat_de_directorios:
        nombre_df = str(i.replace(".","-").split("-")[1]) + "df"
        diccionario_dfs [nombre_df] = pd.read_csv(f"../datos/{i}", encoding='latin-1', sep=';', index_col=0)
    return diccionario_dfs