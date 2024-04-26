# User Story: Add Tabbed Interface - Step-by-Step
⏲️ _Est. time to complete: 30 min._ ⏲️

## User Story 
*As a user, I want to have a cleaner interface for my tasks and move the details, edit and recommendation buttons over to a tabbed interace to reduce clutter*

## 🎯Acceptance Criteria:
- A tabbed interface should be added to the main page with the following tabs: Details, Edit, Recommendations that get displayed when selecting an item from the primary list.
- The Details tab should display the task details
- The Edit tab should allow the user to edit the task
- The Recommendations tab should display the recommendations for the task
- The Details, Edit and Recommendations buttons should be removed from the main list
- The interface should look something like this:
    ![Index](/Track_2_ToDo_App/Sprint-07%20-%20Advanced%20Styling%20Your%20Web%20App/images/outcome-S07-F01-US02.png)

## 🎓Know Before You Start
no resources at this time

## 📋Steps

In order to complete this user story you will need to complete the following tasks

### Open Visual Studio Code
Open Visual Studio Code and open the source code the folder with your completed solution from the previous user story if you prefer you can use the starting reference application from [here](/Track_2_ToDo_App/Sprint-07%20-%20Advanced%20Styling%20Your%20Web%20App/src/app-s07-f01-us01/)

<br/>

### Updating the Web Application Frontend
To get a tabbed-type interface working and functional in the web application, you will need to make the following changes:
- Add a tabbed user interface element to the main page
- Update the styles for the tabbed interface
- Update the application so that you can select a task by clicking on it in the list
- Remove the Details, Edit, and Recommendations buttons from the main list

#### 1. Add a tabbed user interface element to the main page
First, we will add the tabbed user interface element to the `index.html` file. To do this, add the following code right below the `<div class="col-5">` and before the `{% if g.todo != None and g.selectedTab == g.TabEnum.RECOMMENDATIONS %}`:

![ReplaceCode](/Track_2_ToDo_App/Sprint-07%20-%20Advanced%20Styling%20Your%20Web%20App/images/ReplaceCode-S07-F01-US02-01.png)

with the following code:

```html
{% if g.selectedTab != g.TabEnum.NONE %}
    <ul class="nav nav-tabs">
        <li class="nav-item">
            <a id="details-tab" class="nav-link" aria-current="page" href="{{ url_for('details', id=g.todo.id) }}">Details</a>
        </li>
        <li class="nav-item">
            <a id="edit-tab" class="nav-link" href="{{ url_for('edit', id=g.todo.id) }}">Edit</a>
        </li>
        <li class="nav-item">
            <a id="recommendations-tab" class="nav-link" href="{{ url_for('recommend', id=g.todo.id) }}">Recommendations</a>
        </li>
    </ul>
{% endif %}
```

This code will add a tabbed interface to the right panel of the main page. The tabbed interface will have three tabs: Details, Edit, and Recommendations. The tabs will link to the appropriate routes in the application.

<br/>

#### 2. Update the styles for the tabbed interface
You will then need to update the styles for the application . Open the `styles.css` file and add the following code:

```css
.card {
    border-top: none !important;
}

.nav-link {
    background-color: white;
}

.highlighted-item {
    background-color: #f2f2f2;
}
```

This code will update the syles for the tabbed inferface and highlighted items in the application. The code does the following:
- The `card` class will have the top border removed from the previous Details, Edit and Recommendation panes so that it lines up directly below the tabbed interface and looks like one piece. 
- The `nav-link` class is part of the tabbed interface and will have a white background color. 
- The `highlighted-item` class will have a light gray background color and will be used in an upcoming step for highlighting tasks items.

<br/>

#### 3. Run the Application
If you run the application now you will see that the Details, Edit, and Recommendations have been added to the tabbed interface on the right panel of the main page. You can click on the tabs to view the different sections of the task details, edit, and recommendations.  
![Tabbed Interface](/Track_2_ToDo_App/Sprint-07%20-%20Advanced%20Styling%20Your%20Web%20App/images/tabbed-interface-S07-F01-US02-1.png)

