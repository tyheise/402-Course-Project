library(tidyverse)
library(ggplot2)


setwd(dir = getwd())
print(getwd())
toPath <- (paste(getwd(),"codecov",sep="/"))
print(getwd())

#setwd(paste(getwd(),"codecov",sep="/"))
csv_list = list.files(path = toPath, pattern="*.csv")
print(csv_list)

jpg_csv_path <- (paste(getwd(),"codeCoverageScatterPlots",sep="/"))
dir.create(jpg_csv_path)
print(jpg_csv_path)

setwd(toPath)
getwd()


for(i in 1:length(csv_list)){

  data_frame <-read.csv(csv_list[i], header =  TRUE)
  data_frame$dayDifference <- as.numeric(gsub("[^[:digit:]]","",data_frame$dayDifference))
  #if(names(data_frame) %in% "dayDifference"){data_frame$dayDifference <- as.numeric(gsub("[^[:digit:]]","",data_frame$dayDifference))}
  print(data_frame$dayDifference)
  print(csv_list[i])
  gg <- ggplot(data = data_frame , mapping = aes(x = covpercent, y = dayDifference)) +
    geom_point() +
    scale_y_continuous(limits=c(0,max(data_frame$dayDifference))) +
    labs(x = "Code coverage",
         y = "Number of days between releases",
         title = basename(csv_list[i]) # just file name, not whole path
    )
  
  #ggsave(filename = sub('\\.csv$', '.png', csv_list[i]), device = "png", plot = gg) # change file extension to indicate output format
  #message(file.path(png_csv_path, sub('\\.csv$', '.png', basename(csv_list[i]))))
  ggsave(filename = file.path(jpg_csv_path, sub('\\.csv$', '.jpeg', basename(csv_list[i]))),  height =  4, width = 4, units = "in", dpi = 200,  device ="jpeg", plot = gg)
}



