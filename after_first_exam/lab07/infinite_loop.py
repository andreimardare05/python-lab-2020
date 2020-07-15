import sys
import datetime
import random
import time

start = datetime.datetime.now()
while True:
    before = datetime.datetime.now().second
    x = random.randint(int(sys.argv[1]),int(sys.argv[2]))
    print(f'{x} seconds ... ')
    time.sleep(x)
    print(int((datetime.datetime.now() - start).total_seconds()/60))

    