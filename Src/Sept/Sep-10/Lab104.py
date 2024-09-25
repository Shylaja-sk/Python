import os
try:
    file = open('example.txt','r')
    print(file.read()) #FileNotFoundError: [Errno 2] No such file or directory: 'example.txt'
except FileNotFoundError as fnfe:
    print("File not found, fix the path or create a file")
finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)

#example

import os
try:
    full_path = os.getcwd()
    full_path_file = full_path+"/example.txt"
    print(full_path_file)
    print(full_path)
    file = open(full_path+'example.txt','r')
    print(file.read()) #FileNotFoundError: [Errno 2] No such file or directory: 'example.txt'
except FileNotFoundError as fnfe:
    print("File not found, fix the path or create a file")
finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)



