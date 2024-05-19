### Challenges ###

# Cadenas de caracteres
"""
/* EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */
 """

str1 = 'Carlos'
str2 = 'Javier'

# Operaciones con las cadenas
print(str1 + str2) # Concatenacion o union de dos cadenas

character_pos_i = 0 # Acceder a la posicion i de la cadena, i=0 en este caso
print(str1[character_pos_i])

# Extraer algunas subcadenas de una cadena dada
sub_strs = []
original_str = 'ASDFJKLI'
len_original_str = len(original_str)

for i in range(0, len_original_str):
    sub_strs.append(original_str[i:])
print(sub_strs)


# Convertir a mayusculas y a minusculas
result_str = ''
for i in str1:
    if i.lower() == i:
        result_str += i.upper()
    else: result_str += i.lower()
print(result_str)


# Verificar si dos palabras son palindromes a la vez
def is_palindrome(word):
    word1 = word
    word = list(word)
    word = reversed(word)
    word = ''.join(word)
    return(word == word1)

result_to_compare = is_palindrome(str1) and is_palindrome(str2)

print('Ambas son palindromes' if result_to_compare else 'Ambas no son palindromes')

# Para comprobar que dos palabras son anagramas solo deben tener las mismas letras
str_an1 = 'ANARGA'
str_an2 = 'ARANGA'
is_anagram = True

for i in str_an1:
    if not i in str_an2:
        is_anagram = False
        break

print('Son anagramas' if is_anagram else 'No son anagramas')









