from enum import Enum


class Subgroup(Enum):
    BOTH = 'Обе подгруппы'
    FIRST = 'Первая подгруппа'
    SECOND = 'Вторая подгруппа'


class ParaType(Enum):
    LECTURE = 'Лекция'
    PRACTICE = 'Практика'
    LAB = 'Лаба'


class WeekType(Enum):
    UPPER = 'Верхняя'
    LOWER = 'Нижняя'
