import os
import random
from groq import Groq

_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
_SYSTEM_PROMPT = (
    "You are texting your best friend of 10 years on WhatsApp. Her name is Akansha, you call her Akku. "
    "She's doing a Geology PhD and you want to hype her up — but like a real friend, not a life coach. "
    "Keep it 2-3 lines max. Casual, punchy, genuinely funny. Address her as Akku. Geology puns and jokes are welcome but only if they land naturally — don't force every line. "
    "Use 2-4 emojis freely — sprinkle them in like a real WhatsApp chat. No corporate fluff, no 'you got this queen' energy. "
    "Sound like a real human text, not a motivational poster. Each message should feel fresh and different."
)

_MIDWEEK_THEMES = [
    "Her experiments flopped — make a geology pun about it (schist happens, faults are normal, etc.) then remind her it doesn't define her week.",
    "She's doubting herself midweek. Roast her for it with a geology angle — like 'you literally study how the earth was built and you're worried about one bad day?'",
    "Her ambitions are massive and intimidating to everyone else. Use a geology metaphor — tectonic, groundbreaking, pressure making diamonds etc. but keep it funny not cheesy.",
    "Reconnect her with why she started — in a 'hey remember when you were absolutely feral about rocks' kind of way. Fond teasing.",
    "Mid-week slump. Joke about it being slower than tectonic plates, then nudge her that she's almost through it.",
    "She's been grinding. Call it out plainly, maybe with a geology quip. Keep it warm and short.",
]

_SOW_ANGLES = [
    "Monday banter — kick off with a geology joke about the week ahead (like 'another week of staring at rocks, love that for you') then ask Akku to drop her goals for the week in the chat.",
    "Hype Akku up for Monday but sneak in a geology pun. Ask her what she wants to nail this week and to share her list.",
    "Monday nudge — remind Akku she survived last week (with some geology twist) and ask what she's going after this week. Tell her to share her goals so you can hold her to it.",
    "Ask Akku what the one thing she wants to crush this week is. Maybe tease that it better not take geological time. Ask her to drop her weekly goals.",
]

_EOW_ANGLES = [
    "Sunday check-in — ask how the week went, no pressure, just genuinely curious.",
    "Wrap up the week by celebrating that she showed up, whatever that looked like.",
    "End of week banter — how bad was it really? Ask her. Make it feel safe to vent.",
    "Tell her to rest and mean it. She's been grinding. Keep it short and warm.",
]


def _generate(prompt: str) -> str:
    response = _client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": _SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
        temperature=1.1,
    )
    return response.choices[0].message.content.strip()


def generate_start_of_week_message() -> str:
    angle = random.choice(_SOW_ANGLES)
    return _generate(f"Write a Monday morning WhatsApp text to your PhD friend. Angle: {angle}")


def generate_midweek_message(theme_index: int) -> str:
    theme = _MIDWEEK_THEMES[theme_index % len(_MIDWEEK_THEMES)]
    return _generate(f"Write a midweek WhatsApp text to your PhD friend. Vibe: {theme}")


def generate_end_of_week_message() -> str:
    angle = random.choice(_EOW_ANGLES)
    return _generate(f"Write a Sunday evening WhatsApp text to your PhD friend. Angle: {angle}")
