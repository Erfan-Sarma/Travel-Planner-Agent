import asyncio
from dotenv import load_dotenv
from google.adk.runners import InMemoryRunner
from google.genai import types

# Import our modular components
from agents.gatekeeper import gatekeeper_agent

load_dotenv()

async def main():
    print("=== Step 2: Gatekeeper & Personalization Active ===")
    runner = InMemoryRunner(agent=gatekeeper_agent)

    session = await runner.session_service.create_session(
        app_name=runner.app_name,
        user_id="traveler_01"
    )

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in {"exit", "quit"}:
            break

        try:
            events = runner.run(
                user_id=session.user_id,
                session_id=session.id,
                new_message=types.Content(
                    role="user",
                    parts=[types.Part(text=user_input)]
                )
            )

            final_text = ""
            for event in events:
                if event.content and event.content.parts:
                    for part in event.content.parts:
                        if part.text:
                            final_text += part.text

            if final_text.strip():
                print(f"\nAI: {final_text}")
                
                # Internal check: See what's in the state now
                # In a real app, you'd inspect session.state here
        
        except Exception as e:
            print("System Error:", e)

if __name__ == "__main__":
    asyncio.run(main())