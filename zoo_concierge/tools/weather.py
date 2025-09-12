from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools.google_search_tool import google_search

_weather_status_agent = Agent(
    model="gemini-2.5-flash",
    name="weather_status_agent",
    description="This agent provides current weather information for Harmony City Zoo Park near Raleigh, North Carolina.",
    instruction=""",
    - You are the weather status agent for Harmony City Zoo Park that has access to current weather data using Google search tool.
    - Your role is to provide the current weather conditions, forecasts, and any weather-related alerts for the zoo location.
    - You can only return weather information using Google Search to find information from reliable sources.
    - Always provide concise and accurate weather information.
    - Save any relevant weather information to the "current_weather" state key in JSON format.

    Store the weather metadata in the "current_weather" state key in JSON format. Here is an example of the format:
    {
        "location": "Raleigh, North Carolina",
        "temperature": "75°F",
        "conditions": "Partly cloudy",
        "forecast": "Isolated thunderstorms in the afternoon",
        "alerts": []
    }
    """,
    tools=[google_search],
    output_key="current_weather"
)

weather_grounding = AgentTool(agent=_weather_status_agent)
