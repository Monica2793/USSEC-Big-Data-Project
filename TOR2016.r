install.packages('sqldf')
library(sqldf)

Q1 <- read.csv("/Users/monicareddytirupari/Desktop/USSEC\ Big\ Data\ Project/TOR\ 2016/Q1_TOR2016.csv")
Q2 <- read.csv("/Users/monicareddytirupari/Desktop/USSEC\ Big\ Data\ Project/TOR\ 2016/Q2_TOR2016.csv")
Q3 <- read.csv("/Users/monicareddytirupari/Desktop/USSEC\ Big\ Data\ Project/TOR\ 2016/Q3_TOR2016.csv")
Q4 <- read.csv("/Users/monicareddytirupari/Desktop/USSEC\ Big\ Data\ Project/TOR\ 2016/Q4_TOR2016.csv")

names(Q1) <- c('Exchange','TORQ1')
names(Q2) <- c('Exchange','TORQ2')
names(Q3) <- c('Exchange','TORQ3')
names(Q4) <- c('Exchange','TORQ4')

df1 <- sqldf("SELECT Exchange, TORQ1, TORQ2 FROM Q1 JOIN Q2 USING(Exchange)")
df2 <- sqldf("SELECT Exchange, TORQ1, TORQ2, TORQ3 FROM df1 JOIN Q3 USING(Exchange)")
df3 <- sqldf("SELECT Exchange, TORQ1, TORQ2, TORQ3, TORQ4 FROM df2 JOIN Q4 USING(Exchange)")

TOR_2016 <- df3[!(is.na(df3$Exchange) | df3$Exchange==""), ]
View(TOR_2016)

newTor <- t(TOR_2016)
View(newTor)

names(newTor) <- c('Exchange','TORQ4')
plot(newTor$1,newTor$2)
points(TOR_2016$Exchange, TOR_2016$TOR2)
points(TOR_2016$Exchange, TOR_2016$TOR3)
points(TOR_2016$Exchange, TOR_2016$TOR4)

y <- c(TOR_2016$TOR1[1], TOR_2016$TOR1[1], TOR_2016$TOR2[1], TOR_2016$TOR3[1], TOR_2016$TOR4[1])
x <- c(2016.02, 2016.05, 2016.08, 2016.11)
a <- c(102.283690007,89.4658740885, 83.7883113627, 82.6363617293)
b <- c(100.367498655, 90.203441156,
       98.8810692914,
       103.016784055)


plot(x,a, pch=20, col='blue', type = 'bar')
points(x,b, pch =20, col='red', type = 'l')
