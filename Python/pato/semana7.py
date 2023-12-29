import random

print("Bienvenido al juego Piedra, Papel o Tijera.")

while True:
    try:
        opciones = ["Piedra", "Papel", "Tijera"]
        jugador = input(
            "Ingresa tu elección (Piedra, Papel o Tijera): ").capitalize()
        if jugador not in opciones:
            raise ValueError(
                "Elección inválida. Debes ingresar Piedra, Papel o Tijera.")
        break
    except ValueError as e:
        print(e)

computadora = random.choice(opciones)
print(f"La computadora eligió: {computadora}")

if jugador == computadora:
    print("Empate")
elif (jugador == "Piedra" and computadora == "Tijera") or (jugador == "Papel" and computadora == "Piedra") or (jugador == "Tijera" and computadora == "Papel"):
    print("¡Ganaste!")
else:
    print("¡La computadora gana!")
