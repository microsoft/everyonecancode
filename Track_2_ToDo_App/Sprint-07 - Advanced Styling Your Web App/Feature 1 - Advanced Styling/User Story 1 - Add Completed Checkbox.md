# User Story: Add Completed Checkbox and due date details to main list - Step-by-Step
⏲️ _Est. time to complete: 30 min._ ⏲️

## User Story 
*As a user, I want to be able to mark a task as complete from the main list as well see the due date of a task if one is defined*

## 🎯Acceptance Criteria:
- A checkbox should be added to the task list to allow users to mark a task as complete.
- The task should be visually differentiated when marked as complete. i.e., by using strikethrough text on the task name.
- The due date of the task should be displayed in a friendly format underneath the name of the task.
    - If a due date is past due, the due date should be displayed inside a red badge .  
    - If a due date is in the future, the due date should be displayed in light blue badge.
    - If there is no due date set for the task, then nothing should display for the due date.
- The interface should look something like this:

    ![Index](/Track_2_ToDo_App/Sprint-07%20-%20Advanced%20Styling%20Your%20Web%20App/images/outcome-S07-F01-US01.png)


## 🎓Know Before You Start
no resources at this time

## 📋Steps

In order to complete this user story you will need to complete the following tasks

### Open Visual Studio Code
Open Visual Studio Code and open the source code the folder with your completed solution from the previous user story if you prefer you can use the starting reference application from [here](/Track_2_ToDo_App/Sprint-06%20-%20Advanced%20To-Do%20Details/src/app-s06-f01-us01/)

<br/>

### Updating the Web Application Backend

#### 1. New Completed Status Route
In order to support the ability to mark a task as complete when the user checks the checkbox, we will need to add a new route to the backend that will update the completed status of a task. Open the `app.py` file and add the following code to the bottom of the file before the `if __name__ == '__main__':` line:

```python
@app.route('/completed/<int:id>/<complete>', methods=['GET'])
def completed(id, complete):
    g.selectedTab = Tab.NONE
    g.todo = Todo.query.filter_by(id=id).first()
    if (g.todo != None and complete == "true"):
        g.todo.completed = True
    elif (g.todo != None and complete == "false"):
        g.todo.completed = False

    #update todo in the database
    db.session.add(g.todo)
    db.session.commit()
    #
    return redirect(url_for('index'))    
 ```

This code will create a new route called `/completed` that will take in the id and complete status of the task. It will then get the task from the database, update the completed status of the task, and then redirect the user back to the main task list.

<br/>

#### 2. Create a Context Processor to Pass the Current Date to the User Interface
Per the acceptance criteria above there is a requirement to display the due date of the task in a friendly format underneath the name of the task as well as understand if the due date is past due or in the future. To support this requirement, we will need update the app to pass the current date to the user interface.  We could continue to do this through the flask global module  `g` in a similar way that we pass the other variables, but for the sake of this exercise we wanted to show you another way to pass variables to the user interface.  We will do this through context processors.   To enable this we first need to create a new file called `context_processors.py` in the `app` folder.  Add the following code to the file:

```python
from datetime import datetime

def inject_current_date():
    return {'current_date': datetime.now().strftime('%Y-%m-%d')}    
```

This code will create a function called `inject_current_date` that will return the current date in the format `YYYY-MM-DD`.

<br/>

#### 3. Import Context Processor module into the Application
We will then need to add this functionality to our flask application by making two changes to the `app.py` file.  First, we need to import the context processor into the application. Add the following code to the top of the file:

```python
from context_processors import inject_current_date
```
<br/>

#### 4. Register the Context Processor with the Application
Next we will need to register the context processor with the application. Add the following code to the top of the `app.py` file after the `db.init_app(app) with app.app_context(): db.create_all()` lines:

```python
@app.context_processor
def inject_common_variables():
    return inject_current_date()
```
This code will register the `inject_current_date` function as a context processor with the application. This will allow the `current_date` variable to be passed to the user interface on every request, which will be used in a later step to decide how we display the due date of the task (i.e., past due or in the future).   

<br/>

### Updating the Web Application Frontend
There are several changes that we need to make to the user interface to support the ability to mark a task as complete and display the due date of the task.

#### 1. Update the Task List to Include a Checkbox and Due Date Details
First, we need to add a checkbox to the task list and the due date details. Open the `index.html` file and update the code between the `{% for todo in g.todos %}...{% endfor %}` tags as seen below:

Replace the code below:

```html
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
```

with the following code: 

