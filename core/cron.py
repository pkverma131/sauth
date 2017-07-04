import os
import datetime
def counter_job():
  CURRENT_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  BASE_DIR = CURRENT_PATH.split('core')[0]
  f=open(BASE_DIR+'media/analytics/background_task.txt','w+')
  current_time=datetime.datetime.now()
  f.write(str(current_time))
  f.close()
