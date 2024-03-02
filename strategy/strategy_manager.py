from strategy.incruit.incruit_collector import IncruitCollector


class StrategyManager:
    """
    페이지 유형에 따라 페이지를 파싱함
    """

    def __init__(self):
        self.strategies = [IncruitCollector()]
        self.strategy_idx = 0
        self.strategy = self.strategies[self.strategy_idx]

    def get_next_strategy(self) -> None:
        self.strategy_idx += 1
        if self.strategy_idx >= len(self.strategies):
            self.strategy_idx = 0
        self.strategy = self.strategies[self.strategy_idx]

    def execute(self):
        return self.strategy.find_posts()
