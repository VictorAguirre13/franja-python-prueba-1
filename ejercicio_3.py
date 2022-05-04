#Peso argentino en dolar=115
#Peso Chileno en dolar=855
#Peso mexicano a dolar=20
from re import I


Dolar_mexico=20
Dolar_argentino=115
Dolar_chile=855
print ("Eliga que moneda quiere cambiar a dolar")
print ("Ingrese el numero 1 si desea cambiar a peso argentino")
print ("Ingrese el numero 2 si desea cambiar a peso mexicano")
print ("Ingrese el numero 3 si desea cambiar a peso chileno")
numero=int(input("Ingrese su numero"))
pesos=float(input("Ingrese el valor de la moneda a cambiar "))
if numero == 1:
    dolares_argentinos=pesos/Dolar_argentino
    valor1=str(dolares_argentinos)
    print("La cantidad de dolares es : " + valor1)

elif numero == 2:
    dolares_mexicanos=pesos/Dolar_mexico
    valor2=str(dolares_mexicanos)
    print("La cantidad de dolares es : " + valor2)
elif numero == 3:
    dolares_chilenos=pesos/Dolar_chile
    valor3=str(dolares_chilenos)
    print("La cantidad de dolares es :" +  valor3)

