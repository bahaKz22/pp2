n = int(input())
for i in range(n):
  n//=2
  if n == 0:
    break
  print(n,end=" ")
print('\n')

n = int(input())
for j in range(n):
  i**=2
  print(i,end=" ")
print('\n')

n = int(input())
n&=3
print(n)
