from config import *

#SIR(population, infected, transmission, duration)  
#SIR_VD(population, infected, transmission, duration, birth, death)  
#SIRS(population, infected, transmission, duration, immunity)  
#SIRS_VD(population, infected, transmission, duration, birth, death, immunity)  

test = SIRS_VD(1000, 10, 0.3, 10, 0.01, 0.01, 0.001)
test.summarize()
test.cycle(99999)
test.populations()