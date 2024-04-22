# User Story: Allow the user to refresh the recommendations - Step-by-Step
⏲️ _Est. time to complete: 30 min._ ⏲️

## User Story
*As a user, I want to be able to tell the system to re-generate the recommendations on how to complete a task when I click on it*

## Acceptance Criteria:
- The web app should provide a user interface element to refresh the recommendations for a task.
- The system should re-generate the recommendations when the user clicks on the refresh button.
- The new recommendations should be displayed in the recommendations section.
- The new recommendations should be stored in the database and overwrite the old recommendations.
- The AI recommendation engine should not have any reuse old recommendations in the new recommendation list. 
- The interface should look something like this:

    ![Refresh Recommendations](/Track_2_ToDo_App/Sprint-05%20-%20Advanced%20AI%20recommendations/images/outcome-S05-F01-US03.png) 

## 📋Steps

In order to complete this user story you will need to complete the following tasks:

### Open Visual Studio Code
Open Visual Studio Code and open the source code the folder with your completed solution from the previous user story if you prefer you can use the starting reference application from [here](/Track_2_ToDo_App/Sprint-05%20-%20Advanced%20AI%20recommendations/src/app-s05-f01-us02/) 

<br/>

### Update the recommendation engine to allow for refreshing recommendations

#### 1. Update get_recommendations method 
The first thing that we will need to do is update the recommendation engine to enable it to re-generate new recommendations. Open the `recommendation_engine.py` file in the source folder of your application. We will need to replace the `get_recommendations` method with the following code:

```python
async def get_recommendations(self, keyword_phrase, previous_links_str=None):
    prompt = f"""Please return 5 recommendations based on the input string: '{keyword_phrase}' using correct JSON syntax that contains a title and a hyperlink back to the supporting website. RETURN ONLY JSON AND NOTHING ELSE"""
    system_prompt = """You are an administrative assistant bot who is good at giving 
        recommendations for tasks that need to be done by referencing website links that can provide 
        assistance to helping complete the task. 

        If there are not any recommendations simply return an empty collection. 

        EXPECTED OUTPUT:
        Provide your response as a JSON object with the following schema:
        [{"title": "...", "link": "..."},
        {"title": "...", "link": "..."},
        {"title": "...", "link": "..."}]
        """
        
    if previous_links_str is not None:
        prompt = prompt + f". EXCLUDE the following links from your recommendations: {previous_links_str}"  

    message_text = [{"role":"system","content":system_prompt},
                    {"role":"user","content":prompt},]

    response = self.client.chat.completions.create(
                    model= deployment,
                    messages = message_text,
                    temperature=0.14,
                    max_tokens=800,
                    top_p=0.17,
                    frequency_penalty=0,
                    presence_penalty=0,
                    stop=None
                    )

    result = response.choices[0].message.content
    print(result)

    try:
        recommendation = json.loads(result)
    except Exception as e:
        print(f"Error loading recommendations: {e}")
        recommendation = [{"title": "Sorry, unable to recommendation at this time", "link": ""}]

    return recommendation
```

