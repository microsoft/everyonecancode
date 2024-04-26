import json
import asyncio
import semantic_kernel as sk
from services import Service
from openai import AzureOpenAI
from dotenv import dotenv_values

config = dotenv_values(".env")

#uses the USE_AZURE_OPENAI variable from the .env file to determine which AI service to use
#False means use OpenAI, True means use Azure OpenAI
selectedService = Service.AzureOpenAI if config.get("USE_AZURE_OPENAI") == "True" else Service.OpenAI

deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()

class RecommendationEngine:
    
    def __init__(self):

        self.client = AzureOpenAI(azure_endpoint = endpoint, 
                        api_key=api_key,  
                        api_version="2024-02-15-preview"
                        )        


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

async def test_recommendation_engine():
    engine = RecommendationEngine()
    recommendations = await engine.get_recommendations("Buy a birthday gift for mom")
    count = 1
    for recommendation in recommendations:
        print(f"{count} - {recommendation['title']}: {recommendation['link']}")
        count += 1

if __name__ == "__main__":
    asyncio.run(test_recommendation_engine())
    