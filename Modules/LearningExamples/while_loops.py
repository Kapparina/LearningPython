i = 1
while i <= 10:
    print("I am currently ", i)
    i += 1

x = 1
for x in range(20):
    if x <= 10:
        print("I am halfway done with this nonsense!")
        if x <= 15:
            print("I'm calling it early!")
            break
    else:
        print("I am confused!")
