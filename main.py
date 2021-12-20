from tkinter import *
from PIL import Image, ImageTk
from funciones import encender_lampara
from funciones import encender_led
from funciones import mover_servo
from funciones import salir
from funciones import hilo_de_datos
from funciones import leer_monitor_serie
from funciones import hora_actual
# from funciones import estados
from funciones import estado_ventana
import threading 


#------------------------------------------------------------- INTERFAZ -------------------------------------------------------------
ventana = Tk()
ventana.title("Administrador Dormitorio")
ventana.geometry("600x400")
ventana.config(bg="white")
ventana.resizable(0, 0)
ventana.iconbitmap(r"ico/icono.ico")


frame_principal = Frame(ventana, width=600, height=50, bg="#f1f1f1")
frame_principal.pack()

Label(frame_principal, text="Monitor de Control", font=("Arial", 18), bg="#f1f1f1", fg="black").place(x=220, y=7)
monitoreo = Label(frame_principal, bg="#f1f1f1", fg="black")
img_monitoreo = ImageTk.PhotoImage(Image.open(r"ico/monitoreo.png"))
monitoreo["image"] = img_monitoreo
monitoreo.place(x=170, y=2)



#--------------------------- Frame Switches ---------------------------------------------------------
frame_list_box = Frame(ventana, width=200, height=330, bg="white", border=1, highlightbackground="#f1f1f1", highlightthickness=1)
frame_list_box.place(x=5, y=60)

Label(frame_list_box, text="Objetos", font=("Arial bold", 15), bg="white", fg="black").place(x=65, y=5)

# lampara
img_lamp = Label(frame_list_box, bg="white")
imagen_lampara = ImageTk.PhotoImage(Image.open(r"ico/lamp.png"))
img_lamp["image"] = imagen_lampara
img_lamp.place(x=5, y=50)

btn_on_lamp = Button(frame_list_box, text="ON", font=("Arial", 12), bg="#3ea6ff", fg="white", bd=0, command=lambda: encender_lampara("on", btn_off_lamp, btn_on_lamp))
btn_on_lamp.place(x=70, y=60)
btn_off_lamp = Button(frame_list_box, text="OFF", font=("Arial", 12), bg="red", fg="white", bd=0, command=lambda: encender_lampara("off", btn_off_lamp, btn_on_lamp))
btn_off_lamp.place(x=120, y=60)

# led
img_led = Label(frame_list_box, bg="white")
imagen_led = ImageTk.PhotoImage(Image.open(r"ico/led.png"))
img_led["image"] = imagen_led
img_led.place(x=5, y=120)

btn_on_led = Button(frame_list_box, text="ON", font=("Arial", 12), bg="#3ea6ff", fg="white", bd=0, command=lambda: encender_led("on", btn_on_led, btn_off_led))
btn_on_led.place(x=70, y=130)
btn_off_led = Button(frame_list_box, text="OFF", font=("Arial", 12), bg="red", fg="white", bd=0, command=lambda: encender_led("off", btn_on_led, btn_off_led))
btn_off_led.place(x=120, y=130)

# laser
img_laser = Label(frame_list_box, bg="white")
imagen_laser = ImageTk.PhotoImage(Image.open(r"ico/servomotor.png"))
img_laser["image"] = imagen_laser
img_laser.place(x=10, y=180)

# btn_on_laser = Button(frame_list_box, text="ON", font=("Arial", 12), bg="#3ea6ff", fg="white", bd=0)
# btn_on_laser.place(x=70, y=190)
# btn_off_laser = Button(frame_list_box, text="OFF", font=("Arial", 12), bg="red", fg="white", bd=0)
# btn_off_laser.place(x=120, y=190)

caja_servo = Entry(frame_list_box, width=3, font=("Arial", 12), bg="white", fg="black")
caja_servo.place(x=70, y=190)
Button(frame_list_box,
  text="Mover",
  font=("Arial", 12),
  bg="#3ea6ff",
  fg="white",
  bd=0,
  command=lambda: mover_servo(caja_servo.get())).place(x=120, y=190)




#---------------------------- Frame Datos ------------------------------------------------------------

frame_contenedor_datos = Frame(ventana, width=380, height=330, bg="white", border=1, highlightbackground="#f1f1f1", highlightthickness=1)
frame_contenedor_datos.place(x=210, y=60)

Label(frame_contenedor_datos, text="Datos", font=("Arial", 15), bg="white", fg="black").place(x=140, y=5)

img_temperatura = Label(frame_contenedor_datos, bg="white", fg="black")
img_temp = ImageTk.PhotoImage(Image.open(r"ico/temperatura.png"))
img_temperatura["image"] = img_temp
img_temperatura.place(x=20, y=40)
Label(frame_contenedor_datos, text="Temperatura", font=("Arial bold", 10), bg="white", fg="black").place(x=5, y=90)
temperatura =Label(frame_contenedor_datos, text="None", font=("Arial", 10), bg="white", fg="black")
temperatura.place(x=30, y=110)

img_humedad = Label(frame_contenedor_datos, bg="white", fg="black")
img_hum = ImageTk.PhotoImage(Image.open(r"ico/humedad.png"))
img_humedad["image"] = img_hum
img_humedad.place(x=170, y=40)
Label(frame_contenedor_datos, text="Humedad", font=("Arial bold", 10), bg="white", fg="black").place(x=155, y=90)
humedad = Label(frame_contenedor_datos, text="None", font=("Arial", 10), bg="white", fg="black")
humedad.place(x=170, y=110)

img_luz = Label(frame_contenedor_datos, bg="white", fg="black")
img_luz_img = ImageTk.PhotoImage(Image.open(r"ico/luz.png"))
img_luz["image"] = img_luz_img
img_luz.place(x=300, y=40)
Label(frame_contenedor_datos, text="Luz", font=("Arial bold", 10), bg="white", fg="black").place(x=312, y=90)
luz = Label(frame_contenedor_datos, text="None", font=("Arial", 10), bg="white", fg="black")
luz.place(x=310, y=110)

reloj = Label(frame_contenedor_datos, width=5, font=("Arial bold", 20), bg="black", fg="green", justify="center", relief="sunken")  
# reloj.insert(0, "12:00")
reloj.place(x=150, y=280)


ventana.protocol("WM_DELETE_WINDOW", lambda: salir(ventana))


if __name__ == '__main__':
    hilo = threading.Thread(target=leer_monitor_serie)
    hilo.daemon = True
    hilo.start()
    hilo1 = threading.Thread(target=lambda:hilo_de_datos(estado_ventana, temperatura, humedad, luz), name="hilo_de_datos")
    hilo1.daemon = True
    hilo1.start()
    hilo2 = threading.Thread(target=lambda:hora_actual(reloj), name="hilo_de_reloj")
    hilo2.daemon = True
    hilo2.start()
    ventana.mainloop()
    estado_ventana = False
  