Note however that the user interface is still not complete
- the Details, Edit, and Recommendations buttons are still visible on the main list
- you can't select a task by clicking on it in the main list, 
- the selected task is not highlighted when the button's are pressed
- and the tabbed interface really doesn't show which tab is active. 

We will address these in the next set of steps.

<br/>

### Selecting a task by clicking on it in the list
#### 1. Add a showDetails function to user interface
Before we remove the buttons, we need to update the application so that you can select a task by clicking on it in the list otherwise there wouldn't be a way to view the Details, Edit, and Recommendations tabs. Open the `index.html` file and replace the `<li id="task-{{ todo.id }}"...>` with the following code:

```html
<li id="task-{{ todo.id }}" data-id="{{ todo.id }}" class="list-group-item d-flex justify-content-between" onclick="showDetails(this)">
```

This code adds a showDetails function to the task item in the list. The showDetails function will be used to select a task by clicking on it. 

<br/>

#### 2. Implement the showDetails function
We now need to implement the showDetails function as well as several other functions to help with highlighting the selected item and visually showing the right tab. Open the `app.js` file and replace the `handleClick` function 

```javascript
    window.handleClick = function (event, cb) {
        event.stopPropagation();
        const rootUrl = window.location.origin;
        const cbId = cb.id;
        const cbChecked = cb.checked;
        window.location.href = `${rootUrl}/completed/${cbId}/${cbChecked}`;
    };
```

with the following code:

```javascript
const HIGHLIGHTEDITEM = 'highlighted-item';
const currentPath = window.location.pathname;

// Set the active tab based on the URL
const setActiveTab = (tabId) => {
    const tabElement = document.getElementById(tabId);
    if (tabElement) {
        tabElement.classList.add('active');
    }
};

switch (true) {
    case currentPath.includes('/edit'):
        setActiveTab('edit-tab');
        break;
    case currentPath.includes('/completed'):
        setActiveTab('completed-tab');
        break;
    case currentPath.includes('/details'):
        setActiveTab('details-tab');
        break;
    case currentPath.includes('/recommend'):
        setActiveTab('recommendations-tab');
        break;
    default:
        break;
}
    
const highlightedItemId = localStorage.getItem(HIGHLIGHTEDITEM);
console.log('highlightedItemId', highlightedItemId);
if (highlightedItemId) {
    const highlightedItem = document.getElementById(highlightedItemId);
    if (highlightedItem) {
        highlightedItem.classList.add(HIGHLIGHTEDITEM);
    }
}

window.clearHighlight = function() {
    localStorage.removeItem(HIGHLIGHTEDITEM);
};

window.showDetails = function(li) {
    highlight(li);
    const rootUrl = window.location.origin;
    const dataId = li.getAttribute('data-id');
    window.location.href = `${rootUrl}/details/${dataId}`;
};

window.handleClick = function(event, cb) {
    event.stopPropagation();
    const rootUrl = window.location.origin;
    const cbId = cb.id;
    const cbChecked = cb.checked;
    window.location.href = `${rootUrl}/completed/${cbId}/${cbChecked}`;
    clearHighlight();
};


window.highlight = function(element) {
    const highlightedItemId = localStorage.getItem(HIGHLIGHTEDITEM);
    if (highlightedItemId) {
        const highlightedItem = document.getElementById(highlightedItemId);
        if (highlightedItem) {
            highlightedItem.classList.remove(HIGHLIGHTEDITEM);
        }
    }

        const closestListItem = element.closest('li');
        closestListItem.classList.add(HIGHLIGHTEDITEM);

        localStorage.setItem(HIGHLIGHTEDITEM, closestListItem.id);
};
```

This code implements the following:
- **adds a showDetails function** that will be called when a task item is clicked. The function will highlight the selected task item and then redirect the user to the Details tab for the selected task. 
- The **highlight function** will add a class to the selected task item to visually differentiate it from the other task items.
- The **setActiveTab function** will set the active tab based on the URL. 
- The **handleClick function** will be called when the checkbox is clicked and will redirect the user to the completed tab for the selected task. 
- The **clearHighlight function** will remove the highlighted class from the selected task item. 

