#Function to change time format (24hs to 12hs and backwards)
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
  #Split start string to get hours, minutes and AM/PM
  start_hour12 = int(start.split(":")[0])
  start_min = int(start.split(":")[1][0:2])
  start_ampm = start.split(":")[1][3:5]
  
  #Change 12hs format to 24hs format
  start_hour24 = format_hour(start_hour12, start_ampm)
  
  #Split duration string to get hours and minutes
  dur_hour = int(duration.split(":")[0])
  dur_min = int(duration.split(":")[1])

  #Sums minutes and get the rest of the division by 60, in case the sum is equal or bigger than 60. If it is, adds the integer part to dur_hour.
  result_min = (start_min + dur_min) % 60
  dur_hour = dur_hour + int((start_min + dur_min) / 60)

  #Sums hours, similarly that for minutes. If its bigger or equal than 24, stores the number of days in ndays.
  result_hour24 = (start_hour24 + dur_hour) % 24
  ndays = int((start_hour24 + dur_hour) / 24)
  #Change back to 12hs format
  [result_hour12, result_ampm] = format_hour(result_hour24, format_change="24to12")

  #Creates the new_time variable to return the result
  new_time = str(result_hour12) + ":" + str(result_min).zfill(2) + " " + result_ampm

  #List of days to compute the result day, in case the start_day parameter is passed to the function
  days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  if start_day!=1:#if the start_day parameter is passed
    #Searchs for the index of the start day (use lower method to make it case insensitive)
    start_dayid = next(i for i,v in enumerate(days) if v.lower() == start_day.lower())
    #Calculate the result day index adding the number of days to the start day index and taking the rest of the division by 7
    result_dayid = int((start_dayid + ndays) % 7)
    #Includes the result day in the new_time string
    new_time = new_time + ", " + days[result_dayid]
  if ndays == 1:
    #Includes "next day" if ndays=1
    new_time = new_time + " (next day)"
  elif ndays > 1:
    #Includes the numbers of days later if ndays>1
    new_time = new_time + " (" + str(ndays) + " days later)"

  return new_time