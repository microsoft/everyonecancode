# 📖 User Story: Add Item to List - Step-by-Step
⏲️ _Est. time to complete: 10 min._ ⏲️

## User Story

*As a user, I want to be able to add a to-do item to the list by entering the item name and pressing the enter key.*

## 🎯Acceptance Criteria:
- The application should have a command-line/terminal interface that allows the user to add items to the list. 
- The user should be able to add one item to the list at a time. 
- The user should be able to see the complete list of items after adding a new item.
- The user should be able to continue to add items to the list until they choose to exit the program.
- The interface should look something like this:
    ![outcome1](/Track_2_ToDo_App/Sprint-01%20-%20Basic%20Application/images/outcome-S1-F1-US1.png)

## 🎓Know Before You Start
The following resources/videos will help you get a better understanding of some of the basic Python concepts that you will use to complete this user story.
- [The Basic: Using the Print Statement](https://www.youtube.com/watch?v=FhoASwgvZHk&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=5) (3:29 min) <br/>
- [Hello World](https://www.youtube.com/watch?v=wWwr0tDSqnE&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=6) (5:59 min)<br/>
- [Comments](https://www.youtube.com/watch?v=kEuVvUc1Zec&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=7) (3:04 min)<br/>
- [Understanding Conditional Logic](https://www.youtube.com/watch?v=5pPKYWqkoek&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=19) (4:52 min)<br/>
- [Understanding Collections in Python](https://www.youtube.com/watch?v=beA8IsY3mQs&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=25) (11:26 min)<br/>
- [Demo: Collections in Python](https://www.youtube.com/watch?v=4PaSlXNjawM&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=26) (4:01 min)<br/>
- [Loops](https://www.youtube.com/watch?v=9Os0o3wzS_I&list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6&index=27) (5:29 min)

## 📋Steps

In order to complete this user story you will need to complete the following tasks

### Making your first application

#### 1. Open Visual Studio Code
- From the terminal window, navigate to the project directory
  
    ```bash
    cd <project directory>
    ```
- Open up Visual Studio Code in the project directory by executing the following command.
    
    ```cmd
    code . 
    ```
> [!TIP] 
> The repository for this training has a directory named `myApplication` that you can use as your default working directory while building the application or feel free to choose any directory where you would like to put this application. 

<br/>

#### 2. Create the `app.py` application file
Every program needs a starting point. Create a new file named `app.py` in the root of your project folder. Select the new file icon as seen below:

![CreateNewFile](/Track_2_ToDo_App/Sprint-01%20-%20Basic%20Application/images/NewFile-S01-F01-US01-01.png)

then name the file `app.py` and press enter.

![CreateNewFile](/Track_2_ToDo_App/Sprint-01%20-%20Basic%20Application/images/newFile-S01-F01-US01-02.png)

<br/>

#### 3. Create the collection to hold the to-do items
Create an empty collection to hold your to-list items with the variable named 'todo_list' by adding the following code to the top of the `app.py` file.
    
```python
todo_list = []
```

<br/>

#### 4. Create some sample to-do items
Create a few sample to-do items in the list by adding the following code to the `app.py` file right after the 'todo_list' variable declaration.

```python
todo_list.append("Buy milk")
todo_list.append("Learn more about Azure")
todo_list.append("Complete first Python project")
```

The append method on a collection is used to add items to the list. In this case, we are adding three items to the list.

<br/>

#### 5. Print the list to the console
Now we will want to see that we succesfully added all of those sample to-do items to the list. You can do this by printing the list to the console.  Add the following code to the `app.py` file right after the `append` statements.

```python
for todo in todo_list:
    print(todo)
```

This code will loop through the `todo_list` and print each item to the console. Your code should now look something like this:

![FirstApp](/Track_2_ToDo_App/Sprint-01%20-%20Basic%20Application/images/FirstApp-S01-F01-US01-01.png)

<br/>

#### 6. Run the application 
Now let's see this application in action. Open a terminal window within visual studio code and run the application by typing `python app.py` and pressing the enter key or simply click the play button in the top right corner of the Visual Studio Code window.

![RunApplication01](/Track_2_ToDo_App/Sprint-01%20-%20Basic%20Application/images/RunApp-S1-F1-US01-01.png)

🎉 Congratulations, you now have successfully added a to-do item to the list and created the initial code for this to-do list application.  Note however that this is **not a user-friendly** way to interact with the application as all of the to-do items are "hard-coded" meaning they are written directly in the code.  This also does not meet the acceptance criteria that we have outlined above. In the next step you will be adding a user-friendly command-line interface to the application.

<br/>

### Update the application to be interactive

#### 1. Add a menu to the application
In order to create the user-friendly version of this application, we will need to create a basic menu structure that will allow the user to add an item to the to-do list. First, we need to update the code by first removing all the previous 'todo_list.append' statements and the 'for' loop statements to get rid of the 'hard-coded' sample to-do items. 

![RemoveCode](/Track_2_ToDo_App/Sprint-01%20-%20Basic%20Application/images/EditCode-S1-F1-US01-01.png)

and replace it with the following code.

```python
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
```
This code creates a while loop that will continue to run over an over again until the user selects to exit the program by selecting "x" or "X".  For each iteration of the while loop, 
- it will first loop through the collection of to-do items and print them out
- it will display the menu 
- it will accept input from the user on which menu item to perform and will then execute the corresponding code related to that menu item. 

<br/>

#### 2. Run the Application with the Menu
Now let's see this application in action with the menu system in place. Open the terminal in Visual Studio code and run the application by typing `python app.py` and pressing the enter key or simply click the play button in the top right corner of the Visual Studio Code window.

![RunApplication02](/Track_2_ToDo_App/Sprint-01%20-%20Basic%20Application/images/RunApp-S1-F1-US01-02.png)


Now you should see a menu structure where you can interact with the system. Pressing 'a' or 'A' will allow you to add an item to the list. Please experiment by adding a few to-do list items.  Remember that you will need to press 'x' or 'X' to exit the program.

Here's what my application looks like after adding a few items to the list:

![RunApplication03](/Track_2_ToDo_App/Sprint-01%20-%20Basic%20Application/images/RunApp-S1-F1-US01-03.png)

🎉 Hooray! You have now added a user-friendly command-line interface to the application and finished Sprint 1 - Feature 1, User Story 1. You can now add items from the to-do list by entering the item name and pressing the enter key.

<br/>

> [!NOTE]  
> 📄For the full source code for this exercise please see [here](/Track_2_ToDo_App/Sprint-01%20-%20Basic%20Application/src/app-s01-f01-us01/app.py).

<br/>

[🔼 Back **Workshop** Instructions ](/Track_2_ToDo_App/Workshop-Format.md) | [🔼 Back to **Hackathon** Sprint 1 ](../README.md#📖user-story-1---add-item-to-list) | [**Next user story ▶**](/Track_2_ToDo_App/Sprint-01%20-%20Basic%20Application/Feature%201%20-%20Manage%20Todo%20List/User%20Story%202%20-%20Remove%20Item%20from%20List.md)



