setwd(dir = getwd())
print(getwd())
print((paste(getwd(),"completeCodeCov.csv",sep="/")))

completeCodeCov <- read.csv((paste(getwd(),"completeCodeCov.csv",sep="/")), header=FALSE)

codeCov <- subset(completeCodeCov, V5<365)

cor(codeCov$V4, codeCov$V5)

jpeg("covScatter.jpeg", height = 400, width = 400) 
scatter.smooth(x = codeCov$V5, y = codeCov$V4, xlab = "Days Since Last Release", ylab = "Code Coverage Percentage of Release")
dev.off() 

jpeg("covDaysBox.jpeg", height = 400, width = 400) 
boxplot(codeCov$V5, main = "Days Since Last Release")
dev.off()

jpeg("covPercentBox.jpeg", height = 400, width = 400)
boxplot(codeCov$V4, main = "Code Coverage Percentage")
dev.off()

jpeg("covDaysDense.jpeg", height = 400, width = 400)
plot(density(codeCov$V5), main = "Days Since Last Release")
dev.off()

jpeg("covPercentDense.jpeg", height = 400, width = 400)
plot(density(codeCov$V4), main = "Code Coverage Percentage")
dev.off()

