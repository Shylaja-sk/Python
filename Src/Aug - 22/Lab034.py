# Break - based on the condotion exit the loop


for i in range(0, 5):
    print(i)

for i in range(0, 5):
    print(i)
    if i == 3:
        break

for i in range(0, 10):
    print(i, end="-")
    if i == 5:
        break

for i in range(10):
    print(i)  # this is also possible - start and step is optional

for i in range(0, 10, 1):
    if i == 3:
        print(i)
    else:
        print("No o/p")

for i in range(0, 10, 1):
    if i == 3:
        print(i)
    else:
        pass

for i in range(0, 10, 1):
    if i == 5 or i==6:
        print(i)
    else:
        pass