import time 

def countdown_timer(seconds):
    
    while seconds:
        mins,seconds=divmod(seconds, 60)
        timer="{:02d}:{:02d}".format(mins,seconds)
        print(timer , end="\r")
        time.sleep(1)
        seconds -= 1
print("Timer completed")
        
second=input("Enter the time in seconds: ")

countdown_timer(int(second))
