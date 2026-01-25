def chkPrime(num):
    for i in range(2,int(num/2+1)):
        if (num % i == 0):
            return False
    return True

