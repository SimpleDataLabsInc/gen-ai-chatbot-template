from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from prophecy.transpiler import call_spark_fcn
from prophecy.transpiler.fixed_file_schema import *
from web_ingest.config.ConfigStore import *
from web_ingest.udfs.UDFs import *

def clean_fields(spark: SparkSession, web_bronze_sitemap: DataFrame) -> DataFrame:
    return web_bronze_sitemap.select(col("loc").alias("url"), col("result_content").alias("content"))
