def factores(n):#generador que computa factores de un numero
    for k in range(1,n+1):
        if n % k == 0:#aplica el modulo 0para obtener el factor R
            yield k
for factor in factores(100):
    print(factor)