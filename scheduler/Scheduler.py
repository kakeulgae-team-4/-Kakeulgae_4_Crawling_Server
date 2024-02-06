import time
import schedule


class Scheduler(schedule.Scheduler):
    def add_job(self, interval_seconds, job_function):
        job = schedule.every(interval_seconds).seconds.do(job_function)
        self.jobs.append(job)

    def run(self):
        while True:
            schedule.run_pending()
            time.sleep(1)


if __name__ == '__main__':
    scheduler = Scheduler()
    def f():
        print('hi')

    class Test:
        @staticmethod
        def hi():
            time.sleep(1)
            print('this is from class')

        def hi2(self):
            time.sleep(1)
            print('this is instance')

    test = Test()
    scheduler.add_job(3, f)
    scheduler.add_job(5, Test.hi)
    scheduler.add_job(7, test.hi2)
    scheduler.run()
