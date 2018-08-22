def correlationCoef(x,y):
    #initialization
    verX = 0
    verY = 0
    verXY = 0
    #number of samples : N
    N = range(len(x))

    #variance　of x : verX
    for i in N:
        verX += (x[i] - np.mean(x)) ** 2
    verX = verX / (len(N)-1)

    #variance of y : verY
    for i in N:
        verY += (y[i] - np.mean(y)) ** 2
    verY = verY / (len(N)-1)

    #covariance verXY
    for i in N:
        verXY += (x[i] - np.mean(x)) * (y[i] - np.mean(y))
    verXY = verXY / (len(N)-1)

    #correlation　coefficient : C
    C = verXY / ((verX ** 0.5) * (verY ** 0.5))
    return C

if __name__ == '__main__':
    import numpy as np
    #input x and y
    print('Please input x')
    x = list(map(float,input().split()))
    print('Please input y')
    y = list(map(float,input().split()))
    print(correlationCoef(x,y))
