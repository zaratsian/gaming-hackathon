# 🧙‍♂️ NPC Agent Hackathon with ADK

## 🎯 Purpose

Get ready to dive into the world of AI agents with the Google Cloud Agent Development Kit (ADK). This fun, informal hackathon will give you hands-on experience using the ADK to design and orchestrate a complex, multi-agent system in a single session.

You’ll build your own NPC agent for a fantasy world using the provided starter repo and creative MCP server endpoints. The goal is to explore how agents can interact with APIs and bring characters to life through fun, unexpected behaviors.

You can use this starter code as a simple example to get you up and running, but your goal is to personalize it based on your NPC and specific use cases goals.

### What You'll Learn

* ADK Fundamentals: Get hands-on with the core libraries, setup, and deployment processes.

* Multi-Agent Architecture: Understand how to define, connect, and orchestrate specialized agents to solve problems.

* Core ADK Features: Explore tool-use, inter-agent communication, potentially memory management, agent sessions, MCP and more depending on your agent goals.


## 🚀 Getting Started

1.  **Clone the Starter Repo**: This repository contains a simple NPC skeleton (`starter_agent/agent.py`) with placeholders to customize.

    ```bash
    git clone https://github.com/zaratsian/gaming-hackathon.git
    cd gaming-hackathon
    ```

2.  **Run Setup Script**:

    ```bash
    python setup.py
    ```

3.  **Launch Developer UI**: After setup, you can launch the developer UI to test your agent, inspect tools, requests, responses, and states.

    ```bash
    adk web
    ```
    This will typically open in your browser at `localhost:8000`.

4.  **NPC Design**: What do you want your NPC to do? Examples: Trickster Goblin, Weather Sage, Traveling Merchant, Cardmaster.

5.  **Add Personality & Logic**: Update the prompts for your agent(s), add more agents, use the provided functions, and/or create your own responses.

6.  **Use Creative Endpoints**: Call APIs to give your NPC special powers. You can integrate external APIs or create your own MCP server endpoints.

    *   Jokes & Riddles
    *   Deck of Cards & Dice Rolls
    *   Weather Forecasts
    *   Google Maps Lookups
    *   Trivia & Story Prompts

## Stretch Goals

*   Chain multiple endpoints together for more dynamic responses (e.g., give a riddle, then reward with a card draw).
*   Add memory or state variables so your NPC remembers past interactions or certain information.
*   Integrate with MCP servers.
*   Collaborate with others to link NPCs together into a shared storyline. (Agent2Agent)

## NPC Archetypes for Your Hackathon (Ideas)

Here are some archetype ideas to inspire your NPC agent:

### 1. The Trickster Goblin

*   **Personality**: Mischievous, loves wordplay, tests players before helping.
*   **Subagents**: Jester Agent (tells jokes), Riddle Master (generates riddles and evaluates answers).
*   **Tools & APIs**: Jokes API, Riddles API, Trivia API.

### 2. The Weather Sage

*   **Personality**: Mysterious oracle who speaks in omens tied to real-world weather.
*   **Subagents**: Forecast Interpreter (fetches live weather, wraps it in cryptic prophecy), Storm Watcher (alerts players when severe weather is near).
*   **Tools & APIs**: Weather API (current + forecast), News API (weather-related headlines).

### 3. The Cardmaster

*   **Personality**: Runs games of chance, deals fortunes, hands out rewards.
*   **Subagents**: Deck Dealer (shuffles and draws cards), Fortune Teller (interprets cards into prophecies or quests).
*   **Tools & APIs**: Deck of Cards API, Dice Roller API.

### 4. The Traveling Merchant

*   **Personality**: Wandering trader who knows every route and shortcut.
*   **Subagents**: Pathfinder (uses maps to suggest routes or distances), Trade Broker (fetches “market data” or simulated).
*   **Tools & APIs**: Google Maps API (routes, distances, nearby places), News API (market/merchant rumors).

### 5. The Storyteller Bard

*   **Personality**: Spins tales, rewards players with knowledge or quests.
*   **Subagents**: Lore Keeper (pulls trivia facts), Prompt Weaver (generates short quest hooks or plot twists).
*   **Tools & APIs**: Trivia API, Story Prompt API, News API (turns real-world headlines into bardic tales).

### 6. The Puzzle Guardian

*   **Personality**: Guardian of a hidden gate, challenges players with brain teasers.
*   **Subagents**: Gatekeeper (generates riddles and puzzles), Judge (verifies answers and gives hints).
*   **Tools & APIs**: Riddles API, Math/logic puzzle generator (optional custom endpoint).

## Project Structure

Your agent project should follow this structure:

```
parent_folder/
    starter_agent/
        __init__.py
        agent.py
        tools.py
        .env (optional, but this file is generated after running setup.py)
```

*   `__init__.py`:
    ```python
    from . import agent
    ```
*   `agent.py`: Defines your main agent and any sub-agents.
*   `tools.py`: Contains the functions (tools) that your agents can use.

## References

*   [ADK (Agent Development Kit) Docs](https://google.github.io/adk-docs/)
*   [Github ADK Python](https://github.com/google/adk-python)
*   [Github ADK Samples](https://github.com/google/adk-samples/tree/main)
*   [Google Cloud Vertex AI Agent Engine](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview)
*   [MCP with ADK](https://google.github.io/adk-docs/mcp/)
*   [Agent2Agent](https://a2a-protocol.org/latest/)
