from app.agents.llm_client import LocalLLMClient

QUALITY_GUARD_SYSTEM_PROMPT = (
    "Ты — редактор SODMASTER. Твоя задача — переписывать пользовательские тексты так, "
    "чтобы они были вежливыми, позитивными и соответствовали тону SODMASTER. "
    "Не добавляй лишнюю информацию, сохраняй смысл и лаконичность."
)


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
