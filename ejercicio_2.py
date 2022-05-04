dinero_invertido=float(input("Ingrese el numero que desea invertir "))
interes=float(input( "Ingrese el interes porcentual de su año en porcentaje"))
años = int(input("Ingrese los años"))
dinero_final=(dinero_invertido*(interes/100+1)** años)
dinero_final=round(dinero_final , 2)
dinero=str(dinero_final)

print("El Dinero final es de : " + dinero)
