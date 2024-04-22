# User Story: Get Generative AI recommendations - Step-by-Step
⏲️ _Est. time to complete: 30 min._ ⏲️

## User Story
*As a user, I want to receive AI-generated recommendations on how to complete a task when I click on it.*

## 🎯Acceptance Criteria:
- The web app should leverage AI to analyze task name and provide relevant recommendations.
- Recommendations should be displayed in a separate section on the task details page.
- Recommendations could include suggested steps, related resources, or tips to complete the task effectively as well as a link to the resource.
- The interface should look something like this:

    ![Recommendations](/Track_2_ToDo_App/Sprint-05%20-%20Advanced%20AI%20recommendations/images/outcome-S05-F01-US01.png)

## 🎓Know Before You Start
no resources at this time

## 📋Steps

In order to complete this user story you will need to complete the following tasks:

### Open Visual Studio Code
Open Visual Studio Code and open the source code the folder with your completed solution from the previous user story if you prefer you can use the starting reference application from [here](/Track_2_ToDo_App/Sprint-04%20-%20Voice%20To%20Text/src/app-s04-f01-us01/) 

<br/>

### Setup the AI SDK

#### 1. Install the OpenAI Python library
The first thing we need to do is to install the OpenAI and Semantic Kernel Python libraries. Open a terminal window in Visual Studio Code and run the following command:

```bash
pip install openai
pip install semantic-kernel==0.9.5b1
```

### Recommendation Engine
The first step in completing this user story is to create the recommendation engine that will generate AI recommendations based on the task name. The recommendation engine will interact with the AI service to generate recommendations and return them to the web application.

#### 1. Create a Service Enumeration Module 
This recommendation engine will support both OpenAI and Azure OpenAI protocols.  So in order to make working with that easier we are going to setup a quick enumeration module that allows us to see which service we are using.  To do this we will need to create a new Python file called `services.py` in the same folder as your  `app.py` file. Add the following code to the `services.py` file:

```python
from enum import Enum

class Service(Enum):
    OpenAI = "openai"
    AzureOpenAI = "azureopenai"
```

This code defines an enumeration class called `Service` that contains the different AI services that can be used for generating recommendations.  For this example, we will be using the Azure OpenAI service.

<br/>

#### Create the Recommendation Engine

#### 1. Create the Recommendation Engine Module
We need to create the recommendation engine that will generate AI recommendations based on the task name. To do this, we need to create a new Python file called `recommendation_engine.py` in the same folder as your  `app.py` file. Add the following code to the `recommendation_engine.py` file:

```python
import json
import asyncio
import semantic_kernel as sk
from services import Service
from openai import AzureOpenAI
from dotenv import dotenv_values
```

This code imports the necessary libraries and modules for the recommendation engine. The `semantic_kernel` module is used to calculate the semantic similarity between the task name and the recommendations. The `Service` class is used to interact with the Azure OpenAI API. The `AzureOpenAI` class is used to generate the AI recommendations. The `dotenv_values` function is used to load environment variables from a `.env` file.

<br/>

#### 2. Load Configuration and Select AI Service
We now need to have the recommendation engine module load the configuration file and tell the recommendation engine which AI service to use. Add the following code to the `recommendation_engine.py` file right after the imports:

```python
config = dotenv_values(".env")

#uses the USE_AZURE_OPENAI variable from the .env file to determine which AI service to use
#False means use OpenAI, True means use Azure OpenAI
selectedService = Service.AzureOpenAI if config.get("USE_AZURE_OPENAI") == "True" else Service.OpenAI
```

This code loads the configuration file from the `.env` file and determines which AI service to use based on the `USE_AZURE_OPENAI` variable in the configuration file. If the variable is set to `True`, the Azure OpenAI service is selected. If the variable is set to `False`, the OpenAI service is selected.

<br/>

#### 3. Create the Recommendation Engine Class
Next, we will create the recommendation engine class that will generate the AI recommendations. Add the following code to the end of the `recommendation_engine.py` file:

```python

deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()

class RecommendationEngine:
    
    def __init__(self):
        
        self.client = AzureOpenAI(azure_endpoint = endpoint, 
                        api_key=api_key,  
                        api_version="2024-02-15-preview"
                        )    
```

This code defines the `RecommendationEngine` class, which initializes the AI service based on the selected service in the configuration file. If the selected service is Azure OpenAI, an instance of the `AzureOpenAI` class is created with the Azure OpenAI key from the configuration file. If the selected service is OpenAI, an exception is raised since the OpenAI service is not implemented yet. 

<br/>

#### 4. Create the Get Recommendations Method
Next, we will create a method in the `RecommendationEngine` class to generate AI recommendations based on the task name. Add the following code to the `recommendation_engine.py` file as a method of the `RecommendationEngine` class:

