from datetime import datetime
now=datetime.now()
print("Date:",now.strftime("%d-%m-%Y"))
print("Time:", now.strftime("%I:%M %p"))