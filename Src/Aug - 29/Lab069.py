#Dict -- Key value combination - it is unordered collection

student_info = {"name":"Shylaja",
                "age" : "80",
                "age" : "81", #it will take the latest
                "Place" : {"Bangalore","Karnataka"}
                }

print(student_info)
print(student_info["name"])
print(student_info["age"])
print(student_info["Place"])


#Dict
student_info = dict(name="Shylaja",age = "80",Place = "Bangalore")

print(student_info)
print(student_info["name"])
print(student_info["age"])
print(student_info["Place"])
