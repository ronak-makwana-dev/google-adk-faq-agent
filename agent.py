import random # Don't forget this for the tool!
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from typing import Annotated

def get_weather(city: Annotated[str, "The name of the city"]) -> str:
    """Returns the current weather conditions for a specific city."""
    weather_conditions = ["sunny", "rainy", "cloudy", "stormy", "snowy"]
    temp = random.randint(10, 35)
    condition = random.choice(weather_conditions)
    # can invoke external api and retrieve the weather, Keeping it simple here
    return f"The weather in {city} is {condition} with {temp}°C."

faq_agent = Agent(
    name="faq_agent",
    model=Gemini(model="gemini-3-flash-preview"),
    description="An agent that answers questions and checks weather.",
    instruction="""
    You are a professional assistant. 
    1. If the user asks for the weather of a specific location, use the 'get_weather' tool.
    2. For math or general knowledge, answer directly using your internal knowledge.
    3. ALWAYS return your final answer in JSON format: {"answer": "...", "source": "..."}.
    
    Example for Math: {"answer": "300", "source": "direct_calculation"}
    Example for Weather: {"answer": "The weather in Paris is sunny with 22°C.", "source": "weather_tool"}
    """,
    tools=[get_weather]
)