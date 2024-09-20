#Understanding Decorators in Python
#lambda arguments : expression
#List
#Tuple


def make_pizza(*toppings): # here * is unlimted
    for top in toppings:
        print(toppings)

Shy = make_pizza("olives")
shra = make_pizza("olives","panner")
shra1 = make_pizza("olives","panner","mashroom")
shra2 = make_pizza("olives","panner","mashroom","corn")
