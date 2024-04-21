# 📖 User Story: Add Item through Web Form - Step-by-Step
⏲️ _Est. time to complete: 10 min._ ⏲️

## User Story

*As a user, I want to input tasks through a web form, so I can interact with the application easily.*

## 🎯Acceptance Criteria:
- The web app should provide a form for users to input data.
- The form should simply capture the name of the to-do item, similar to the original terminal app for a seamless transition.
- The application should add the task to the list when the form is submitted.
- The interface should look something like this:

    ![outcome1](/Track_2_ToDo_App/Sprint-02%20-%20Web%20Application/images/outcome-S02-f01-US02.png)

## 🎓Know Before You Start
no resources at this time

## 📋Steps

In order to complete this user story you will need to complete the following tasks

### Updating the Web Application Frontend
The first set of changes that we will need to make is to update the web application's user interface to allow the user to add new items via the web page.

#### 1. Open Visual Studio Code
Open Visual Studio Code and open the source code the folder with your completed solution from the previous user story if you prefer you can use the starting reference application from [here](/Track_2_ToDo_App/Sprint-02%20-%20Web%20Application/src/app-s02-f01-us01/)


#### 2. Update the User interface to Add New To-Do Items
To do this, we need to update the `index.html` to add a basic form to allow a user to add tasks and call the backend server to add it to the file. Your HTML should be updated to look like this:

>[!TIP]
>You can use GitHub Copilot with a prompt like *add form to add task with add route*

```html
<!DOCTYPE html>
<html>
<head>
    <title>To-Do List</title>
</head>
<body>
    <h1>To-Do List</h1>
    <ol>
        {% for todo in todo_list %}
            <li>{{ todo }}</li>
        {% endfor %}
    </ol>
    <form action="/add" method="post">
        <label for="todo">Add a to-do:</label>
        <input type="text" name="todo">
        <button type="submit">Add</button>
    </form>
</body>
</html>
```
The code above creates a simple form that allows users to input a to-do item. When the form is submitted, a POST request is sent to the "/add" URL, which will trigger functionality in the back-end to save the to-do item to a file.  A POST request sends all of the data in the form to the back-end server.

<br/>

### Update the Web Application Backend
The next set of changes that we will need to make is to update the python code to enable the backend server to handle adding new to-do items and save them to the file.


#### 1. Update Web Server to Handle New To-Do Items
First, we need to update the python code to enable the backend server to handle new to-do items. This will be accomplished by adding a new route to support this functionality. To do this, open up the `app.py` file and add the following right after the homepage route/index function:

```python
@app.route("/add", methods=["POST"])
def add_todo():
    todo = request.form["todo"]
    todo_list.append(todo)
    save_todo_list()
    return redirect(url_for("index"))
```

The code above creates a new route that listens for POST requests to the "/add" URL. When a POST request is received, the function add_todo is called. This function retrieves the value of the "todo" form field from the request, appends it to the todo_list, saves it to the file and then redirects the user back to the index page.

Note that the save_todo_list() function is not yet implemented but we will add it in the next step.

<br/>

#### 2. Add Function to Save To-Do List
To complete the back-end server, we need the ability to save these tasks to our file so they persist between sessions (similar to the save functionlity we had in Sprint1). To do this we will implement a function that will write the tasks to the file right after the `add_todo()` function:

>[!TIP]
>You can use GitHub Copilot to create this with a prompt such as *Add a route to save todo list items*

```python
def save_todo_list():
    with open("todo_list.txt", "w") as file:
        for todo in todo_list:
            file.write(todo + "\n")
```

<br/>

#### 3. Run the Application
Run the app by running ```python app.py``` in the terminal and browse to the local site. Test it out by adding a tasks.
    
![RunApp-S2-F1-US02-01](/Track_2_ToDo_App/Sprint-02%20-%20Web%20Application/images/outcome-S02-f01-US02.png)


<br/>
🎉 Congratulations! You have now updated your basic web application to include a form to allow adding tasks and persisting them a file.

<br/>

> [!NOTE]
> 📄For the full source code for this exercise please see [here](/Track_2_ToDo_App/Sprint-02%20-%20Web%20Application/src/app-s02-f01-us02/).

<br/>

[🔼 Back **Workshop** Instructions ](/Track_2_ToDo_App/Workshop-Format.md) | [🔼 Back to **Hackathon** Sprint 2 ](/Track_2_ToDo_App/Sprint-02%20-%20Web%20Application/README.md) | [**◀ Previous user story**](User%20Story%201%20-%20Convert%20To%20Web%20App.md) | [**Next user story** ▶](User%20Story%203%20-%20Remove%20Item%20through%20Web%20Form.md)




