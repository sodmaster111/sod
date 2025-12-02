"""Endpoints for retrieving sacred texts."""

from fastapi import APIRouter, Query

from app.integrations.sefaria_client import fetch_text

router = APIRouter(prefix="/texts", tags=["texts"])


@router.get("/tanakh")
async def get_tanakh_text(ref: str = Query(..., description="Например: Tehillim 23:1"), lang: str = "he"):
    text = await fetch_text(ref, lang)
    return {"ref": ref, "lang": lang, "text": text}
