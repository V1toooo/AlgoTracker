from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from algotracker.models.base import Base

if TYPE_CHECKING:
    from algotracker.models.problem import Problem
    from algotracker.models.topic import Topic

class Algorithm(Base):
    __tablename__ = 'algorithms'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    # many-to-many: один алгоритм может относиться к нескольким темам,
    # одна тема может включать несколько алгоритмов
    topics: Mapped[list["Topic"]] = relationship(secondary="algorithm_topics", back_populates="algorithms")

    # many-to-many: один алгоритм может использоваться в нескольких задачах,
    # одна задача может использовать несколько алгоритмов
    problems: Mapped[list["Problem"]] = relationship(secondary="algorithm_problems", back_populates="algorithms")