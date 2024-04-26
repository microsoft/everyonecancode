# User Story: Add traditional details to to-do item - Step-by-Step
⏲️ _Est. time to complete: 30 min._ ⏲️

## User Story
*As a user, I want to be able to store the calendar date for when this task is due, set a priority for each task, provide more details about the task as well as the completion status*

## 🎯Acceptance Criteria:
- A due date field should be stored in the database for each task (as optional)
- Add a priority field to the database for each task (as optional)
- Add a notes field to the database for each task (as optional)
- Add a completion status field to the database for each task (as optional)
- The add task functionality should behave as it did in previous iterations. i.e. you will NOT need to supply any of the additional fields when adding a task.  The due date, priority and notes should simply default to None and the completion status should default to False. 
- Additional UI should be created to both allow a user to see the details of a task as well as the ability to edit all of the new fields. 
- The interface should look something like this:

    Index:

    ![Index](/Track_2_ToDo_App/Sprint-06%20-%20Advanced%20To-Do%20Details/images/outcome-S06-F01-US01-INDEX.png)

    Details Page:
        
    ![Details](/Track_2_ToDo_App/Sprint-06%20-%20Advanced%20To-Do%20Details/images/outcome-S06-F01-US01-DETAILS-2.png)

    Edit Page:
      
    ![Edit](/Track_2_ToDo_App/Sprint-06%20-%20Advanced%20To-Do%20Details/images/outcome-S06-F01-US01-EDIT-2.png)

    Recommendations Page:
        
    ![Recommendations](/Track_2_ToDo_App/Sprint-06%20-%20Advanced%20To-Do%20Details/images/outcome-S06-F01-US01-RECOMMENDATIONS.png)

## 🎓Know Before You Start
no resources at this time

## 📋Steps

In order to complete this user story you will need to complete the following tasks:

### Open Visual Studio Code
Open Visual Studio Code and open the source code the folder with your completed solution from the previous user story if you prefer you can use the starting reference application from [here](/Track_2_ToDo_App/Sprint-05%20-%20Advanced%20AI%20recommendations/src/app-s05-f01-us03/) 

<br/>

### Updating the Database Model

#### 1. Add the new fields to the database model
The first step in completing this user story is to update the database model to include the new fields for the task details. Open the `database.py` file in the source folder of your application. Add the following code right under the `recommendations_json` instance variable to create the additional columns for the task details:

```python
notes = db.Column(String(100))
priority = db.Column(Integer, default=0)
completed = db.Column(Boolean, default=False)
due_date = db.Column(String(50))
```

This code adds several new columns to the `Todo` model for the due date, priority, notes, and completion status of the task. 
- The `notes` columns is of type `String` and will be used to hold additional information about the task. 
- The `priority` column is of type `Integer` and will be used to store the priority of the task in a numerical format and will represent the following values: 
    - 0 - Not Set
    - 1 - High
    - 2 - Medium
    - 3 - Low
- The `completed` column is of type `Boolean` and will be used to store the completion status of the task.
- The `due_date` column is of type `String` and will be used to store the calendar date in string format for when the task is due.

<br/>

#### 2. Update the imports in the database module
You will notice that the `Boolean` datatype may have a squiggly line under it.  This is because we have not imported that datatype into the file yet.  To fix this, update the `from sqlalchemy...` import statement at the top of the `database.py` file to include the `Boolean` datatype.  The updated import statement should look like this:

```python
from sqlalchemy import Integer, String, Boolean
```
<br/>

#### 3. Add methods to the ToDo model to make the fields more user-friendly
These fields will be used throughout the application and since several of these fields including `completed` and `priority` are being stored in a **format that isn't as user-readable as we would like, we will need to add some additional code to the application to make these fields more user-friendly**.  To do this we will add a couple of additional methods to our ToDo model.  Open the `database.py` file in the source folder of your application. Add the following code right after the `__str__(self)` method:

```python
def priority_str(self):
    """
    Returns the priority as a string.
    """
    str = "Not Set"
    if self.priority == 1:
        str = "High"
    elif self.priority == 2:
        str = "Medium"
    elif self.priority == 3:
        str = "Low"

    return str

def completed_str(self):
    """
    Returns the completed status as a string.
    """
    if self.completed:
        return "Yes"
    else:    
        return "No"
```



