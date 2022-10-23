def lee_numero():
    return int(input("Introduce un número: "))
 
def mayor(a,b,c):
    if a>b and a>c:
        return a
    if b>c:
        return b
    else:   
        return c
 
valores=[]
for i in range(3):
    valores.append(lee_numero())
 
print(f"El número con mayor valor de los tres es el {mayor(valores[0], valores[1],valores[2])}")