import matplotlib.pyplot as mlp
import asyncio
from solver.data_for_plotter import Solver

async def main():
    equa = input('уравнение например, x**2 - 4 ')
    solver = Solver(equa, [])
    
    await solver.zapolnenie(a=0)
    await solver.x(e=int(input('шаг ')))
    await solver.y()

    step1 = solver.step1
    step2 = solver.step2

    a, b = solver.get_intersection_points()
    if a is not None and b is not None:
        print(f"значения для метода хорд - a = {a}, b = {b}")
    else:
        print("не найдены")

    plotter(step1, step2, equa)

def plotter(step1, step2, equa):
    mlp.plot(step1, step2, marker='o')
    mlp.xlabel('x')
    mlp.ylabel('f(x)')
    mlp.title(equa)
    mlp.grid()
    mlp.show()

if __name__ == "__main__":
    asyncio.run(main())
