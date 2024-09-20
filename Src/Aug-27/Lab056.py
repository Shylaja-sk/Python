my_shopping_list= ["bread","Milk","butter"]
print(my_shopping_list[0])
print(len(my_shopping_list))

def bring_more_food(my_list):
    my_list.append("corn") #append more in list
    more_item = input("Enter the item")
    my_list.append(more_item)  #input is also possible
    my_list.remove(more_item) #To remove
    my_list.insert(0,more_item) #to insert

    return my_list


l=bring_more_food(my_shopping_list)
print(l)



