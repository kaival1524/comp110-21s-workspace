"""A vaccination calculator."""

__author__ = "730402855"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


population: int = int(input("Popululation: "))
doses_administered: int = int(input("Doses administered: "))
doses_per_day: int = int(input("Doses per day: "))
target_percent_vaccinated: int = int(input("Target percent vaccinated: "))

today: datetime = datetime.today()

doses_remaining: float = float(2 * population * (target_percent_vaccinated / 100)) - doses_administered
vaccination_target_complete: float = float(doses_remaining / doses_per_day)
round(vaccination_target_complete)

time_completion: timedelta = timedelta(vaccination_target_complete)
future_day: datetime = today + time_completion

print("We will reach " + str(target_percent_vaccinated) + "% vaccination in " + str(round(vaccination_target_complete)) + " days, which falls on " + future_day.strftime("%B %d, %Y"))