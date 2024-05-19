### List Comprehension ###

my_original_list = [2, 3, 1, 5]

my_list = [i for i in range(2, 20)]
print(my_list)

my_list = [i * 2 for i in range(2, 10)]
print(my_list)

# El cuadrado de cada numero de la lista
my_list = [i * i for i in my_original_list]
print(my_list)

# Usando funciones lambda
func = (lambda i: i // 2 + 1)
my_list = [func(i) for i in range(2, 15)]
print(my_list)

################################################
# Exercise #1: Fibonacci
n_numbers = 5

func = lambda array, pos: array[(pos - 1)] + array[(pos - 2)]

list_original = [0 for i in range(n_numbers)]
list_original[0] = 1
list_original[1] = 1

fib_list = [0, 1] + [func(list_original, i) for i in range(2, n_numbers)]

print(fib_list)
