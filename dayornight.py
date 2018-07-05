from datetime import datetime as dt 

# check if its day or night

current = dt.now()

if dt(dt.now().year, dt.now().month, dt.now().day, 5) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
    print("Its day")
else:
    print("Its probably dark")