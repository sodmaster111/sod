from app.agents.llm_client import LocalLLMClient
from app.agents.prompts import QUALITY_GUARD_SYSTEM_PROMPT


async def clean_text(text: str) -> str:
    client = LocalLLMClient()
    user_prompt = (
        "Проверь и при необходимости мягко перепиши этот текст в стиле SODMASTER:\n\n"
        f"{text}"
    )
    return await client.generate(
        system_prompt=QUALITY_GUARD_SYSTEM_PROMPT,
        user_prompt=user_prompt,
    )
