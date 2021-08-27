import pandas as pd
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Causes").getOrCreate()