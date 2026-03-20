import os
import logging
import google.cloud.logging
from dotenv import load_dotenv

from google.adk import Agent
from google.adk.agents import SequentialAgent
from google.adk.tools.tool_context import ToolContext

# Setup Logging
cloud_logging_client = google.cloud.logging.Client()
cloud_logging_client.setup_logging()

load_dotenv()
model_name = os.getenv("MODEL")

# 1. Technical Researcher (The "Brain")
tech_researcher = Agent(
    name="tech_researcher",
    model=model_name,
    description="Finds precise Python commands and GCP service details.",
    instruction="""
    You are a technical expert. Your goal is to find the exact code or command the user needs.
    - If they ask for Python: Provide the most modern, efficient code snippet.
    - If they ask for Cloud: Suggest the best GCP service (Compute Engine, Cloud Run, etc.).
    - Focus on facts and syntax. Output the raw technical data.
    """,
    output_key="technical_data" # This saves the facts for the next agent
)

# 2. College Mentor (The "Voice")
student_mentor = Agent(
    name="student_mentor",
    model=model_name,
    description="Translates tech data into a friendly, helpful guide for students.",
    instruction="""
    You are a helpful Senior TA for college students. 
    Take the 'TECHNICAL_DATA' and present it clearly:
    - Start with an encouraging, friendly greeting.
    - Use analogies (like comparing a Docker container to a 'shipping box' for code).
    - Bold the important commands.
    - Add a 'Pro-Tip' section at the end focusing on cost-saving or best practices.
    
    TECHNICAL_DATA:
    {{ technical_data }}
    """
)

# The Sequential Workflow (First Research, then Format)
mentor_workflow = SequentialAgent(
    name="mentor_workflow",
    description="Workflow to research tech info then format it for students.",
    sub_agents=[
        tech_researcher, 
        student_mentor,
    ]
)

# The Root Agent (The Entry Point)
root_agent = Agent(
    name="greeter",
    model=model_name,
    description="The main entry point for the Cloud Companion.",
    instruction="""
    - Let the student know you are their Cloud Companion and Mentor.
    - Ask what Python or Google Cloud topic they are working on today.
    - Once they provide a topic, pass control to the 'mentor_workflow'.
    """,
    sub_agents=[mentor_workflow]
)