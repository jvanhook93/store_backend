from data import me


#get data from the dictionary
print(me["first_name"] + " " + me["last_name"])

# modify
me["color"] = "gray"

# add
me["age"] = 29


#read non existing key
# print(me["title"]) # crash you code

#check if a key exist inside a dictionary
if "title" in me:
  print(me["title"])


  # print the full address
  # street num, city

address = me["address"]

print(address["street"] + " " + str(address["number"]) + ", " + address["city"])