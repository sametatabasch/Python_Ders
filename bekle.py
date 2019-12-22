import time,os,sys
def bekle():
    sys.stdout.write(".")
    time.sleep(.5)
    sys.stdout.write(".")
    time.sleep(.5)
    sys.stdout.write(".")
    time.sleep(.5)
    sys.stdout.write("\b")
    time.sleep(.5)
    sys.stdout.write("\b")
    time.sleep(.5)
    sys.stdout.write("\b")

bekle()