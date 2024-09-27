import os
#operating system -  help to work wth files, OS and path related to OS

print(os.name) #nt in windows
if os.name == 'posix':
    print("using mac")
else:
    print("using windows")

#print(os.getcwd())
#os.mkdir('new_directory')

print(os.listdir('.')) #--['example.txt', 'Lab100.py', 'Lab101.py', 'Lab102.py', 'Lab103.py', 'Lab104.py', 'Lab105.py', 'new_directory', '__init__.py']
for file in os.listdir('.'): #this is also possible
    print(file)

#os.remove('example.txt')
#os.remove('new_directory')

print(os.path.exists('example.txt'))
print(os.path.isfile('example.txt'))
print(os.path.isdir('new_directory'))


