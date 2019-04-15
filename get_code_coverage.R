library(tidyverse)
library(ggplot2)




setwd(paste(getwd(),"codecov",sep="/"))
csv_list = list.files(pattern="*.csv")
print(csv_list)


png_csv_path <- (paste(getwd(),"codecov_png",sep="/"))
dir.create(png_csv_path)
print(png_csv_path)





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
  ggsave(filename = file.path(png_csv_path, sub('\\.csv$', '.png', basename(csv_list[i]))), device ="png", plot = gg)
}



