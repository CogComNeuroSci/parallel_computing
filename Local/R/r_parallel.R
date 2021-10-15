# delete all previous data 
rm(list = ls())

# add library
library(foreach)
library(doParallel)

# driver for simulation
main <- function(){
  
  # simulation parameters
  DATADIR = "C:/Users/pieter/Downloads/r_parall_test"
  
  # random data
  simulation = rnorm(1000)
  
  # save data
  filename = sprintf("Simulation %d.RData", sample(1:100000, 1))
  save(simulation, 
       file = file.path(DATADIR, filename))
  
  # sleep a bit
  Sys.sleep(5)
  
}

# Simulation ----

# parallel run: 5 cores
cat("** Simulation **\nStart time:", as.character(Sys.time()), "\n")

registerDoParallel(cl <- makeCluster(5))
foreach (i=1:5) %dopar% {
  main()
}
stopCluster(cl)

# 25 seconds serial, 5 parallel (perhaps more due to overhead)
cat("Completion time:", as.character(Sys.time()), "\n")
