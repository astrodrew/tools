# -*-conding:utf-8-*-

from pyspark.sql import SQLContext
from pyspark.sql.types import StringType, BooleanType
from pyspark import SparkContext
import datetime
from pyspark.sql.functions import udf
from pyspark.sql.types import *
from pyspark.sql.functions import *
import types

sc = SparkContext("local", "wordcount app")
sqlContext = SQLContext(sc)
a = datetime.datetime.now()
df = sqlContext.read.format('com.databricks.spark.csv').options(header='false', inferschema='true', delimiter="\t") \
    .load('E:\code\pythonprj\sparktest\爬虫未验证规则\*.csv')

df.toDF('domain', 'target', 'selector', 'score', 'un1', 'un2', 'un3').createOrReplaceTempView("raw_table")

# df = sqlContext.sql("select * from raw_table")
#
# df.show()

def myfunc(target, selector):
    if target == "title":
        return True
    rules = [".", "#"]
    for rule in rules:
        if rule in selector:
            return True
    return False

sqlContext.udf.register("myfunc", myfunc, BooleanType())

sqlContext.sql("select * from (select domain, target, selector, score, myfunc(target, selector) as valid from raw_table) as t  where valid=true").\
    createOrReplaceTempView("valid_view")

sqlContext.sql("select domain, count(*) as c from valid_view group by domain").createOrReplaceTempView("count_view")

sqlContext.sql("select a.*, b.c from valid_view a inner join count_view b on a.domain=b.domain where b.c==2 order by domain").createOrReplaceTempView("lastview")



result = sqlContext.sql("select a.domain ,a.target, a.selector from lastview  a")


result.toPandas().to_json("rule", index=False)

