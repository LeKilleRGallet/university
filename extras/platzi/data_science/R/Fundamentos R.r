library("readr")

orangeec <- read_csv("Platzi/R/orangeec.csv")

View(orangeec)

str(orangeec)

class(orangeec$GDP.PC)

summary(orangeec)

library("plyr")

orangeec[orangeec$'GDP PC'>=15000,]

orangeec[orangeec$'Creat Ind % GDP'<=2,]

neworangeec <- subset(orangeec, 'Internet penetration % population' > 80 
& 'Education invest % GDP' >= 4.5, select = 'Creat Ind % GDP')

neworangeec

rename(orangeec, c('Creat Ind % GDP' = 'Creative Industry % GDP') )
