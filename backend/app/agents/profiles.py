from app.agents.base import AgentProfile


DEFAULT_SYSTEM_PROMPT = "You are SODMASTER, a local-first AI agency that responds concisely and safely."


def get_default_profile() -> AgentProfile:
    """Return the default agent profile used across the stack."""
    return AgentProfile(name="default", system_prompt=DEFAULT_SYSTEM_PROMPT)
