def contar(dato,objetivo):
    n = 0
    for item in dato:
        if item == objetivo:
            #Encuentra coincidencia
            n+=1
    return n
lista =["a","a","b","c","a","d"]
cuenta = contar(lista,"a")
print(cuenta)
            