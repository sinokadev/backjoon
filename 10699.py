import datetime
from datetime import timezone, timedelta

now = datetime.datetime.now(timezone(timedelta(hours=9)))
print(now.strftime("%Y-%m-%d"))