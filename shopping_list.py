global_shopping_list = {'Target':['apples','bananas']}




def Menu():
    print "0 -  Main Menu"
    print "1 -  Show all lists."
    print "2 -  Show a specific list."
    print "3 -  Add a new shopping list."
    print "4 -  Add an item to a shopping list."
    print "5 -  Remove an item from a shopping list."
    print "6 -  Remove a list by nickname."
    print "7 -  Exit when you are done."
    

# menu 1
def show_lists():
    print global_shopping_list.items()

# menu 2
def spec_lists(list_you_want):
 
    print global_shopping_list[list_you_want]

# menu 3
def add_new_list(new_list):
    
    global_shopping_list[new_list] = []
    print global_shopping_list
# menu 4
def add_item(which_list, item_add):
    the_list = global_shopping_list[which_list]
    if item_add in the_list:
        print "Item has already been added. Please add something else!"
    else:
        the_list.append(item_add)
        the_list.sort()
        print the_list
# menu 5
def remove_item(which_list, item_remove): 
    the_list = global_shopping_list[which_list]   
    if item_remove in the_list:
        the_list.remove(item_remove)
        the_list.sort()
        print the_list
        
    else: 
        print item_remove + " is not in the list"
      
# menu 6
def remove_list(which_list):
    
    del global_shopping_list[which_list]
    print global_shopping_list


def main():
    Menu()

    while(True):
        choice = int(raw_input("What would you like to do? "))
        if choice == 0:
            Menu()
        elif choice == 1:
            show_lists()
        elif choice == 2:
            list_you_want = raw_input("Which list do you want to see? ")
            spec_lists(list_you_want)
        elif choice == 3:
            new_list = raw_input("Which list do you want to add? ")
            add_new_list(new_list)
        elif choice == 4:
            which_list = raw_input("Which list would you like to modify? ")
            item_add = raw_input("Which item would you like to add? ")
            add_item(which_list, item_add)
        elif choice == 5:
            which_list = raw_input("Which list would you like to modify? ")
            item_remove = raw_input("Which item would you like to remove? ")
            remove_item(which_list, item_remove)
        elif choice == 6:
            which_list = raw_input("Which list would you like to modify? ")
            remove_list(which_list)
        else:
            Break


if __name__ == '__main__':
    main()