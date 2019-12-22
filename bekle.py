import time,sys
def bekle():
    for i in range(3):
        sys.stdout.write(".")
        time.sleep(.5)
    for i in range(3):
        sys.stdout.write("\b")
        time.sleep(.5)
bekle()