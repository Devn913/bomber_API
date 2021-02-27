from fastapi import FastAPI, BackgroundTasks
from typing import Optional
from smsbomber import Bomber


app = FastAPI()

@app.get("/")
async def home():
    return {"status": "Welcome to API :)"}


@app.get("/bomb")
async def bomb(background_tasks: BackgroundTasks,number: str, noOfMsg: Optional[int] = 50):
    if len(number) == 10 and number.isdigit():
        pass
    else:
        return {"status": "Check Your Entries"}
    bombobj = Bomber(number, noOfMsg)
    background_tasks.add_task(bombobj.startBombing) # Calling it as background task so the responce dont take time.
    return {"status": "Sending"}
