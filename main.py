from datetime import datetime
from apiobserver.timedInfityLoop import timedLoop

# precisa ser gmt0 pra n bugar o sleep em prod
firstFetch = datetime(2022, 10, 30, 13, 55)
lastFetch = datetime(2022, 11, 1, 2, 55)

allAreaAbbreviation = ['br', 'ac', 'al', 'ap', 'am', 'ba', 'ce', 'df', 'es', 'zz', 'go', 'ma', 'mt', 'ms',
                       'mg', 'pr', 'pb', 'pa', 'pe', 'pi', 'rj', 'rn', 'rs', 'ro', 'rr', 'sc', 'se', 'sp', 'to']

governadorArea = ['am', 'pe', 'ro', 'ms', 'se',
                  'es', 'rs', 'sc', 'al', 'ba', 'pb', 'sp']

timedLoop(firstFetch, allAreaAbbreviation, 5, lastFetch, governadorArea)
