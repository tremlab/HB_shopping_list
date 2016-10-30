shopping_list = []

def main_menu():
	while(True):

		choice = int(raw_input("\nWhat would you like to do here? \nYour options are: \n 0 for Main Menu \n 1 for Show Current List \n 2 for Add an Item to your List \n 3 to Remove an Item from your list \n 4 to Exit \n "))

		if choice == 0:
			# print "Your options are \n 0 for Main Menu \n 1 for Show Current List, \n 2 for Add an Item to your List \n 3 Remove an Item from your list \n 4 to Exit "
			pass		
		elif choice == 1:
			sort_list()
			print "\nYour current shopping list is " + str(shopping_list[0:]) + '\n'
		elif choice == 2:
			add_to_list()
			print "\nYour current shopping list is " + str(shopping_list[0:]) + '\n'
		elif choice == 3:
			remove_from_list()
			print "\nYour current shopping list is " + str(shopping_list[0:]) + '\n'
		elif choice == 4:
			break
	

def add_to_list():
	add_item = str.lower(raw_input("What do you want to add to the list? "))
	if shopping_list.count(add_item) != 0:
		print "\nYou've already added this item to the list."
	else:
	 	shopping_list.append(add_item)
	shopping_list.sort()
	

def sort_list():
	shopping_list.sort()
	print shopping_list[0:]


def remove_from_list():
	remove_item = str.lower(raw_input("What do you want to remove from the list? "))
	if shopping_list.count(remove_item) == 0:
		print "\nThis item isn't on your list! "
	else:
		shopping_list.remove(remove_item)

	shopping_list.sort()

def main():
	main_menu()
		

if __name__ == '__main__':
	main()