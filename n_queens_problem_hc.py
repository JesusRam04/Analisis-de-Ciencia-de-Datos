import time
import random
import math

x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
y = [1.0, 1.0, 2.0, 4.0, 5.0, 4.0, 4.0, 5.0, 6.0, 5.0]

class reg(object):
    def __init__(self, x, y):
        self.a = random.randint(0, 15)
        self.b = random.randint(0, 15)
        self.c = random.randint(0, 15)
        self.d = random.randint(0, 15)
        self.x = x
        self.y = y

    def show(self):
        print("a:", self.a, "b:", self.b, "c:", self.c, "d:", self.d)
        print("------------------------------------")
        
    def f(self, x):
        return math.cos(self.a * x) + self.b * x - self.c * x**2 + self.d
    
    def cost(self):
        errors = [abs(self.f(x) - y) for x, y in zip(self.x, self.y)]
        return max(errors)

    def best_neighbor(self, step_size):
        best_neighbor = self
        best_error = self.cost()
        for i in range(len(self.x)):
            neighbor = reg(self.x, self.y)
            neighbor.a += random.randint(-step_size, step_size)
            if neighbor.a < 0:
                neighbor.a = 0
            if neighbor.a > 15:
                neighbor.a = 15
            neighbor.b += random.randint(-step_size, step_size)
            if neighbor.b < 0:
                neighbor.b = 0
            if neighbor.b > 15:
                neighbor.b = 15
            neighbor.c += random.randint(-step_size, step_size)
            if neighbor.c < 0:
                neighbor.c = 0
            if neighbor.c > 15:
                neighbor.c = 15
            neighbor.d += random.randint(-step_size, step_size)
            if neighbor.d < 0:
                neighbor.d = 0
            if neighbor.d > 15:
                neighbor.d = 15
            neighbor_error = neighbor.cost()
            if neighbor_error < best_error:
                best_neighbor = neighbor
                best_error = neighbor_error
        return best_neighbor
    
random.seed(time.time()*1000)

solution = reg(x, y)
solution.show()

cost = solution.cost()
print("Initial Cost: ", cost)

step = 0
max_steps = 10
while step < max_steps:
    step += 1
    
    neighbor = solution.best_neighbor(step_size=1)
    new_cost = neighbor.cost()

    if new_cost < cost:
        solution = neighbor
        cost = new_cost

    print("Iteration: ", step, "    Cost: ", cost)
    neighbor.show()

print("\n--------Solution-----------")
solution.show()
print("Final Cost: ", cost)
