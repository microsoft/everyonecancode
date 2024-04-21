# User Story: Voice Enabled Task Addition - Step-by-Step
⏲️ _Est. time to complete: 30 min._ ⏲️

## User Story

*As a user, I want to add tasks to the web app using voice commands, so I can quickly input tasks without typing.*

## 🎯Acceptance Criteria:
- The web app should integrate a voice recognition system for task input.
- Users should be able to activate voice input through a designated button or command.
- The system should accurately transcribe voice commands into text for task creation.
- The interface should look something like this  (note the arrow shows the addition of the voice button):

    ![Voice Button](/Track_2_ToDo_App/Sprint-04%20-%20Voice%20To%20Text/images/App_With_Voice_Button.png)

## 🎓Know Before You Start
no resources at this time

## 📋Steps

In order to complete this user story you will need to complete the following tasks

### Open Visual Studio Code
Open Visual Studio Code and open the source code the folder with your completed solution from the previous user story. If you prefer you can use the starting reference application from [here](/Track_2_ToDo_App/Sprint-03%20-%20Database%20Integration/src/app-s03-f01-us01/) 

<br/>

### Add Voice Recognition to the Web App

> [!NOTE]
> **💻 Note for Mac M1 Users** - If you are using a Mac M1 device, please note that you will need to use Chrome or Safari as the voice-to-text mechanism used here is not supported in Edge on Mac M1 devices.

#### 1. Update user interface to include voice recognition button
We are going to use the Web Speech API to add voice recognition to the web app. This API is built into modern web browsers and allows you to interact via your voice.  

In order to do this, we must update the add functionality in the web app by replacing the code for the form `<form action="/add>...</form>` in your `index.html` file: 

```html
<form action="/add" method="post" class="my-4">
    <div class="form-group">
        <label for="todo">Add a to-do:</label>
        <input type="text" name="todo" class="form-control">
    </div>
    <button type="submit" class="btn btn-primary">Add</button>
</form>
```

with the following code:

```html
<form action="/add" method="post" class="my-4">
    <div class="form-group">
        <br />
    </div>
    <span class="input-group-text">
        <input type="text" id="todo" name="todo" class="form-control" placeholder="Add a new task">
                    
        <button type="button" class="btn btn-outline-secondary" onclick="captureVoice()">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"  class="bi bi-mic" viewBox="0 0 16 16">
                <path d="M3.5 6.5A.5.5 0 0 1 4 7v1a4 4 0 0 0 8 0V7a.5.5 0 0 1 1 0v1a5 5 0 0 1-4.5 4.975V15h3a.5.5 0 0 1 0 1h-7a.5.5 0 0 1 0-1h3v-2.025A5 5 0 0 1 3 8V7a.5.5 0 0 1 .5-.5"></path>
                <path d="M10 8a2 2 0 1 1-4 0V3a2 2 0 1 1 4 0zM8 0a3 3 0 0 0-3 3v5a3 3 0 0 0 6 0V3a3 3 0 0 0-3-3"></path>
            </svg>
            <span class="visually-hidden" title="Use Microphone"></span>
        </button>
        <button type="submit" class="btn btn-success">Add</button>
    </span>
</form>
```

This code adds a button to the form that will allow the user to activate the microphone and speak their task. The `captureVoice()` function will be covered in the next step.

<br/>

#### 2. Add Javascript to support voice recognition
You will now need to create a Javascript file to help with the automation of capturing the voice from the browser.  Create a new file called `app.js` in the `static/js` folder of your application.  If these folders do not exist you will need to create them first.  Add the following code to the `app.js` file:

```javascript
document.addEventListener("DOMContentLoaded", function() {
    const nameInput = document.getElementById("todo");
    
    //add javascript to support speech recognition for the todo input field
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const recognition = new SpeechRecognition();
    recognition.continuous = false;
    recognition.lang = "en-US";
    recognition.interimResults = false;
    
    window.captureVoice = function() {
        recognition.start();
        nameInput.value = "Your microphone is activated, speak to record voice";
    };

    recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript;
        const recognizedText = transcript.endsWith('.') ? transcript.slice(0, -1) : transcript;
        nameInput.value = recognizedText;
    };

    recognition.onspeechend = function() {
        recognition.stop();
    };

    recognition.onnomatch = function(event) {
        nameInput.value = "I didn't recognize that prompt.";
    };

    recognition.onerror = function(event) {
        nameInput.value = "Error occurred in recognition: " + event.error;
    };
});
```

This code will add the necessary Javascript to the web app to allow the user to activate the microphone and speak their task. The `captureVoice()` function will start the speech recognition process, and the `recognition.onresult` function will capture the voice input and display it in the input field. The `recognition.onspeechend` function will stop the speech recognition process when the user stops speaking. The `recognition.onnomatch` and `recognition.onerror` functions will handle errors that may occur during the speech recognition process. 

<br/>

#### 3. Link the Javascript file to the HTML document
Link the Javascript file to the HTML document by adding the following code to the `<head>` tag in your `index.html` file.

```html
    <script src="{{ url_for('static', filename='js/app.js') }}"></script>
```

<br/>

#### 4. Run the Application
Now you can test the voice recognition feature by running the web app and clicking on the microphone button. Speak a task into the microphone and see it appear in the input field. Click the "Add" button to add the task to the list. The App should look something like this  (note the arrow shows the addition of the voice button):

![Voice Button](/Track_2_ToDo_App/Sprint-04%20-%20Voice%20To%20Text/images/App_With_Voice_Button.png)

<br/>
🎉 Congratulations! You have now added voice recognition to your web app, allowing users to add tasks via voice commands. This feature will provide a convenient way for users to input tasks without typing.

<br/>

> [!NOTE]
> 📄For the full source code for this exercise please see [here](/Track_2_ToDo_App/Sprint-04%20-%20Voice%20To%20Text/src/app-s04-f01-us01/).

<br/>

[🔼 Back **Workshop** Instructions ](/Track_2_ToDo_App/Workshop-Format.md) | [🔼 Back to **Hackathon** Sprint 4 ](/Track_2_ToDo_App/Sprint-04%20-%20Voice%20To%20Text/README.md) | [**◀ Previous user story** (in previous sprint)](/Track_2_ToDo_App/Sprint-03%20-%20Database%20Integration/Features%201%20-%20Shift%20task%20storage%20to%20database/User%20Story%201%20-%20Move%20from%20File%20Storage%20to%20database.md) | [**Next user story** (in next sprint) ▶](/Track_2_ToDo_App/Sprint-05%20-%20Advanced%20AI%20recommendations/Feature%201%20-%20Get%20Generative%20AI%20recommendation/User%20Story%201%20-%20Get%20Gen%20AI%20recommendation.md)
