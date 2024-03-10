from typing import List
from datetime import datetime


class AfterProcessDto:
    __company_name: str
    __post_name: str
    __career: List[str]  # ['신입', '경력']
    __education: str
    __region_1st: str
    __region_2nd: str
    __work_type: str
    __deadline: datetime  # 2024-03-21
    __url: str
    __created_at: datetime
