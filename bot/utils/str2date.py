import datetime

__all__ = ['str2date']


def str2date(date: str):
    return datetime.datetime.strptime(date, '%d.%m.%Y').date()
