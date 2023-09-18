 # PosicaoNoAlfabeto
""" Dada a letra N do alfabeto, nos diga qual a sua posição.
Entrada: Um único caracter N, uma letra maiúscula ('A'-'Z') do alfabeto (que contém 26 letras).
Saída: Um único inteiro, que representa a posição da letra no alfabeto.
 
Entrada | Saída
   C        3
   J       10
   Z       26                         
   A        1      """

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
