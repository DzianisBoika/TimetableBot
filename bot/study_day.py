from bot.para import Para
from bot.utils import get_week_type
from bot.enums import WeekType

import datetime
from dataclasses import dataclass
from typing import List, Iterable


@dataclass
class StudyDay:
    name: str
    upper: List[Para]
    lower: List[Para]

    def _get_paras_by_date(self, date: datetime.date) -> Iterable[Para]:
        week_type = get_week_type(date)

        paras = self.upper if week_type is WeekType.UPPER else self.lower

        paras = [
            para
            for para in paras
            if para.from_date <= date <= para.to_date
        ]

        return paras

    def build_schedule(self, date: datetime.date):
        week_type = get_week_type(date)
        paras = self._get_paras_by_date(date)

        str_paras = [
            f'* {para}'
            for para in paras
        ]

        return '\n'.join([
            f'{self.name} ({week_type.value} неделя)',
            *str_paras,
        ])
