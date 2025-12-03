from datetime import datetime, timezone
from zoneinfo import ZoneInfo

from hdate import HolidayTypes, Months, date_info, hebrew_date


def _to_timezone(dt: datetime, tz: str) -> datetime:
    """Convert datetime to specified timezone, assuming UTC if naive."""
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(ZoneInfo(tz))


def is_shabbat(dt: datetime, tz: str = "Asia/Jerusalem") -> bool:
    """
    Возвращает True, если в указанной временной зоне сейчас шаббат
    (между заходом солнца в пятницу и выходом шаббата в субботу).
    Пока можно реализовать упрощённо: считать шаббатом всю субботу по календарному дню.
    """
    local_dt = _to_timezone(dt, tz)
    return local_dt.weekday() == 5


def is_no_send_time(dt: datetime, tz: str = "Asia/Jerusalem") -> bool:
    """
    Возвращает True, если в указанное время нельзя делать автоматические рассылки.
    На первом этапе:
    - Шаббат (вся суббота по календарю в указанной tz)
    - Йом-тов (основные праздники, определяемые через hdate)
    """

    local_dt = _to_timezone(dt, tz)

    if is_shabbat(local_dt, tz):
        return True

    info = date_info.HDateInfo(local_dt.date())

    yom_tov_holidays = {
        "rosh_hashana_i",
        "rosh_hashana_ii",
        "yom_kippur",
        "pesach",
        "pesach_vii",
        "shavuot",
        "sukkot",
        "shmini_atzeret",
        "simchat_torah",
    }

    yom_tov_dates = {
        (Months.TISHREI, 1),
        (Months.TISHREI, 2),
        (Months.TISHREI, 10),
        (Months.NISAN, 15),
        (Months.NISAN, 21),
        (Months.SIVAN, 6),
        (Months.TISHREI, 15),
        (Months.TISHREI, 22),
    }

    hebrew_dt = info.date
    if (hebrew_dt.month, hebrew_dt.day) in yom_tov_dates:
        return True

    for holiday in info.holidays:
        if holiday.type == HolidayTypes.YOM_TOV and holiday.name in yom_tov_holidays:
            return True

    return False


def get_hebrew_date(dt: datetime, tz: str = "Asia/Jerusalem") -> str:
    """
    Возвращает строку с еврейской датой (например: '1 Tishrei 5786').
    """
    local_dt = _to_timezone(dt, tz)
    hebrew_dt = hebrew_date.HebrewDate.from_gdate(local_dt.date())
    return str(hebrew_dt)
