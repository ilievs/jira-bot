from datetime import tzinfo, datetime
from random import randint


def get_random_date_underscored(date_timezone: tzinfo = None):
    current_year = datetime.now().year
    return datetime(year=randint(2005, current_year),
                    month=randint(1, 12),
                    day=randint(1, 28),
                    tzinfo=date_timezone)\
        .strftime('%Y_%m_%d')


def get_random_date_iso(date_timezone=None):
    current_year = datetime.now().year
    return datetime(year=randint(2005, current_year),
                    month=randint(1, 12),
                    day=randint(1, 28),
                    tzinfo=date_timezone)\
        .isoformat()