```python
async def get_recommendations(self, keyword_phrase):
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
        
    message_text = [{"role":"system","content":system_prompt},
                    {"role":"user","content":prompt},]

    response = self.client.chat.completions.create(
                    model = deployment,
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

> [!NOTE]
> That when copy/pasting code from the browser into Visual Studio Code, the indentation may not be correct. Make sure to check the indentation of the code after pasting it into Visual Studio Code.

This code defines the `get_recommendations` method, which generates AI recommendations based on the task name. The method constructs a prompt for the AI model to generate recommendations based on the input keyword. The response from the AI model is parsed to extract the recommendations in JSON format. If an error occurs during parsing, a default error message is returned.

There are a few things to note in the code above:
- The `system_prompt` variable contains the instructions for the AI model on how to generate recommendations. This text is used to guide the AI model in generating the recommendations.  For this scenario we are using the following system_prompt

```text
You are an administrative assistant bot who is good at giving recommendations 
for tasks that need to be done by referencing website links that can provide 
assistance to helping complete the task.
```

- The `prompt` variable contains the input string that the AI model will use to generate recommendations. The `keyword_phrase` parameter is used to construct the prompt and should be the task name.  For this scenario we are using the following prompt:
        
```text
Please return 5 recommendations based on the input string: '{keyword_phrase}' 
using correct JSON syntax that contains a title and a hyperlink back to the 
supporting website. RETURN ONLY JSON AND NOTHING ELSE
```
- The combination of the `system_prompt` and `prompt` variables is used to create the `message_text` variable, which is passed to the AI model to generate recommendations.
- Tweaking these prompts to get the best results from the AI model is a key part of the process and is known as **prompt engineering**. 
- The `temperature`, `max_tokens`, `top_p`, `frequency_penalty`, and `presence_penalty` parameters are used to control the behavior of the AI model and the quality of the recommendations. These parameters can be adjusted to fine-tune the recommendations generated by the AI model.

<br/>

#### 5. Create configuration settings for Azure OpenAI
We now need to add the `.env` file to our project.  This file will contain all of the keys and secrets needed to properly configure the Azure OpenAI service. Create a `.env` file in the same folder as your `app.py` file.  This file will be used to store the configuration settings for the Azure OpenAI service and should look something like this: 

```text
USE_AZURE_OPENAI=True
AZURE_OPENAI_DEPLOYMENT_NAME=<deployment_name>
AZURE_OPENAI_API_KEY=<api_key>
AZURE_OPENAI_ENDPOINT=<endpoint>
```

This code sets the `USE_AZURE_OPENAI` variable to `True` to use the Azure OpenAI service. The `AZURE_OPENAI_DEPLOYMENT_NAME`, `AZURE_OPENAI_API_KEY`, and `AZURE_OPENAI_ENDPOINT` variables are used to configure the Azure OpenAI service. Replace `<deployment_name>`, `<api_key>`, and `<endpoint>` with the appropriate values for your Azure OpenAI service (you will be given these by one of the coaches).  The rest of the keys you can ignore for now.

<br/>

#### 6. Build Unit Test for Recommendation Engine
Given that this functionality is complex we will want to be able to test the code outside of the larger application.  A quick way to do this is to add a test function in the same file and if the developer "runs" this file instead of the app.py file, they will get the recommendation engine test function to run.   To do this we need to add the following code to the end of the file `recommendation_engine.py` to test the recommendation engine:

```python
async def test_recommendation_engine():
    engine = RecommendationEngine()
    recommendations = await engine.get_recommendations("Buy a birthday gift for mom")
    count = 1
    for recommendation in recommendations:
        print(f"{count} - {recommendation['title']}: {recommendation['link']}")
        count += 1

if __name__ == "__main__":
    asyncio.run(test_recommendation_engine())
