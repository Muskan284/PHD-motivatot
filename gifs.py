import random

# Add your favourite GIF direct URLs here (right-click a GIF on Giphy/Tenor → "Copy image address")
# Format: https://media.giphy.com/media/<id>/giphy.gif  OR  https://media.tenor.com/<id>/name.gif

MONDAY_GIFS = [
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdWE1bnk0OHZjMm83Nmx2dHo3aHZhbzFsdGJxbjh0bWwxcXpwanV3eSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l0MYt5jPR6QX5pnqM/giphy.gif",   # let's go
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHVyNHdzNW80OHA4NGMwYWdlbThqNXdlcWplMnVpcHZ0ZWVxdTVwNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/CjmvTCZf2U3p09Cn0h/giphy.gif",  # morning coffee
]

MIDWEEK_GIFS = [
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaWo0aTVhNWE2NjN6b2Y3Njc3NTR6enVhcHI0aGlsMGpib2g5dWpyMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/26BRuo6sLetdllPAQ/giphy.gif",   # you got this
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNzM3Nm83NzBhOTVzMXM2OWd6cWs4aXBoaWdiZGE1MWVsaTBzaGYwYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKSha51ATTx9KzC/giphy.gif", # keep going
]

SUNDAY_GIFS = [
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbzZrcWthbjRjM3VlMnVudjdhZWF5bzNiNnVzbzFhOTJqeXlrNHpkcSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l4Ep6uxU6aedrYUuk/giphy.gif",   # chill/rest
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbzZrcWthbjRjM3VlMnVudjdhZWF5bzNiNnVzbzFhOTJqeXlrNHpkcSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xT9IgG50Lg7russbDa/giphy.gif", # proud of you
]


def random_monday_gif() -> str:
    return random.choice(MONDAY_GIFS)


def random_midweek_gif() -> str:
    return random.choice(MIDWEEK_GIFS)


def random_sunday_gif() -> str:
    return random.choice(SUNDAY_GIFS)
