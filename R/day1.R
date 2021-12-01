library(tidyverse)

# Part 1

input <- tibble(num = as.numeric(read_lines("data/input_1.txt"))) 

input %>% 
  mutate(increased = num > lag(num)) %>% 
  pull(increased) %>% 
  sum(., na.rm = TRUE)

# Part 2

input %>% 
  mutate(increased = num > lag(num, 3)) %>% 
  pull(increased) %>% 
  sum(., na.rm = TRUE)
