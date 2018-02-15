Arca <- read.csv("/Users/monicareddytirupari/Desktop/USSEC\ Big\ Data\ Project/GOOGL\ All\ Exchange/Arca.csv")
Boston <- read.csv("/Users/monicareddytirupari/Desktop/USSEC\ Big\ Data\ Project/GOOGL\ All\ Exchange/Boston.csv")
CHX <- read.csv("/Users/monicareddytirupari/Desktop/USSEC\ Big\ Data\ Project/GOOGL\ All\ Exchange/CHX.csv")
Nasdaq <- read.csv("/Users/monicareddytirupari/Desktop/USSEC\ Big\ Data\ Project/GOOGL\ All\ Exchange/Nasdaq.csv")
NSX <- read.csv("/Users/monicareddytirupari/Desktop/USSEC\ Big\ Data\ Project/GOOGL\ All\ Exchange/NSX.csv")
Phlx <- read.csv("/Users/monicareddytirupari/Desktop/USSEC\ Big\ Data\ Project/GOOGL\ All\ Exchange/Phlx.csv")

names(Arca) <- c('Date','Exchange','Ticker','TradeVol')
names(Boston) <- c('Date','Exchange','Ticker','TradeVol')
names(CHX) <- c('Date','Exchange','Ticker','TradeVol')
names(Nasdaq) <- c('Date','Exchange','Ticker','TradeVol')
names(NSX) <- c('Date','Exchange','Ticker','TradeVol')
names(Phlx) <- c('Date','Exchange','Ticker','TradeVol')


df1 <- sqldf("SELECT Date, Arca.TradeVol as ArcaTradeVol, Boston.TradeVol as BostonTradeVol FROM Arca JOIN Boston USING(Date)")
df2 <- sqldf("SELECT Date, ArcaTradeVol, BostonTradeVol, CHX.TradeVol as CHXTradeVol FROM df1 JOIN CHX USING(Date)")
df3 <- sqldf("SELECT Date, ArcaTradeVol, BostonTradeVol, CHXTradeVol, Nasdaq.TradeVol as NasdaqTradeVol
             FROM df2 JOIN Nasdaq USING(Date)")
df4 <- sqldf("SELECT Date, ArcaTradeVol, BostonTradeVol, CHXTradeVol, NasdaqTradeVol, 
             NSX.TradeVol as NSXTradeVol FROM df3 JOIN NSX USING(Date)")
GOOGLTrendAnalysis <- sqldf("SELECT Date, ArcaTradeVol, BostonTradeVol, CHXTradeVol, NasdaqTradeVol, 
             NSXTradeVol, Phlx.TradeVol as PhlxTradeVol FROM df4 JOIN Phlx USING(Date)")

View(GOOGLTrendAnalysis)

write.csv(GOOGLTrendAnalysis, "/Users/monicareddytirupari/Desktop/GOOGLTrendAnalysis.csv")
