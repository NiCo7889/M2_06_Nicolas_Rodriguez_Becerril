import math
def area_circulo():
     Radio = float(input("Dime el radio de un círculo:\n")) 
     Area = math.pi*(Radio*Radio)
     return 'El área de un circulo de radio {} es de {} unidades cuadradas.'.format(Radio, Area)

print (area_circulo())