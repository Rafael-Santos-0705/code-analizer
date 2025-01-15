from entities import AnalysisHistory
from repositories.base_db import BaseDBRepository


class AnalyzerRepository(BaseDBRepository):
    def __init__(self):
        super().__init__(AnalysisHistory)
