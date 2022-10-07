from palabras import palabras
import random
import string
from ahorcado_diagrama import vidas_diccionario_visual

def obtener_palabras_valida(palabras):
    #seleccionar palabra al azar de la lista
    # de palabras validas
    palabra = random.choice(palabras)
    
    while  '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
    return palabra.upper()    
    

def ahorcado():
    print("====================================")
    print("Bienvenido(a), al juego del Ahorcado")
    print("====================================")

    palabra = obtener_palabras_valida(palabras)
    
    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase)
    
    vidas = 7
    
    while len(letras_por_adivinar) > 0 and vidas > 0 :
        print(f"Te quedan {vidas} vidas y usaste las letras: {' '.join(letras_adivinadas)}")
        
        #Mostrar el estado actual de la palabra
        palabra_lista = [letra if letra in letras_adivinadas
        else '-' for letra in palabra]
        print(vidas_diccionario_visual[vidas])
        print(f"Palabra: {' '.join(palabra_lista)}")
        
        letra_usuario = input("Escoge una letra: ")
        letra_usuario.upper()
        
        
        # Si la letra escogida por el usuario esta en el 
        # abecedario  y no esta en el conjunto de letras_adivinadas
        # que ya se han ingresado, se añade la letra al conjunto de letras ingresadas
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
            
            # Si la letra esta en la palabra_lista
            # quitar la letra del conjunto de letras pendientes por adivinar
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas -= 1
                print(f"\n Tu letra,{letra_usuario} no esta en la palabra.")
        # Si la letra escogida por el usuario ya fue ingresada.
        elif letra_usuario in letras_adivinadas:
            print("\n Ya escogiste esa letra. Por favor escoge una letra nueva.")
        else:
            print("\n Esta letra no es valida.")
       
    # El juego llega a esta linea cuando se adivinan todas las letras de la palabra 
    # o cuando se agotan las vidas del jugador
    if vidas == 0:
        print("vidas_diccionario_visual[vidas]")
        print(f"Ahorcado!. Acabas de perder el juego. La palabra era: {palabra}")
    else:
        print(f"FELICIDADES!. Adivinaste la palabra {palabra}")


#ejecutando el juego        
ahorcado()