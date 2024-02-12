import time
import schedule


class Scheduler(schedule.Scheduler):
    def add_job_with_seconds(self, interval_seconds, job_function, *args):
        job = schedule.every(interval_seconds).seconds.do(job_function, *args)
        self.jobs.append(job)

    def add_job_with_minutes(self, interval_minutes, job_function):
        job = schedule.every(interval_minutes).minutes.do(job_function)

    def run(self):
        while True:
            schedule.run_pending()
            time.sleep(1)


