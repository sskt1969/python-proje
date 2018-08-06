def largest(n1,arr):
  max = arr[0]
  for i in range(1, n1):
    if arr[i] > max:
            max = arr[i]
  return max
 

n1 = int(input())
arr = int(input())
Ans = largest(n1,arr)
print (Ans)
