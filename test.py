from config import *

#SIRS(self, population, infected, transmission, duration, immunity = 0)
#SIRS_VD(self, population, infected, transmission, duration, birth, death, immunity = 0)

test_vd = SIRS_VD(1000, 10, 0.3, 10, 0.01, 0.01, 10)
test_vd = SIRS(1000, 10, 0.3, 10, 10)
test_vd.summarize()
test_vd.cycle(1)
test_vd.summarize()