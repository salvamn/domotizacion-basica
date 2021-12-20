from tkinter import Button, Label, messagebox
from tkinter.constants import E
from db.conexion_db import obtener_datos
from db.conexion_db import put_datos_sensores
from arduino import conexion_serial as cnx
import time
import json



tiempo_de_espera = 300
estado_ventana = True
estados = {"led" : 0, "lampara" : 0, "servo" : 0}

ser = cnx.conexion()
ser.open()


def mostrar_datos(temperatura: Label, humedad: Label, luz: Label):
    """
    Esta funcion permite mostrar los datos en la ventana principal, para ello se utiliza la funcion\n
    `obtener_datos` que obtiene los datos de la base de datos y luego los pinta en los `Label`\n
    correspondientes de la libreria tkinter.

    args:
    -----
        temperatura: Label
        humedad: Label
        luz: Label
    
    """
    datos = obtener_datos()
    temp = datos["temperatura"]
    hume = datos["humedad"]
    iluminacion = datos["luz"]
    print("-----------------------------------------")
    print("Datos de la base de datos:\n", datos)
    print("-----------------------------------------")
    
    if(temp == None):
        temperatura.config(fg="grey")
    elif(temp >= 28):
        temperatura.config(fg="red")
    elif(temp >= 21 and temp <= 27):
        temperatura.config(fg="gold")
    elif(temp >= 15 and temp <= 20):
        temperatura.config(fg="green")
    elif(temp <= 14):
        temperatura.config(fg="blue")
        

    if(hume == None):
        humedad.config(fg="grey")
    elif(hume >= 30 and hume <= 50):
        humedad.config(fg="green")
    elif(hume >= 51 and hume <= 70):
        humedad.config(fg="gold")
    elif(hume >= 71 and hume <= 90):
        humedad.config(fg="red")

    
    luz_maxima = 50
    obtener_porcentaje_luz = (iluminacion * 100) / luz_maxima

    if(iluminacion == None):
        luz.config(fg="grey")
    elif(iluminacion >= 30):
        luz.config(fg="green")
    elif(iluminacion >= 11 and iluminacion <= 30):
        luz.config(fg="gold")
    elif(iluminacion >= 1 and iluminacion <= 10):
        luz.config(fg="red")

    temperatura["text"] = str(temp) + "°C"
    humedad["text"] = str(hume) + "%"
    luz["text"] = str(obtener_porcentaje_luz) + "%"




def encender_lampara(estado_boton: str, btn_off_lamp: Button, btn_on_lamp: Button):
    """
    La funcion lee un nodo de firebase llamado `Lampara` este nodo devuelve un\n
    `dict` con un valor de 1 o 0, si el valor devuelto es 1 la lampara esta\n
    encendida y procede a desactivar el `btnOn`, para apagar la lampara se\n
    debe cambiar el valor del nodo a 0 y el estado del boton a "ON".

    args:
    -----
        estado_boton: str
        btn_off_lamp: Button
        btn_on_lamp: Button
    
    example:
    --------
        encender_lampara("on", btnOn, btnOff)

    """

    

    try:
        
        # ser.open()

        if(estado_boton == "on"):
            if(btn_off_lamp["state"] == "disabled"):
                btn_off_lamp["state"] = "normal"
                btn_off_lamp["bg"] = "red"
            
            estados["lampara"] = 1
            json.dumps(estados)
            ser.write(f"{estados}".encode("utf-8"))
            # ser.write(b'1')

            btn_on_lamp["state"] = "disabled"
            btn_on_lamp["bg"] = "gray"
            messagebox.showinfo("Lampara", "Lampara encendida")
    
        if(estado_boton == "off"):
            if(btn_on_lamp["state"] == "disabled"):
                btn_on_lamp["state"] = "normal"
                btn_on_lamp["bg"] = "#3ea6ff"

            estados["lampara"] = 0
            json.dumps(estados)
            ser.write(f"{estados}".encode("utf-8"))
            # ser.write(b'0')

            btn_off_lamp["state"] = "disabled"
            btn_off_lamp["bg"] = "gray"
            messagebox.showinfo("Lampara", "Lampara apagada")

    except Exception as e:
        print("encender_lampara: Error --> ", e)
        # print("Error al conectar con el arduino")

    
def encender_led(estado_led: str, btn_led_on: Button, btn_led_off: Button):
    """"""

    try:

        if(estado_led == "on"):
            if(btn_led_off["state"] == "disabled"):
                btn_led_off["state"] = "normal"
                btn_led_off["bg"] = "red"

            estados["led"] = 1
            json.dumps(estados)
            ser.write(f"{estados}".encode("utf-8"))
            # print(b""+estados)
        
            btn_led_on["state"] = "disabled"
            btn_led_on["bg"] = "gray"
            messagebox.showinfo("Led", "Led encendido")
        
        if(estado_led == "off"):
            if(btn_led_on["state"] == "disabled"):
                btn_led_on["state"] = "normal"
                btn_led_on["bg"] = "#3ea6ff"

            estados["led"] = 0
            json.dumps(estados)
            ser.write(f"{estados}".encode("utf-8"))

            btn_led_off["state"] = "disabled"
            btn_led_off["bg"] = "gray"
            messagebox.showinfo("Led", "Led apagado")

    except Exception as e:
        print("encender_led: Error --> ", e)



def mover_servo(mover: int):
    """"""

    estados["servo"] = mover

    json.dumps(estados)

    ser.write(f"{estados}".encode("utf-8"))




def hilo_de_datos(estado_ventana: str, temperatura: Label, humedad: Label, luz: Label):
    """
    Esta funcion esta hecha para que se ejecute en un hilo aparte, para que\n
    se pueda actualizar la informacion de los datos en la ventana principal\n
    de manera automatica.

    args:
    -----
        estado_ventana: str
        temperatura: Label
        humedad: Label
        luz: Label

    
    """
    print("Solicitando datos de la base de datos...")
    # bandera = True

    while True:
        print("Estado de la ventana: ", estado_ventana)
        mostrar_datos(temperatura, humedad, luz)
        time.sleep(tiempo_de_espera)




def leer_monitor_serie():
    """
    Esta funcion esta hecha para leer los datos del serial, estos datos son\n
    enviados por el arduino y se guardan en la base de datos, la funcion se\n
    corre en un hilo aparte para que se pueda actualizar la informacion.

    """
    print("Leyendo datos del monitor serie...")

    try:
        # ser = cnx.conexion()
        # ser.open()

        while True:
            datos_tipo_bytes = ser.readline().decode("utf-8")
            datos_deserializados = json.loads(datos_tipo_bytes)
            print("----------------------------------")
            print("Datos del monitor:\n",datos_deserializados)
            print("----------------------------------")

            put_datos_sensores(datos_deserializados)

    except Exception as e:
        print("leer_monitor_serie: Error --> ", e)

   


def hora_actual(entry_hora: Label):
    """
    Funcion que permite obtener la hora actual y mostrarla en un `Label`\n
    tambien esta hecha para que se ejecute en un hilo aparte.
    
    args:
    -----
        entry_hora: Label

    """
    while True:
        fecha = time.localtime()
        hora = time.strftime("%H:%M", fecha)
        # entry_hora.insert(0, hora)
        entry_hora["text"] = hora

        time.sleep(60)




def salir(ventana):
    respuesta = messagebox.askquestion("Salir", "¿Desea salir del programa?")

    if(respuesta == "yes"):
        ser.close()
        ventana.destroy()



# leer_monitor_serie()
