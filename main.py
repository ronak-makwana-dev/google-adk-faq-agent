import sys
import asyncio
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types 
from agent import faq_agent

load_dotenv()

async def run_cli():

    user_query = sys.argv[1]
    APP_NAME, USER_ID, SESSION_ID = "faq_app", "user_001", "session_001"
    
    session_service = InMemorySessionService()
    runner = Runner(agent=faq_agent, app_name=APP_NAME, session_service=session_service)
    
    await session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
    
    message_content = types.Content(
        role="user",
        parts=[types.Part(text=user_query)]
    )
    
    print(f"--- Querying Agent: {user_query} ---\n")
    
    try:
        event_stream = runner.run_async(
            user_id=USER_ID,
            session_id=SESSION_ID,
            new_message=message_content
        )
        
        async for event in event_stream:
            if event.content and event.content.parts:
                for part in event.content.parts:
                    if hasattr(part, 'text') and part.text:
                        print(part.text, end="", flush=True)
        print("\n")

    except Exception as e:
        if "429" in str(e):
            print("\n[Quota Error]: You've hit the free tier limit. Please wait 60 seconds and try again.")
        else:
            print(f"\n[Execution Error]: {e}")

if __name__ == "__main__":
    asyncio.run(run_cli())