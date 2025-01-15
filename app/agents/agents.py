from crewai import Agent
from fastapi import Depends

from entities.llm_provider import LLMProvider


class Agents:
    def __init__(self, llm_provider: LLMProvider = Depends()):
        self.llm = llm_provider.model

    def get_code_improvement_agent(self) -> Agent:
        return Agent(
            role="Code Improvement Specialist",
            goal="Analyze the existing code and suggest improvements based on SOLID principles and key design patterns.",
            backstory=(""""
            This agent specializes in identifying violations of best development practices and proposing solutions 
            that follow SOLID principles (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion). 
            It is also capable of recommending and applying design patterns such as Factory, Singleton, Strategy, and Observer, 
            enhancing the maintainability and extensibility of the system.
            """),
            llm=self.llm
        )
