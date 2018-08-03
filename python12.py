def  sumOfAP(a,  d,  n):
    sum = (n / 2) * (2 * a + (n - 1) * d)
    return sum
     
    
n = input()
a = input()
d = input()
 
print(sumOfAP(a, d, n))
