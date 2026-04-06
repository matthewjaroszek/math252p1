from config import *

#SIRS(population, infected, transmission, duration, immunity = 0)
#SIRS_VD(population, infected, transmission, duration, birth, death, immunity = 0)

test = SIRS_VD(1000, 10, 0.3, 10, 0.01, 0.01, 0.001)
test.summarize()
test.cycle(999999)
test.populations()