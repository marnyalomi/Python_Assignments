def is_sator_square(tablet):
    n=len(tablet)
    for i in range(len(tablet)):
        for j in range(len(tablet)//2 + 1):
            if tablet[i][j] != tablet[j][i] or tablet[i][j] != tablet[n-1 - j][n-1 - i]:
                return False
            else:
                pass
    return True