<br/>


### Updating the Web Application Backend
The next set of steps will involve updating the backend of the web application to handle the new task details.

#### 1. New Tabs Enumeration
Now that we are adding the ability to edit and see details about the task we will need to have multiple panels in the user interface to show the different types of information (i.e., recommendations, details, and the ability to edit) and therefore we will need a way to tell the UI which panel to show.  To do this we will first create a new enumeration class to represent the different panels that can be shown. Create a new file called `tab.py` in the same folder as your `app.py` file. Add the following code to the file:

```python
from enum import Enum

class Tab(Enum):
    NONE = 0,
    DETAILS = 1,
    EDIT = 2,
    RECOMMENDATIONS = 3
```
<br/>

#### 2. Include Tab Enumeration in the Web Application
Next, let's integrate the new fields into the web application. Open the `app.py` file in the source folder of your application. Add the following code right after the `from flask import...` statement to import the new `Tab` enumeration class:

```python
from tab import Tab
```
<br/>

#### 3. Update the g object to include the new Tab enumeration
We now need to make that Tab enumeration class available to the user interface, we will do this by updating our `load_data_to_g` function.  Open the `app.py` file in the source folder of your application and add two new variables one named `g.TabEnum` and one named `g.selectedTab` to the `load_data_to_g` function. The updated function should look like this:

```python
@app.before_request
def load_data_to_g():
    todos = Todo.query.all()
    g.todos = todos 
    g.todo = None
    g.TabEnum = Tab
    g.selectedTab = Tab.NONE
```

By default at the beginning of every request we set the selecedTab to NONE.  Individual routes may alter this tab based on what they want to dispaly
<br/>

#### 4. New Details, Edit, and Update Routes
Next, we need to create additional routes on our web server to handle the new functionality to "show task details", "edit a task", as well as "update the task" after editing. Open the `app.py` file in the source folder of your application. Add the following code right after the `add_todo()` method to create these additional routes:

```python
# Details of ToDo Item
@app.route('/details/<int:id>', methods=['GET'])
def details(id):
    g.selectedTab = Tab.DETAILS
    g.todos = Todo.query.all()
    g.todo = Todo.query.filter_by(id=id).first()
        
    return render_template('index.html')

# Edit a new ToDo
@app.route('/edit/<int:id>', methods=['GET'])
def edit(id):
    g.selectedTab = Tab.EDIT
    g.todos = Todo.query.all()
    g.todo = Todo.query.filter_by(id=id).first()

    return render_template('index.html')

# Save existing To Do Item
@app.route('/update/<int:id>', methods=['POST'])
def update_todo(id):
    g.selectedTab = Tab.DETAILS

    if request.form.get('cancel') != None:
        return redirect(url_for('index'))

    # Get the data from the form
    name = request.form['name']
    due_date = request.form.get('duedate')
    notes=request.form.get('notes')
    priority=request.form.get('priority')
    completed=request.form.get('completed')

    todo = db.session.query(Todo).filter_by(id=id).first()
    if todo != None:
        todo.name = name

        if due_date != "None":
            todo.due_date = due_date

        if notes != None:
            todo.notes = notes

        if priority != None:
            todo.priority = int(priority) 

        if completed == None:
            todo.completed = False
        elif completed == "on":
            todo.completed = True
    #
    db.session.add(todo)
    db.session.commit()
    #
    return redirect(url_for('index'))
```

This code adds three new routes to the web application:
- `/details/<int:id>`: This route takes the task ID as a parameter and retrieves the task from the database based on the ID. The route sets the selected tab to `DETAILS` and renders the `index.html` template.
- `/edit/<int:id>`: This route takes the task ID as a parameter and retrieves the task from the database based on the ID. The route sets the selected tab to `EDIT` and renders the `index.html` template.
- `/update/<int:id>`: This route takes the task ID as a parameter and updates the task in the database based on the form data submitted by the user. The route sets the selected tab to `DETAILS` and redirects the user to the home page after updating the task.

<br/>

