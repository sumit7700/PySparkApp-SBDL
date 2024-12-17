import sys

from lib import utils
from lib.logger import log4J

if __name__ =="__main__":

    if len(sys.argv) < 3:
        print("Usage  Capstone {local,qa,prod} {load_date} : Arguments are missing")
        sys.exit(-1)
