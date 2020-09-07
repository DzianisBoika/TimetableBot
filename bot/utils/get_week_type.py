from bot.enums import WeekType

import datetime

__all__ = ['get_week_type']


def get_week_type(date: datetime.date):
    week_num = date.isocalendar()[1]
    if week_num % 2 == 1:
        return WeekType.LOWER
    else:
        return WeekType.UPPER
