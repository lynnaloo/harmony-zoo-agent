"""Booking agent and sub-agents, handling the confirmation and payment of bookable events."""

from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.genai.types import GenerateContentConfig
from zoo_concierge.tools.memory import memorize

from zoo_concierge.sub_agents.booking import prompt

booking_agent = Agent(
    model="gemini-2.5-flash",
    name="booking_agent",
    description="Given an itinerary, completes the reservation of tickets and event/activity bookings.",
    instruction=prompt.BOOKING_AGENT_INSTR,
    tools=[
        memorize
    ],
    generate_content_config=GenerateContentConfig(
        temperature=0.0, top_p=0.5
    )
)
