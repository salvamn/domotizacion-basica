# Domotización de un Dormitorio 
El proyecto permite obtener la temperatura, humedad y luz de un dormitorio, para luego enviarlos al serial de un arduino en un formato de tipo Json, a continuacion se tomaran esos datos y seran enviados a una base de datos (Firebase) para  ser pintados en una interfaz grafica de escritorio.
       
Tambien aparte de obtener valores de distintos sensores podremos encender y apagar un led, lampara y mover un pequeño servomotor.

( proximamente parte dos con nodmcu )

<img width="50%" src="https://user-images.githubusercontent.com/61121429/148105862-d04da7e5-f28a-4ccb-bfea-98e1d8ea59a9.PNG"></img>


## Materiales

<div style="display: inline-flex; flex-direction: row; justify-content: center;">
  <img width="15%" src="https://user-images.githubusercontent.com/61121429/148106040-81f7d0e5-5e67-449f-a289-d5fc82380ffd.png"></img>
  <img width="15%" src="https://user-images.githubusercontent.com/61121429/148106330-e40e0831-607d-4042-8ce5-e5dae3dee07f.png"></img>
  <img width="15%" src="https://user-images.githubusercontent.com/61121429/148106333-b3e4b9fa-faf9-4e36-a9ec-5bf989a46f72.png"></img>
  <img width="15%" src="https://user-images.githubusercontent.com/61121429/148106347-acd9c644-7932-4d73-a979-b16e25429524.png"></img>
  <img width="15%" src="https://user-images.githubusercontent.com/61121429/148106338-65715dcf-00da-4ee1-a1de-d33a96543d88.png"></img>
  <img width="15%" src="https://user-images.githubusercontent.com/61121429/148106327-f2a20ff9-bde4-46db-8e37-9f645e60f46b.png"></img>
</div>


## Librerias
- <a href="https://docs.python.org/es/3/library/tk.html">Tkinter</a>
- <a href="https://pillow.readthedocs.io/en/stable/">Pillow</a>
- <a href="https://docs.python.org/es/3.8/library/threading.html">Threading</a>
- <a href="https://pyserial.readthedocs.io/en/latest/pyserial.html">Serial</a>
- <a href="https://docs.python.org/es/3/library/time.html">Time</a>
- <a href="https://docs.python.org/es/3/library/json.html">Json</a>
- <a href="http://ozgur.github.io/python-firebase/">Python Firebase</a>
- <a href="https://github.com/adafruit/DHT-sensor-library">DHT11</a>
- <a href="https://github.com/arduino-libraries/Servo">Servo</a>
- <a href="https://arduinojson.org/">Arduino Json</a>
