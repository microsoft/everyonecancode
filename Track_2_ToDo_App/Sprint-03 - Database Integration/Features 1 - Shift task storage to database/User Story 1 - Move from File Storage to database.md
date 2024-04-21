# 📖 User Story: Move from File Storage to database - Step-by-Step
⏲️ _Est. time to complete: 15 min._ ⏲️

## User Story

*As a user, I would like to have my tasks stored in a database so that I can access them from any device with internet connectivity and not have to worry about concurrent users.*

## 🎯Acceptance Criteria:
- The application should store the tasks in a database instead of a file.

## 🎓Know Before You Start
no resources at this time

## 📋Steps

In order to complete this user story you will need to complete the following tasks

### Open Visual Studio Code
Open Visual Studio Code and open the source code the folder with your completed solution from the previous user story if you prefer you can use the starting reference application from [here](/Track_2_ToDo_App/Sprint-02%20-%20Web%20Application/src/app-s02-f02-us02/) 

<br/>

### Setup SQL Alchemy tookit

#### 1. Install SQL Alchemy
We will be using the SQL Alchemy toolkit to help us interact with the database. If it is not already installed, you can install it via pip through the Visual Studio Code terminal by running the following command:

```
pip install flask-sqlalchemy --only-binary=:all:
```

> [!NOTE]
> If you setup the virtual environment for this project, then SQLAlchemy should already be installed. You can check by running ```pip list``` in the terminal and looking for the module name in the list.

<br/>

### Creating Database Integration Class
In order to store our tasks in a database, we will need to perform the following steps:

#### 1. Create Database model
You will now need to create a class that we can use to store the tasks in the database. Create a new file called ```database.py``` in the same folder as your ```app.py``` file.

![Database Integration](/Track_2_ToDo_App/Sprint-03%20-%20Database%20Integration/images/DatabaseFile-S3-F1-US1-01.png)

>[!TIP]
>You can use GitHub Copilot to create this class for you with a prompt like *Create a python class call ToDo to store todo id and name in the sql lite database using SQLAlchemy*

<br/>

#### 2. Import the required packages
Add the following code to import the SQL Alchemy packages into the ```database.py``` file:

```python
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase
```

The flask_sqlalchemy package provides an easy way to interact with a database using SQLAlchemy. SQLAlchemy is a powerful SQL toolkit and Object-Relational Mapping (ORM) library for Python. It provides a high-level interface for interacting with databases, allowing you to define database models as Python classes and perform database operations using Python code.

<br/>


#### 3. Create the database base class
We will first create the base class for our database and declare the ```db``` variable to hold the database instance. Add the following code to the ```database.py``` file right after the import statements:

```python
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
```

The Base class is a simple class that we will use as the base class for our database models. The db variable is an instance of the SQLAlchemy class that we will use to interact with the database.

<br/>

#### 4. Create the Todo class
Now we will create a class to represent the tasks in the database. Add the following code to the ```database.py``` file:

```python
class Todo(db.Model):
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(100), nullable=False)

    def __str__(self):
        return self.name
```

The Todo class is a database model that represents a task or to-do item in the database. It has two columns: id, which is the primary key for the task, and name, which is the name of the task. The __str__ method is a special method that returns a string representation of the task, which we will use to display the task in the web app.

<br/>

#### Updating the Web Application Backend

#### 1. Import the g module from Flask
First we will need to update the ```app.py``` file to include ```g``` module from Flask.  This will be used in a later step to pass information to the HTML page during rendering.  Simply replace the ```from flask import Flask, render_template, request, redirect, url_for``` line with the following code:

```python
from flask import Flask, render_template, request, redirect, url_for, g
```

The g object is a special object provided by Flask that is used to store data that is shared between different parts of the application during a single request. We will use it to store the list of tasks that we retrieve from the database.

<br/>

#### 2. Import the Database class and the Todo class into the app.py file
We also need to bring in the Database class and the Todo class from the database module. Add the following code to the ```app.py``` file right after the code from the previous step:

```python
from database import db, Todo
```

<br/>

#### 3. Update the app initialization code
You will now need to update the app initialization code to include the database configuration. In the ```app.py``` file, replace this line 

```python
todo_file = os.path.join(basedir, 'todo_list.txt')
```

with the following code:

```python
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'todos.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```

The SQLALCHEMY_DATABASE_URI configuration variable specifies the location of the database file. In this case, we are using a SQLite database, which is a lightweight database that stores data in a single file. The SQLALCHEMY_TRACK_MODIFICATIONS configuration variable is set to False to disable tracking modifications, which can improve performance.

>[!TIP]
>You can try to use GitHub Copilot to update your app.py file with a prompt such as *update this to use the ToDo class instead of a text file*

<br/>

#### 4. Updating the Web Application Backend to use Database
We will now need to remove the file initialization code from the ```app.py``` file as it will no longer be needed because the items will now be stored in a database.  DELETE the following lines from app.py:
    
```python
todo_list = []

# Load the to-do list from a file. This will create the to-do list file if it does not exist (that is what r+ is for - see here for other options: [https://www.freecodecamp.org/news/file-handling-in-python/](https://www.freecodecamp.org/news/file-handling-in-python/))
try:
    with open("todo_list.txt", 'r+') as file:
        for line in file:
            todo_list.append(line.strip())
except FileNotFoundError:
    pass
```

and replace it with: 

