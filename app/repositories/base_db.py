from typing import TypeVar, Type, Any, List, Dict
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session as ORMSession, Query
from utils import Environment

T = TypeVar("T")


class BaseDBRepository:
    _engine: Any = create_engine(Environment.get("DATABASE_URL"), echo=True)
    _Session: ORMSession = sessionmaker(bind=_engine)

    def __init__(self, entity: Type[T]):
        """
        Initializes the repository with a specific entity.
        """
        self.session: ORMSession = self._Session()
        self.entity = entity

    def __del__(self):
        self.session.close()

    def find_all(self) -> List[T]:
        """
        Returns all records of the entity.
        """
        return self.session.query(self.entity).all()

    def find_by(self, **filters: Dict[str, Any]) -> Query[T]:
        """
        Returns filtered records for the entity.
        """
        query = self.session.query(self.entity)

        if filters:
            filter_conditions = [
                getattr(self.entity, attr) == value
                for attr, value in filters.items()
                if hasattr(self.entity, attr)
            ]

            if filter_conditions:
                query = query.filter(and_(*filter_conditions))

        return query

    def create(self, entity_instance: T):
        """
        Adds a new instance of the entity to the database.
        """
        self.session.add(entity_instance)
        self.session.commit()

    def update(self, uid: Any, **kwargs: Dict[str, Any]):
        """
        Updates a record by its UID.
        """
        instance = self.find_by(uid=uid).one_or_none()

        if instance:
            for key, value in kwargs.items():
                setattr(instance, key, value)

            self.session.commit()

    def delete(self, uid: Any):
        """
        Deletes a record by its UID.
        """
        instance = self.find_by(uid=uid).one_or_none()

        if instance:
            self.session.delete(instance)
            self.session.commit()