#### 5. Update the Recommendations Route
We also need to update our recommendations functionality to now tell it to select the RECOMMENDATIONS tab when being called.  We can do this by simply adding the following line to the top of the `recommend` function in the `app.py` file:

```python
g.selectedTab = Tab.RECOMMENDATIONS
```

<br/>

### Updating the Web Application FrontEnd
Now we need to update the user interface to display to handle two new panels, one for showing the details of a task and one for editing a task.  To do this we will make several changes to the `index.html` file in the `templates` folder of your application.
- We will need to add two new buttons to the task list that will allow a user to view the details of a task and edit the details of a task.
- We will need to update the recommendations tab to only show the recommendations when a user selects that functionality 
- We will add a new tab to the right of the task list that will display the details of a task when a user clicks on a task.
- We will add a new tab to the right of the task list that will allow a user to edit the details of a task when a user clicks on a task.
- We will add a new form to the edit tab that will allow a user to update the details of a task.<br/><br/>

#### 1. Update the user interface to include the new fields
For the sake of making these changes easier in this step-by-step, instead of walking through each change we will simply ask update the `index.html` file in the `templates` folder of your application with the following code: 

```html
<!DOCTYPE html>
<html>
<head>
    <title>My To-Do List</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}" />
    <link rel="icon" type="image/x-icon" href="{{ url_for('static', filename='images/favicon.ico') }}">
    <script src="{{ url_for('static', filename='js/app.js') }}"></script>
</head>
<body>
    <br/>
    <br/>
    <div class="container">
        <div class="h-100 p-5 bg-body-tertiary border rounded-3">
            <h1>My To-Do List</h1>
        </div>
        <br />
        <div class="row">
            <div class="col-7">
                <form>
                    <ol class="list-group">
                        {% for todo in g.todos %}
                            <li id="task-{{ todo.id }}" data-id="{{ todo.id }}" class="list-group-item d-flex justify-content-between">
                                <div class="task">
                                        <div class="title" id="title-{{ todo.id }}">{{ todo.name }}</div>
                                </div>
                            <span>
                                <button type="submit" class="btn btn-success" formaction="{{ url_for('details', id=todo.id) }}" formmethod="GET">Details</button>
                                <button type="submit" class="btn btn-success" formaction="{{ url_for('edit', id=todo.id) }}" formmethod="GET">Edit</button>
                                <button type="submit" class="btn btn-success" formaction="{{ url_for('recommend', id=todo.id) }}" formmethod="GET">Recommendations</button>
                                <button type="submit" class="btn btn-danger" formaction="{{ url_for('remove_todo', id=todo.id) }}" formmethod="POST">Remove</button>
                            </span>
                        </li>
                        {% endfor %}
                    </ol>
                </form>
                <form action="/add" method="post" class="my-4">
                    <div class="form-group">
                        <br />
                    </div>
                    <span class="input-group-text">
                        <input type="text" id="todo" name="todo" class="form-control" placeholder="Add a new task">
                        
                        <button type="button" class="btn btn-outline-secondary" onclick="captureVoice()">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-mic" viewBox="0 0 16 16">
                                <path d="M3.5 6.5A.5.5 0 0 1 4 7v1a4 4 0 0 0 8 0V7a.5.5 0 0 1 1 0v1a5 5 0 0 1-4.5 4.975V15h3a.5.5 0 0 1 0 1h-7a.5.5 0 0 1 0-1h3v-2.025A5 5 0 0 1 3 8V7a.5.5 0 0 1 .5-.5"></path>
                                <path d="M10 8a2 2 0 1 1-4 0V3a2 2 0 1 1 4 0zM8 0a3 3 0 0 0-3 3v5a3 3 0 0 0 6 0V3a3 3 0 0 0-3-3"></path>
                            </svg>
                            <span class="visually-hidden" title="Use Microphone"></span>
                          </button>
                        <button type="submit" class="btn btn-success">Add</button>
                    </span>
                </form>

            </div>
            <div class="col-5">
                {% if g.todo != None and g.selectedTab == g.TabEnum.RECOMMENDATIONS %}       
                <div id="recommendations-div" class="card">                     
                    <div class="card-body">
                        <div class="list-group" id="list-of-recommendations">
                            <h5>AI Recommendations for "{{ g.todo.name }}"</h5>
                            {% for recommend in g.todo.recommendations %}
                            <a href="{{ recommend.link }}" class="list-group-item list-group-item-action"> {{ recommend.title }} </a>
                            {% endfor %}
                            <br />
                            Don't like recommendations? 
                            <a href="{{ url_for('recommend', id=g.todo.id, refresh=true) }}" class="btn btn-info btn-fixed-width"> Refresh </a>
                        </div>
                    </div>
                </div>
                {% endif %}
                {% if g.todo != None and g.selectedTab == g.TabEnum.DETAILS %}
                <div id="details-div" class="card">
                    <div class="card-body">
                        <p><strong>Task:</strong> {{ g.todo.name }}</p>
                        <p><strong>Priority: </strong> {{ g.todo.priority_str() }}</p>
                        <p><strong>Due Date:</strong> {{ g.todo.due_date }} </p> 
                        <p><strong>Additional Notes:</strong> {{ g.todo.notes }}</p>
                        <p><strong>Completed:</strong> {{ g.todo.completed_str() }}</p>
                    </div>
                </div>
                {% endif %}
                {% if g.todo != None and g.selectedTab == g.TabEnum.EDIT %}               
                <div id="edit-div" class="card">
                    <div class="card-body">
                        <form action="{{ url_for('update_todo', id=g.todo.id) }}" method="post">
                            <input type="hidden" name="id" value="{{g.todo.id}}">
                            <div class="form-group">
                                <label for="name">Name:</label>
                                <input type="text" id="name" name="name" value="{{g.todo.name}}" class="form-control">
                            </div>
                            <br/>
                            <div>
                                <p>Priority:</p>
                                {% if g.todo != None and g.todo.priority_str() == "High" %} 
                                <div class="form-check form-check-inline">
                                    <input class="form-check-input" type="radio" name="priority" id="inlinePriority1" value="1" checked>
                                    <label class="form-check-label" for="inlinePriority1">High</label>
                                </div>
                                {% else %}
                                <div class="form-check form-check-inline">
                                    <input class="form-check-input" type="radio" name="priority" id="inlinePriority1" value="1">
                                    <label class="form-check-label" for="inlinePriority1">High</label>
                                </div>
                                {% endif %}
                                {%if g.todo != None and g.todo.priority_str() == "Medium" %} 
                                <div class="form-check form-check-inline">
                                    <input class="form-check-input" type="radio" name="priority" id="inlinePriority2" value="2" checked>
                                    <label class="form-check-label" for="inlinePriority2">Medium</label>
                                </div>
                                {% else %}
                                <div class="form-check form-check-inline">
                                    <input class="form-check-input" type="radio" name="priority" id="inlinePriority2" value="2">
                                    <label class="form-check-label" for="inlinePriority2">Medium</label>
                                </div>
                                {% endif %}
                                {%if g.todo != None and g.todo.priority_str() == "Low" %} 
                                <div class="form-check form-check-inline">
                                    <input class="form-check-input" type="radio" name="priority" id="inlinePriority3" value="3" checked>
                                    <label class="form-check-label" for="inlinePriority3">Low</label>
                                </div>
                                {% else %}
                                <div class="form-check form-check-inline">
                                    <input class="form-check-input" type="radio" name="priority" id="inlinePriority3" value="3">
                                    <label class="form-check-label" for="inlinePriority3">Low</label>
                                </div>
                                {% endif %}
                            </div>
                            <br/>
                            <div class="form-group">
                                <label for="duedate">Due Date:</label>
                                <input type="date" id="duedate" name="duedate" value="{{g.todo.due_date}}" class="form-control">
                            </div>
                            <br />
                            <div class="form-group">
                                <label for="notes">Description:</label>
                                <textarea id="notes" name="notes" rows="4" placeholder="additional details?" class="form-control">{{g.todo.notes}}</textarea>
                            </div>
                            <br />
                            <div class="form-check form-switch">
                                {% if g.todo.completed %} 
                                    <input type="checkbox" id="completed" name="completed" role="switch" checked class="form-check-input">
                                    <label for="completed" class="form-check-label">Completed</label>
                                {% else %}
                                    <input type="checkbox" id="completed" name="completed" role="switch" class="form-check-input">
                                    <label for="completed" class="form-check-label">Completed</label>
                                {% endif %}
                            </div>
                            <br />
                            <button type="submit" class="btn btn-primary" formaction="{{ url_for('update_todo', id=g.todo.id) }}" formmethod="POST">Update</button>
                            <button type="submit" class="btn btn-secondary" formaction="{{ url_for('index') }}" formmethod="GET">Cancel</button>
                        </form>
                    </div>
                </div>
                {% endif %}
            </div>  
        </div>
    </div>
</body>
</html>
```

