from firebase import firebase
from typing import Union

db = firebase.FirebaseApplication("https://certamen-final-iot-default-rtdb.firebaseio.com/", None)

db_dormitorio = firebase.FirebaseApplication("https://domotizacion-dormitorio-default-rtdb.firebaseio.com/", None)

def obtener_datos() -> dict:
    """ Obtiene los datos del sub nodo `DHT11`, y los retorna en un diccionario.
    
    Returns:
    --------
        dict: Diccionario con los datos del sub nodo `DHT11`.\n
    
    """
    try:
        return db_dormitorio.get('/' ,'datos-sensores') 
    except:
        return {"temperatura": None, "humedad": None, "luz": None}



def put_datos_sensores(datos: dict):
    """"""

    db_dormitorio.put("/", "datos-sensores", datos)
    


def put_lampara(datos: dict) -> Union[dict, None]:
    """ Actualiza el nodo `estado` de la base de datos
    
    parameters:
    -----------
        datos: Diccionario con el nuevo estado para la lampara.\n

    
    returns:
    --------
        `Dict`: si los dato se actualizaron\n
        `None`: si los datos no se actualizaron\n
        `False`: si el tipo de dato recibido no es un diccionario\n
    

    example:
    --------
        Enviar un diccionario con el estado de la lampara\n
        de la siguiente forma:\n
        1 = Encendido\n
        0 = Apagado\n
        `{"estado": "1"}`\n

    """

    tipo_dato = True if type(datos) == dict else False
    resultado = None

    if tipo_dato:
        resultado = db_dormitorio.put("/", "Lampara", datos)

        return resultado

    return tipo_dato, resultado


def obtener_estado_lampara():
    """ Obtiene el estado de la lampara del nodo `estado` de la base de datos """

    resultado = db_dormitorio.get("/", "Lampara")

    return resultado



# print(put_lampara({"estado":"ON"}))
# print(put_lampara(2))
# print(obtener_estado_lampara())
# print(obtener_datos().keys())
# print(obtener_datos())