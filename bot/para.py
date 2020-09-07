from bot.enums import Subgroup, ParaType
from bot.utils import str2date
from bot.constants import TIMES

import datetime
from dataclasses import dataclass, InitVar
from typing import Union


@dataclass
class Para:
    order: int
    type: ParaType
    subject: str
    auditory: str
    subgroup: Subgroup = Subgroup.BOTH

    from_: InitVar[Union[datetime.date, str]] = str2date('01.09.2020')
    to: InitVar[Union[datetime.date, str]] = str2date('20.12.2020')

    def __post_init__(self, from_, to):
        self.from_date = str2date(from_) if type(from_) is str else from_
        self.to_date = str2date(to) if type(to) is str else to

    @property
    def interval(self):
        return TIMES[self.order]

    def __str__(self):
        return f'{self.interval}\n{self.subject}, {self.type.value} ({self.auditory}, {self.subgroup.value})'
