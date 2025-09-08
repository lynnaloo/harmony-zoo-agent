
from datetime import datetime
import json
import os
from typing import Dict, Any

from google.adk.agents.callback_context import CallbackContext
from google.adk.sessions.state import State
from google.adk.tools import ToolContext
from .constants import SYSTEM_TIME, ITIN_INITIALIZED, ITIN_KEY, ITIN_START_DATE, ITIN_END_DATE, ITIN_DATETIME, START_DATE, END_DATE

def memorize_list(key: str, value: str, tool_context: ToolContext):
    """
    Memorize pieces of information.

    Args:
        key: the label indexing the memory to store the value.
        value: the information to be stored.
        tool_context: The ADK tool context.

    Returns:
        A status message.
    """
    mem_dict = tool_context.state
    if key not in mem_dict:
        mem_dict[key] = []
    if value not in mem_dict[key]:
        mem_dict[key].append(value)
    return {"status": f'Stored "{key}": "{value}"'}


def memorize(key: str, value: str, tool_context: ToolContext):
    """
    Memorize pieces of information, one key-value pair at a time.

    Args:
        key: the label indexing the memory to store the value.
        value: the information to be stored.
        tool_context: The ADK tool context.

    Returns:
        A status message.
    """
    mem_dict = tool_context.state
    mem_dict[key] = value
    return {"status": f'Stored "{key}": "{value}"'}


def _set_initial_states(source: Dict[str, Any], target: State | dict[str, Any]):
    """
    Setting the initial session state given a JSON object of states.

    Args:
        source: A JSON object of states.
        target: The session state object to insert into.
    """
    if SYSTEM_TIME not in target:
        target[SYSTEM_TIME] = str(datetime.now())

    # Always set _time context variable to current time (ISO format)
    target["_time"] = datetime.now().isoformat()

    if ITIN_INITIALIZED not in target:
        target[ITIN_INITIALIZED] = True

        target.update(source)

        itinerary = source.get(ITIN_KEY, {})
        # Print itinerary object
        print(f"Loaded Itinerary: {itinerary}")
        if itinerary:
            # set to current value or current date
            target[ITIN_START_DATE] = itinerary[START_DATE] or str(datetime.now().date())
            target[ITIN_DATETIME] = itinerary[START_DATE] or str(datetime.now())



def _load_precreated_itinerary(callback_context: CallbackContext):
    """
    Sets up the initial state.
    Set this as a callback as before_agent_call of the root_agent.
    This gets called before the system instruction is contructed.

    Args:
        callback_context: The callback context.
    """    
    data = {
        "state": {
            "user_profile": {},
            "recommendations": {},
            "itinerary": {},
            "bookings": {}
        }
    }
    _set_initial_states(data["state"], callback_context.state)
