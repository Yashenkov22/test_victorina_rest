from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import Answer
from schemas import AnswerModel


async def save_record(session: AsyncSession, obj: AnswerModel):
    obj.created_at = obj.created_at.replace(tzinfo=None)
    async with session() as session:
        async with session.begin():
            await session.execute(insert(Answer).values(obj.dict()))


async def select_last_record(session: AsyncSession):
    async with session() as session:
        async with session.begin():
            result = await session.execute(select(Answer).order_by(Answer.pk.desc()).limit(1))
    return result.scalar_one_or_none()