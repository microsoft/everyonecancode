# 📖 User Story: Remove Item from List - Step-by-Step
⏲️ _Est. time to complete: 10 min._ ⏲️

## User Story

*As a user, I want to be able to remove to-do item from the list by entering the item number and pressing the enter key*

## 🎯Acceptance Criteria:
- The application should have a command-line/terminal interface that allows users to remove items from the list.
- The user should be able to remove one item from the list at a time.
- The user should be able to see the complete list of existing items after removing an item.
- The user should be able to continue to add or remove items from the list until they choose to exit the program.
- The interface should look something like this:
    ![outcome2](/Track_2_ToDo_App/Sprint-01%20-%20Basic%20Application/images/outcome-S1-F1-US2.png)

## 🎓Know Before You Start
The following resources/videos will help you get a better understanding of some of the basic Python concepts that you will use to complete this user story.
- [Formatting Strings](https://www.youtube.com/watch?v=bQQqxysLIGE&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=11) (4:08 min) <br/>
- [Understanding Collections in Python](https://www.youtube.com/watch?v=beA8IsY3mQs&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=25) (11:26 min) - Same video as previous user story<br/>
- [Demo: Collections in Python](https://www.youtube.com/watch?v=4PaSlXNjawM&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=26) (4:01 min) - same video as previous user story<br/>
     

## 📋Steps

#### 1. Open Visual Studio Code
- Go to your application directory and start visual studio code by typing `code .` in the terminal window and pressing enter.

- Open the `app.py` file in the root of your project folder.

<br/>

#### 2. Add a new menu option to remove an item from the list
The first change that we will need to make to the application will be to add a new menu option that will allow the user to remove an item from the list. Update your menu structure to include the "R - Remove to-do item" option. You menu structure should now look like this:

```python
# Print the menu
print() # Add a couple of blank lines
print("Actions:")
print("A - Add to-do item")
print("R - Remove to-do item")     #<--- ***HERE***
print("X - Exit")
choice = input("Enter your choice (A, R, or X): ")  #<--- ***ALSO UPDATE MENU OPTIONS with the 'R' ***
choice = choice.upper() #converts the choice to uppercase
```

> [!TIP]
> Be aware that Python programs depend on spacing/tabs to determine the structure of the code. If you are copying and pasting the code above, make sure that the spacing is correct.  You may have to indent this code
as this code is part of the while loop

<br/>

#### 3. Identifying items in the list
Next, we need a way to identify a to-do item so that we can remove it from the list.  The easiest way to do this is to add a line number to each item that identifies that item in the list. This will allow the user to select an item from the list by providing a line number.  To do this, we will need to update our code to print out the line number for each item in the list.   Replace the code that prints out the list at the top of the while loop 

![replacecode](/Track_2_ToDo_App/Sprint-01%20-%20Basic%20Application/images/EditCode-S1-F1-US02-01.png)

with the following code.

> [!TIP]
> If you simply do not want to copy/paste the code below.  You can use GitHub Copilot to adjust this method. Use a prompt such as: *adjust this for loop to print item number next to each item*   

```python
print("To-do list: ") # Print the title of the list
item_number = 1
for todo in todo_list: # Loop through existing to-do items
    print(f'{item_number}: {todo}')
    item_number += 1
```

This code will print out the list of items in the list along with the line number of each item.  Note the use of the `item_number` variable to keep track of the line number of each item in the list. This will allow the user to select the item they would like to delete.  Also note the use of the `f-string` to customize what we are printing to the terminal. Using the `f-string` allows us to easily insert the `item_number` and `todo` variables into the string that we are printing by using `{}` around the variable names.  This is a very powerful feature of Python and allows you to easily create strings that are customized to the data that you are working with.

<br/>

#### 4. Add the code to remove an item from the list
Finally, you will need to add the code that will allow the user to remove an item from the list. Add the following code right below the code to add an item.

![addcode](/Track_2_ToDo_App/Sprint-01%20-%20Basic%20Application/images/EditCode-S1-F1-US02-02.png)

> [!TIP]
> You can use GitHub Copilot to adjust this method instead of just copying and pasting the code below. Use a prompt such as: *create a choice for R which will remove items from the list given item number*

```python
#user selected 'r' or 'R' - To Remove an item from the list
if choice == "R":
    item_number = int(input("Enter the number of the item to remove: "))
    if item_number > 0 and item_number <= len(todo_list):
        todo_list.pop(item_number - 1)
    else:
        print("Invalid item number")
    continue
```

Note that the `pop` method on the collection allows you to remove an item from the list by providing the index of the item that you would like to remove.  In this case, we are using the `item_number` variable that the user provided to remove the item from the list. Since python collections are zero-based (i.e., their first index is 0) and our list displays items starting at 1 so we need to adjust the menu number by subtracting 1 from it to match where the item is stored in the collection. 

Also note that we are checking to make sure that the `item_number` is within the range of the list before we attempt to remove the item.  If the `item_number` is not within the range of the list, we print an error message to the user and continue to the next iteration of the loop.

<br/>

#### 5. Run the Application
Now let's see this application in action. Open the terminal within Visual Studio code and run the application by typing `python app.py` and pressing the enter key or simply click the play button in the top right corner of the Visual Studio Code window.

Please experiment by adding a few to-do list items and then try to remove an item. When selecting "R" you will be prompted to enter the number of the item you would like to remove (as seen in the picture below). Remember that you will need to press 'x' or 'X' to exit the program.

![RunApplication01](/Track_2_ToDo_App/Sprint-01%20-%20Basic%20Application/images/RunApp-S1-F1-US02-01.png)


🎉 Congratulations you can now mark the "Complete first python application" officially off your list! You have completed Sprint 1 - Feature 1, User Story 2.

❕Note that if you run the application multiple times, you will see that the items that you added in the previous run are no longer there. This is because the list is stored in memory and is not saved to a file. We will be adding this feature in the next user story.

<br/>

> [!NOTE]    
> 📄For the full source code for this exercise please see [here](/Track_2_ToDo_App/Sprint-01%20-%20Basic%20Application/src/app-s01-f01-us02/app.py).

<br/>


[🔼 Back **Workshop** Instructions ](/Track_2_ToDo_App/Workshop-Format.md) | [🔼 Back to **Hackathon** Sprint 1 ](../README.md#📖user-story-1---add-item-to-list) | [**◀ Previous user story**](User%20Story%201%20-%20Add%20Item%20to%20List.MD) | [**Next user story ▶**](/Track_2_ToDo_App/Sprint-01%20-%20Basic%20Application/Feature%202%20-%20Save%20To-Do%20List/User%20Story%201%20-%20Save%20To-Do%20List%20to%20File.md)
