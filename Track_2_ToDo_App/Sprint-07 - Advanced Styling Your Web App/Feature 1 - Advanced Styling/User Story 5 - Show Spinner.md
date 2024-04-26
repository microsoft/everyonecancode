# User Story: Show spinner when loading recommendations Step-by-Step
⏲️ _Est. time to complete: 30 min._ ⏲️

## User Story 
*Clicking on the recommendations tab can take some time so we need to let the user visually know that the system is working on loading the recommendations by showing a spinner graphic*

## 🎯Acceptance Criteria:
- The spinner should be displayed when the recommendations tab is clicked
- The spinner should be removed when the recommendations are loaded
- The spinner should look something like this:

    ![Index](/Track_2_ToDo_App/Sprint-07%20-%20Advanced%20Styling%20Your%20Web%20App/images/outcome-S07-F01-US05.png)

## 🎓Know Before You Start
no resources at this time

## 📋Steps

In order to complete this user story you will need to complete the following tasks

### Open Visual Studio Code
Open Visual Studio Code and open the source code the folder with your completed solution from the previous user story if you prefer you can use the starting reference application from [here](/Track_2_ToDo_App/Sprint-07%20-%20Advanced%20Styling%20Your%20Web%20App/src/app-s07-f01-us04/)

<br/>

### Update the user interface to show a spinner when clicking on the recommendation tab

#### 1. Update the user interface to support the spinner
In order to add a spinner, first we need to update the user interface to support this functionality. Open the `index.html` file and replace the `<li class="nav-item">...</li>` element for the recommendation tab with the following code:

```html
<li class="nav-item">
    <a id="recommendations-tab" class="nav-link" href="{{ url_for('recommend', id=g.todo.id) }}">
        <span id="recommendation-spinner" class="spinner-border spinner-border-sm" role="status" aria-hidden="true" hidden></span>
        Recommendations
    </a>
</li>
```
This code will add a spinner to the recommendations tab. The spinner will be hidden by default.

<br/>

#### 2. Update Javascript to handle tab clicks
Next, we need to update the `app.js` file to show the spinner when the recommendations tab is clicked.  To do this we are going to override the default "click" behavior so that we can enable the spinner user interface element before calling the server to load recommendations.  This will visually show the spinner while we wait for the server to respond.  Open the `app.js` file and add the following code within the `DOMContentLoaded` event listener:

```javascript
//override the default behavior of the nav links so that we can 
//turn on a spinner control when the user clicks on the recommendations tab
const navLinks = document.getElementsByClassName('nav-link');
Array.from(navLinks).forEach((navLink) => {
    navLink.addEventListener('click', function(e) {
        e.preventDefault();
        const currentPath = this.getAttribute('href');
        const rootUrl = window.location.origin;

        //turn on the spinner control if the user clicks on the recommendations tab
        if (this.getAttribute('id') === 'recommendations-tab') {
            var recommend_pane = document.querySelector("span[id='recommendation-spinner']");
            if (recommend_pane) {
                recommend_pane.removeAttribute('hidden');
        } 
    }
        window.location.href = rootUrl + currentPath;
    });
});
```
<br/>

### Update the user interface to show the spinner when hitting the refresh button

#### 1. Update the user interface to support the spinner on the refresh button
Since the recommendation functionality can also be called through the refresh button, we will need to update the user interface to show the spinner when the refresh button is clicked. Open the `index.html` file and add an onclick event to the refresh button, the new code should look like:

```html
<a href="{{ url_for('recommend', id=g.todo.id, refresh=true) }}" class="btn btn-info btn-fixed-width" onclick="handleRefresh()"> Refresh </a>
```
<br/>

#### 2. Update the `app.js` file to handle the new onclick event
We also need to update the `app.js` file handle this new onclick event. Open the `app.js` file and add the following code within the `DOMContentLoaded` event listener:

```javascript
window.handleRefresh = function() {
    var recommend_pane = document.querySelector("span[id='recommendation-spinner']");
    if (recommend_pane) {
        recommend_pane.removeAttribute('hidden');
    } 
}
```

#### 3. Run the Application
Save all the changes and run the application. Click on the recommendations tab. You should see a spinner displayed next to the Recommendations text. The spinner should be removed when the recommendations are loaded.  This should be true for both the initial click on the recommendations tab and the refresh button.  The change should look something like this:  The partial circle before the recommendations text in the picture should be a spinning circle when you actually run the application versus a partial circle for this screenshot

![outcome](/Track_2_ToDo_App/Sprint-07%20-%20Advanced%20Styling%20Your%20Web%20App/images/outcome-S07-F01-US05.png)

<br/>
🎉 Congratulations! You have now updated the user interface to visually show the user when recommendations are loading

<br/>

> [!NOTE]
> 📄For the full source code for this exercise please see [here](/Track_2_ToDo_App/Sprint-07%20-%20Advanced%20Styling%20Your%20Web%20App/src/app-s07-f01-us05/).

<br/>

[🔼 Back **Workshop** Instructions ](/Track_2_ToDo_App/Workshop-Format.md) | [🔼 Back to **Hackathon** Sprint 7 ](/Track_2_ToDo_App/Sprint-07%20-%20Advanced%20Styling%20Your%20Web%20App/README.md) | [**◀ Previous user story** ](User%20Story%204%20-%20Confirm%20Delete.md) | [**Next user story** (in next sprint) ▶](/Track_2_ToDo_App/Sprint-08%20-%20Deploy%20to%20the%20Cloud/Feature%201%20-%20Deploy%20to%20Azure.md/User%20Story%201%20-%20Deploy%20to%20Azure.md)

