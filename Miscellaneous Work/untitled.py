#GOOGL #Nasdaq

from pyspark.sql.types import StringType
from pyspark import SQLContext
sqlContext = SQLContext(sc)
rdd_data = sc.textFile("/user/cloudera/*.csv").map(lambda line: line.split(","))



data = rdd_data.toDF(['Date','Security','Ticker','Exchange','McapRank','TurnRank','VolatilityRank','PriceRank','Cancels','Trades',
'LitTrades','OddLots','Hidden','TradesForHidden','OrderVol','TradeVol','LitVol','OddLotVol','HiddenVol','TradeVolForHidden'])

data.show()



data.registerTempTable("USSEC")

table=sqlContext.sql("select Floor(Date) as Date, Exchange, Ticker, TradeVol from USSEC where Date Like '2%' and Ticker = 'GOOGL' order by Exchange")

table.registerTempTable("output")

table.show()

Arca=sqlContext.sql("select * from output where Exchange = 'Arca'")
Arca.registerTempTable("Arca")
BatsY=sqlContext.sql("select * from output where Exchange = 'BatsY'")
BatsY.registerTempTable("BatsY")
BatsZ=sqlContext.sql("select * from output where Exchange = 'BatsZ'")
BatsZ.registerTempTable("BatsZ")
Boston=sqlContext.sql("select * from output where Exchange = 'Boston'")
Boston.registerTempTable("Boston")
CHX=sqlContext.sql("select * from output where Exchange = 'CHX'")
CHX.registerTempTable("CHX")
EdgeA=sqlContext.sql("select * from output where Exchange = 'EdgeA'")
EdgeA.registerTempTable("EdgeA")
EdgeX=sqlContext.sql("select * from output where Exchange = 'EdgeX'")
EdgeX.registerTempTable("EdgeX")
NSX=sqlContext.sql("select * from output where Exchange = 'NSX'")
NSX.registerTempTable("NSX")
Nasdaq=sqlContext.sql("select * from output where Exchange = 'Nasdaq'")
Nasdaq.registerTempTable("Nasdaq")
Phlx=sqlContext.sql("select * from output where Exchange = 'Phlx'")
Phlx.registerTempTable("Phlx")


Arca.rdd.map(lambda x: ",".join(map(str, x))).coalesce(1).saveAsTextFile("/user/cloudera/output_spark/Arca.csv")
BatsY.rdd.map(lambda x: ",".join(map(str, x))).coalesce(1).saveAsTextFile("/user/cloudera/output_spark/BatsY.csv")
BatsZ.rdd.map(lambda x: ",".join(map(str, x))).coalesce(1).saveAsTextFile("/user/cloudera/output_spark/BatsZ.csv")
Boston.rdd.map(lambda x: ",".join(map(str, x))).coalesce(1).saveAsTextFile("/user/cloudera/output_spark/Boston.csv")
CHX.rdd.map(lambda x: ",".join(map(str, x))).coalesce(1).saveAsTextFile("/user/cloudera/output_spark/CHX.csv")
EdgeA.rdd.map(lambda x: ",".join(map(str, x))).coalesce(1).saveAsTextFile("/user/cloudera/output_spark/EdgeA.csv")
EdgeX.rdd.map(lambda x: ",".join(map(str, x))).coalesce(1).saveAsTextFile("/user/cloudera/output_spark/EdgeX.csv")
NSX.rdd.map(lambda x: ",".join(map(str, x))).coalesce(1).saveAsTextFile("/user/cloudera/output_spark/NSX.csv")
Nasdaq.rdd.map(lambda x: ",".join(map(str, x))).coalesce(1).saveAsTextFile("/user/cloudera/output_spark/Nasdaq.csv")
Phlx.rdd.map(lambda x: ",".join(map(str, x))).coalesce(1).saveAsTextFile("/user/cloudera/output_spark/Phlx.csv")
