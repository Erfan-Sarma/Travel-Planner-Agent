from google.adk.agents import LlmAgent, ParallelAgent

# 1. Attractions Specialist
attractions_agent = LlmAgent(
    name="AttractionsAgent",
    model="gemini-2.5-flash-lite",
    instruction="Research the top 3 historical/cultural attractions in the destination. Provide a brief fact for each."
)

# 2. Accommodation Specialist
hotel_agent = LlmAgent(
    name="HotelAgent",
    model="gemini-2.5-flash-lite",
    instruction="Suggest 3 lodging options that fit the user's budget. Include estimated prices."
)

# 3. Services Specialist
services_agent = LlmAgent(
    name="ServicesAgent",
    model="gemini-2.5-flash-lite",
    instruction="Research local transport and 3 restaurants. Strictly follow dietary constraints (e.g., Vegetarian)."
)

# 4. The Parallel Team (The Container)
# Note: No 'instruction' here!
research_team = ParallelAgent(
    name="ResearchTeam",
    sub_agents=[attractions_agent, hotel_agent, services_agent]
)