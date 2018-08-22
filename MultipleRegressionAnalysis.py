def regressionAnalysis2(Y,x1,x2,):
    #Y = a*x1 + b*x2 + c
    #return (a,b,c)
    import numpy as np
    number = len(x1)
    X = np.array([x1, x2, np.ones(number)]).T
    XtX = np.dot(X.T,X)
    XtY = np.dot(X.T,Y)
    if np.linalg.matrix_rank(XtX) != 3:
        print("The rank of XtX not equal 3")
        print("I can't get the inverse matrixXtX")
        return -1
    XtXinv = np.linalg.inv(XtX)
    A = np.dot(XtXinv,XtY)
    return(A)

if __name__ == '__main__':
    import numpy as np
    print("Please leave a space and enter a number")
    print('Please input y')
    Y = list(map(float,input().split()))
    print('Please input x1')
    x1 = list(map(float,input().split()))
    print('Please input x2')
    x2 = list(map(float,input().split()))
    print(regressionAnalysis2(Y,x1,x2,))
