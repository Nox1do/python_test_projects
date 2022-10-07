import random

def guess_pc(x):
    print("=========================")
    print("Bienvenido(a) al juego")
    print("=========================")
    
    print(f"Selecicona un numero entre 1 y {x}. Tratare de adivinar")
    
    limite_inferior = 1
    limite_superior = x
    
    respuesta = ""
    while respuesta != "c":
        #generar guess_pc                             
        if limite_inferior != limite_superior: #ente [1 y 10]
            guess = random.randint(limite_inferior,limite_superior)
        else:
            guess = limite_inferior #tambien prodria ser el limite limite_superior
            
        #obtener respuesta del usuario
        respuesta = input(f"Mmm..pienso que es el numero.. {guess}. Si es alto, ingresa (A). Si es bajo, ingresa (B). Si es correcto, ingresa (C)")
        respuesta.lower()
        
        if respuesta == "a":
             limite_superior = guess - 1
        elif guess == "b": 
             limite_inferior = guess + 1
             
    print(f"LO SABIA!, Es el {x}!!!!!!! Soy mejor que ALEXA!. SIIII..!")
             
             #intervalo inicial : [1,10]
             #Guess : 6
             #Respuesta: "a"
             #Intervarlo : [1,5]
guess_pc(10)