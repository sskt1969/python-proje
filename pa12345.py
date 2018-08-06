def largest(n,arr):
  max = arr[0]
  for i in range(1, n):
    if arr[i] > max:
            max = arr[i]
  return max
 

n = int(input())
arr = int(input())
Ans = largest(n,arr)
print (Ans)
