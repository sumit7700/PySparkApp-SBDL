import configparser

from pyspark import SparkConf

def get_spark_app_config():
    spark_conf = SparkConf()
    config = configparser.ConfigParser()
    #config.read(r'C:\\Sumeet\\Coding\\Python\\PySpark_Udemy_Course\\Initial_Hello_Spark\\lib\\spark.conf')
    config.read("lib\spark.conf")

    for(key,val) in config.items("SPARK_APP_CONFIGS"):
        spark_conf.set(key,val)
    
    return spark_conf

def load_survey_df(spark,data_file):
    survey_df = spark.read \
                .format("csv") \
                .option("header","true") \
                .option("inferSchema","true") \
                .load(data_file)
    
    return survey_df

def count_by_country(survey_df):
    return survey_df.filter("Age < 40") \
        .select("Age", "Gender", "Country", "state") \
        .groupBy("Country") \
        .count()
