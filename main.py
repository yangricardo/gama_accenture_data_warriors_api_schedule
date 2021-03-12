from fastapi import FastAPI
import schedule
import time
import threading
from scenery import Scenery


class GetDataJob(object):

    def __init__(self, message="I'm working...", seconds=10):
        self.schedule = schedule
        self.message = message
        self.seconds = seconds

    def job(self):
        print(self.message)

    def runJob(self):
        self.schedule.every(self.seconds).seconds.do(self.job)
        while True:
            self.schedule.run_pending()
            time.sleep(1)


app = FastAPI()


@app.on_event("startup")
async def startup_event():
    imWorkingJob = GetDataJob(seconds=2)
    imWorkingJobThread = threading.Thread(
        target=imWorkingJob.runJob, args=())
    imWorkingJobThread.start()
    imStillWorkingJob = GetDataJob(message="I'm still working...", seconds=3)
    imStillWorkingJobThread = threading.Thread(
        target=imStillWorkingJob.runJob, args=())
    imStillWorkingJobThread.start()


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
