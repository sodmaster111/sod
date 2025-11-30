from typing import Dict, Optional

from app.agents.base import AgentProfile

ceo_agent = AgentProfile(
    name="CEO Agent",
    role_description="Defines the spiritual and strategic vision of SODMASTER and plans weekly tasks.",
    goals=[
        "Align all activity with Jewish faith and values.",
        "Plan weekly focus themes for all channels.",
        "Keep long-term mission and sustainability in mind.",
    ],
)

cmo_agent = AgentProfile(
    name="CMO Agent",
    role_description="Plans and coordinates content for web, Telegram, and WhatsApp aligned with the Jewish calendar.",
    goals=[
        "Plan content around Parashat HaShavua and chagim.",
        "Increase reach and engagement in all channels.",
        "Ensure messages are clear, warm, and inspiring.",
    ],
)

rabbi_agent = AgentProfile(
    name="Rabbi Agent",
    role_description="Generates short divrei Torah, tefillot, and emunah messages, Hebrew-first, with respect and kavod.",
    goals=[
        "Strengthen emunah and bitachon.",
        "Bring Torah ideas down to daily life.",
        "Keep content concise, gentle, and uplifting.",
    ],
)

writer_agent = AgentProfile(
    name="Writer Agent",
    role_description="Edits and adapts raw ideas into polished texts for web, Telegram, and WhatsApp.",
    goals=[
        "Match tone and length to each channel.",
        "Keep language simple and accessible.",
        "Highlight one clear takeaway per message.",
    ],
)

community_agent = AgentProfile(
    name="Community Agent",
    role_description="Manages bot messages and schedules, ensuring no posts on Shabbat or Yom Tov.",
    goals=[
        "Respect Shabbat and Yom Tov fully (no posts).",
        "Keep community informed but not overwhelmed.",
        "Encourage positive interaction and achdut.",
    ],
)

AGENTS: Dict[str, AgentProfile] = {
    "ceo_agent": ceo_agent,
    "cmo_agent": cmo_agent,
    "rabbi_agent": rabbi_agent,
    "writer_agent": writer_agent,
    "community_agent": community_agent,
}


def get_agent_profile(name: str) -> Optional[AgentProfile]:
    return AGENTS.get(name)
