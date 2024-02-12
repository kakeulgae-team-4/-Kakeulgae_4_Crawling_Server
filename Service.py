from scheduler.Scheduler import Scheduler
from StrategyManager import StrategyManager


class Service:
    def __init__(self):
        self.scheduler = Scheduler()
        self.strategy_manager = StrategyManager()

    def start(self):
        self.scheduler.add_job_with_seconds(10, self.strategy_manager.execute())
        # self.scheduler.add_job(10, self.strategy_manager.get_next_strategy())
        self.scheduler.run()
