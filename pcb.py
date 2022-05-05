import datetime
import time
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


while True:
    ctime = datetime.datetime.now().strftime("%H:%M:%S")
    print(ctime)
    time.sleep(1)
    cls()
