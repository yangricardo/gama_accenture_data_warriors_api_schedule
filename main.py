from fastapi import FastAPI
import schedule
import time
import threading


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
    return {"Hello": "World"}
