def format_hour(hour, ampm = "AM", format_change="12to24"):
  if format_change == "12to24":
    if ampm == "AM":
      if hour == 12:
        hour24 = 0
      else:
        hour24 = hour
    elif ampm == "PM":
      if hour == 12:
        hour24 = hour
      else:
        hour24 = hour + 12
    return hour24

  if format_change == "24to12":
    if hour == 0:
      hour12 = 12
      ampm = "AM"
    elif hour >= 1 and hour <= 12:
      hour12 = hour
      if hour == 12:
        ampm = "PM"
      else:
        ampm = "AM"
    elif hour >= 13 and hour <= 23:
      hour12 = hour - 12
      ampm = "PM"
  
  return [hour12, ampm]

def add_time(start, duration, start_day=1):
  start_hour12 = int(start.split(":")[0])
  start_min = int(start.split(":")[1][0:2])
  start_ampm = start.split(":")[1][3:5]
  
  start_hour24 = format_hour(start_hour12, start_ampm)

  dur_hour = int(duration.split(":")[0])
  dur_min = int(duration.split(":")[1])

  result_min = (start_min + dur_min) % 60
  dur_hour = dur_hour + int((start_min + dur_min) / 60)

  result_hour24 = (start_hour24 + dur_hour) % 24
  ndays = int((start_hour24 + dur_hour) / 24)
  [result_hour12, result_ampm] = format_hour(result_hour24, format_change="24to12")

  new_time = str(result_hour12) + ":" + str(result_min).zfill(2) + " " + result_ampm
  
  if start_day==1:
    if ndays == 1:
      new_time = new_time + " (next day)"
    elif ndays > 1:
      new_time = new_time + " (" + str(ndays) + " days later)"

  #new_time = [start_hour12, start_min, start_ampm, start_hour24, result_hour12, result_min, result_ampm, ndays]
  return new_time

print(add_time("3:30 PM", "2:12"))
print(add_time("11:55 AM", "3:12"))
print(add_time("9:15 PM", "5:30"))
print(add_time("11:40 AM", "0:25"))
print(add_time("2:59 AM", "24:00"))
print(add_time("11:59 PM", "24:05"))
print(add_time("8:16 PM", "466:02"))
print(add_time("5:01 AM", "0:00"))