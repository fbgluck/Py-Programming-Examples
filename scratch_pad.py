import datetime
birth_date = datetime.datetime(1956, 6, 3)
now=datetime.datetime.now()
print(f"You were born on {birth_date}")
print(f"It is now {now}")
how_long=now.date()-birth_date.date()
print (f"You have been alive for {how_long.days} days")
print (f"You have been alive for {how_long.seconds} seconds")