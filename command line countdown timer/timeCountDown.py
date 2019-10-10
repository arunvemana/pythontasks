import os
import time
from win10toast import ToastNotifier
toaster = ToastNotifier()
print("Enter the choice \n 1. Hours \n 2. Minutes \n 3. seconds")
print("Choose time input format!\n")
userinput = input(">>")
os.system('cls || clear')
print("Provide the Time in given choice format")
time_input = int(input(">>"))
if userinput == "1":
    h = time_input
    m = h * 60
    s = m * 60
elif userinput == "2":
    m = time_input
    s = m * 60
    h = int(m/60)
elif userinput =="3":
    s = time_input
    m = int(s/60)
    h = int(m/60)
else:
    print("provide right choice")


os.system('cls || clear')
os.system("mode con lines=5")
while s >=0:
    time_left = str(h).zfill(2) + ":" +str(m).zfill(2)+ ":" + str(s).zfill(2)
    toaster.s
    toaster.show_toast("Demo notification",
                       time_left,
                       duration=1)
    print(time_left + "\r",end="")
    if s>0:
        time.sleep(1)
    s -=1
os.system("mode con lines=20")
