import time
a = 0 
while True:
    if a == 0:
        time.sleep(0.35)
        print(" O/")
        print("/|")
        print("/ \ ")
        a = 1
    if a == 1:
        time.sleep(0.35)
        print(" O__")
        print("/|")
        print("/ \ ")     
        a = 0
