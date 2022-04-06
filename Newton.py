import imp


import decimal

import numpy


def function(Size, array, x):
    sum = 0
    temp = 1
    for i in range(Size):
        for j in range(Size-i-1):
            temp = temp*x
        sum = sum + temp*array[i]
        temp = 1
    return sum


def main():
    while True:
        Size = int(input("輸入最高次數:"))
        Size += 1
        F = []
        f = []
        X = [-4]
        for i in range(Size):
            temp = int(input("%d次方之係數:" % (Size-i-1)))
            F.append(temp)
        for i in range(Size):
            f.append(F[i]*(Size-i-1))
        for i in range(100):
            X.append(X[i] - (function(Size, F, X[i])/function(Size-1, f, X[i])))
            if(function(Size, F, X[i]) == 0):
                break
        print("四捨五入到小數第四位:%s" % (numpy.round((X[-1]), 4)))
        print(X[-1])
        a = int(input("如果想重新請輸入1,結束輸入2\n"))
        if a == 1:
            continue
        elif a == 2:
            break


if __name__ == '__main__':
    main()
