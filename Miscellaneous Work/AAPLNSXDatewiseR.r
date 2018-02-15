AAPLNSX <- read.csv("/Users/monicareddytirupari/Desktop/USSEC\ Big\ Data\ Project/AAPL\ NSX/AAPLNSX.csv")

names(AAPLNSX) <- c('Date','Exchange','Ticker','TradeVol(000)')

View(AAPLNSX)

plot(AAPLNSX$Date, AAPLNSX$`TradeVol(000)`, type = 'l')
View(df)

