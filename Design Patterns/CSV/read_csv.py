import os
import pprint
import csv

DATADIR     = ""
DATAFILE    = "beatles-diskography.csv"

def parse_csv(DATAFILE):
    data = []
    n = 0
    with open(DATAFILE  ,'rt') as csvF:
        r = csv.DictReader(csvF)
        for line in r:
            data.append(line)
    return data

if __name__ == '__main__':
    DATAFILE = os.path.join(DATADIR,DATAFILE)
    parse_csv(DATAFILE)
    d = parse_csv(DATAFILE)
    pprint.pprint(d)