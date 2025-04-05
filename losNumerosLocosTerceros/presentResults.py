import numpy as np
import matplotlib.pyplot as plt
from newtonInterpolation import newtonInterpolation

def presentResults(originalFunction, xNodes, yNodes, lowerInterval, higherInterval, wzor, xInterp=None):
    interp_func = lambda x: newtonInterpolation(xNodes, yNodes, x)

    intervalWidth = higherInterval - lowerInterval
    extraMargin = intervalWidth
    fullLower = lowerInterval - extraMargin
    fullUpper = higherInterval + extraMargin

    xDenseFunc = np.linspace(fullLower, fullUpper, 1000)
    yTrue = [originalFunction(x) for x in xDenseFunc]

    xDenseInterp = np.linspace(lowerInterval, higherInterval, 1000)
    yInterp = [interp_func(x) for x in xDenseInterp]

    plt.figure(figsize=(10, 6))
    plt.plot(xDenseFunc, yTrue, label='Oryginalna funkcja', linewidth=2)
    plt.plot(xDenseInterp, yInterp, '--', label='Wielomian interpolacyjny (Newton)', linewidth=2)
    plt.plot(xNodes, yNodes, 'ro', label='Węzły interpolacji', markersize=6)

    if xInterp is not None:
        yInterpPoint = interp_func(xInterp)
        plt.axvline(xInterp, color='gray', linestyle=':', label=f'x = {xInterp}')
        plt.plot(xInterp, yInterpPoint, 'ks', label=f'Interpolacja: f({xInterp}) ≈ {yInterpPoint:.3f}', markersize=8)

    plt.title(f'Interpolacja Newtona dla funkcji: {wzor}')
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
