import uuid
from sqlalchemy import Column, String, func, TIMESTAMP
from sqlalchemy_utils import UUIDType

from . import BaseEntity


class AnalysisHistory(BaseEntity):
    __tablename__ = 'analysis_history'

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    code_snippet = Column(String, nullable=False)
    suggestions = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)


    def as_dict(self):
        return {
            "id": str(self.id),
            "code_snippet": self.code_snippet,
            "suggestions": self.suggestions ,
            "created_at": self.created_at,
        }
