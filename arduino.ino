#include <Servo.h>
#include <ArduinoJson.h>
#include <DHT.h>

StaticJsonDocument<200> doc;
StaticJsonDocument<200> docObjetos;

const int dhtPin = 12;
const int ledRojoPin = 11;
const int fotoPin = A0;
const int servoPin = 9;
const int rgbAzul = 8;
const int rgbVerde = 7;
const int rgbRojo = 6;
String dato_recibido;

Servo servo;
DHT dht(dhtPin, DHT11);

// millis devuelve el tiempo transcurrido desde el inicio del programa
// unsigned solo devuelve valores positivos
unsigned long tiempo = millis();
const long intervalo = 60000; // 1 minuto

void setup()
{
    Serial.begin(9600);
    dht.begin();
    servo.attach(9); // Vinculamos el servo al pin 9
    servo.write(0);
    pinMode(ledRojoPin, OUTPUT);
    pinMode(rgbAzul, OUTPUT);
    pinMode(rgbVerde, OUTPUT);
    pinMode(rgbRojo, OUTPUT);
    pinMode(fotoPin, INPUT);
}

void loop()
{
    // available() devuelve el número de bytes disponibles para leer
    if(Serial.available() > 0)
    {
        // Leemos todos los bytes disponibles en el buffer
        dato_recibido = Serial.readString();
        // deserializationerror devuelve true si hubo un error
        DeserializationError error = deserializeJson(docObjetos, dato_recibido);
        int estado_lampara = docObjetos["lampara"];
        int estado_led = docObjetos["led"];
        int estado_servo = docObjetos["servo"];

   
        if(estado_led == 1)
        {
            digitalWrite(ledRojoPin, HIGH);
        }

        else if(estado_led == 0)
        {
            digitalWrite(ledRojoPin, LOW);
        }

        if(estado_lampara == 1){
            
        }


        servo.write(estado_servo);
  

    }


    // Si el tiempo transcurrido es mayor o igual al intervalo, se ejecuta la función
    if(millis() - tiempo >= intervalo)
    {
        datosSensores();
        // Se actualiza el tiempo
        tiempo = millis();
    }
}


void datosSensores(){
    float h = dht.readHumidity(); // Leemos la humedad 
    float t = dht.readTemperature(); // Leemos la temperatura
    int luz = analogRead(fotoPin); // Leemos la luz

    // verificamos que la humedad y la temperatura no sean nulos
    if (isnan(h) || isnan(t)) {
        return;
    }

    // Se crean las claves para los datos en el documento
    doc["humedad"] = h;
    doc["temperatura"] = t;
    doc["luz"] = luz;

    // Se imprime el JSON en la consola
    serializeJson(doc, Serial);
    Serial.println();
}


void combinarColoresRGB(){

}