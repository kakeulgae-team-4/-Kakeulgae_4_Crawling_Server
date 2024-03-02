from strategy.incruit.incruit_collector import IncruitCollector
from strategy.jobkorea.jobkorea_collector import JobkoreaCollector
from strategy.saramin.saramin_collector import SaraminCollector


class StrategyManager:
    """
    페이지 유형에 따라 페이지를 파싱함
    """

    def __init__(self):
        self.strategies = [IncruitCollector(), JobkoreaCollector(), SaraminCollector()]
        self.strategy_idx = 0
        self.strategy = self.strategies[self.strategy_idx]

    def get_next_strategy(self) -> None:
        self.strategy_idx += 1
        if self.strategy_idx >= len(self.strategies):
            self.strategy_idx = 0
        self.strategy = self.strategies[self.strategy_idx]

    def execute(self):
        for i in range(len(self.strategies)):
            self.strategy.find_posts()
            self.get_next_strategy()
