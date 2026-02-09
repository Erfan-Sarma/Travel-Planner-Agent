from google.adk.agents import LlmAgent, LoopAgent
from google.adk.tools import exit_loop

# 1. The Critic: The "Quality Assurance" agent
critic = LlmAgent(
    name="Critic",
    model="gemini-2.5-flash-lite",
    instruction="""
    Evaluate the provided travel itinerary for the following:
    1. Does it strictly follow the user's budget?
    2. Are the restaurant choices actually vegetarian?
    3. Is the timing realistic (e.g., no 5 attractions in one morning)?
    
    If the plan is PERFECT, call the 'exit_loop' tool.
    If not, specify exactly ONE major improvement needed.
    """,
    tools=[exit_loop]
)

# 2. The Improver: The "Editor" agent
improver = LlmAgent(
    name="Improver",
    model="gemini-2.5-flash-lite",
    instruction="""
    Take the feedback from the Critic and modify the itinerary to fix the identified issue.
    Keep the rest of the plan intact. 
    Pass the updated plan back for another review.
    """
)

# 3. The Loop (The Container)
optimizer_loop = LoopAgent(
    name="OptimizerLoop",
    sub_agents=[critic, improver],
    max_iterations=3 # Prevents infinite loops and saves tokens
)