```html
{% for todo in g.todos %}
<li id="task-{{ todo.id }}" data-id="{{ todo.id }}" class="list-group-item d-flex justify-content-between">
    <div class="task">
        <div class="form-check">
            {% if todo.completed %}
                <input class="form-check-input" type="checkbox" id="{{ todo.id }}" checked onclick="handleClick(event, this)">
            {% else %}
                <input class="form-check-input" type="checkbox" id="{{ todo.id }}" onclick="handleClick(event, this)">
            {% endif %}
                                 
            <div class="title" id="title-{{ todo.id }}">{{ todo.name }}</div>
            <div class="subtitle" id="duedate-{{ todo.id }}">
                {% if todo.completed %}
                    <small class="badge bg-success">Completed</small>
                {% elif todo.due_date %}
                    {% if todo.due_date < current_date %}
                        <small class="badge bg-danger">Past Due: {{ todo.due_date }}</small>
                    {% else %}
                        <small class="badge bg-info">Due Date: {{ todo.due_date }}</small>
                    {% endif %}
                {% endif %}
            </div>
        </div>
    </div>
    <span>
        <button type="submit" class="btn btn-success" formaction="{{ url_for('details', id=todo.id) }}" formmethod="GET">Details</button>
        <button type="submit" class="btn btn-success" formaction="{{ url_for('edit', id=todo.id) }}" formmethod="GET">Edit</button>
        <button type="submit" class="btn btn-success" formaction="{{ url_for('recommend', id=todo.id) }}" formmethod="GET">Recommendations</button>
        <button type="submit" class="btn btn-danger" formaction="{{ url_for('remove_todo', id=todo.id) }}" formmethod="POST">Remove</button>
    </span>
</li>
{% endfor %}
```

This code will adds the following functionality:
- **add a checkbox to the task list**. Upon loading of the web page, if the task is marked as completed, the checkbox will be checked. If the task is not completed, the checkbox will be unchecked. This is handled through the `checked` attribute in the `<input>` tag. There is also an `onclick` event that will call the `handleClick` function when the checkbox is clicked. This function will be created in the next step.
- **due date** - If there is a due date assigned, the due date will be displayed in a friendly format underneath the name of the task. If the task is marked as completed, a "Completed" badge will be displayed. If the task is past due, a "Past Due" badge will be displayed in red text. If the task is not past due, a "Due Date" badge will be displayed in blue text.

<br/>

#### 2. Add Javascript to Handle Checkbox Click
Next, we need to add the `handleClick` function to the `static/js/app.js` file. Open the `app.js` file and add the following code within the DOMContentLoaded event listener:

```javascript
window.handleClick = function(event, cb) {
    event.stopPropagation();
    const rootUrl = window.location.origin;
    const cbId = cb.id;
    const cbChecked = cb.checked;
    window.location.href = `${rootUrl}/completed/${cbId}/${cbChecked}`;
};
```

This code will create a function called `handleClick` that will be called when the checkbox is clicked. The function will stop the event from propagating, get the id and checked status of the checkbox, and then redirect the user to the `/completed` route with the id and checked status as parameters.

<br/>

## 3. Update the `style.css` File
Finally, we will need to update the `style.css` file to add a strikethrough effect to the task name when it is marked as completed. Add the following code to the bottom of the file:

```css
.form-check input[type="checkbox"]:checked + .title {
    text-decoration: line-through;
}

.title {
    display: inline-flex;
    font-weight: bold;
    color: #333;
}

.subtitle {
    font-size: 14px;
    color: #666;
    padding-left: 20px;
}
```

This code will add a strikethrough effect to the task name when the task is marked as completed.  It will also update the styling of the task name and due date to make it more visually appealing.

<br/>

#### 4. Run the Application
Now let's run the application to see the checkbox in action. Open a terminal window in Visual Studio Code and run the following command:

```bash
python app.py
```

You should now see a checkbox next to each task in the task list. When you click on the checkbox, the task should be marked as completed and visually differentiated with a strikethrough effect. The web page should look something like this:

![outcome-S07-F01-US01](/Track_2_ToDo_App/Sprint-07%20-%20Advanced%20Styling%20Your%20Web%20App/images/outcome-S07-F01-US01.png)


<br/>
🎉 Congratulations! You have now updated the user interface to include a checkbox to mark tasks as completed and visually differentiate completed tasks.
<br/>

> [!NOTE]
> 📄For the full source code for this exercise please see [here](/Track_2_ToDo_App/Sprint-07%20-%20Advanced%20Styling%20Your%20Web%20App/src/app-s07-f01-us01/).

<br/>

[🔼 Back **Workshop** Instructions ](/Track_2_ToDo_App/Workshop-Format.md) | [🔼 Back to **Hackathon** Sprint 7 ](/Track_2_ToDo_App/Sprint-07%20-%20Advanced%20Styling%20Your%20Web%20App/README.md) | [**◀ Previous user story** (in previous sprint)](/Track_2_ToDo_App/Sprint-06%20-%20Advanced%20To-Do%20Details/Feature%201%20-%20Add%20Additional%20To-Do%20Details/User%20Story%201%20-%20Add%20additional%20details%20to%20to-do%20item.md) | [**Next user story**  ▶](User%20Story%202%20-%20Add%20Tabbed%20Interface.md)
