# MÉTODO ord(): Retorna o valor  ASCII de cada letra ou símbolo do teclado;
# TODO: De acordo com a entrada, imprima a posição dessa letra no Alfabeto;

import string as st

"""a = list(st.ascii_lowercase)
letra = input("Digite uma letra: ")
for i in range(ord(letra)+1):
    a.append(chr(i))

print(letra)"""

alfabeto = st.ascii_letters
letra = input("Digite uma letra: ")
#valor = (ord(letra)+1)
#print(valor)
print(alfabeto.find(letra))

"""for x in alfabeto:
    letra = +1
    print(alfabeto.find(letra))"""

#print(ord(letra))
#print(alfabeto.find(letra))
#print(alfabeto.ord(letra))