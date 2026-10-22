from tkinter import Tk,Button,Label,Entry
import requests
ESP32_IP = "10.207.4.202"
window = Tk()
window.title('car           made by: parsa')
def up():
    requests.get(f"http://{ESP32_IP}/up")  
def down():
    requests.get(f"http://{ESP32_IP}/down")  
def left():
    requests.get(f"http://{ESP32_IP}/left")  
def right():
    requests.get(f"http://{ESP32_IP}/right")  
def stop():
    requests.get(f"http://{ESP32_IP}/stop")  
def checkWifi():
    requests.get(f"http://{ESP32_IP}/check_wifi")  
upBtn = Button(window,text= 'UP',command=up)
upBtn.pack()
downBtn = Button(window,text= 'DOWN',command=down)
downBtn.pack()
leftBtn = Button(window,text= 'LEFT',command=left)
leftBtn.pack()
rightBtn = Button(window,text= 'RIGHT',command=right)
rightBtn.pack()
stopBtn = Button(window,text= 'STOP',command=stop)
stopBtn.pack()
checkWifiBtn = Button(window,text= 'CHECK WIFI',command=checkWifi)
checkWifiBtn.pack()

window.geometry('400x300')
window.mainloop()