import time
def countDown_timer(seconds):
    while seconds > 0:
        mins = int(seconds/60)
        secs = int(seconds%60)
        if(mins < 10):
            mins = "0" + str(mins)
        if(secs < 10):
            secs = "0" + str(secs)
        timer = f'{mins}:{secs}'
        print(timer,end = '\r')
        time.sleep(1)
        seconds -= 1
    print("Time is Up!")
seconds = int(input("Enter the end of the time in seconds: "))
countDown_timer(seconds)

