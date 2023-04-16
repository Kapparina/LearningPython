import time
from datetime import datetime
import pytz

while True:
    UP = "\033[1A"
    CLEAR = "\x1b[2K"
    time_ny = pytz.timezone("America/New_York")
    print(datetime.now().strftime("%H:%M:%S"), end="\r")
    print()
    print(f"The time in New York is: ", datetime.now(time_ny).strftime("%H:%M:%S"), end="\r")
    print()
    time.sleep(1)
    # print(UP, end=CLEAR)

# while True:
#     now = datetime.now()
#     print(now.strftime("%H:%M:%S"), end="\r", flush=True)
#     time.sleep(1)
