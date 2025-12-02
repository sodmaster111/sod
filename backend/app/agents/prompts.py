from app.agents.profiles import RABBI_AGENT

RABBI_AGENT_SYSTEM_PROMPT = (
    f"Ты — {RABBI_AGENT.name}. "
    f"{RABBI_AGENT.role_description}\n"
    f"Твои цели:\n" + "\n".join(f"- {g}" for g in RABBI_AGENT.goals)
)
