from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from algotracker.models.base import Base


class AlgorithmProblems(Base):
    __tablename__ = "algorithm_problems"

    # ассоциативная таблица (junction table) для many-to-many Algorithm <-> Problem
    # каждая строка = одна пара "задача решается с помощью такого-то алгоритма"
    problem_id: Mapped[int] = mapped_column(ForeignKey("problems.id"), primary_key=True)
    algorithm_id: Mapped[int] = mapped_column(ForeignKey("algorithms.id"), primary_key=True)