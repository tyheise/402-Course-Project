completeLOC <- read.csv("~/Documents/402/402-Course-Project/completeLOC.csv", header=FALSE)
LOC <- subset(completeLOC, V5<365 & V7<10000 & V7>-10000 & V4 <100000)

cor(LOC$V7, LOC$V5)
cor(LOC$V4, LOC$V5)

jpeg("LOCChangeScatter.jpeg", height = 400, width = 400) 
scatter.smooth(x = LOC$V5, y = LOC$V7, xlab = "Days Since Last Release", ylab = "Lines of Testing Code Changed")
dev.off() 

jpeg("LOCScatter.jpeg", height = 400, width = 400) 
scatter.smooth(x = LOC$V5, y = LOC$V4, xlab = "Days Since Last Release", ylab = "Lines of Testing Code")
dev.off() 

jpeg("LOCDaysBox.jpeg", height = 400, width = 400) 
boxplot(LOC$V5, main = "Days Since Last Release")
dev.off()

jpeg("LOCChangeBox.jpeg", height = 400, width = 400)
boxplot(LOC$V7, main = "LOTC Change")
dev.off()

jpeg("LOCBox.jpeg", height = 400, width = 400)
boxplot(LOC$V4, main = "LOTC")
dev.off()

jpeg("LOCDaysDensejpeg", height = 400, width = 400)
plot(density(LOC$V5), main = "Days Since Last Release")
dev.off()

jpeg("LOCChangeDense.jpeg", height = 400, width = 400)
plot(density(LOC$V7), main = "LOTC Change")
dev.off()

jpeg("LOCense.jpeg", height = 400, width = 400)
plot(density(LOC$V7), main = "LOTC")
dev.off()

