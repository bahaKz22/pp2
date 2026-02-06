#factorial
n = int(input())
c = 1
for i in range(1,n+1):
  c*=i
  print(c,end=" ")
print('\n')
#bolindiler
b = int(input())
for j in range(b):
  b/=2
  if b%2 != 0:
    break
  print(b,end=" ")
print('\n')
#qaldyk
m = 50
print(m%2)
