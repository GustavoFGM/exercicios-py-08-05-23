'''
#EXERCICIO 8

numeros = []
x = 1

while x <= 20: 
    a = int(input("numero:"))
    numeros.append(a)
    x += 1
print(min(numeros))
    
# -----------------------------------------------------------------------------
#EXERCICIO 9 
pares = []
impares = []

while True:
    a = int(input("numero ou 0 para sair: "))
    if a == 0:
        break
    elif a%2 != 0:
        impares.append(a)
    elif a %2 == 0:
        pares.append(a)
        
k = sum(pares)
l = sum(impares)
    
print(k, l)
-----------------------------------------------------------------------------

# EXERCICIO 11
def fatorial(a):
    x = 1
    z = 1
    while x <= a:
        resultado = (a - x + 1)
        z = resultado * z
        x += 1
    return z   
    
s = int(input("Numero a ser fatorado: "))

final = fatorial(s)
print(final)

#-------------------------------------------------------------------------------
# EXERCICIO 12

num = int(input("numero base: "))
x = 1

while x <= num:
    res = (1/x)
    x += 1
    
fim = (res + 1)
print("resultado:",fim)
 # ---------------------------------------------------------------------------   
'''
x = 1
n = 1
lista = []

while x <= 10:
    
    if n % 2 or n % (n**0.5) == 0:
        lista.append(n)
        n += 1
        x += 1
        
print(lista)   
    
