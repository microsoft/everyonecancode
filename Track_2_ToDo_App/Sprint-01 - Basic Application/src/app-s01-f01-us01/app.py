###############################################################################
## Sprint 1: Basic Application
## Feature 1: Create and Manage a To-Do List
## User Story 1: Add Item to List
###############################################################################

todo_list = []

#continue to loop and display menu until user selects to exit the program
while True:
    print() # Add a couple of blank lines
    print()
    print("To-do list: ") # Print the title of the list
    for todo in todo_list: # Loop through existing to-do items
        print(todo)

    # Print the menu
    print() # Add a of blank lines
    print("Actions:")
    print("A - Add to-do item")
    print("X - Exit")
    choice = input("Enter your choice (A or X): ")
    choice = choice.upper() #converts the choice to uppercase

    #user selected 'a' or 'A' - To Add an item to the list
    if choice == "A":
        todo = input("Enter the to-do item: ")
        todo_list.append(todo)
        continue  #tells the program to go back to the start of the loop

    #user selected 'x' or 'X' to exit program
    if choice == "X":
        break #tells the program to exit the loop

    #user selected something else
    print("Invalid choice")