This code adds three new sections to the `index.html` template:
- The `recommendations-div` section is updated to only show the recommendations when a user selects that functionality.
- The `details-div` section displays the details of a task when the user clicks on a task. The section includes the task name, priority, due date, notes, and completion status.
- The `edit-div` section allows the user to edit the details of a task. The section includes form fields for the task name, priority, due date, notes, and completion status. The user can update the task by clicking the "Update" button or cancel the update by clicking the "Cancel" button.

The code also adds two new buttons to the task list that allow the user to view the details of a task and edit the details of a task. The code also updates the recommendations button to include a refresh button that allows the user to refresh the recommendations.

<br/>

#### 2. Delete the existing database file
Before we can test this change, we will need to delete the `todos.db` file in your directory. This is because we have added columns to the database and to keep things simple we will just start fresh versus trying to update the database schema.  This approach works fine when you are in development, but if this was a production system you would want to update the database schema and migrate the data.  When you do this any items saved in the database will be lost.

> [!WARNING]
> If you do not delete the `todos.db` file you will get an error when you run the app.  The error will be something like `sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) no such column: todos.notes`.  This error is because the database schema does not match the model.

#### 3. Run the Application
Now let's run the application to test the AI recommendations. Open a terminal window in Visual Studio Code and run the following command:

