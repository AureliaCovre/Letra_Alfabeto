# MÉTODO ord(): Retorna o valor  ASCII de cada letra ou símbolo do teclado;
# TODO: De acordo com a entrada, imprima a posição dessa letra no Alfabeto;

import string as st

alfabeto = st.ascii_uppercase  # Apenas as letras maiúsculas

letra = input("Digite uma letra maiúscula: ")

posicao = alfabeto.find(letra) + 1

if posicao > 0:
    print(posicao)
else:
    print("Por favor, digite uma letra maiúscula válida.")