import time
from win10toast import *

def toast(title, message, time, icon):
    toaster = ToastNotifier()
    #toaster.show_toast(title, notification message, duration, icon)
    toaster.show_toast(title, message, duration=time, icon_path=icon)

t = input("Hi ! please input any positive integral number Here. for timer's time \n >>>> ")
t = int(t)

while True: 
    print("timer started.")

    time.sleep(t);

    print("times up")
    toast("timer", "times up", 20, "DarkEyes.ico")