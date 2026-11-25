# Dada uma string s consistindo apenas dos caracteres 'a' e 'b',
# Retorne verdadeiro se 'a' aparecer antes de cada 'b' na string.
# Caso contrário, retorne falso.

minha_string = "ababababa"

if 'ba' not in minha_string:
    print(True)
else:
    print(False)