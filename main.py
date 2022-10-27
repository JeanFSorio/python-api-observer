from datetime import datetime, timedelta
from apiobserver.timedInfityLoop import timedLoop

firstFetch = datetime(2022, 10, 30, 17, 5)
lastFetch = datetime(2022, 11, 1, 12, 15)

allAreaAbbreviation = ['br', 'ac', 'al', 'ap', 'am', 'ba', 'ce', 'df', 'es', 'zz', 'go', 'ma', 'mt', 'ms',
       'mg', 'pr', 'pb', 'pa', 'pe', 'pi', 'rj', 'rn', 'rs', 'ro', 'rr', 'sc', 'se', 'sp', 'to']

timedLoop(firstFetch, allAreaAbbreviation,5, lastFetch)
