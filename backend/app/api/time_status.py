from datetime import datetime, timezone

from fastapi import APIRouter

from app.utils.jewish_calendar import (
    get_hebrew_date,
    is_no_send_time,
    is_shabbat,
)

router = APIRouter(prefix="/time", tags=["time"])


@router.get("/status")
async def get_time_status():
    """
    Возвращает текущую григорианскую и еврейскую дату,
    а также флаги is_shabbat и is_no_send_time для Asia/Jerusalem.
    """
    now_utc = datetime.now(timezone.utc)

    return {
        "now_utc": now_utc.isoformat(),
        "hebrew_date": get_hebrew_date(now_utc, tz="Asia/Jerusalem"),
        "is_shabbat": is_shabbat(now_utc, tz="Asia/Jerusalem"),
        "is_no_send_time": is_no_send_time(now_utc, tz="Asia/Jerusalem"),
    }
