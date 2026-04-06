import pandas as pd
import matplotlib.pyplot as plt

class SIRS:
    def __init__(self, population, infected, transmission, duration, immunity = 0):
        self.population = population
        self.infected = infected
        self.transmission = transmission
        self.duration = duration
        self.recovery = 1 / self.duration
        self.susceptible = population - infected
        self.recovered = 0
        self.immunity = immunity

    def summarize(self):
        print('Populations')
        print(f'Current pupulation: {self.population}')
        print(f'Currently susceptible: {self.susceptible}')
        print(f'Currently infected: {self.infected}')
        print(f'Currently recovered: {self.recovered}')
        print('\nRates')
        print(f'Infectious: {self.transmission}')
        print(f'Recovery: {self.recovery}')
        if (self.immunity != 0):
            print(f'Immunity: {self.immunity}')
        

class SIRS_VD(SIRS):
    def __init__(self, population, infected, transmission, duration, birth, death, immunity = 0):
        super().__init__(population, infected, transmission, duration, immunity)
        self.birth = birth
        self.death = death
    
    def summarize(self):
        super().summarize()
        print(f'Birth: {self.birth}')
        print(f'Death: {self.death}')