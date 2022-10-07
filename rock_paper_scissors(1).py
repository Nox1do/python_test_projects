import random

def jugar():
    usuario =  input("ingresa una opcion: 'pi' para piedra, 'pa' para papel, 'ti' para tijera.\n")
    usuario.lower()
    computadora = random.choice(['pi','pa','ti'])
    if usuario == computadora:
        return f"Empate!, yo tambien escogi {computadora}"
    if player_win(usuario,computadora):
        return f"Ganaste...{usuario} vence a {computadora}..pura suerte"
        
    return f"He Ganado, {computadora} vence a {usuario}. Yo tengo el poder!!".lower()
    
def player_win(jugador,oponente):
    #Retornar el valor True si gana jugador.
    #Piedra > Tijera, Tijera < Papel, Papel < Piedra
    if ((jugador == 'pi' and oponente == 'ti')
    or (jugador == 'ti' and oponente == 'pa')
    or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False
        
        
print(jugar())