from google.adk.agents import LlmAgent, SequentialAgent

# 1. The Architect: Creates the empty slots for the days
structurer = LlmAgent(
    name="Structurer",
    model="gemini-2.5-flash-lite",
    instruction="""
    Create a high-level day-by-day framework for the trip. 
    Do not add specific details yet. Just define 'Morning', 'Afternoon', and 'Evening' slots 
    for each day based on the trip duration.
    """
)

# 2. The Decorator: Fills the slots with the research data
filler = LlmAgent(
    name="Filler",
    model="gemini-2.5-flash-lite",
    instruction="""
    Take the framework provided by the Structurer and the research data (Attractions, Hotels, Food).
    Populate the slots with specific names, historical facts, and restaurant choices.
    Ensure travel times between locations are realistic.
    """
)

# 3. The Quality Controller: Checks for logical errors
logical_reviewer = LlmAgent(
    name="LogicalReviewer",
    model="gemini-2.5-flash-lite",
    instruction="""
    Review the completed itinerary. 
    Check for:
    1. Budget alignment.
    2. Dietary consistency (is every meal vegetarian?).
    3. Logistics (is the sequence of locations geographically sensible?).
    Finalize the plan into a polished, readable format.
    """
)

# 4. The Pipeline (Sequential)
itinerary_pipeline = SequentialAgent(
    name="ItineraryPipeline",
    sub_agents=[structurer, filler, logical_reviewer]
)