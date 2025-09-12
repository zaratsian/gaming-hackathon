from google.adk.agents import Agent
from starter_agent.tools import (
    get_joke,
    get_current_time,
    pick_a_number, 
    guess_number,
    get_corporate_buzzwords,
)

# Example Agent
jester_agent = Agent(
    name="jester_agent",
    model="gemini-2.5-flash",
    description="""A sub-agent that tells jokes to entertain players.""",
    instruction="""You are a jester. Your primary role is to tell jokes when asked.""",
    tools=[
        get_joke
    ],
)

# Root (Orchestration) Agent
root_agent = Agent(
    name="fantasy_npc_agent",
    model="gemini-2.5-flash",
    description="""
        A customizable NPC agent for a fantasy world hackathon.
        This agent can be given a persona and extended with various tools
        to interact with players and the game environment.
    """,
    # TODO Customize the NCP personality and logic based on your chosen NPC role.
    instruction="""  
        You are a helpful fantasy NPC agent. Your goal is to interact with players
        in a fantasy world. You can use various tools to provide information,
        offer quests, tell stories, or play games.
        
        
    """, 
    sub_agents = [
        jester_agent, # Example sub-agent
        # Optional TODO: Add more sub_agents here
    ],
    tools=[
        # Optional TODO: Add more tools here
        get_current_time,
        pick_a_number,
        guess_number,
    ],
)