```bash
python app.py
```

The application should start and you should now be able to select across all three tabs and should look something like this:

Home Page:

![home](/Track_2_ToDo_App/Sprint-06%20-%20Advanced%20To-Do%20Details/images/outcome-S06-F01-US01-INDEX.png)

Details Page: (after making edits to the task)

![details](/Track_2_ToDo_App/Sprint-06%20-%20Advanced%20To-Do%20Details/images/outcome-S06-F01-US01-DETAILS-2.png)

Edit Page: (after making and saving edits to the task)
    
![edit](/Track_2_ToDo_App/Sprint-06%20-%20Advanced%20To-Do%20Details/images/outcome-S06-F01-US01-EDIT-2.png)

Recommendations Page:
    
![recommendations](/Track_2_ToDo_App/Sprint-06%20-%20Advanced%20To-Do%20Details/images/outcome-S06-F01-US01-RECOMMENDATIONS.png)

<br/>
🎉 Congratulations! You have now added additional fields to your application allowing users to get have more details about their to-do items.
   
<br/>

> [!NOTE]
> 📄For the full source code for this exercise please see [here](/Track_2_ToDo_App/Sprint-06%20-%20Advanced%20To-Do%20Details/src/app-s06-f01-us01/).


<br/>

[🔼 Back **Workshop** Instructions ](/Track_2_ToDo_App/Workshop-Format.md) | [🔼 Back to **Hackathon** Sprint 6 ](/Track_2_ToDo_App/Sprint-06%20-%20Advanced%20To-Do%20Details/README.md) | [**◀ Previous user story** (in previous sprint)](/Track_2_ToDo_App/Sprint-05%20-%20Advanced%20AI%20recommendations/Feature%201%20-%20Get%20Generative%20AI%20recommendation/User%20Story%203%20-%20Refresh%20Recommendations.md) | [**Next user story** (in next sprint) ▶](/Track_2_ToDo_App/Sprint-07%20-%20Advanced%20Styling%20Your%20Web%20App/Feature%201%20-%20Advanced%20Styling/User%20Story%201%20-%20Add%20Completed%20Checkbox.md)