<br/>

#### 3. Run the Application
If you run the application now you will see that you can select a task by clicking on it in the list. The selected task will be highlighted and the Details tab will be displayed in the right panel.  The details tab name will also show in black font to show that it is highlight. These changes are somewhat subtle but enhance the overall user experience and help the end user see where they are at in the application.  

![Tabbed Interface-2](/Track_2_ToDo_App/Sprint-07%20-%20Advanced%20Styling%20Your%20Web%20App/images/tabbed-interface-S07-F01-US02-2.png)

Note however, that the Details, Edit, and Recommendations buttons are still visible on the main list. We will remove these in the next step. 

<br/>

#### Removing extra buttons from the main list

#### 1. Remove the Details, Edit, and Recommendations buttons from the main list
Next, we need to remove the Details, Edit, and Recommendations buttons from the main list. Open the `index.html` file and remove the following code from the `<li id="task-{{ todo.id }}"...>`:

```html
<button type="submit" class="btn btn-success" formaction="{{ url_for('details', id=todo.id) }}" formmethod="GET">Details</button>
<button type="submit" class="btn btn-success" formaction="{{ url_for('edit', id=todo.id) }}" formmethod="GET">Edit</button>
<button type="submit" class="btn btn-success" formaction="{{ url_for('recommend', id=todo.id) }}" formmethod="GET">Recommendations</button>
```

This code will remove the Details, Edit, and Recommendations buttons from the main list. The tabs on the right panel will now be the only way to access the Details, Edit, and Recommendations sections of the task.

#### 2. Run the Application
Run the application again and you will see that the Details, Edit, and Recommendations buttons have been removed from the main list.  This will help to reduce clutter and provide a cleaner interface for users to interact with. 

![Tabbed Interface-3](/Track_2_ToDo_App/Sprint-07%20-%20Advanced%20Styling%20Your%20Web%20App/images/tabbed-interface-S07-F01-US02-3.png)

<br/>

### Updating Add button to remove highlighting from previously selected task

#### 1. Add an onclick event to the Add button
If you add a new task you may notice that the highlighting is not removed from the previously selected task. This is because the highlighted class is not being removed when a new task is created. To fix this, we need to make an update the `index.html` with the following code:

```html
<button type="submit" class="btn btn-success" onclick="clearHighlight()">Add</button>
```
This code will add an `onclick` event to the Add button that will call the `clearHighlight` function when the button is clicked. The `clearHighlight` function will remove the highlighted class from the selected task item.

<br/>

#### 2. Run the Application
If you run the application now you will see that the Details, Edit, and Recommendations buttons have been removed from the main list. You can select a task by clicking on it in the list and the selected task will be highlighted. The Details, Edit, and Recommendations tabs will be displayed in the right panel. You can click on the tabs to view the different sections of the task details, edit, and recommendations. If you add a new task, the highlighting will be removed from the previously selected task.

<br/>

🎉 Hooray! You have successfully added a tabbed interface to the main page of your application. This will help to reduce clutter and provide a cleaner interface for users to interact with.

<br/>

> [!NOTE]
> 📄For the full source code for this exercise please see [here](/Track_2_ToDo_App/Sprint-07%20-%20Advanced%20Styling%20Your%20Web%20App/src/app-s07-f01-us02/).

<br/>

[🔼 Back **Workshop** Instructions ](/Track_2_ToDo_App/Workshop-Format.md) | [🔼 Back to **Hackathon** Sprint 7 ](/Track_2_ToDo_App/Sprint-07%20-%20Advanced%20Styling%20Your%20Web%20App/README.md) | [**◀ Previous user story** ](User%20Story%201%20-%20Add%20Completed%20Checkbox.md) | [**Next user story**  ▶](User%20Story%203%20-%20Prevent%20User%20from%20adding%20blank%20task.md)
