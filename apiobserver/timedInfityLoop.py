from apiobserver.fetchJson import fecthJson
from apiobserver.saveMany import saveMany
from datetime import datetime, timedelta
import time
import pytz

from apiobserver.saveManyMongo import saveManyMongo


def timedLoop(fetchTime, areaAbbreviation, pauseTiming, lastFetch, governadorArea):
    sleepTime = (fetchTime-datetime.now()).total_seconds()
    print({"tempo de pausa(m:ss)": f"{int(sleepTime/60)}:{int(sleepTime%60)}", "horaSistema": f"{datetime.now()}", "horaProximaProcura": f"{fetchTime}"})
    if sleepTime > 0:
        time.sleep(sleepTime)
    timeNow = datetime.now(pytz.timezone('Brazil/East'))

    getPresidente(areaAbbreviation, timeNow)
    getGovernador(governadorArea, timeNow)

    nextFetch = fetchTime + timedelta(minutes=pauseTiming)
    if lastFetch >= datetime.now():
        timedLoop(nextFetch, areaAbbreviation,
                  pauseTiming, lastFetch, governadorArea)
    else:
        print("Carga de dados terminada")

def getPresidente(areaAbbreviation, timeNow):
    response = fecthJson(areaAbbreviation, 1, 545)
    #saveMany(response, timeNow, 'p')
    saveManyMongo(response)


def getGovernador(governadorArea, timeNow):
    response = fecthJson(governadorArea, 3, 547)
    #saveMany(response, timeNow, 'g')
    saveManyMongo(response)

