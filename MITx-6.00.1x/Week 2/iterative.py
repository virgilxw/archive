def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = 1
    for i in range(0, exp):
        result *= base
        print (i)

    return result

iterPower(base, exp)