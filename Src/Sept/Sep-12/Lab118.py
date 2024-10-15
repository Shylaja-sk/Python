'''collections in Python
1. List
2. Set
3. Tuple
4. Dict

Advance Collection
1. Deque - Queue
2. Default Dict
3. Counter
4. Ordered Dict
5. ChainMap
6. nameTuple'''

#Deque [first in first out]

from collections import deque

d= deque()
d = deque ([1,2,3,4])
print(d)

d.append(5)
print(d)

d.appendleft(0)
print(d)

d.extend([6])
print(d)

print(d.pop())

print((d))

d.reverse()
print((d))






