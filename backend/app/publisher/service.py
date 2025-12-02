from app.agents.llm_client import LocalLLMClient
from app.publisher import PUBLISHER_AGENT_SYSTEM_PROMPT


async def format_for_telegram(text: str) -> str:
    """Format arbitrary text into a ready-to-post Telegram message."""
    client = LocalLLMClient()
    user_prompt = f"Приведи этот текст к формату готового поста для Telegram:\n\n{text}"
    return await client.generate(
        system_prompt=PUBLISHER_AGENT_SYSTEM_PROMPT,
        user_prompt=user_prompt,
    )
