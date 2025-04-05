from forwardDifferences import forwardDifferences


def newtonInterpolation(xNodes, yNodes, xValue):
    h = xNodes[1] - xNodes[0]
    diff = forwardDifferences(yNodes)
    t = (xValue - xNodes[0]) / h
    result = yNodes[0]

    factorial = 1
    product = 1
    for i in range(1, len(xNodes)):
        factorial *= i
        product *= (t - (i - 1))
        result += (diff[i][0] * product) / factorial
    return result