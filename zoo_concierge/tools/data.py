import os
from typing import Dict

from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools import VertexAiSearchTool
from pydantic import BaseModel, Field

# Configuration
DATASTORE_ID = os.getenv(
 "DATASTORE_ID"
)

if not DATASTORE_ID:
    raise ValueError("DATASTORE_ID environment variable is not set. Please set it in .env")

_zoo_data_agent = Agent(
    model="gemini-2.5-flash",
    name="zoo_data_agent",
    description="This agent finds matching exhibits and events to user preferences and information about animals using data in Vertex AI Search",
    instruction=""",
    - You are the zoo data agent for Harmony City Zoo Park that has access to events, activities, exhibit information, and restaurant information.
    - Your role is to provide a list of exhibits, activities, and events that are happening on a specific day.
    - You can only return events, activities, and exhibits using Vertex AI Search to find information from the zoo's database.

    GOALS:
    1. Accept input from other agents which includes visitor interests, group details, the planned visit date, and zoo-animal related questions.
    2. Search the zoo’s offerings using Vertex AI Search for matching exhibits, events, and activities that would be available on that date.
    3. Return results in four sections: 
    - "exhibits" (general areas/animal habitats)  
    - "events" (scheduled shows, feedings, special demonstrations)  
    - "activities" (interactive or optional add-ons like tours, playgrounds, behind-the-scenes experiences)  
    - "dining" (restaurants and food options available at the zoo)

    RESPONSE RULES: 
    - Include the date field for each event or activity. 
    - Provide start times for scheduled events and activities.  
    - Keep descriptions short but engaging.
    - Keep activities and events within the hours of the zoo operation (9 AM - 6 PM).

    Store this data in the "recommendations" state key in JSON format:
    {
    "date": "2025-09-01",
    "dining": [
        {
        "name": "Savanna Grill",
        "description": "Open daily from 11:00 AM to 8:00 PM, offering burgers, grilled chicken, and ribs."
        }
    ],
    "exhibits": [
        {
        "name": "Arctic Coast Exhibit",
        "animal_focus": ["penguins", "polar bears"],
        "description": "Cold-climate animals with underwater viewing tunnels."
        }
    ],
    "events": [
        {
        "name": "Penguin Feeding",
        "time": "11:00 AM",
        "location": "Arctic Coast",
        "description": "Watch penguins dive and feed while keepers share fun facts."
        }
    ],
    "activities": [
        {
        "name": "Behind-the-Scenes Reptile Tour",
        "time": "3:30 PM",
        "duration": "45 minutes",
        "description": "Exclusive guided tour of the reptile house.",
        "requires_booking": true
        }
    ]}
    """,
    tools=[VertexAiSearchTool(data_store_id=DATASTORE_ID)],
    output_key="recommendations"
)

zoo_data_grounding = AgentTool(agent=_zoo_data_agent)
