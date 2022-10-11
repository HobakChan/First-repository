def multiply(m1,m2):
    mul = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m2[0])):
            a = 0
            for k in range(len(m2)):
                a += m1[i][k] * m2[k][j]
            row.append(a)
        mul.append(row)

    return mul