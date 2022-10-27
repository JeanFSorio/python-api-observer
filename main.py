from datetime import datetime
from apiobserver.timedInfityLoop import timedLoop

firstFetch = datetime(2022, 10, 27, 00, 55)
lastFetch = datetime(2022, 10, 27, 12, 55)

allAreaAbbreviation = ['br', 'ac', 'al', 'ap', 'am', 'ba', 'ce', 'df', 'es', 'zz', 'go', 'ma', 'mt', 'ms',
                       'mg', 'pr', 'pb', 'pa', 'pe', 'pi', 'rj', 'rn', 'rs', 'ro', 'rr', 'sc', 'se', 'sp', 'to']

governadorArea = ['am', 'pe', 'ro', 'ms', 'se',
                  'es', 'rs', 'sc', 'al', 'ba', 'pb', 'sp']

timedLoop(firstFetch, allAreaAbbreviation, 5, lastFetch, governadorArea)
