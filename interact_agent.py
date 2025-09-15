import asyncio
import os
from dotenv import load_dotenv
from vertexai import agent_engines

async def interact_with_agent():
    load_dotenv()

    agent_resource_name = os.getenv("AGENT_RESOURCE_NAME")
    if not agent_resource_name:
        agent_resource_name = input("Please enter your deployed agent's resource name (e.g., projects/YOUR_PROJECT_ID/locations/us-central1/agents/YOUR_AGENT_ID): ")
        if not agent_resource_name:
            print("Agent resource name is required.")
            return

    print(f"Connecting to agent: {agent_resource_name}")
    remote_app = agent_engines.get(agent_resource_name)

    user_id = "test_user_123" # Hardcoded for hackathon, but would typically be dynamically set

    session_id_input = input("Enter an existing session ID to resume (optional, press Enter to create a new session): ")
    if session_id_input:
        session_id = session_id_input
        print(f"Resuming session with ID: {session_id}")
    else:
        print(f"Creating a new remote session for user: {user_id}")
        remote_session = await remote_app.async_create_session(user_id=user_id)
        print(f"Session created: {remote_session}")
        session_id = remote_session["id"]
        print(f"New Session ID: {session_id}")

    while True:
        message = input("\nEnter your message to the agent (or 'quit' to exit): ")
        if message.lower() == 'quit':
            break

        print(f"\nSending query to agent: '{message}'")
        async for event in remote_app.async_stream_query(
            user_id=user_id,
            session_id=session_id,
            message=message,
        ):
            print(event)

if __name__ == "__main__":
    asyncio.run(interact_with_agent())
