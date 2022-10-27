from apiobserver.fetchJson import fecthJson
from apiobserver.saveMany import saveMany
from datetime import datetime, timedelta
import time
import pytz


def timedLoop(fetchTime, areaAbbreviation, pauseTiming, lastFetch, governadorArea):
    sleepTime = (fetchTime-datetime.now()).total_seconds()
    print(sleepTime, datetime.now(), fetchTime, areaAbbreviation, pauseTiming, lastFetch, governadorArea)
    time.sleep(sleepTime)
    timeNow = datetime.now(pytz.timezone('Brazil/East'))

    getPresidente(areaAbbreviation, timeNow)
    getGovernador(governadorArea, timeNow)

    nextFetch = fetchTime + timedelta(minutes=pauseTiming)
    if lastFetch >= datetime.now():
        timedLoop(nextFetch, areaAbbreviation,
                  pauseTiming, lastFetch, governadorArea)


def getPresidente(areaAbbreviation, timeNow):
    response = fecthJson(areaAbbreviation, 1, 545)
    saveMany(response, timeNow, 'p')


def getGovernador(governadorArea, timeNow):
    response = fecthJson(governadorArea, 3, 547)
    saveMany(response, timeNow, 'g')
