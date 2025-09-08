from google.adk.agents import Agent

from zoo_concierge import prompt

from zoo_concierge.sub_agents.booking.agent import booking_agent
from zoo_concierge.sub_agents.inspiration.agent import inspiration_agent
from zoo_concierge.sub_agents.planning.agent import planning_agent
from zoo_concierge.tools.weather import weather_grounding

from zoo_concierge.tools.memory import _load_precreated_itinerary


root_agent = Agent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="Acts like a digital zoo employee, orchestrates subagents.",
    instruction=prompt.ROOT_AGENT_INSTR,
    sub_agents=[
        inspiration_agent,
        planning_agent,
        booking_agent
    ],
    before_agent_callback=_load_precreated_itinerary,
)