#area y volumen de un cilindro

print ("calculemos el area y el volumen de un cilinfro")
r= float (input("ingresa el radio del cilindro: "))
h= float (input("ingresa la altura del cilindro: "))

area= 2*3.14*r*(r+h)
volumen= 3.14*r**2*h
print ("el area del cilindro es: ", area)
print (" el volumen del cilindro es: ", volumen)