# Różnice progresywne
def forwardDifferences(y):
    n = len(y)
    diff = [y.copy()]
    for i in range(1,n):
        row = [diff[i - 1][j + 1] - diff[i - 1][j] for j in range(n - i)]
        diff.append(row)
    return diff