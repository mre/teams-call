import os
from pathlib import Path
import re

def getLogFile():
    uname = os.uname()
    home = str(Path.home())

    match uname.sysname:
        case 'Linux':
            return home + '/.config/Microsoft/Microsoft Teams/logs.txt'
        case 'Darwin':
            return home + '/Library/Application Support/Microsoft/Teams/logs.txt'
        case _:
            raise Exception('OS not supported!')

def isInCall():
    logFile = getLogFile()
    if not os.path.isfile(logFile):
        raise Exception('Log file not found: ' + logFile)

    output = os.popen('tac "' + logFile +  '" | grep -oh "eventData: s::;m::1;a::[0-9]" | head -n1').read().split('\n')

    if output[0][-1] in ['0', '1']:
        #print("In Call")
        return True
    else:
        #print("Not In Call")
        return False

if __name__ == '__main__':
    isInCall()
