# User Story: Prevent User from adding blank task and limit characters- Step-by-Step
⏲️ _Est. time to complete: 30 min._ ⏲️

## User Story 
*As a user, I want to prevent someone from accidentally entering a task with no name and I want to limit the name to 75 characters*

## 🎯Acceptance Criteria:
- Disable add button if the task name is blank
- Enable add button if the task name is not blank
- Don't allow the user to add a task if the task name is blank
- Limit the task name to 75 characters
- The interface should look something like this:

    ![Index](/Track_2_ToDo_App/Sprint-07%20-%20Advanced%20Styling%20Your%20Web%20App/images/outcome-S07-F01-US03.png)
  

## 🎓Know Before You Start
no resources at this time


## 📋Steps

In order to complete this user story you will need to complete the following tasks

### Open Visual Studio Code
Open Visual Studio Code and open the source code the folder with your completed solution from the previous user story if you prefer you can use the starting reference application from [here](/Track_2_ToDo_App/Sprint-07%20-%20Advanced%20Styling%20Your%20Web%20App/src/app-s07-f01-us02/)


### Update the user interface to prevent adding a blank task

#### 1. Update the user interface elements to support this functionality
The first step is to update the user interface elements to support this functionality.  Open the `index.html` file and replace the `<form action="/add" method="post" class="my-4">... </form` tag with the following code:

```html
<form action="/add" method="post" class="my-4">
    <span class="input-group-text">
        <input type="text" id="todo" name="todo" maxlength="75" class="form-control" placeholder="Add a new task">
                        
        <button type="button" class="btn btn-outline-secondary" onclick="captureVoice()">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-mic" viewBox="0 0 16 16">
                <path d="M3.5 6.5A.5.5 0 0 1 4 7v1a4 4 0 0 0 8 0V7a.5.5 0 0 1 1 0v1a5 5 0 0 1-4.5 4.975V15h3a.5.5 0 0 1 0 1h-7a.5.5 0 0 1 0-1h3v-2.025A5 5 0 0 1 3 8V7a.5.5 0 0  1 .5-.5"></path>
                <path d="M10 8a2 2 0 1 1-4 0V3a2 2 0 1 1 4 0zM8 0a3 3 0 0 0-3 3v5a3 3 0 0 0 6 0V3a3 3 0 0 0-3-3"></path>
            </svg>
            <span class="visually-hidden" title="Use Microphone"></span>
        </button>
        <button type="submit" id="addButton" class="btn btn-success" onclick="clearHighlight()" disabled>Add</button>
    </span>
    <small class="limit-text">Maximum 75 characters</small>
</form>
```
We are making the following changes to the form:
- We are adding a `maxlength` attribute to the input field with a value of 75. This will limit the number of characters the user can enter in the input field to 75.  
- We are adding an id of `addButton` to the button tag and setting the `disabled` attribute to `true`. This will disable the button by default. The button will be enabled when the user types in the input field.  the id of `addButton` will be used by the javascript code to enable and disable the button in one of the next steps.
- We are adding a `<small>` tag with a class of `text-muted` to display a message to the user that the maximum number of characters is 75.

<br/>

#### 2. Add Javascript listener to enable the add button when the task name is not blank
Next, we need to add a check to see if the task name is blank. Open the `app.js` file and add the following function: 

```javascript
nameInput.addEventListener("keyup", function() {
    const addButton = document.querySelector("button[id='addButton']");
    addButton.disabled = this.value.trim() === "";
});
```
This code will add an event listener to the input field with the id of `todo`. When the user types in the input field, the function will check if the value of the input field is blank. If the value is blank, the add button will be disabled. If the value is not blank, the add button will be enabled.

<br/>

#### 3. Update `recognition.onresult` function
We also need to update the `recognition.onresult` function in our Javascript to enable the add button when the name input field is updated with the voice functions. Open the `app.js` file and replace the `recognition.onresult` function with the following code: 

```javascript
recognition.onresult = function(event) {
    const transcript = event.results[0][0].transcript;
    const recognizedText = transcript.endsWith('.') ? transcript.slice(0, -1) : transcript;
    nameInput.value = recognizedText;

    const addButton = document.querySelector("button[id='addButton']");
    addButton.disabled = false;
};
```
This code will add an event listener to the input field with the id of `todo`. When the user types in the input field, the function will check if the value of the input field is blank. If the value is blank, the add button will be disabled. If the value is not blank, the add button will be enabled.

<br/>

#### 4. Update the `style.css` file
We need to update the `style.css` file to change the text-muted class to have a color of white so that it shows up better against the current background image:

```css
.limit-text {
    color: white;
}
```

<br/>

#### 5. Run the application
Now let's run the application to test the Add button is initially disabled and by either typing in the window or adding a name via the voice functionality that the Add button will become enabled and allow you to add a task. Open a terminal window in Visual Studio Code and run the following command:

```bash
python app.py
```
The initial interface should look like this:

![outcome](/Track_2_ToDo_App/Sprint-07%20-%20Advanced%20Styling%20Your%20Web%20App/images/outcome-S07-F01-US03.png)

🎉 Congrats! You have successfully added logic to prevent a user from accidentally adding a blank to-do item.

<br/>

> [!NOTE]
> 📄For the full source code for this exercise please see [here](/Track_2_ToDo_App/Sprint-07%20-%20Advanced%20Styling%20Your%20Web%20App/src/app-s07-f01-us03/).

<br/>

[🔼 Back **Workshop** Instructions ](/Track_2_ToDo_App/Workshop-Format.md) | [🔼 Back to **Hackathon** Sprint 7 ](/Track_2_ToDo_App/Sprint-07%20-%20Advanced%20Styling%20Your%20Web%20App/README.md) | [**◀ Previous user story** ](User%20Story%202%20-%20Add%20Tabbed%20Interface.md) | [**Next user story**  ▶](User%20Story%204%20-%20Confirm%20Delete.md)