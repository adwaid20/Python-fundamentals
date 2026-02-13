from datetime import datetime
n=datetime.now()
print(n)
print(n.date())
print(n.time())
print(n.strftime("%m-%y-%d %H/%M/%S"))
my_event=datetime(2025,9,24,11,50)
print(my_event)
d=my_event-n
print(d)
