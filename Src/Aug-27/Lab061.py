#Lambda Expression
#is anynomous function that returns some form of data.... it is rearlly used

def triple_me(num):
    return num ** 3

o = triple_me(10)
print(o)

#In lambda

o = lambda num : num ** 3
print(o(10))

#Limitations

def add_10(n):
    return n+10

o = add_10(100)
print(o)

#using Lambda

o = lambda n : n+10
print(o(100))

#Another example wth 2 args

def with_alpha(a,b):
    return a+b

aa = with_alpha(10,20)
print(aa)

#with lambda

aa = lambda a,b: a+b
print(aa(10,20))