```python
db.init_app(app)
with app.app_context():
    db.create_all()

@app.before_request
def load_data_to_g():
    todos = Todo.query.all()
    g.todos = todos
    g.todo = None
```
The db.init_app(app) function initializes the database with the Flask app instance. The with app.app_context(): block creates a context for the application, which is required to interact with the database. The db.create_all() function creates the database tables based on the database models defined in the database module.

The load_data_to_g() function is a before_request handler that runs before each request to the application. It retrieves all the tasks from the database and stores them in the g object, which is shared between different parts of the application during a single request. This allows us to access the list of tasks in the database from different parts of the application.

<br/>

#### 5. Update the home page route
Next we will need to modify the index function to use the database instead of the todo_list. Replace the ```index``` function in the ```app.py``` file with the following code:

```python
@app.route("/")
def index():
    return render_template("index.html")
```

This code removes the todo_list variable as the data will now be passed via the g object. 

<br/>

#### 6. Update Add Route to work with Database
Next, we will need to make our add_todo() function work with a database instead of a collection that gets stored in a file.  Replace the ```add_todo()``` function in the ```app.py``` file with the following code:

```python
@app.route("/add", methods=["POST"])
def add_todo():
    # Get the data from the form
    todo = Todo(
        name=request.form["todo"],
    )

    # Add the new ToDo to the list
    db.session.add(todo)
    db.session.commit()
    
    # Add the new ToDo to the list
    return redirect(url_for('index'))
```

The add_todo() function is a route handler that is called when the user submits the add to-do form. It retrieves the to-do item from the form data, creates a new Todo object with the name of the to-do item, adds the object to the database session, and commits the changes to the database. Finally, it redirects the user back to the index page.

<br/>

#### 7. Update the remove functionality to work with the database
We also need to update the remove functionality to work with the database.  Replace your ```remove_todo()``` function with the following code:

```python
@app.route('/remove/<int:id>', methods=['GET', "POST"])
def remove_todo(id):
    db.session.delete(Todo.query.filter_by(id=id).first())
    db.session.commit()
    return redirect(url_for('index'))
```

The remove_todo() function is a route handler that is called when the user submits the remove to-do form. It retrieves the item number from the form data, queries the database for the to-do item with the corresponding id, deletes the item from the database session, and commits the changes to the database. Finally, it redirects the user back to the index page.

<br/>

#### 8. Remove the save_todo_list function
Now that we are saving our tasks to the database we no longer need to save them to a file.  So remove the ```save_todo_list()``` function from the ```app.py``` file: 

<br/>

### Updating the Web Application Frontend

#### 1. Update the user interface for displaying tasks
Finally, you will need to update the ```index.html``` file to use the tasks from the database instead of the todo_list. Replace the code between the ```<ol>``` tags in the ```index.html``` file with the following code:

```html
<form method="post">
    <ol class="list-group">
        {% for todo in g.todos %}
            <li id="task-{{ todo.id }}" data-id="{{ todo.id }}" class="list-group-item d-flex justify-content-between">
                <div class="task">
                    <div class="title" id="title-{{ todo.id }}">{{ todo.name }}</div>
                </div>
                <span>
                    <button type="submit" class="btn btn-danger" formaction="{{ url_for('remove_todo', id=todo.id) }}">Remove</button>
                </span>
            </li>
        {% endfor %}
    </ol>
</form>
```

The code above uses Jinja templating to loop through the tasks stored in the g object and display them in a list. Each task is displayed as a list item with a unique id (which will be used to identify the to-do item that needs to be removed) and a remove button that allows the user to delete the task.

<br/>

#### 2. Remove the form for 'removing' tasks
You will also need to remove the following code from the ```index.html``` file as we no longer will be using a form to remove tasks but rather the remove buttons added above.

```html
        <div class="col-6">
            <form action="/remove" method="post" class="my-4">
                <div class="form-group">
                    <label for="item_number">Remove task number:</label>
                    <input type="number" name="item_number" min="1" class="form-control">
                </div>
                <button type="submit" class="btn btn-danger">Remove</button>
            </form>
        </div>
```

<br/>

#### 3. Run the application
Run the app by running ```python app.py``` in the terminal and browse to the local site. Test it out by adding a task and then removing a task.

![Database Integration](/Track_2_ToDo_App/Sprint-03%20-%20Database%20Integration/images/DatabaseIntegration-S3-F1-US1-01.png)

<br/>

🎉 Congratulations! You have now updated your web application to store and retrieve the todo items from a databaase. 

<br/>

> [!NOTE]
> 📄For the full source code for this exercise please see [here](/Track_2_ToDo_App/Sprint-03%20-%20Database%20Integration/src/app-s03-f01-us01/).

<br/>

[🔼 Back **Workshop** Instructions ](/Track_2_ToDo_App/Workshop-Format.md) | [🔼 Back to **Hackathon** Sprint 3 ](/Track_2_ToDo_App/Sprint-03%20-%20Database%20Integration/README.md) | [**◀ Previous user story** (in previous sprint)](/Track_2_ToDo_App/Sprint-02%20-%20Web%20Application/Feature%202%20-%20Basic%20Styling/User%20Story%202%20-%20Personalize%20Website.md) | [**Next user story** (in next sprint) ▶](/Track_2_ToDo_App/Sprint-04%20-%20Voice%20To%20Text/Feature%201%20-%20Add%20Voice/User%20Story%201%20-%20Add%20Voice.md)



