from solver.solution import metod
from solver.plotter import main as plot_main

if __name__ == "__main__":
    plot_main()
    
    a = float(input("a = "))
    b = float(input("b = "))
    
    def func(x):
        return eval(input("уравнение ").replace('x', str(x)))

    solver = metod(func)
    
    try:
        root = solver.find_root(a, b)
        print(f"рут {root}")
    except ValueError as e:
        print(e)