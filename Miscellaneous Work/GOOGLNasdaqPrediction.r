install.packages('plotly')
install.packages('forecast')
library(plotly)
library(forecast)
data = read.csv('/Users/monicareddytirupari/GOOGLNasdaq2.csv')

data = ts(data[,2],start = c(2015,1),frequency = 250)
plot(data, xlab='Years', ylab = 'Trade Volume', col = 'darkviolet')

plot(diff(data),ylab='Differenced Trade Volume', col = 'maroon')

plot(log10(data),ylab='Log (Trade Volume)', col = 'darkblue')

plot(diff(log10(data)),ylab='Differenced Log (Trade Volume)', col = 'darkorange')

par(mfrow = c(1,2))
acf(ts(diff(log10(data))),main='ACF Trade Volume')
pacf(ts(diff(log10(data))),main='PACF Trade Volume')

require(forecast)
ARIMAfit = auto.arima(log10(data), approximation=FALSE,trace=FALSE)
summary(ARIMAfit)

par(mfrow = c(1,1))
pred = predict(ARIMAfit, n.ahead = 36)
View(pred)
plot(data,type='l',xlim=c(2017,2017.3),ylim=c(1,1600),xlab = 'Year',ylab = 'Trade Volume', pch = 0.5, col = 'darkgreen')
lines(10^(pred$pred),col='blue')
lines(10^(pred$pred+2*pred$se),col='orange')
lines(10^(pred$pred-2*pred$se),col='orange')

par(mfrow=c(1,2))
acf(ts(ARIMAfit$residuals),main='ACF Residual')
pacf(ts(ARIMAfit$residuals),main='PACF Residual')

