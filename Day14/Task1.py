#List
my_list = [1, 2, 3, 4, 5]
my_list[2] = 10   # modify an element
my_list.append(6) # add an element
my_list.remove(4) # remove an element
print(my_list)    # [1, 2, 10, 5, 6]


#tuple
my_tuple = (1, 2, 3, 4, 5)
# my_tuple[2] = 10  # raises a TypeError: 'tuple' object does not support item assignment
print(my_tuple[2])  # 3


#set
my_set = {1, 2, 3, 4, 5}
my_set.add(6)    # add an element
my_set.remove(4) # remove an element
print(my_set)    # {1, 2, 3, 5, 6}