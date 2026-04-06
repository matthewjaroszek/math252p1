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

    def populations(self):
        print('Populations')
        print(f'Susceptible: {self.susceptible}')
        print(f'Infected: {self.infected}')
        print(f'Recovered: {self.recovered}')

    def rates(self):
        print('\nRates')
        print(f'Infectious: {self.transmission}')
        print(f'Recovery: {self.recovery}')
        if (self.sirs):
            print(f'Immunity: {self.immunity}')

    def summarize(self):
        self.populations()
        self.rates()
    
    def delta_susceptible(self):
        return (-1 * self.transmission * self.susceptible * self.infected) / self.population + (self.immunity * self.recovered)
    
    def delta_infected(self):
        print('-s: ', (-1 * self.delta_susceptible()), ' eI: ', (self.immunity * self.infected))
        return (-1 * self.delta_susceptible()) - (self.immunity * self.infected)
    
    def delta_recovered(self):
        return self.immunity * self.infected
    
    def cycle(self, cycles = 1):
        print()
        for _ in range(cycles):
            self.susceptible, self.infected, self.recovered = self.susceptible + self.delta_susceptible(), self.infected + self.delta_infected(), self.recovered + self.delta_recovered()
        

class SIRS_VD(SIRS):
    def __init__(self, population, infected, transmission, duration, birth, death, immunity = 0):
        super().__init__(population, infected, transmission, duration, immunity)
        self.birth = birth
        self.death = death
    
    def summarize(self):
        super().summarize()
        print(f'\bBirth: {self.birth}')
        print(f'Death: {self.death}')

    def delta_susceptible(self):
        return (self.birth * self.population) + super().delta_susceptible() - (self.death * self.susceptible)

    def delta_infected(self):
        return super().delta_infected() - (self.death * self.infected)

    def delta_recovered(self):
        return super().delta_recovered() - (self.death * self.recovered)