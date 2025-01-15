from crewai import Task
from agents.agents import Agents
from utils import Environment


class Tasks:
    def __init__(self, agents: Agents):
        self.agents = agents
        self.language = Environment.get("LANGUAGE_RESPONSE","Brazilian Portuguese")

    def get_code_improvement_task(self, code: str) -> Task:
        return Task(
            description=f"""
                  Review the following code snippet and identify possible improvements in terms of structure, 
                  readability, reusability, and adherence to development standards, Clean Architecture, and SOLID principles. 
                  Highlight suboptimal practices and suggest refactorings to enhance code clarity and efficiency.

                  Please ensure that the analysis and suggestions are provided in **{self.language}**.

                  Code to review:
                  {code}
              """,
            agent=self.agents.get_code_improvement_agent(),
            expected_output="A detailed analysis of the code, identifying areas for improvement in best practices, organization, and efficiency, along with actionable suggestions for enhancement. The output must be in Brazilian Portuguese."
        )
