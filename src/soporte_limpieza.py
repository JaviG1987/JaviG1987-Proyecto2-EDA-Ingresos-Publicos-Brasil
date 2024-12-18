
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
    
