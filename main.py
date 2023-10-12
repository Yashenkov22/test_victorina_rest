import aiohttp

from fastapi import FastAPI

from sqlalchemy.exc import IntegrityError

from config import PUBLIC_API_URL
from schemas import RequestModel, AnswerModel
from utils import get_last_record
from db.queries import save_record
from db.init_db import start_db, async_session


app = FastAPI(
    title='Victorina service',
)


@app.on_event('startup')
async def on_startup():
    await start_db()


@app.post('/get_questions')
async def get_questions(request: RequestModel):
    last_record = await get_last_record()
    questions_num = request.questions_num

    async with aiohttp.ClientSession() as session:
        while questions_num > 0:
            async with session.get(PUBLIC_API_URL.format(questions_num)) as response:
                list_obj = await response.json()

                for obj in list_obj:
                    record = AnswerModel(**obj)
                    try:
                        await save_record(async_session, record)
                    except IntegrityError:
                        continue
                    else:
                        questions_num -= 1
    
    return last_record if last_record else {}