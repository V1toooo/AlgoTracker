import enum
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Enum, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from algotracker.models.base import Base

if TYPE_CHECKING:
    from algotracker.models.algorithm import Algorithm

class Difficulty(str, enum.Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


class Status(str, enum.Enum):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    SOLVED = "solved"


class Problem(Base):
    __tablename__ = "problems"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    url: Mapped[str] = mapped_column(String(500), nullable=True)
    difficulty: Mapped[Difficulty] = mapped_column(Enum(Difficulty), nullable=False)
    status: Mapped[Status] = mapped_column(Enum(Status), default=Status.NOT_STARTED)
    solved_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    # many-to-many: обратная сторона связи Algorithm.problems
    algorithms: Mapped[list["Algorithm"]] = relationship(
        secondary="algorithm_problems",
        back_populates="problems",
    )