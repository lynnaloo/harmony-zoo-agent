
import os
import sys
from dotenv import load_dotenv

print("Loading .env...")
load_dotenv()

print(f"DATASTORE_ID: {os.getenv('DATASTORE_ID')}")

try:
    print("Importing zoo_concierge.agent...")
    import zoo_concierge.agent
    print("Import successful.")
    print(f"root_agent: {zoo_concierge.agent.root_agent}")
except Exception as e:
    print(f"Import failed: {e}")
    import traceback
    traceback.print_exc()

print("Checking sub-agents...")
try:
    from zoo_concierge.sub_agents.inspiration.agent import inspiration_agent
    print("Inspiration agent imported.")
except Exception as e:
    print(f"Inspiration agent import failed: {e}")
    traceback.print_exc()

try:
    from zoo_concierge.sub_agents.booking.agent import booking_agent
    print("Booking agent imported.")
except Exception as e:
    print(f"Booking agent import failed: {e}")
    traceback.print_exc()

try:
    from zoo_concierge.sub_agents.planning.agent import planning_agent
    print("Planning agent imported.")
except Exception as e:
    print(f"Planning agent import failed: {e}")
    traceback.print_exc()
