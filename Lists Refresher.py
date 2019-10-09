#------------------------------------------------
#Dylan Friesen
#Lists Refresher
#Monday, October, 2019
#------------------------------------------------

inventory = [] #blank inventory that the user can add one item to.
item_list = ["you chose banana", "you chose turkey leg", "you chose CheeseBurger", "you chose Steve Brule"]

item = input("what u want?")
inventory.append(item) #using append to add the item they wrote to the blank inventory.
print(inventory)

selection = input("What item would you like to use?") #code that gives the user a selection of items to use, doesn't really do anything.
if selection == "banana":
    inventory.append("banana")
    print (item_list [0])
elif selection == "turkey leg": #everyone loves turkey.
    inventory.append("turkeyleg")
    print (item_list [1])
elif selection == "Cheeseburger":
    inventory.append("CheeseBurger")
    print (item_list [2])
elif selection == "Steve Brule": #Steve Brule because Steve Brule
    inventory.append("Steve Brule")
    print (item_list [3])
else:
    inventory.append("slime")
    print ("slime")

print(inventory)
    
item_remove = input("What do you want to remove?") #removing chosen item
inventory.remove(item_remove) #using remove to remove item
print(inventory)
    
if "banana" in inventory:
    print("gas em")
if "Steve Brule" in inventory:
    print("Dangatang")
if "Cheeseburger" in inventory:
    print("goobo")
if "turkeyleg" in inventory:
    print("yum")
if "slime" in inventory:
    print("gobbos")
    