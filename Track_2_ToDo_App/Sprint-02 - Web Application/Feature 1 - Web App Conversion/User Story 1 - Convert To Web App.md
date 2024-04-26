# 📖 User Story: Convert to Web App - Step-by-Step
⏲️ _Est. time to complete: 15 min._ ⏲️

## User Story

*As a user, I want to access the application through a web browser, so I can use it on any device with internet connectivity.*

## 🎯Acceptance Criteria:
- Users should be able to access the web app using common web browsers such as Chrome, Firefox, and Edge.
- For this first step, only the ability to print out the saved to-do items is required. The ability to add and remove items will be added in the next user stories. 
- The application should have a user-friendly web interface.  The interface should look something like this:
 
    ![outcome1](/Track_2_ToDo_App/Sprint-02%20-%20Web%20Application/images/outcome-S02-f01-US01.png)

## 🎓Know Before You Start
no resources at this time


## 📋Steps

In order to complete this user story you will need to complete the following tasks

### Install Web Framework
The first step in converting the application to a web application is to install a web framework. We will be using **Flask** for this workshop. Flask is a lightweight web framework that is easy to use and perfect for small projects like this one.

#### 1. Open Visual Studio Code
Open Visual Studio Code and open the source code the folder with your completed solution from the end of Sprint 1 or if you prefer you can use the starting reference application from [here](/Track_2_ToDo_App/Sprint-01%20-%20Basic%20Application/src/app-s01-f02-us02/). 

<br/>

#### 2. Setup Flask Environment
To setup the Flask Environment if it is not already installed you can install it via pip from a terminal window in Visual Studio Code: 

```
pip install flask
```
> [!NOTE]
> Note if you setup the virtual environment through the sprint 0 instructions than Flask will already be installed, you can verify it by `pip list` int the terminal window and looking to see if the Flask module is installed

<br/>

### Convert the Application to a Web Application
> [!TIP]
> You can ask GitHub Copilot to convert a basic python file to a web app. It will generally work well at converting to a starting point that you can adjust and work with. Try it out with a prompt such as: *Convert this app to a flask based web app*

#### 1. Add Flask to the Application
We now need to update our application to include the Flask framework. Open `app.py` and import some important packages from Flask by adding the following to the very top of the file:

```python
from flask import Flask, render_template, request, redirect, url_for
```

Flask is the package that will allow you to create a web application. render_template is a function that will allow you to render an HTML file. request is a package that will allow you to handle requests from the user. redirect and url_for are packages that will allow you to redirect the user to a different page.

<br/>

#### 2. Import the os Package
Next, we want to import the os package to handle file operations. Add the following to the top of the file right after the `from flask...` statement:

```python
import os
```

os is a package that will allow you to interact with the operating system. In this case, you will use it to find the current directory of the application so that we know where to store the file.

<br/>


#### 3. Initialize the Flask App
To use the Flask framework you will need to initialize the Flask app. To do this, add the following right after the `import os` statement in step 2:

```python
app = Flask(__name__)
```

<br/>

#### 4. Get location of the to-do list file 
Since this app will be running as a web application we want to make sure that we load the to-do list from the correct location. To do this, let's create a variable to find the current directory in which this web application is running as well as create the variable to store were the to-do list will be stored.  Put this code right underneath your app initialization:

```python
basedir = os.path.abspath(os.path.dirname(__file__))
todo_file = os.path.join(basedir, 'todo_list.txt')
```

<br/>

#### 5. Load the to-do list from the file
We now need to make sure that we are loading the file from the right directory, replace the `with open(...)` statement in the file with the following code:

```python
with open(todo_file, "r") as file:
```  

This code replaces the prevously hard-code file name with the variable `todo_file` that we created in the earlier sprint to make sure that we are loading from the right location.

<br/>

#### 6. Create a route for the homepage
Now that we are using the Flask Framework we will also need to define the entry point for the application on the back-end server.  You do this by creating "routes".  Routes are the URL paths that the user can access in the web application.  You will need to define a route for the homepage.  To do this, add the following code snippet below to replace ALL of the code starting with the `while True:` statement all the way to the end of the file.  This code is no longer needed for the web application.

![replacecode](/Track_2_ToDo_App/Sprint-02%20-%20Web%20Application/images/ReplaceCode-S2-F1-US01-01.png)

with the following code:

```python
@app.route("/")
def index():
    with open(todo_file, "r") as file:
        todo_list = file.read().splitlines()
    return render_template("index.html", todo_list=todo_list)
```

Routes are defined using the @app.route decorator. This decorator tells Flask that the function below it is a route. In this case, the route is the homepage ("/"). The function below the decorator is called index. This function will read the todo_list.txt file and pass the todo_list variable to the index.html file.

<br/>

#### 7. Create Application starting point
Finally, to enable the app to run you need to add this code to the bottom of the file:

```python
if __name__ == "__main__":
    app.run(debug=True)
```

This code will run the Flask app when you run the Python script. The debug=True parameter will allow you to see any errors in the browser when you run the app.

> [!NOTE]
> In a production environment you would set Debug=False so that end-users would NOT see a stack trace when something fails.

<br/>

#### 8. Create the User Interface for the Web Application
At this point, you have the backend functionality to run the Flask app, but you need to define a front end page to render the view. To do this you will need to define the html to display when the homepage route is engaged. 

Create a ```index.html``` file in a subfolder called ```templates```.

![Directory01](/Track_2_ToDo_App/Sprint-02%20-%20Web%20Application/images/Directory01.png)

Add the following code to this index.html file:

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
</body>
</html>
```

This code will create a basic HTML page that will display the to-do list items in an ordered list. The `{% for todo in todo_list %}` loop will iterate through each item in the todo_list and display it as a list item. The `{{ todo }}` will display the item in the list.  The use of `{% ... %}` in the HTML are used to render dynamic content for a flash application and are called Jinja2 templates.

<br/>

#### 9. Run the Application
You can now test this out by running ```python app.py```. This will launch a browser and show the home page (or you can browse to http://localhost:5000). You can add tasks to a to-do_list.txt file to see them display on the page.

![WebApp01](/Track_2_ToDo_App/Sprint-02%20-%20Web%20Application/images/outcome-S02-f01-US01.png)

🎉 Congratulations! You have now updated your basic application to the most basic web application.  In the next set of user stories we will add back in the functionality to add a to-do list item as well as delete one. 

<br/>

> [!NOTE]
> 📄For the full source code for this exercise please see [here](/Track_2_ToDo_App/Sprint-02%20-%20Web%20Application/src/app-s02-f01-us01/).

<br/>

[🔼 Back **Workshop** Instructions ](/Track_2_ToDo_App/Workshop-Format.md) | [🔼 Back to **Hackathon** Sprint 2 ](/Track_2_ToDo_App/Sprint-02%20-%20Web%20Application/README.md) | [**◀ Previous user story** (in previous sprint)](/Track_2_ToDo_App/Sprint-01%20-%20Basic%20Application/Feature%202%20-%20Save%20To-Do%20List/User%20Story%202%20-%20Load%20To-Do%20List%20from%20File.md) | [**Next user story** ▶](User%20Story%202%20-%20Add%20Item%20through%20Web%20Form.md)



