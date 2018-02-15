#AAPL #NSX

from pyspark.sql.types import StringType
from pyspark import SQLContext
sqlContext = SQLContext(sc)
rdd_data = sc.textFile("/user/cloudera/*.csv").map(lambda line: line.split(","))



data = rdd_data.toDF(['Date','Security','Ticker','Exchange','McapRank','TurnRank','VolatilityRank','PriceRank','Cancels','Trades',
'LitTrades','OddLots','Hidden','TradesForHidden','OrderVol','TradeVol','LitVol','OddLotVol','HiddenVol','TradeVolForHidden'])

data.show()



data.registerTempTable("USSEC")

table=sqlContext.sql("select Floor(Date), Exchange, Ticker, TradeVol from USSEC where Date Like '2%' and Exchange = 'NSX' and Ticker = 'AAPL' order by Date")

table.registerTempTable("output")

table.show()



table.rdd.map(lambda x: ",".join(map(str, x))).coalesce(1).saveAsTextFile("/user/cloudera/output_spark/AAPLNSX.csv")


