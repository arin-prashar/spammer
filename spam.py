import pyautogui
import time
c,i=0,int(input("Input the number of times you want to send: "))
time.sleep(3)
while c<i:
    pyautogui.typewrite("L")
    pyautogui.press("enter")
    time.sleep(0.2)
    c=c+1
