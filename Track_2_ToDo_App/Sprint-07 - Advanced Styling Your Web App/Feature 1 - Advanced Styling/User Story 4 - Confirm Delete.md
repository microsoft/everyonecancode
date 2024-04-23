# User Story: Confirm Delete - Step-by-Step
⏲️ _Est. time to complete: 30 min._ ⏲️

## User Story 
*As a user, I want to be able to verify that you really want to delete a task before deleting it.*

## 🎯Acceptance Criteria:
- A modal dialog should be displayed when the delete button is clicked to verify if you really want to delete the selected item
- The modal dialog should have a cancel and confirm button
- If the confirm button is clicked, the task should be deleted
- If the cancel button is clicked, the modal dialog should be closed and the task should not be deleted
- The interface should look something like this:

  ![Index](/Track_2_ToDo_App/Sprint-07%20-%20Advanced%20Styling%20Your%20Web%20App/images/outcome-S07-F01-US04.png)

## 🎓Know Before You Start
no resources at this time

## 📋Steps

In order to complete this user story you will need to complete the following tasks

### Open Visual Studio Code
Open Visual Studio Code and open the source code the folder with your completed solution from the previous user story if you prefer you can use the starting reference application from [here](/Track_2_ToDo_App/Sprint-07%20-%20Advanced%20Styling%20Your%20Web%20App/src/app-s07-f01-us03/)

<br/>

### Delete Confirmation
If you currently run the application, you may have noticed that if you accidentally hit the "remove" button on any task, the task is immediately deleted.  This is generally thought of as a bad user experience.  To improve this, we will add a modal dialog to confirm that you really want to delete a task before deleting it.

#### 1. Add additional Bootstrap script 
First, we need to add an additional bootstrap script to the `index.html` file to add support for modal dialogues. Open the `index.html` file and add the following code within the `<head>` tag:

```html
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
```
<br/>

#### 2. Update the user interface to include a modal dialog
First, we need to add a modal dialog to the application. Open the `index.html` file and add the following code to the bottom of the file before the closing `</body>` tag:

```html
<!-- Bootstrap Modal -->
<div class="modal" tabindex="-1" id="confirmModal">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Delete Task</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <p>Are you sure you want to delete?</p>
          <p id="taskName"></p>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
          <a type="button" class="btn btn-danger" id="deleteLink">Delete</a>
        </div>
      </div>
    </div>
</div>
```

This code will add a modal dialog to the application. The modal dialog will have a title of "Delete Task", a message asking the user if they are sure they want to delete the task, a cancel button, and a delete button. The modal dialog will be hidden by default.

<br/>

#### 3. Update the remove button to show the modal dialog
Next we need to update the remove button to show the modal dialog when the delete button is clicked. Open the `app.js` file replace the `<button type='submit'...>Remove</button>` with the following code:

```html
<a type="button" class="btn btn-danger delete-btn" data-bs-toggle="modal" data-bs-target="#confirmModal" data-url="{{ url_for('remove_todo', id=todo.id) }}" data-taskname="{{ todo.name }}"">Remove</a>
```

<br/>

#### 4. Add an event listener to the delete button
Next, we need to add an event listener to the delete button to show the modal dialog when the delete button is clicked. Open the `app.js` file and add the following code within the DOMContentLoaded event listener:

```javascript
const myModal = document.getElementById('confirmModal')
const deleteButtons = document.getElementsByClassName('delete-btn');
Array.from(deleteButtons).forEach((deleteButton) => {
    deleteButton.addEventListener('click', function(e) {
        e.stopPropagation();
        e.preventDefault();
        const url = this.getAttribute('data-url');
        document.getElementById('deleteLink').setAttribute('href', url);
        const taskname_paragraph = document.querySelector("p[id='taskName']");
        const taskname = this.getAttribute('data-taskname');
        taskname_paragraph.textContent = taskname;
        myModal.addEventListener('shown.bs.modal', () => {
            deleteButton.focus()
        })
        clearHighlight();
    });
});
```

This code will add an event listener to the delete button. When the delete button is clicked, the code will get the URL of the delete link and the name of the task to be deleted. The code will then set the href attribute of the delete link to the URL of the delete link and set the text of the task name paragraph to the name of the task to be deleted.

<br/>

#### 5. Run the application
Save the changes to the `app.js` and `index.html` files and run the application. Open the application in a browser and try to delete a task. A modal dialog should be displayed asking if you are sure you want to delete the task. If you click the delete button, the task should be deleted. If you click the cancel button, the modal dialog should be closed and the task should not be deleted.  The interface should look something like this:

![Index](/Track_2_ToDo_App/Sprint-07%20-%20Advanced%20Styling%20Your%20Web%20App/images/outcome-S07-F01-US04.png)

<br/>

🎉 Congratulations! You have now updated the user interface to confirm that you really want to delete a task before deleting it.

<br/>

> [!NOTE]
> 📄For the full source code for this exercise please see [here](/Track_2_ToDo_App/Sprint-07%20-%20Advanced%20Styling%20Your%20Web%20App/src/app-s07-f01-us04/).

<br/>

[🔼 Back **Workshop** Instructions ](/Track_2_ToDo_App/Workshop-Format.md) | [🔼 Back to **Hackathon** Sprint 7 ](/Track_2_ToDo_App/Sprint-07%20-%20Advanced%20Styling%20Your%20Web%20App/README.md) | [**◀ Previous user story** ](User%20Story%203%20-%20Prevent%20User%20from%20adding%20blank%20task.md) | [**Next user story**  ▶](User%20Story%205%20-%20Show%20Spinner.md)

