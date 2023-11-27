```# №1

x=int(input("выведите x:"))
y=int(input("выведите y:"))

if(1<=x<=y and x<10000 and y<10000):
  print(x,y)
  n=y-x+1
  print(n)
  if(x-1)%n==0:
    print("Yes")

  else:
    print('No')
else:
  print("Ошибка")

# №2


plus = int(input("Количество знаков + в выражении"))
res = 1+1
for i in range(plus-1):
  res = 1+1/res
  print(res)
result_round = str(round(res%1,5))
print("L1#"+result_round)




# №3
A=int(input())
B=int(input())
if 1000<=A<=9999 and 1000<= B <=9999:
  for i in range(A,B+1):
     if (i // 1000 == i % 10) and (i // 100 % 10 == i % 100 // 10):
       print(i)
else:
  print("Ошибка")

# №4
N = int(input())
results = list(map(int, input().split()))

results.sort(reverse=True)

silver = results[1]
print(silver)```
