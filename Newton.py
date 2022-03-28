def function(Size, array, x):
    sum = 0
    temp = 1
    for i in range(Size):
        for j in range(Size-i-1):
            temp = temp*x
        sum = sum + temp*array[i]
        temp = 1
    return sum


Size = int(input())
F = []
f = []
X = [4]
for i in range(Size):
    i = int(input())
    F.append(i)
for i in range(Size):
    f.append(F[i]*(Size-i-1))
for i in range(100):
    X.append(X[i] - (function(Size, F, X[i])/function(Size-1, f, X[i])))
    print(i+1, X[i+1])
    if(function(Size, F, X[i]) == 0):
        break
