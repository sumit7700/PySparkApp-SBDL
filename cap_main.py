import sys

from lib import utils
from lib.logger import log4J

if __name__ =="__main__":

    if len(sys.argv) < 3:
        print("Usage  Capstone {local,qa,prod} {load_date} : Arguments are missing")
        sys.exit(-1)

    job_run_env = sys.argv[1].upper()
    load_date = sys.argv[2]

    spark = utils.get_spark_session(job_run_env)
    logger = log4J(spark)

    logger.info("Finished creating Spark Session")


