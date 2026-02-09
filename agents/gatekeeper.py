from google.adk.agents import LlmAgent
from tools.preferences import save_preference
from callbacks.security import security_guard
from agents.researchers import research_team
from agents.itinerary import itinerary_pipeline
from agents.optimizer import optimizer_loop

gatekeeper_agent = LlmAgent(
    name="TravelPlanner",
    model="gemini-2.5-flash-lite",
    instruction="""
    Role: Lead Travel Planner.
    
    Workflow:
    1. Collect user details (destination, budget, constraints).
    2. Call 'ResearchTeam' to get raw data.
    3. Call 'ItineraryPipeline' to format that data.
    4. Call 'OptimizerLoop' to check if the plan is actually realistic (especially the budget).
    
    CRITICAL RULES:
    - Do NOT show the user the raw research data.
    - Only provide the FINAL, optimized itinerary.
    - The final output MUST be entirely in Persian (Farsi).
    - If a budget is impossible (like 1M IRR for 10 museums), politely explain why in Persian and suggest a free alternative (like a walking tour).
    """,
    tools=[save_preference],
    sub_agents=[research_team, itinerary_pipeline, optimizer_loop],
    before_model_callback=security_guard
)