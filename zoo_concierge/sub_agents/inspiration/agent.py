from google.adk.agents import Agent
from zoo_concierge.tools.memory import memorize, save_user_profile
from zoo_concierge.tools.data import zoo_data_grounding
from zoo_concierge.tools.weather import weather_grounding
from zoo_concierge.sub_agents.inspiration import prompt
from google.genai.types import GenerateContentConfig


inspiration_agent = Agent(
    model="gemini-2.5-flash",
    name="inspiration_agent",
    description="""
    A travel inspiration agent who inspire visitors; Provides information about exhibits, activities, events. 
    Provides weather updates and dining options.
    """,
    instruction=prompt.INSPIRATION_AGENT_INSTR,
    tools=[
        zoo_data_grounding,
        memorize,
        save_user_profile,
        weather_grounding
    ],
    generate_content_config=GenerateContentConfig(
        temperature=0.1, top_p=0.5
    )
)
