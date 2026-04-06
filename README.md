# math252p1

b = infectious rate = prob of transmitting from susceptible to infectious  
y = recovery rate = 1 / d such d is the duration of the disease  
e = immunity loss rate = rate which recovered individuals return to susceptible  
S = # susceptible  
I = # infected  
R = # recovered  
N = S + I + R = total population  
u = birth rate  
v = death rate  

SIR w/out Vital Dynamics  
Short infection period  
Non-fatal disease  
Ignore birth and death rate  
Eventually dies out  
Existing pop is immmune  
S' = -(bSI) / N  
I' = (bSI) / N - yI  
R' = R' = yI  

SIR w/ Vital Dynamics  
Births add susceptible ppl to pop  
Epidemic is more sustained  
Disease reach steday state as endemic  
S' = uN - (bSI) / N - vS  
I' = (bSI) / N - yI - vI  
R' = yI - vR  

SIRS w/out Vital Dynamics  
recovered individuals lose inmmunity and return to susceptible states  
S' = -(bSI) / N + eR  
I' = (bSI) / N - yI  
R' = R' = yI - eR  

SIRS w/ Vital Dynamics  
Births add susceptible ppl to pop  
Epidemic is more sustained  
Disease reach steday state as endemic  
S' = uN - (bSI) / N - vS +eR  
I' = (bSI) / N - yI - vI  
R' = yI - vR - eR  