from typing import TYPE_CHECKING

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from algotracker.models.base import Base

if TYPE_CHECKING:
    from algotracker.models.algorithm import Algorithm

class Topic(Base):
    __tablename__ = "topics"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text(), nullable=False)

    # many-to-many: обратная сторона связи Algorithm.topics
    algorithms: Mapped[list["Algorithm"]] = relationship(
        secondary="algorithm_topics",
        back_populates="topics",
    )
