from sqlalchemy.ext.declarative import declarative_base
BaseEntity = declarative_base()
from .analysis_history import AnalysisHistory
from .llm_provider import LLM
