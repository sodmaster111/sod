"""Client helpers for retrieving texts from Sefaria API."""

import httpx

BASE_URL = "https://www.sefaria.org/api/texts/"


async def fetch_text(ref: str, lang: str = "he") -> str:
    """
    Получает текст по ссылке ref (например: 'Tehillim 23:1') через публичное Sefaria API
    или возвращает понятное сообщение об ошибке.
    """

    url = f"{BASE_URL}{ref}"
    params = {"lang": lang}

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
    except httpx.HTTPError as exc:  # pragma: no cover - network errors not covered in tests
        return f"Ошибка при обращении к Sefaria API: {exc}"

    try:
        payload = response.json()
    except ValueError:
        return "Некорректный ответ от Sefaria API."

    content_key = "he" if lang == "he" else "text"
    content = payload.get(content_key)

    if isinstance(content, list):
        content = " ".join(filter(None, content))

    if not content:
        return "Текст не найден или отсутствует."

    if not isinstance(content, str):
        content = str(content)

    return content
