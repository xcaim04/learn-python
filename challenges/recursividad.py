"""
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
"""

print('--------> 100 to 0 <-----------')

def f(number=100):
    if number < 0: return None
    print(number, end=' ')
    f(number-1)
f()

print('\n-------> Factorial of N <------')

def factorial(number):
    if number < 2: return 1
    return factorial(number-1) * number
print(factorial(5))

print('---------> N_i fibonacci\'s numbers <----------')

def fib(number):
    if number == 0 or number == 1: return number
    return fib(number-1) + fib(number-2)

print(fib(6))


