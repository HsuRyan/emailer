import schedule
import datetime

from RTDUpdate import *
from config import *


#This will only check the time once
#You want to continually poll the current time I think and only change the scheduled jobs if the time is in your period.
if datetime.datetime.now().hour >= primary_begin_time and datetime.datetime.now().hour < primary_end_time:
    schedule.every(15).minutes.do(market_update_mailer, market_update_BCC)
else:
    schedule.every(1).minutes.do(market_update_mailer, market_update_BCC_secondary)
    
#This is not the right way to do this
#Should be cron job on linux or task schedule on windows
while True:
    schedule.run_pending()
    time.sleep(60)
    print("email sent")