from typing import Any

def save_preference(preference: str, value: str, tool_context: Any):
    """
    Saves a specific user preference into the persistent session state.
    Categories include: destination, budget, dietary_needs, or interests.
    """
    # We store it in the state dictionary provided by the ADK context
    tool_context.state[f"user_{preference.lower()}"] = value
    print(f"DEBUG: [State] Saved {preference} = {value}")
    return f"Successfully recorded your {preference} as: {value}"