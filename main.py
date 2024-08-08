a = int(input("digite seu primeiro num: "))
b = int(input("digite seu segundo num: "))

if(a < b):
    soma = 0
    for termo in range(a,b + 1):
        soma=soma+termo
    print(soma)
else:
 print("error, tente novamente")