from fastapi import APIRouter, Query

from app.integrations.sefaria_client import fetch_text

router = APIRouter(prefix="/texts", tags=["texts"])


@router.get("/tanakh")
async def get_tanakh_text(
    ref: str = Query(..., description="Например: 'Tehillim 23:1'"),
    lang: str = Query("he", pattern="^(he|en)$"),
):
    """
    Возвращает текст Танаха по ссылке ref из Sefaria.
    Параметр lang: 'he' или 'en'.
    """
    text = await fetch_text(ref=ref, lang=lang)  # type: ignore[arg-type]
    return {"ref": ref, "lang": lang, "text": text}
