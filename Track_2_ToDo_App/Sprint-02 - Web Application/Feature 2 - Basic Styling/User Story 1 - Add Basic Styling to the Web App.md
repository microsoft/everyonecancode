# 📖 User Story: Add Basic Styling to the Web App - Step-by-Step
⏲️ _Est. time to complete: 10 min._ ⏲️

## User Story

*As a user, I want to have a basic stylized interface to look and feel more like a proper web app*

## 🎯Acceptance Criteria:
- The web app should have some basic style features to look like a modern web application.  The interface should look something like this:

    ![outcome4](/Track_2_ToDo_App/Sprint-02%20-%20Web%20Application/images/outcome-S02-f02-US01.png)

## 🎓Know Before You Start
no resources at this time

## 📋Steps

In order to complete this user story you will need to complete the following tasks

### Open Visual Studio Code
Open Visual Studio Code and open the source code the folder with your completed solution from the previous user story if you prefer you can use the starting reference application from [here](/Track_2_ToDo_App/Sprint-02%20-%20Web%20Application/src/app-s02-f01-us03/) 

### Updating the Web Application Frontend

#### 1. Add Bootstrap to the Application
When it come to creating a modern web application using modern styling, the bootstrap framework has become one of the most popular choices. We are going to use bootstrap for some basic styling. Go to https://getbootstrap.com/ and get the Include via CDN link. Add this link in between the `<head>` tags in your `index.html` as so:

```html
<head>
    <title>To-Do List</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>
```

> [!NOTE]
> Bootstrap is a popular CSS framework that provides a wide range of styles and components for building modern web applications. By including the Bootstrap CSS file in your HTML, you can easily apply these styles to your web app.

<br/>

#### 2. Update the HTML to use Bootstrap classes
To take advantage of bootstrap we will need to make some changes to our HTML. Replace the content of the `<body>` in the `index.html` file with the following code:

>[!TIP]
>You can highlight the body code and ask Copilot to update to use bootstrap with a prompt like *update to use bootstrap styling*

```html
<body>
    <div class="container">
        <h1 class="text-center my-4">To-Do List</h1>
        <div class="row">
            <div class="col-12">
                <ol class="list-group list-group-numbered">
                    {% for todo in todo_list %}
                        <li class="list-group-item">{{ todo }}</li>
                    {% endfor %}
                </ol>
            </div>
        <div class="row">
            <div class="col-6">
                <form action="/add" method="post" class="my-4">
                    <div class="form-group">
                        <label for="todo">Add a to-do:</label>
                        <input type="text" name="todo" class="form-control">
                    </div>
                    <button type="submit" class="btn btn-primary">Add</button>
                </form>
            </div>
            <div class="col-6">
                <form action="/remove" method="post" class="my-4">
                    <div class="form-group">
                        <label for="item_number">Remove task number:</label>
                        <input type="number" name="item_number" min="1" class="form-control">
                    </div>
                    <button type="submit" class="btn btn-danger">Remove</button>
                </form>
            </div>
        </div>
    </div>
</body>
```
    
The code above uses Bootstrap classes to style the elements on the page. The container class creates a centered container for the content, while the text-center class centers the heading. The list-group and list-group-item classes create a styled list for the to-do items. The form-group and form-control classes style the form elements, and the btn and btn-primary classes style the buttons.

<br/>

#### 3 Run the Application
Run the app by running ```python app.py``` in the terminal and browse to the local site. It should now look something like this:
    
![outcome](/Track_2_ToDo_App/Sprint-02%20-%20Web%20Application/images/outcome-S02-f02-US01.png)


<br/>
🎉 Congratulations! You have now updated your web application to have some basic styling. This will serve as a foundation for the rest of the workshops.

<br/>

> [!NOTE]
> 📄For the full source code for this exercise please see [here](/Track_2_ToDo_App/Sprint-02%20-%20Web%20Application/src/app-s02-f02-us01/).


[🔼 Back **Workshop** Instructions ](/Track_2_ToDo_App/Workshop-Format.md) | [🔼 Back to **Hackathon** Sprint 2 ](/Track_2_ToDo_App/Sprint-02%20-%20Web%20Application/README.md) | [**◀ Previous user story**](/Track_2_ToDo_App/Sprint-02%20-%20Web%20Application/Feature%201%20-%20Web%20App%20Conversion/User%20Story%203%20-%20Remove%20Item%20through%20Web%20Form.md) | [**Next user story** ▶](User%20Story%202%20-%20Personalize%20Website.md)



