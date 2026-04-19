import hashlib
import logging
import os
from datetime import date

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from dotenv import load_dotenv

load_dotenv()

from messages import (
    generate_end_of_week_message,
    generate_midweek_message,
    generate_start_of_week_message,
)
from whatsapp import send_message

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)

TIMEZONE = os.getenv("TIMEZONE", "Asia/Kolkata")
scheduler = BlockingScheduler(timezone=TIMEZONE)


def _midweek_theme_index(today: date) -> int:
    """Deterministically pick a theme index (0-3) based on the week number."""
    seed = int(hashlib.md5(f"{today.year}-{today.isocalendar()[1]}".encode()).hexdigest(), 16)
    return seed % 4


def _midweek_chosen_day(today: date) -> int:
    """Deterministically pick one day per week: 2=Tue, 3=Wed, 4=Thu (ISO weekday)."""
    seed = int(hashlib.md5(f"day-{today.year}-{today.isocalendar()[1]}".encode()).hexdigest(), 16)
    return [2, 3, 4][seed % 3]


@scheduler.scheduled_job(CronTrigger(day_of_week="mon", hour=9, minute=0, timezone=TIMEZONE))
def start_of_week_job():
    log.info("Running start-of-week job")
    msg = generate_start_of_week_message()
    send_message(msg)


@scheduler.scheduled_job(CronTrigger(day_of_week="tue,wed,thu", hour=13, minute=0, timezone=TIMEZONE))
def midweek_job():
    today = date.today()
    if today.isoweekday() != _midweek_chosen_day(today):
        log.info("Midweek job skipped — not the chosen day this week")
        return
    theme_index = _midweek_theme_index(today)
    log.info("Running midweek job (theme index: %d)", theme_index)
    msg = generate_midweek_message(theme_index)
    send_message(msg)


@scheduler.scheduled_job(CronTrigger(day_of_week="sun", hour=19, minute=0, timezone=TIMEZONE))
def end_of_week_job():
    log.info("Running end-of-week job")
    msg = generate_end_of_week_message()
    send_message(msg)


if __name__ == "__main__":
    log.info("Scheduler starting — timezone: %s", TIMEZONE)
    log.info("Jobs: Monday 9am | Tue/Wed/Thu 1pm (one day only) | Sunday 7pm")
    scheduler.start()
