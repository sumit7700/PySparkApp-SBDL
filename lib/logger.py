class log4J:
    def __init__(self,spark):
        log4j = spark._jvm.org.apache.log4j
        self.logger = log4j.LogManager.getLogger("sbdl")

    def info(self,message):
        self.logger.info(message)
    
    def warn(self,message):
        self.logger.warn(message)

    def error(self,message):
        self.logger.error(message)

    def debug(self,message):
        self.logger.debug(message)