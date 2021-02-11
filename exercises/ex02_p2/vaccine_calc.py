"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730402855"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    days: int = days_to_target(population, doses, doses_per_day, target)
    date_reached: str = future_date(days)
    print("We will reach " + str(target) + "% vaccinated in " + str(days) + " days, which falls on " + date_reached)


def days_to_target(a: int, b: int, c: int, d: int) -> int:
    """Tells us how many days until target vaccination is reached."""
    doses_remaining: float = float(2 * a * (d / 100)) - b
    vaccination_complete: float = float(doses_remaining / c)
    x: int = int(round(vaccination_complete))
    return x


def future_date(x: int) -> str:
    """Tells us the date that vaccination target is reached."""
    today: datetime = datetime.today()
    time_completion: timedelta = timedelta(x)
    future_day: datetime = today + time_completion
    future_day_complete: str = str(future_day.strftime("%B %d, %Y"))
    return future_day_complete


if __name__ == "__main__":
    main()
