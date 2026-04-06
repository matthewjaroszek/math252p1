from config import *

#SIR(self, population, infected, transmission, duration)
#SIR_VD(self, population, infected, transmission, duration, birth, death)

test = SIR_VD(1000, 10, 0.3, 10, 0.01, 0.01)
test.summarize()