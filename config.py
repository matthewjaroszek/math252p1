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
        self.sirs = (immunity != 0)

    def summarize(self, new_line = True):
        print('Populations')
        print(f'Current pupulation: {self.population}')
        print(f'Currently susceptible: {self.susceptible}')
        print(f'Currently infected: {self.infected}')
        print(f'Currently recovered: {self.recovered}')
        print('\nRates')
        print(f'Infectious: {self.transmission}')
        print(f'Recovery: {self.recovery}')
        if (self.sirs):
            print(f'Immunity: {self.immunity}')
        if (new_line):
            print('')
    
    def delta_susceptible(self):
        return (-1 * self.transmission * self.susceptible * self.infected) / self.population + (self.immunity * self.recovered)
    
    def delta_infected(self):
        return (-1 * self.delta_susceptible()) - (self.immunity * self.infected)
    
    def delta_recovered(self):
        return self.immunity * self.infected
    
    def cycle(self, cycles = 1):
        print()
        for _ in range(cycles):
            self.susceptible, self.infected, self.recovered = self.delta_susceptible, self.delta_infected, self.delta_recovered
        

class SIRS_VD(SIRS):
    def __init__(self, population, infected, transmission, duration, birth, death, immunity = 0):
        super().__init__(population, infected, transmission, duration, immunity)
        self.birth = birth
        self.death = death
    
    def summarize(self):
        super().summarize(False)
        print(f'\bBirth: {self.birth}')
        print(f'Death: {self.death}')
        print('')

    def delta_susceptible(self):
        return (self.birth * self.population) + super().delta_susceptible() - (self.death * self.susceptible)

    def delta_infected(self):
        return super().delta_infected() - (self.death * self.infected)

    def delta_recovered(self):
        return super().delta_recovered - (self.death * self.recovered)