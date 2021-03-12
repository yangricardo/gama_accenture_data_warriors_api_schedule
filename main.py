import threading
from fastapi import FastAPI
from scenery import Scenery
from consume_covid19_api_job import ConsumeCovid19Api

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    consume_api = ConsumeCovid19Api()
    consume_api_thread = threading.Thread(
        target=consume_api.run_scheduled_job, args=())
    consume_api_thread.start()


@app.get("/")
def read_root():
    import json
    scenery = Scenery()
    sceneries = []
    sceneries.append(scenery.daily_cases())
    sceneries.append(scenery.daily_deaths())
    sceneries.append(scenery.total_cases())
    sceneries.append(scenery.total_deaths())
    sceneries = list(
        map(lambda s: {'title': s[0], 'data': json.loads(s[1].to_json(orient='records'))}, sceneries))
    return sceneries
