from tkinter import messagebox
from typing import Union
import serial
import serial.tools.list_ports

def conexion():
    """ Funcion que permite realizar una conexion serial con el arduino.

    return:
    -------
        Serial: si la conexion fue exitosa, objeto serial.
        False: en caso de no poder realizar la conexion.
    
    """
    ser = None

    try:
        ser = serial.Serial(buscar_puerto(), 9600)

        if(ser.is_open):
            ser.close()
            return ser

        elif(ser.is_open == False):
            print("No se pudo abrir el puerto")
            messagebox.showinfo("Conexion", "Conexion fallida revise la conexion del arduino")
            ser.close()
            
    except TypeError as e:
        print(e)





def buscar_puerto() -> Union[str, None]:
    """ Funcion que permite buscar los puertos disponibles en el sistema.
    
    return:
    -------
        str: nombre del puerto `COM3`.
        None: en caso de no encontrar ningun puerto.
        
    """

    puertos = serial.tools.list_ports.comports()

    for puerto in puertos:
        if(puerto is None):
            print("No se encontro ningun puerto")
            return None
        # print(puerto.name)
        return puerto.name
    

# conexion()
# print(buscar_puerto())