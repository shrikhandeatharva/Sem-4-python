import datetime
import calendar

# Get today's date
today = datetime.date.today()

# Get the current day of the week (0 - Monday, 1 - Tuesday, ..., 6 - Sunday)
current_day = today.weekday()

# Create a list of weekdays
weekdays = list(calendar.day_name)

# Print the next five weekdays
for i in range(0, 5):
    next_day = today + datetime.timedelta(days=i)
    next_day_of_week = weekdays[(current_day + i) % 7]
    print(next_day_of_week)
