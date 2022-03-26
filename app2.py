
name = str(input("Cual es tu nombre? "))
weight =int (input("Cual es tu peso? "))
h = float (input("Cual es tu altura? "))
calculo = weight / (h **2)

    
print("Tu imc es " + str(calculo))

if (calculo >= 18.5 and calculo <= 24.9):
    print("You are fine!")

elif calculo < 18:
    print("You are more less")

if calculo >= 25:
    print("Estás un poco sobre tu peso")
    
elif calculo >= 30:
    print("Lo siento, tienes obesidad")
     