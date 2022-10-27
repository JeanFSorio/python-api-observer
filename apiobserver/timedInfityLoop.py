from apiobserver.fetchJson import fecthJson
from apiobserver.saveMany import saveMany
from datetime import datetime, timedelta
import time
import pytz



def timedLoop(fetchTime, areaAbbreviation, pauseTiming,lastFetch):
    #fetch form url
    t = datetime.now()
    time.sleep((fetchTime-t).total_seconds())
    timeNow = datetime.now(pytz.timezone('Brazil/East'))

    response = fecthJson(areaAbbreviation)
    saveMany(response, timeNow)
    nextFetch =fetchTime + timedelta(minutes=pauseTiming)
    if lastFetch >= t:
        timedLoop(nextFetch,areaAbbreviation, pauseTiming, lastFetch)

 