#How to write to a file

with open('Testdata.txt','r') as file:
    lines = file.readlines()
    for line in lines:
        print(line,end=" ")

with open('Testdata.txt','a') as file:
    file.write("Hi hello")