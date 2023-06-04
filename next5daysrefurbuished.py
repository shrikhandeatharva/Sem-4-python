import datetime
import calendar

# Get today's date
today = datetime.date.today()

# Get the current day of the week (0 - Monday, 1 - Tuesday, ..., 6 - Sunday)
current_day = today.weekday()

# Create a list of weekdays
weekdays = list(calendar.day_name)

i = current_day
for j in range(0,5):
  print(weekdays[i])
  i = (i+1)%7
  j = j+1