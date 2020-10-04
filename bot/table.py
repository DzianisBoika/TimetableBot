from bot.enums import ParaType, Subgroup
from bot.para import Para
from bot.study_day import StudyDay
from bot.utils import str2date

import datetime
from typing import Union

__all__ = ['get_schedule_by_date']

SCHEDULE = [
    StudyDay(
        name='Понедельник',
        upper=[
            Para(3, ParaType.LECTURE, 'ССП', '1/109'),
            Para(4, ParaType.PRACTICE, 'ТПИС', '2/06'),
            Para(5, ParaType.LECTURE, 'СИИТ', '2/103'),
        ],
        lower=[
            Para(3, ParaType.LECTURE, 'ССП', '1/109'),
            Para(4, ParaType.LECTURE, 'ССП', '1/109'),
        ],
    ),
    StudyDay(
        name='Вторник',
        upper=[
            Para(3, ParaType.LAB, 'ТПИС', '2/310', Subgroup.FIRST),
            Para(3, ParaType.LAB, 'ГИИС', '2/411', Subgroup.SECOND),

            Para(4, ParaType.LAB, 'ТПИС', '2/310', Subgroup.FIRST),
            Para(4, ParaType.LAB, 'ГИИС', '2/411', Subgroup.SECOND),

            Para(5, ParaType.LECTURE, 'ГИИС', '2/209'),
        ],
        lower=[
            Para(3, ParaType.LAB, 'ГИИС', '2/411', Subgroup.FIRST),
            Para(3, ParaType.LAB, 'ТПИС', '2/310', Subgroup.SECOND),

            Para(4, ParaType.LAB, 'ГИИС', '2/411', Subgroup.FIRST),
            Para(4, ParaType.LAB, 'ТПИС', '2/310', Subgroup.SECOND),

            Para(5, ParaType.LECTURE, 'ГИИС', '2/209'),
        ],
    ),
    StudyDay(
        name='Среда',
        upper=[
            Para(1, ParaType.LAB, 'ЕЯИИС', '3/129', Subgroup.FIRST),
            Para(1, ParaType.LAB, 'ССП', '2/310', Subgroup.SECOND),

            Para(2, ParaType.LAB, 'ЕЯИИС', '3/129', Subgroup.FIRST),
            Para(2, ParaType.LAB, 'ССП', '2/310', Subgroup.SECOND),

            Para(3, ParaType.LECTURE, 'ТПИС', '1/310'),
            Para(4, ParaType.LECTURE, 'ГИИС', '2/409'),
        ],
        lower=[
            Para(1, ParaType.LAB, 'ССП', '2/310', Subgroup.FIRST),
            Para(1, ParaType.LAB, 'ЕЯИИС', '3/129', Subgroup.SECOND),

            Para(2, ParaType.LAB, 'ССП', '2/310', Subgroup.FIRST),
            Para(2, ParaType.LAB, 'ЕЯИИС', '3/129', Subgroup.SECOND),

            Para(3, ParaType.LECTURE, 'ТПИС', '1/310'),
            Para(4, ParaType.PRACTICE, 'ГИИС', '2/409'),
        ],
    ),
    StudyDay(
        name='Четверг',
        upper=[
            Para(0, ParaType.LAB, 'СИИТ', '2/215 (ДО)',
                 Subgroup.FIRST, '17.09.2020', '29.10.2020'),
            Para(1, ParaType.LAB, 'СИИТ', '2/215 (ДО)',
                 Subgroup.FIRST, '17.09.2020', '29.10.2020'),
            Para(2, ParaType.LECTURE, 'СИИТ', '2/215 (ДО)', to='19.11.2020'),
            Para(3, ParaType.LECTURE, 'СМЗКС', '2/109 (ДО)'),

        ],
        lower=[
            Para(0, ParaType.LAB, 'СИИТ', '2/215 (ДО)',
                 Subgroup.SECOND, to='17.10.2020'),
            Para(1, ParaType.LAB, 'СИИТ', '2/215 (ДО)',
                 Subgroup.SECOND, to='17.10.2020'),
            Para(2, ParaType.LECTURE, 'СИИТ', '2/215 (ДО)', to='19.11.2020'),
            Para(3, ParaType.LECTURE, 'СМЗКС', '2/109 (ДО)'),
        ],
    ),
    StudyDay(
        name='Пятница',
        upper=[],
        lower=[],
    ),
    StudyDay(
        name='Суббота',
        upper=[
            Para(4, ParaType.LECTURE, 'ЕЯИИС', '1/402'),
            Para(5, ParaType.LAB, 'СМЗКТ', '2/215 (ДО)'),
        ],
        lower=[
            Para(4, ParaType.LECTURE, 'ЕЯИИС', '1/402'),
            Para(5, ParaType.LAB, 'СМЗКТ', '2/215 (ДО)'),
        ],
    ),
    StudyDay(
        name='Воскресенье',
        upper=[],
        lower=[],
    ),
]


def get_schedule_by_date(date: Union[datetime.date, str]):
    if date == 'today':
        date = datetime.datetime.now().date()
        if type(date) is str:
            date = str2date(date)
        weekday = date.weekday()
        study_day = SCHEDULE[weekday]
        schedule = study_day.build_schedule(date)

    if date == 'tomorrow':
        today = datetime.date.today()
        date = today + datetime.timedelta(days=1)
        if type(date) is str:
            date = str2date(date)
        weekday = date.weekday()
        study_day = SCHEDULE[weekday]
        schedule = study_day.build_schedule(date)

    if type(date) is not datetime.date:
        raise TypeError

    return schedule