```

This code defines a test function `test_recommendation_engine` that creates an instance of the `RecommendationEngine` class and generates AI recommendations based on the input keyword phrase "Buy a birthday gift for mom". The recommendations are printed to the console. The test function is executed when the file is run as the main program.

<br/>

#### 7. Test the Recommendation Engine
Go to the terminal window in Visual Studio Code and run the following command to test the recommendation engine:

```bash
python recommendation_engine.py
```
You should see results that are similar to this:
![Recommendation Engine Test](/Track_2_ToDo_App/Sprint-05%20-%20Advanced%20AI%20recommendations/images/recommendation_engine_test-S5-F1-US1-01.png)

Feel free to modify the input keyword phrase in the `test_recommendation_engine` method to test different recommendations.

<br/>

### Integrate Recommendation Engine into Web Application
Now that we have tested that our recommendation engine is working properly we will integrate the recommendation engine into the web application. 

#### 1. Install Flask Asynchronous Support
First, we need to make sure that we have asynchronous support in our flask application. Open a terminal window in Visual Studio Code and run the following command:

```bash
pip install 'flask[async]'
```

This command installs the asynchronous support for Flask, which allows us to use asynchronous functions in our web application.

<br/>

#### 2. Update the Database Model
We need to update our model to hold the recommendations.  Open the `database.py` file in the source folder of your application. Add the following code right under the `name` instance variable to create the additional column

```python
recommendations = []   
```

This code adds a new transient column to the `Todo` model called `recommendations`. This column will hold the collection of recommendations that come back from the recommendation engine, but it will not be stored in the database.   

<br/>

#### 3. Import Recommendation Engine into Application
We now need integrate the recommendation engine into the application.  Open the `app.py` file in the source folder of your application. Add the following module import to the `app.py` file right after the `from database...` statement to make the recommendation engine accessible to the flask application.

```python
from recommendation_engine import RecommendationEngine
```    

<br/>

#### 4. Create Recommendation Route to handle recommendations
Now that we have tested that our recommendation engine is working properly we will integrate the recommendation engine into the web application. Open the `app.py` file in the source folder of your application. Add the following code right after the `remove_todo()` function to the `app.py` file to create the backend functionality that the web app will use to get AI recommendations based on the task name:

```python
# Show AI recommendations
@app.route('/recommend/<int:id>', methods=['GET'])
async def recommend(id):
    recommendation_engine = RecommendationEngine()
    g.todo = db.session.query(Todo).filter_by(id=id).first()
    g.todo.recommendations = await recommendation_engine.get_recommendations(g.todo.name)
        
    return render_template('index.html')
```    

This code defines a new route `/recommend/<int:id>` that takes the task ID as a parameter. The route initializes the recommendation engine, retrieves the task from the database based on the ID, and generates AI recommendations based on the task name. The recommendations are stored in the task object and rendered in the `index.html` template.

<br/>

### Updating the Web Application FrontEnd

#### 1. Update the User Interface to Display Recommendations
To display the AI recommendations in the web application, we need to update the user interface to show the recommendations when a user clicks on a task. We will add a button to each task that will trigger the AI recommendations and display them in a separate tab on the right side of the task list.  To accompish this, we will make several changes to the `index.html` file in the `templates` folder of your application.
- We will add a button to each task that will trigger the AI recommendations for each task
- We will move our add button into the same col as the list of tasks, so that the add button stays aligned with the task list as the recommendation tab may vary in size. 
- We will adjust the width of the task list to leave room on the right for the recommendations
- We will display the recommendations in a separate tab to the right of the list

For the sake of making these changes easier in this step-by-step, instead of walking through each change we will simply ask you to replace the code in the `index.html` file with the code provided below.  This will allow you to see the changes in the web application and understand how the changes were made.

Open the `index.html` file in the `templates` folder of your application. Replace the entire contents of the `index.html` file with the following code:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My To-Do List</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}" />
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
                {% if g.todo != None %}       
                <div id="recommendations-div" class="card">                     
                    <div class="card-body">
                        <div class="list-group" id="list-of-recommendations">
                            <h5>AI Recommendations for "{{ g.todo.name }}"</h5>
                            {% for recommend in g.todo.recommendations %}
                            <a href="{{ recommend.link }}" class="list-group-item list-group-item-action"> {{ recommend.title }} </a>
                            {% endfor %}
                          </div>
                          <br />
                    </div>
                </div>
                {% endif %}
            </div>  
        </div>
    </div>
</body>
</html>
```

<br/>

#### 2. Run the Application
Now let's run the application to test the AI recommendations. Open a terminal window in Visual Studio Code and run the following command:

```bash
python app.py
```
the application should start and you should be able to see the AI recommendations when you click on the 'Recommendations' button for a task. The recommendations should be displayed in a separate tab on the right side of the task list and look something like this:
![outcome](/Track_2_ToDo_App/Sprint-05%20-%20Advanced%20AI%20recommendations/images/outcome-S05-F01-US01.png)

<br/>
🎉 Congratulations! You have now added AI recommendations to your web app, allowing users to get additional information on how to complete their tasks. 

<br/>

> [!NOTE]
> 📄For the full source code for this exercise please see [here](/Track_2_ToDo_App/Sprint-05%20-%20Advanced%20AI%20recommendations/src/app-s05-f01-us01/).


<br/>

[🔼 Back **Workshop** Instructions ](/Track_2_ToDo_App/Workshop-Format.md) | [🔼 Back to **Hackathon** Sprint 5 ](/Track_2_ToDo_App/Sprint-05%20-%20Advanced%20AI%20recommendations/README.md) | [**◀ Previous user story** (in previous sprint)](/Track_2_ToDo_App/Sprint-04%20-%20Voice%20To%20Text/Feature%201%20-%20Add%20Voice/User%20Story%201%20-%20Add%20Voice.md) | [**Next user story** ▶](User%20Story%202%20-%20Cache%20recommendations%20in%20DB.md)
