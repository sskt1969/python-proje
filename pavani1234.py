def  sumOfAP(a,  d,  n):
    sum = (n / 2) * (2 * a + (n - 1) * d)
    return sum
     
    
n = int(input())
a = int(input())
d = int(input())
 
print(sumOfAP(a, d, n))
