import math
import random

# Datos proporcionados
x_data = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
y_data = [1.0, 1.0, 2.0, 4.0, 5.0, 4.0, 4.0, 5.0, 6.0, 5.0]

# Función objetivo
def f(x, a, b, c, d):
    return math.cos(a*x) + b*x - c*x**2 + d

# Función de error
def cost(params):
    a, b, c, d = params
    errors = [abs(f(x, a, b, c, d) - y) for x, y in zip(x_data, y_data)]
    return max(errors)

# Generar una solución inicial
def init():
    return [random.randint(0, 15) for _ in range(4)]

# Generar el mejor vecino
def best_neighbor(solution, step_size):
    best_neighbor = solution[:]
    best_error = cost(solution)
    for i in range(len(solution)):
        neighbor = solution[:]
        neighbor[i] += random.randint(-step_size, step_size)
        neighbor_error = cost(neighbor)
        if neighbor_error < best_error:
            best_neighbor = neighbor
            best_error = neighbor_error
    return best_neighbor

# Mostrar la solución actual y el costo
def show(iteration, solution, error):
    print("Iteración:", iteration)
    print("Solución actual:", solution)
    print("Error actual:", error)
    print("------------------------------------")

# Hill Climbing
def hill_climbing(iterations, step_size):
    current_solution = init()
    best_solution = current_solution[:]
    best_error = cost(best_solution)

    for i in range(iterations):
        neighbor = best_neighbor(current_solution, step_size)
        if cost(neighbor) < best_error:
            best_solution = neighbor[:]
            best_error = cost(best_solution)
        current_solution = neighbor[:]
        show(i+1, current_solution, best_error)

    return best_solution, best_error

# Ejecutar Hill Climbing con un número de iteraciones especificado
iterations = 10
step_size = 2
best_params, best_error = hill_climbing(iterations, step_size)

print("Mejores parámetros encontrados:", best_params)
print("Error mínimo encontrado:", best_error)