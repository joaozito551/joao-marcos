a = int(input("digite o primeiro termo: "))
b = int(input("digite a quantidade de termos: "))
c = int(input("digite a razao"))

p =0
for x in range(a,b +1, c):
    p += x
print(p)