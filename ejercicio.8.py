#promedio de tres numeros 
print ("hagamos tu promedio de notas")
n= int(input("ingrese la cantidad de notas: "))
suma=0
x=1
while(x<=n):
    print("ingrese 5la nota numero: ",x)
    nota=float(input())
    suma=suma+nota
    x+=1
prom=suma/n
print ("el promedio de notas es:", prom)