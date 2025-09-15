import os
import vertexai
from vertexai import agent_engines
from starter_agent.agent import root_agent

PROJECT_ID       = os.environ.get("GOOGLE_CLOUD_PROJECT")
LOCATION         = os.environ.get("GOOGLE_CLOUD_LOCATION")
STAGING_BUCKET   = "gs://lunar-data-tmp" # TODO Update based on your preferences
APP_DISPLAY_NAME = "hackathon-npc-agent" # TODO: Update based on your preferences

vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
    staging_bucket=STAGING_BUCKET,
)

app = agent_engines.AdkApp(
    agent=root_agent,
    enable_tracing=True,
)

# Deploy to Google Cloud Vertex AI Agent Engine
print(f"Deploying agent '{APP_DISPLAY_NAME}' to Agent Engine...")
remote_app = agent_engines.create(
    display_name=APP_DISPLAY_NAME,
    agent_engine=app,
    requirements=[
        "google-cloud-aiplatform[adk,agent_engines]",
    ],
    extra_packages=[
        "starter_agent"
    ]
)
print(f"Agent deployed! Resource Name: {remote_app.resource_name}")
print("You can monitor the deployment status in the Agent Engine UI in the Google Cloud Console.")
