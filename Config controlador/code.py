# Based on CircuitPython AnalogIn Demo
# Preparado por Frander Hernández
# 12/01/2021

####################################################################################
# Declaración de librerías
####################################################################################
import time
import digitalio
import board
from analogio import AnalogIn

####################################################################################
# Declaración de pines
####################################################################################
# Declara el uso del LED built-in (integrado) en el Feather M0
# Pin #13
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

# Pines digitales para utilizarlos como alimentación (ON/OFF)
power1 = digitalio.DigitalInOut(board.D12)
power1.direction = digitalio.Direction.OUTPUT
power2 = digitalio.DigitalInOut(board.D11)
power2.direction = digitalio.Direction.OUTPUT
power3 = digitalio.DigitalInOut(board.D10)
power3.direction = digitalio.Direction.OUTPUT
power5 = digitalio.DigitalInOut(board.D6)
power5.direction = digitalio.Direction.OUTPUT
power4 = digitalio.DigitalInOut(board.D5)
power4.direction = digitalio.Direction.OUTPUT


# Pines para lectura analógica (valores de 0 a 65535)
analog_in1 = AnalogIn(board.A1)
analog_in2 = AnalogIn(board.A2)
analog_in3 = AnalogIn(board.A3)
analog_in4 = AnalogIn(board.A4)
analog_in5 = AnalogIn(board.A5)

# Pin para lectura analógica del pin A7 (BATTERY) (valores de 0 a 65535)
analog_inVAT = AnalogIn(board.VOLTAGE_MONITOR)

####################################################################################
# Funciones
####################################################################################
#Colecta el valor analógico leído en el Pin (0 a 65535)
def get_lecture(pin):
    return pin.value

# Colecta el valor analógico leído en el Pin (0 a 65535) y lo transforma a voltaje
def get_voltage(pin):
    return (pin.value * 3.3) / 65536

# Colecta el valor analógico de la batería leído en el Pin A7 (0 a 65535) y lo transforma a voltaje
def get_VAT(pin):
    return (pin.value * 2 * 3.3) / 65536

# Función para el LED indicador de estatus: recibe el pin, el delay entre parpadeos
# y las veces que parpadea.
def blink(led, delay, veces):
    for i in range(0,veces):
        led.value = True
        time.sleep(delay)
        led.value = False
        time.sleep(delay)

# Mapea las lecturas a un intervalo de 0% a 100% de humedad
def mapeo_lineal(value, fromLow, fromHigh, toLow, toHigh):
    m = (toHigh-toLow)/(fromHigh-fromLow)
    b = toHigh-m*fromHigh
    result = m*value+b
    return round(result, 2)

####################################################################################
# Ciclo infinito
####################################################################################

while True:
    # Enciende los pines digitales (HIGH)
    power1.value = True
    power2.value = True
    power3.value = True
    power4.value = True
    power5.value = True
    # Delay para estabilizar la lectura
    time.sleep(1)
    print("Sensor 1 Lectura:", analog_in1.value)
    #print("Sensor 1 Voltaje Humedad:", get_voltage(analog_in1))

    print("Sensor 2 Lectura:", analog_in2.value)
    #print("Sensor 2 Voltaje Humedad:", get_voltage(analog_in2))

    print("Sensor 3 Lectura:", analog_in3.value)
    #print("Sensor 3 Voltaje Humedad:", get_voltage(analog_in3))

    print("Sensor 4 Lectura:", analog_in4.value)
    #print("Sensor 4 Voltaje Humedad:", get_voltage(analog_in4))

    print("Sensor 5 Lectura:", analog_in5.value)
    #print("Sensor 5 Voltaje Humedad:", get_voltage(analog_in5))

    print("Nivel de bateria:", get_VAT(analog_inVAT))
    # Apaga los pines digitales (LOW)
    power1.value = False
    power2.value = False
    power3.value = False
    power4.value = False
    power5.value = False
    blink(led, 0.1, 3)
    # Lee datos cada 5 segundos (1 s pines HIGH + 4 s delay)
    time.sleep(4)

    print(".....................Lectura.....................")