The only changes that we made to this function are as follows:
![Recommendation Engine Changes](/Track_2_ToDo_App/Sprint-05%20-%20Advanced%20AI%20recommendations/images/Recommendation_engine_changes-S05-F01-US03.png)
- We added the `previous_links_str` parameter to the function. This parameter will be used to pass in any previous recommendations that we want to exclude from the new recommendations.
- We updated the prompt to include the `previous_links_str` if it is passed in. You will notice that we simply append some additional prompt text to the exiting prompt to exclude previous recommendations where `{previous_links_str}` is replaced with the string of the previous recommendations. 

    ```text
    . EXCLUDE the following links from your recommendations: {previous_links_str}   

<br/>

### Updating Web Application Backend to handle refreshing recommendations

#### 1. Update Recommend Route
We now need to update the backend route to handle the refresh of the recommendations.  Open the `app.py` file and replace the `recommend` route with the following code:

```python
@app.route('/recommend/<int:id>', methods=['GET'])
@app.route('/recommend/<int:id>/<refresh>', methods=['GET'])
async def recommend(id, refresh=False):
    recommendation_engine = RecommendationEngine()
    g.todo = db.session.query(Todo).filter_by(id=id).first()

    if g.todo and not refresh:
        try:
            #attempt to load any saved recommendation from the DB
            if g.todo.recommendations_json is not None:
                g.todo.recommendations = json.loads(g.todo.recommendations_json)
                return render_template('index.html')
        except ValueError as e:
            print("Error:", e)

    previous_links_str = None
    if refresh:
        g.todo.recommendations = json.loads(g.todo.recommendations_json)
        # Extract links
        links = [item["link"] for item in g.todo.recommendations]
        # Convert list of links to a single string
        previous_links_str = ", ".join(links)

    g.todo.recommendations = await recommendation_engine.get_recommendations(g.todo.name, previous_links_str)
        
    # Save the recommendations to the database
    try:
        g.todo.recommendations_json = json.dumps(g.todo.recommendations)
        db.session.add(g.todo)
        db.session.commit()
    except Exception as e:
        print(f"Error adding and committing todo: {e}")
        return

    return render_template('index.html')
```

This code adds a new route `/refresh/<int:id>/refresh` to the existing recommend function that will handle the refresh of the recommendations.  It also updates the parameter to the `recommend` route to include a `refresh` parameter that will be used to determine if the user is requesting a refresh of the recommendations.  If the user is requesting a refresh, the existing recommendations are loaded from the database and passed to the `get_recommendations` method along with the `previous_links_str` that is generated from the existing recommendations.  The new recommendations are then saved to the database and displayed on the UI.

<br/>

### Update the User Interface to include a "refresh" button

#### 1. Update the `index.html` file
Finally we will need to update the UI to include a "refresh" button.  Open the `index.html` file in the `templates` folder of your application.  Replace the `<div id="recommendations-div"...>`section with the following changes:

```html
<div id="recommendations-div" class="card">                     
    <div class="card-body">
        <div class="list-group" id="list-of-recommendations">
            <h5>AI Recommendations for "{{ g.todo.name }}"</h5>
            {% for recommend in g.todo.recommendations %}
                <a href="{{ recommend.link }}" class="list-group-item list-group-item-action"> {{ recommend.title }} </a>
            {% endfor %}
        </div>
        <br />
        Don't like recommendations? 
        <a href="{{ url_for('recommend', id=g.todo.id, refresh=true) }}" class="btn btn-info btn-fixed-width"> Refresh </a>
    </div>
</div>
```
 
This code adds a "Refresh Recommendations" button to the UI that will call the `/recommend/<int:id>/refresh` route when clicked. This will allow the user to refresh the recommendations for a task and see new recommendations generated by the AI recommendation engine.

<br/>

#### 2. Run the Web Application
Now let's see this functionality in action.  Start the web app by running the following command in the terminal:

```bash
python app.py
```

You should now see a "Refresh" button within the recommendations section of the task details page.  It should look something like this:
![Refresh Recommendations](/Track_2_ToDo_App/Sprint-05%20-%20Advanced%20AI%20recommendations/images/outcome-S05-F01-US03.png)

    
<br/>
🎉 Congratulations! You have now have the ability to refresh your AI recommendations.

<br/>

> [!NOTE]
> 📄For the full source code for this exercise please see [here](/Track_2_ToDo_App/Sprint-05%20-%20Advanced%20AI%20recommendations/src/app-s05-f01-us03/).


<br/>

[🔼 Back **Workshop** Instructions ](/Track_2_ToDo_App/Workshop-Format.md) | [🔼 Back to **Hackathon** Sprint 5 ](/Track_2_ToDo_App/Sprint-05%20-%20Advanced%20AI%20recommendations/README.md) | [**◀ Previous user story**](User%20Story%202%20-%20Cache%20recommendations%20in%20DB.md) | [**Next user story** (in next sprint) ▶](/Track_2_ToDo_App/Sprint-06%20-%20Advanced%20To-Do%20Details/Feature%201%20-%20Add%20Additional%20To-Do%20Details/User%20Story%201%20-%20Add%20additional%20details%20to%20to-do%20item.md)
