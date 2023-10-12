from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, declarative_base

Base = declarative_base()


class Answer(Base):
    __tablename__ = 'answers'

    pk: Mapped[int] = mapped_column(primary_key=True)
    id: Mapped[int] = mapped_column(unique=True)
    question: Mapped[str] = mapped_column(unique=True)
    answer: Mapped[str]
    created_at: Mapped[datetime]
