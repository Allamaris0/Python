for i in range(1,8):
    if i==5:
        print("Znalazłem " + str(i) + "!")
        continue
    print(i)


a = list(range(1,9))

print("Moja lista",a)

for x in a:
    if x==5:
        break
    print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

b=0

while b<20:
    b+=1
    if b%3==0:
        print(b)
        continue



z=1

while z<=21:
    print(z)
    z += 5

print("------------------")
n=10

while n>=0:
    print(n)
    n-=1


print("---------------")

choose_letter=input("wpisz n lub c: ")
if choose_letter == "n" or "c":
  print("Dziękuję!")
else:
  print("wpisałeś niepoprawną literę")

print("----------------")

suma = 0

for x in range(5):
  print("Wprowadź wartość")
  x1 = int(input())
  suma += x1

print("Suma wartości:", str(suma))
