"""
Local test script — run: python test.py
"""
import os
from dotenv import load_dotenv

load_dotenv()


def check_env():
    required = ["GROQ_API_KEY", "GREEN_API_INSTANCE_ID", "GREEN_API_TOKEN", "WHATSAPP_GROUP_CHAT_ID"]
    missing = [k for k in required if not os.getenv(k)]
    if missing:
        print(f"❌ Missing env vars: {', '.join(missing)}")
        print("   Copy .env.example to .env and fill in your keys first.")
        return False
    print("✅ All env vars present")
    return True


def test_messages():
    from messages import (
        generate_start_of_week_message,
        generate_midweek_message,
        generate_end_of_week_message,
    )

    print("\n" + "=" * 60)
    print("  Generating all message types via Groq")
    print("=" * 60)

    print("\n[MON] Start of week")
    print("-" * 40)
    monday = generate_start_of_week_message()
    print(monday)

    print("\n[MID] Midweek — theme 0 (self-worth)")
    print("-" * 40)
    midweek_0 = generate_midweek_message(0)
    print(midweek_0)

    print("\n[MID] Midweek — theme 2 (dream big)")
    print("-" * 40)
    midweek_2 = generate_midweek_message(2)
    print(midweek_2)

    print("\n[SUN] End of week")
    print("-" * 40)
    sunday = generate_end_of_week_message()
    print(sunday)

    print("\n" + "=" * 60)
    return monday, midweek_0, midweek_2, sunday


def test_all_midweek_themes():
    from messages import generate_midweek_message

    print("\n" + "=" * 60)
    print("  All 6 midweek themes")
    print("=" * 60)
    for i in range(6):
        print(f"\n[Theme {i}]")
        print("-" * 40)
        print(generate_midweek_message(i))
    print("\n" + "=" * 60)


def test_gif_urls():
    from gifs import MONDAY_GIFS, MIDWEEK_GIFS, SUNDAY_GIFS
    import requests

    print("\n" + "=" * 60)
    print("  Checking GIF URLs are reachable")
    print("=" * 60)
    all_ok = True
    for label, urls in [("Monday", MONDAY_GIFS), ("Midweek", MIDWEEK_GIFS), ("Sunday", SUNDAY_GIFS)]:
        for url in urls:
            try:
                r = requests.head(url, timeout=5)
                status = "✅" if r.status_code == 200 else f"⚠️  {r.status_code}"
                all_ok = all_ok and r.status_code == 200
            except Exception as e:
                status = f"❌ {e}"
                all_ok = False
            print(f"  {label}: {status}  {url[:70]}...")
    print()
    return all_ok


def send_full_flow(msg_type: str):
    from messages import (
        generate_start_of_week_message,
        generate_midweek_message,
        generate_end_of_week_message,
    )
    from gifs import random_monday_gif, random_midweek_gif, random_sunday_gif
    from whatsapp import send_message, send_gif

    if msg_type == "mon":
        msg, gif = generate_start_of_week_message(), random_monday_gif()
    elif msg_type == "mid":
        msg, gif = generate_midweek_message(0), random_midweek_gif()
    else:
        msg, gif = generate_end_of_week_message(), random_sunday_gif()

    print(f"\nMessage:\n{msg}\n")
    print(f"GIF: {gif}\n")
    print("Sending message...")
    send_message(msg)
    print("Sending GIF...")
    send_gif(gif)
    print("✅ Done! Check your WhatsApp group.")


if __name__ == "__main__":
    if not check_env():
        exit(1)

    print("\nWhat do you want to test?")
    print("  1 - Generate all messages (no WhatsApp send)")
    print("  2 - Check all GIF URLs are reachable")
    print("  3 - All 6 midweek themes")
    print("  4 - Send full Monday flow to WhatsApp (message + GIF)")
    print("  5 - Send full Midweek flow to WhatsApp (message + GIF)")
    print("  6 - Send full Sunday flow to WhatsApp (message + GIF)")
    print("  q - Quit")

    choice = input("\nChoice: ").strip().lower()

    if choice == "1":
        test_messages()
    elif choice == "2":
        test_gif_urls()
    elif choice == "3":
        test_all_midweek_themes()
    elif choice == "4":
        send_full_flow("mon")
    elif choice == "5":
        send_full_flow("mid")
    elif choice == "6":
        send_full_flow("sun")
    else:
        print("Bye!")
