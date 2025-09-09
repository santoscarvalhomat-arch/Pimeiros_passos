# Programa que desafia o usuário a adivinhar um número entre 1 e 10

import random

# Gera um número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)

# Pede pro usuário tentar adivinhar
palpite = int(input("Adivinhe o número entre 1 e 10: "))

# Verifica se acertou
if palpite == numero_secreto:
    print("Parabéns! Você acertou 🎉")
else:
    print("Errou! O número era", numero_secreto)
