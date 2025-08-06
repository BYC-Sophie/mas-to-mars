from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
# from crewai_tools import SerperDevTool
import yaml, os
from pathlib import Path
from onboard.tools.custom_tool import get_navigation_results, get_onboarding_information, get_display_information
# from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource

# text_source = TextFileKnowledgeSource(
#     file_paths=["guide-test-ver-2.txt"]
# )

@CrewBase
class Onboard:
    """Onboard Crew"""
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def navigating_robot(self) -> Agent:
        return Agent(
            config=self.agents_config['navigating_robot'],
            tools=[get_navigation_results],
            verbose=True,
            max_iter=3
        )

    @agent
    def info_collection_robot(self) -> Agent:
        return Agent(
            config=self.agents_config['info_collection_robot'],
            tools=[get_onboarding_information],
            verbose=True,
            max_iter=3
        )

    @agent
    def info_display_robot(self) -> Agent:
        return Agent(
            config=self.agents_config['info_display_robot'],
            tools=[get_display_information],
            verbose=True,
            max_iter=3
        )

    
    @task
    def navigate_HCW (self) -> Task:
        return Task(
            config=self.tasks_config['navigate_HCW'],
            agent=self.navigating_robot(),
            output_file="output/navigate_hcw.txt",
        )
    
    @task
    def collect_info(self) -> Task:
        return Task(
            config=self.tasks_config['collect_info'],
            agent=self.info_collection_robot(),
            output_file="output/collect_info.txt",
        )
    
    @task
    def display_info(self) -> Task:
        return Task(
            config=self.tasks_config['display_info'],
            agent=self.info_display_robot(),
            output_file="output/display_info.txt",
        )
    

    @task
    def reflection_task(self) -> Task:
        return Task(
            config=self.tasks_config['reflection_task']
        )


    @crew
    def crew(self) -> Crew:
        """Creates the Research Crew"""

        # Create the manager agent instance first
        manager = Agent(
            config=self.agents_config['manager'],
            verbose=True,
            allow_delegation=True
        )

        
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.hierarchical,
            # manager_llm="gpt-4o",  # Pass the actual agent instance
            manager_agent=manager,
            verbose=True,
            memory=True, 
            output_log_file=True,
            # knowledge_sources=[text_source]
        )
