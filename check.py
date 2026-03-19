import numpy as np

def f1(x):
    return x**2

def f2(x):
    return np.sin(x)

def f3(x):
    return np.exp(x)

def f4(x):
    return 1/(1+x**2)

def F1(x):
    return (x**3)/3

def F2(x):
    return -np.cos(x)

def F3(x):
    return np.exp(x)

def F4(x):
    return np.arctan(x)

functions = [
    {"name": "x^2", "f": f1, "F": F1, "a": 0, "b": 1},
    {"name": "sin(x)", "f": f2, "F": F2, "a": 0, "b": np.pi/2},
    {"name": "exp(x)", "f": f3, "F": F3, "a": 0, "b": 1},
    {"name": "1/(1+x^2)", "f": f4, "F": F4, "a": 0, "b": 1}
]

def left_rectangle(f, a, b, n):
    h = (b - a)/n
    result = 0.0
    for i in range(n):
        result += f(a + i*h)
    return result*h

def right_rectangle(f, a, b, n):
    h = (b - a)/n
    result = 0.0
    for i in range(1, n+1):
        result += f(a + i*h)
    return result*h

def midpoint_rectangle(f, a, b, n):
    h = (b - a)/n
    result = 0.0
    for i in range(n):
        result += f(a + i*h + h/2)
    return result*h

def trapezoidal(f, a, b, n):
    h = (b - a)/n
    result = (f(a) + f(b))/2
    for i in range(1, n):
        result += f(a + i*h)
    return result*h

def simpson(f, a, b, n):
    h = (b - a)/n
    result = f(a) + f(b)
    for i in range(1, n):
        if i % 2 == 0:
            result += 2*f(a + i*h)
        else:
            result += 4*f(a + i*h)
    return result*h/3

n_values = [4, 8, 16, 32]

for func in functions:
    print("="*70)
    print(f"ФУНКЦИЯ: {func['name']} на отрезке [{func['a']}, {func['b']}]")
    exact = func["F"](func["b"]) - func["F"](func["a"])
    print(f"Точное значение: {exact}")
    print("="*70)
    
    for n in n_values:
        print(f"\nn = {n}:")
        print("-"*50)
        
        I_left = left_rectangle(func["f"], func["a"], func["b"], n)
        I_right = right_rectangle(func["f"], func["a"], func["b"], n)
        I_mid = midpoint_rectangle(func["f"], func["a"], func["b"], n)
        I_trap = trapezoidal(func["f"], func["a"], func["b"], n)
        I_simp = simpson(func["f"], func["a"], func["b"], n)
        
        print(f"Левые прямоугольники:  {I_left}  (погрешность: {abs(I_left - exact)})")
        print(f"Правые прямоугольники: {I_right}  (погрешность: {abs(I_right - exact)})")
        print(f"Средние прямоугольники: {I_mid}  (погрешность: {abs(I_mid - exact)})")
        print(f"Трапеций:              {I_trap}  (погрешность: {abs(I_trap - exact)})")
        print(f"Симпсона:              {I_simp}  (погрешность: {abs(I_simp - exact)})")
    
    print("\n")
