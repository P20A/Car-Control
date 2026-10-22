import network
import socket
import time
from machine import Pin

in1 = Pin(5,Pin.OUT)
in2 = Pin(17,Pin.OUT)
in3 = Pin(16,Pin.OUT)
in4 = Pin(4,Pin.OUT)
led = Pin(25, Pin.OUT)

def leftWheelForward(in1,in2):
    in1.value(0)
    in2.value(1)
def leftWheelBackward(in1,in2):
    in1.value(1)
    in2.value(0)
def rightWheelForward(in3,in4):
    in3.value(1)
    in4.value(0)
def rightWheelBackward(in3,in4):
    in3.value(0)
    in4.value(1)
def carStop(in1,in2,in3,in4):
    in1.value(0)
    in2.value(0)
    in3.value(0)
    in4.value(0)
def led_on():
    led.value(1)
    print("LED ON")

def led_off():
    led.value(0)
    print("LED OFF")


# -------- WIFI --------
SSID = "Galaxy-S24-FE-5F36"
PASSWORD = "14426Parsa@"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    time.sleep(1)
led_on()
time.sleep(2)
led_off()
ip = wlan.ifconfig()[0]
print("ESP32 IP:", ip)

# -------- SERVER --------
addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)

print("Listening on http://", ip)

while True:
    client, addr = s.accept()
    request = client.recv(1024).decode()
    if "/check_wifi" in request:
        led_on()
        response = "LED ON"
        time.sleep(2)
        led_off()
    elif "/up" in request:
        leftWheelForward(in1,in2)
        rightWheelForward(in3,in4)
        response = "CAR UP"
    elif "/down" in request:
        leftWheelBackward(in1,in2)
        rightWheelBackward(in3,in4)
        response = "CAR DOWN"
    elif "/right" in request:
        leftWheelForward(in1,in2)
        rightWheelBackward(in3,in4)
        response = "CAR RIGHT"
    elif "/left" in request:
        leftWheelBackward(in1,in2)
        rightWheelForward(in3,in4)
        response = "CAR LEFT"
    elif "/stop" in request:
        carStop(in1,in2,in3,in4)
        response = "CAR STOP"
    else:
        response = "ESP32 OK"

    client.send("HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n")
    client.send(response)
    client.close()

