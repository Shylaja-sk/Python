#Ordered dict
# Dictionary that remembers insertion order

from collections import OrderedDict, defaultdict

d = {"name" : "shylaja" , "age" : 50, "address" : "KA", "id" : 123}
print(d)

od = OrderedDict() #main the order how we entered
od['banana'] = 2
od['Apple'] = 1
od['Orange'] = 5
od['Musk'] =4
print(od)

dd= defaultdict(int)
print(dd)