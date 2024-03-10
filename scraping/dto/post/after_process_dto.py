from typing import List, Dict
from datetime import datetime

class AfterProcessDto:
    def __init__(self):
        self.__company_name: str
        self.__post_name: str
        self.__career: List[str]
        self.__education: str
        self.__location = Dict[str]
        self.__work_type: str
        self.__deadline: datetime
        self.__url: str
        self.__created_at: datetime
