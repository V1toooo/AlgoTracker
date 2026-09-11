from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from algotracker.models.base import Base


class AlgorithmTopics(Base):
    __tablename__ = "algorithm_topics"

    # ассоциативная таблица (junction table) для many-to-many Algorithm <-> Topic
    # каждая строка = одна пара "алгоритм принадлежит теме"
    topic_id: Mapped[int] = mapped_column(ForeignKey("topics.id"), primary_key=True)
    algorithm_id: Mapped[int] = mapped_column(ForeignKey("algorithms.id"), primary_key=True)