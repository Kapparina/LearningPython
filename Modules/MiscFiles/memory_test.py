from datetime import datetime
from datetime import timedelta

memory1 = "*" * 1024**3

start = datetime.now()

j = 0

while (datetime.now() - start) < timedelta(minutes=1):
    j += 1

memory2 = "*" * 1024**3

while (datetime.now() - start) < timedelta(minutes=2):
    j += 1