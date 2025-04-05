import numpy as np
from time import sleep

from horner import horner
from newtonInterpolation import newtonInterpolation
from presentResults import presentResults
from tabulateFunction import tabulateFunction

mainDecision = False

wzory = ["f(x) = 3x-2", "f(x)=|x-2|", "f(x)=x^3-4x^2+x+6", "f(x)=sin(x)", "f(x)=sin(x^2)"]

while not mainDecision:

    print(f'Chose a proper function:'
          f'\n a) {wzory[0]}'
          f'\n b) {wzory[1]}'
          f'\n c) {wzory[2]}'
          f'\n d) {wzory[3]}'
          f'\n e) {wzory[4]}')

    val = input("Select your option: ").lower()

    properOptions = ["a", "b", "c", "d", "e"]

    if val not in properOptions:
        if val == "":
            print("You have entered an empty string!")
        else:
            print("Invalid input!")
            sleep(1)
    else:
        mainDecision = True


    match val:
        case "a":
            coefficients = [3, -2]
            f = lambda x: horner(x, coefficients)
            wzor = wzory[0]
        case "b":
            coefficients = [1, 2]
            f = lambda x: abs(horner(x, coefficients))
            wzor = wzory[1]
        case "c":
            coefficients = [1, -4, 1 ,6]
            f = lambda x: horner(x, coefficients)
            wzor = wzory[2]
        case "d":
            f = lambda x: np.sin(x)
            wzor = wzory[3]
        case "e":
            f = lambda x: np.sin(np.pow(x,2))
            wzor = wzory[4]

intervalDecision = False

while not intervalDecision:
    try:
        lowerInterval = float(input("Select lower value for the interpolation: "))
        higherInterval = float(input("Select higher value for the inteprolation: "))

        if higherInterval <= lowerInterval:
            print("Invalid input! Please choose a second value as the greater one.")
            sleep(1)
        else:
            intervalDecision = True

    except ValueError:
        print("Invalid input! Please enter numerical values only.")
        sleep(1)
        
numberOfNodes = None
while numberOfNodes is None:
    try:
        numberOfNodes = int(input("Enter the number of nodes: "))
    except ValueError:
        print("Invalid input! Please enter a numerical value.")


xNodes, yNodes = tabulateFunction(f, lowerInterval, higherInterval, numberOfNodes)

print("\nTablicowane wartości:")
for xi, yi in zip(xNodes, yNodes):
    print(f"x = {xi:.3f}, f(x) = {yi:.3f}")

xInterp = float(input("\nPodaj punkt, w którym chcesz obliczyć wartość funkcji: "))
yInterp = newtonInterpolation(xNodes, yNodes, xInterp)

print(f"\nInterpolowana wartość f({xInterp}) ≈ {yInterp:.6f}")

presentResults(f, xNodes, yNodes, lowerInterval, higherInterval, wzor, xInterp)