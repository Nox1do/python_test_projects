import random

def adivina_el_numero (x):
    print("==============================")
    print("Bienvenido(a) al juego")
    print("==============================")
    print("Tu meta es adivinar el número generado por la computadora.")
    
    numero_aleatorio = random.randint(1,x+1) #numero aleatorio entre 1 y x.
    
    guess = 0
    while guess != numero_aleatorio:
        #el usuario ingresa un numero
        guess = int(input(f"Adivina un numero entre 1 y {x}: ")) #f-string
        
        if guess < numero_aleatorio:
            print("Intenta de nuevo. tu numero es  muy pequeño")
        elif guess > numero_aleatorio:
            print("Intenta de nuevo. tu numero es muy grande")
    print(f"Felicidades!, Adivinaste el numero {numero_aleatorio} correctamente.")
    
adivina_el_numero(10)