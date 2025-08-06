#!/usr/bin/env python
import sys
import warnings
import os
from dotenv import load_dotenv

from datetime import datetime

from onboard.crew import Onboard

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


import agentops
load_dotenv()

AGENTOPS_API_KEY = os.getenv("AGENTOPS_API_KEY") 
agentops.init(AGENTOPS_API_KEY,auto_start_session=False)


# TC2: Navigation Failure, Recovery Success
inputs_TC2 = {
    "scenario_navigate": "A new patient has just arrived in the emergency department, showing signs of confusion and distress. Immediate medical attention is required. The system has assigned human care worker #80 to assist. Please guide HCW #80 to patient room ER-12.",
    "scenario_collect": "The initial navigation to HCW #80 failed, but the issue was resolved by finding an alternative human care worker #90. HCW #90 successfully arrives at ER-12 and scans their ID card on the ID scanner.",
    "scenario_display": "The information of HCW #90 is successfully collected."
}


def run():
    """
    Run the crew.
    """
    
    try:
        agentops.start_session()
        Onboard().crew().kickoff(inputs=inputs_TC2)
        agentops.end_session("agentops_session success")
    except Exception as e:
        agentops.end_session("agentops_session fail")
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        Onboard().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Onboard().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    try:
        Onboard().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
