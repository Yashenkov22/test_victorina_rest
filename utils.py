from db.queries import select_last_record
from schemas import AnswerModel
from db.init_db import async_session


async def get_last_record():
    last_record = await select_last_record(async_session)

    if last_record:
        ans = AnswerModel(**last_record.__dict__)
        return ans.dict()