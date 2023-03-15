fav_tools = { 
  1:"Linux", 
  2:"Git", 
  3:"Docker", 
  4:"Kubernetes", 
  5:"Terraform", 
  6:"Ansible", 
  7:"Chef"
}

# print the dictionary
print(fav_tools)

# access a value by key using square bracket notation
print("My favourite tool is :"+fav_tools[3])  # "Docker"

# access a value by key using the get() method
print(fav_tools.get(1))  # "Linux"

# add a new key-value pair to the dictionary
fav_tools[8] = "Jenkins"
print(fav_tools)

# remove a key-value pair from the dictionary using del statement
del fav_tools[2]
print(fav_tools)

# remove a key-value pair from the dictionary using the pop() method
fav_tools.pop(4)
print(fav_tools)