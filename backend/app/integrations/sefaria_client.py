from typing import Literal
from urllib.parse import quote

import httpx

BASE_URL = "https://www.sefaria.org/api/texts"


async def fetch_text(ref: str, lang: Literal["he", "en"] = "he") -> str:
    """
    Получает текст Танаха по ссылке ref (например: 'Tehillim 23:1')
    через публичное API Sefaria.

    Если запрос не удался или структура другая — возвращает понятную строку-ошибку.
    """
    url = f"{BASE_URL}/{quote(ref)}?lang={lang}&commentary=0"

    async with httpx.AsyncClient(timeout=10) as client:
        resp = await client.get(url)

    if resp.status_code != 200:
        return f"Ошибка запроса к Sefaria: HTTP {resp.status_code}"

    data = resp.json()

    # В ответе Sefaria обычно есть поле 'he' или 'text'
    # Попробуем вытащить основной текст.
    if lang == "he":
        texts = data.get("he") or data.get("text") or []
    else:
        texts = data.get("text") or data.get("he") or []

    if not texts:
        return "Текст не найден или пуст."

    # Если это список строк — склеиваем.
    if isinstance(texts, list):
        return "\n".join([str(line) for line in texts if line])

    return str(texts)
