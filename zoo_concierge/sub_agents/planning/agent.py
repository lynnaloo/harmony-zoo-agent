"""Planning agent. A pre-booking agent covering the planning part of the trip."""

from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.genai.types import GenerateContentConfig
from zoo_concierge.sub_agents.planning import prompt
from zoo_concierge.tools.memory import memorize, save_itinerary
from zoo_concierge.tools.weather import weather_grounding
from zoo_concierge.tools.data import zoo_data_grounding

planning_agent = Agent(
    model="gemini-2.5-flash",
    description="Builds a visitor itinerary based on user preferences and inspirations.",
    name="planning_agent",
    instruction=prompt.PLANNING_AGENT_INSTR,
    tools=[
        memorize,
        save_itinerary,
        zoo_data_grounding,
        weather_grounding
    ],
    generate_content_config=GenerateContentConfig(
        temperature=0.1, top_p=0.5
    )
)
