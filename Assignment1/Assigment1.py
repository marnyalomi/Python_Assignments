
tablet = [['B', 'A', 'T', 'S'],
          ['A', 'B', 'U', 'T'],
          ['T', 'U', 'B', 'A'],
          ['S', 'T', 'A', 'B']]
def satorsquare(tablet):
    for i in range(len(tablet)):
        for j in range(len(tablet)):
            if tablet[i][j] != tablet[j][i] or tablet[i][j] != tablet[-1 - j][-1 - i]:
                return False
            else:
                pass
    return True
print(satorsquare(tablet))

#or
def satorsquare(tablet):
    for i in range(len(tablet)):
        for j in range(len(tablet)):
            if tablet[i][j] == tablet[j][i] and tablet[i][j] == tablet[-1 - j][-1 - i]:
                pass
            else:
                return False
    return True
print(satorsquare(tablet))