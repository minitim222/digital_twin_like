# src/digital_twin_like/crew.py
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from digital_twin_like.tools.knowledge_tool import KNOWLEDGE_TOOLS

@CrewBase
class DigitalTwinLike():
    """DigitalTwinLike crew"""

    @agent
    def digital_twin_tim(self) -> Agent:
        return Agent(
            config=self.agents_config['digital_twin_tim'],
            verbose=True,
            tools=KNOWLEDGE_TOOLS  # Add knowledge base tools
        )

    @task
    def introduction_task(self) -> Task:
        return Task(
            config=self.tasks_config['introduction_task'],
        )

    @task
    def research_explanation_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_explanation_task'],
        )

    @task
    def skills_showcase_task(self) -> Task:
        return Task(
            config=self.tasks_config['skills_showcase_task'],
        )

    @task
    def career_goals_task(self) -> Task:
        return Task(
            config=self.tasks_config['career_goals_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the DigitalTwinLike crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )