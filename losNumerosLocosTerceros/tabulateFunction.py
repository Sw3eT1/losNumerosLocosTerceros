#Tworzenie rownoodleglych wezlow i wartosci funkcji
import numpy as np

def tabulateFunction(f, lowerInterval, hiigherInterval, numberOfNodes):
    x = np.linspace(lowerInterval, hiigherInterval, numberOfNodes)
    y = f(x)
    return x,y