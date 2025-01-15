from crewai import Crew
from fastapi import HTTPException, Depends
import logging
from typing import Optional, Dict, Any

from agents.agents import Agents
from agents.tasks import Tasks
from entities import AnalysisHistory
from entities.llm_provider import LLMProvider
from repositories import AnalyzerRepository


class CodeAnalyzerService:
    def __init__(self, analyzer_repository: AnalyzerRepository = Depends()):
        llm_provider = LLMProvider()
        self.agents = Agents(llm_provider)
        self.analyzer_repository = analyzer_repository
        self.tasks = Tasks(self.agents)

    def code_analizer(self, code: str) -> Optional[Dict[str, Any]]:
        try:
            code_improvement_task = self.tasks.get_code_improvement_task(code)
            crew = Crew(
                agents=[
                    self.agents.get_code_improvement_agent(),
                ],
                tasks=[code_improvement_task],
            )
            crew_result = crew.kickoff()
            analysis_entry = AnalysisHistory(
                code_snippet=str(code),
                suggestions=str(crew_result)
            )
            self.analyzer_repository.create(analysis_entry)
            return str(crew_result)
        except Exception as e:
            logging.error(e)
            raise HTTPException(status_code=500, detail=f"Erro na análise de código")
