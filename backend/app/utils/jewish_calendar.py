from datetime import datetime, timezone
from zoneinfo import ZoneInfo

from hdate import HDate


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


def get_hebrew_date(dt: datetime, tz: str = "Asia/Jerusalem") -> str:
    """
    Возвращает строку с еврейской датой (например: '1 Tishrei 5786').
    """
    local_dt = _to_timezone(dt, tz)
    hebrew_date = HDate(local_dt.date())
    return str(hebrew_date)
