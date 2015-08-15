import time
from Tkinter import *

#trackSecond = 0
#tracktenSecond = 0

GUI = Tk()

test = [0,0,":",0,0,":",0,0]

newlist = list()



    


stringtime1 = "00:00:00"
label = Label(GUI, text=stringtime1 ,bg = "black", fg="yellow")
label.config(width=16)
label.grid(row=0,column=0)


def main():
    return tenhourCounter()

def labelskeleton():
    global stringtime1
    label = Label(GUI, text=stringtime1 ,bg = "black", fg="yellow")
    label.config(width=16)
    label.grid(row=0,column=0)
    GUI.after(0050,labelskeleton)

def secondCounter():
    trackSecond = 0
    global stringtime1
    while trackSecond < 10:
        time.sleep(1)
        test[7] = trackSecond
        trackSecond += 1
        stringtime1 = ''.join(map(str,test))
        label.update()
    return trackSecond 


def tenSeconds():
    tracktenSecond = 0
    while tracktenSecond < 6:
        test[6] = tracktenSecond
        secondCounter()
        tracktenSecond += 1
    tracktenSecond = 0
    return tracktenSecond 

def minuteCounter():
    trackMinute = 0
    while trackMinute < 10:
        test[4] = trackMinute
        tenSeconds()
        trackMinute += 1
        test[4] = trackMinute
    trackMinute = 0
    return trackMinute

def tenminuteCounter():
    tracktenMinute = 0
    while tracktenMinute < 6:
        test[3] = tracktenMinute
        minuteCounter()
        tracktenMinute += 1
    tracktenMinute = 0
    return tracktenMinute

def hourCounter():
    trackHour = 0
    while trackHour < 10:
        test[1] = trackHour
        tenminuteCounter()
        trackHour += 1
        test[1] = trackHour
    trackHour = 0
    return trackHour

def tenhourCounter():
    tracktenHour = 0
    while tracktenHour < 3:
        test[0] = tracktenHour
        hourCounter()
        tracktenHour += 1
        test[0] = tracktenHour
    tracktenHour = 0
    return tracktenHour

GUI.after(100,labelskeleton)
GUI.after(200,main)
GUI.mainloop()
