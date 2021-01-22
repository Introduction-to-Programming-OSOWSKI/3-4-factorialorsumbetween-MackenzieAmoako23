def factOrSum(O, x):
    num = 1

    if O == "factorial":
        for i in range( 1, x + 1):
            num = num * i
        return num

    else:
        total = 0
        
        for i in range(0 , x):
            total = total + i
        return total