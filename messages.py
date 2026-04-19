import os
import anthropic

_client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
_MODEL = "claude-opus-4-6"

_BASE_SYSTEM = (
    "You are a warm, caring friend sending a WhatsApp message to a PhD student girl. "
    "Keep messages concise (3-5 sentences), genuine, and conversational — not corporate or preachy. "
    "Write in flowing prose, no bullet points, no headers. Use at most 2 emojis. "
    "Address the recipient directly. Never mention the sender by name."
)

_MIDWEEK_THEMES = [
    (
        "Self-worth: remind her that she is enough regardless of her research progress today. "
        "Her value as a person is not tied to her output, experiments, or publications."
    ),
    (
        "Confidence: her unique perspective, curiosity, and intelligence are exactly what the world needs. "
        "She belongs in every room she walks into."
    ),
    (
        "Dream big: her ambitions are valid and she should never shrink them to fit other people's comfort. "
        "The size of her dreams is a feature, not a flaw."
    ),
    (
        "Why she chose PhD: reconnect her with the original spark of curiosity and passion that brought her "
        "to this path. Remind her that her research matters and she chose this for a reason that still holds true."
    ),
]


def _generate(user_prompt: str) -> str:
    msg = _client.messages.create(
        model=_MODEL,
        max_tokens=512,
        system=_BASE_SYSTEM,
        messages=[{"role": "user", "content": user_prompt}],
    )
    return msg.content[0].text.strip()


def generate_start_of_week_message() -> str:
    return _generate(
        "Generate a Monday morning message for a PhD student. "
        "Set a positive, energized tone for the week ahead. "
        "Acknowledge that PhD life is hard but remind her she chose this path for a reason. "
        "Warmly invite her to share what she wants to achieve this week — her plan or checklist. "
        "Keep it personal and uplifting, not generic."
    )


def generate_midweek_message(theme_index: int) -> str:
    theme = _MIDWEEK_THEMES[theme_index % len(_MIDWEEK_THEMES)]
    return _generate(
        f"Generate a midweek motivational message for a PhD student. Focus on this theme: {theme} "
        "Be specific, heartfelt, and empowering. Speak to her as someone who genuinely believes in her."
    )


def generate_end_of_week_message() -> str:
    return _generate(
        "Generate a Sunday evening message for a PhD student wrapping up her week. "
        "Warmly check in on how her week went. Celebrate effort and progress, not just outcomes. "
        "Acknowledge that some weeks are harder than others and that's perfectly okay. "
        "Leave her feeling peaceful and ready to rest. Gently ask how the week treated her."
    )
