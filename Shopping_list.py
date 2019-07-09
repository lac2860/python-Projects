#Create a new empty list named shopping_list
shopping_list = []
    

#Create a function named add_to_list that declares a parameter named item 
def add_to_list(item):
    #Add the item to the list 
    shopping_list.append(item)
    #Notify user that the item was added and state the number of items in the list currently
    print("The item was added to the list, Number of items:",len(shopping_list))

#define a new function show_list that prints all the items on the list
def show_list():
    print("Here is your list:")
    for item in shopping_list:
        print(item)
    
def show_help():
    print("What should we pick up at the store?:")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list
""")
    
show_help()
while True:
    new_item = input("> ")
    
    
    if new_item ==  'DONE':
        break
        
    elif new_item == 'HELP':
        show_help()
        continue
    #Enable the SHOW command to show the list. Don't forget to update the HELP documentation.
    elif new_item == 'SHOW':
        show_list()
        continue

    #call add_to_list with new_item as an argument 
    add_to_list(new_item)
    
show_list()
    
