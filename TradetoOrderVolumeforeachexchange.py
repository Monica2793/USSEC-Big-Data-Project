#Trade to Order Volume for Each Exchange

from pyspark.sql.types import StringType
from pyspark import SQLContext
sqlContext = SQLContext(sc)
rdd_data = sc.textFile("/user/cloudera/*.csv").map(lambda line: line.split(","))



data = rdd_data.toDF(['Date','Security','Ticker','Exchange','McapRank','TurnRank','VolatilityRank','PriceRank','Cancels','Trades',
'LitTrades','OddLots','Hidden','TradesForHidden','OrderVol','TradeVol','LitVol','OddLotVol','HiddenVol','TradeVolForHidden'])

data.show()



data.registerTempTable("SEC")

table1=sqlContext.sql("select Date, Exchange, OrderVol, TradeVol from SEC where Date > '20160100' and Date < '20160400'")

table1.registerTempTable("output1")

table1=sqlContext.sql("select Date, Exchange, OrderVol, TradeVol from SEC where Date > '20160400' and Date < '20160700'")

table1.registerTempTable("output2")

table1=sqlContext.sql("select Date, Exchange, OrderVol, TradeVol from SEC where Date > '20160700' and Date < '20161000'")

table1.registerTempTable("output3")

table1=sqlContext.sql("select Date, Exchange, OrderVol, TradeVol from SEC where Date > '20161000' and Date < '20161200'")

table1.registerTempTable("output4")

table1=sqlContext.sql("select Date, Exchange, OrderVol, TradeVol from SEC where Date > '20150100' and Date < '20150400'")

table1.registerTempTable("output5")

table1=sqlContext.sql("select Date, Exchange, OrderVol, TradeVol from SEC where Date > '20150400' and Date < '20150700'")

table1.registerTempTable("output6")

table1=sqlContext.sql("select Date, Exchange, OrderVol, TradeVol from SEC where Date > '20150700' and Date < '20151000'")

table1.registerTempTable("output7")

table1=sqlContext.sql("select Date, Exchange, OrderVol, TradeVol from SEC where Date > '20151000' and Date < '20151200'")

table1.registerTempTable("output8")




sumtable1=sqlContext.sql("select Exchange, Sum(output1.OrderVol) as TotOrderVol, Sum(output1.TradeVol) as TotTradeVol from output1 group by Exchange")

sumtable1.registerTempTable("sumtable1")

sumtable2=sqlContext.sql("select Exchange, Sum(output2.OrderVol) as TotOrderVol, Sum(output2.TradeVol) as TotTradeVol from output2 group by Exchange")

sumtable2.registerTempTable("sumtable2")

sumtable3=sqlContext.sql("select Exchange, Sum(output3.OrderVol) as TotOrderVol, Sum(output3.TradeVol) as TotTradeVol from output3 group by Exchange")

sumtable3.registerTempTable("sumtable3")

sumtable4=sqlContext.sql("select Exchange, Sum(output4.OrderVol) as TotOrderVol, Sum(output4.TradeVol) as TotTradeVol from output4 group by Exchange")

sumtable4.registerTempTable("sumtable4")

sumtable5=sqlContext.sql("select Exchange, Sum(output5.OrderVol) as TotOrderVol, Sum(output5.TradeVol) as TotTradeVol from output5 group by Exchange")

sumtable5.registerTempTable("sumtable5")

sumtable6=sqlContext.sql("select Exchange, Sum(output6.OrderVol) as TotOrderVol, Sum(output6.TradeVol) as TotTradeVol from output6 group by Exchange")

sumtable6.registerTempTable("sumtable6")

sumtable7=sqlContext.sql("select Exchange, Sum(output7.OrderVol) as TotOrderVol, Sum(output7.TradeVol) as TotTradeVol from output7 group by Exchange")

sumtable7.registerTempTable("sumtable7")

sumtable8=sqlContext.sql("select Exchange, Sum(output8.OrderVol) as TotOrderVol, Sum(output8.TradeVol) as TotTradeVol from output8 group by Exchange")

sumtable8.registerTempTable("sumtable8")





Q1_2016 = sqlContext.sql("select Exchange, TotTradeVol*100/TotOrderVol as TradeOrderRatio from sumtable1")

Q1_2016.registerTempTable("Q1_2016")

Q2_2016 = sqlContext.sql("select Exchange, TotTradeVol*100/TotOrderVol as TradeOrderRatio from sumtable2")

Q2_2016.registerTempTable("Q2_2016")

Q3_2016 = sqlContext.sql("select Exchange, TotTradeVol*100/TotOrderVol as TradeOrderRatio from sumtable3")

Q3_2016.registerTempTable("Q3_2016")

Q4_2016 = sqlContext.sql("select Exchange, TotTradeVol*100/TotOrderVol as TradeOrderRatio from sumtable4")

Q4_2016.registerTempTable("Q4_2016")

Q1_2015 = sqlContext.sql("select Exchange, TotTradeVol*100/TotOrderVol as TradeOrderRatio from sumtable5")

Q1_2015.registerTempTable("Q1_2015")

Q2_2015 = sqlContext.sql("select Exchange, TotTradeVol*100/TotOrderVol as TradeOrderRatio from sumtable6")

Q2_2015.registerTempTable("Q2_2015")

Q3_2015 = sqlContext.sql("select Exchange, TotTradeVol*100/TotOrderVol as TradeOrderRatio from sumtable7")

Q3_2015.registerTempTable("Q3_2015")

Q4_2015 = sqlContext.sql("select Exchange, TotTradeVol*100/TotOrderVol as TradeOrderRatio from sumtable8")

Q4_2015.registerTempTable("Q4_2015")




Q1_2015.rdd.map(lambda x: ",".join(map(str, x))).coalesce(1).saveAsTextFile("/user/cloudera/output_spark/Q1_2015.csv")
Q2_2015.rdd.map(lambda x: ",".join(map(str, x))).coalesce(1).saveAsTextFile("/user/cloudera/output_spark/Q2_2015.csv")
Q3_2015.rdd.map(lambda x: ",".join(map(str, x))).coalesce(1).saveAsTextFile("/user/cloudera/output_spark/Q3_2015.csv")
Q4_2015.rdd.map(lambda x: ",".join(map(str, x))).coalesce(1).saveAsTextFile("/user/cloudera/output_spark/Q4_2015.csv")
Q1_2016.rdd.map(lambda x: ",".join(map(str, x))).coalesce(1).saveAsTextFile("/user/cloudera/output_spark/Q1_2016.csv")
Q2_2016.rdd.map(lambda x: ",".join(map(str, x))).coalesce(1).saveAsTextFile("/user/cloudera/output_spark/Q2_2016.csv")
Q3_2016.rdd.map(lambda x: ",".join(map(str, x))).coalesce(1).saveAsTextFile("/user/cloudera/output_spark/Q3_2016.csv")
Q4_2016.rdd.map(lambda x: ",".join(map(str, x))).coalesce(1).saveAsTextFile("/user/cloudera/output_spark/Q4_2016.csv")
