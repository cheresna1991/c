#основной код
import math

def solve_quadratic(a, b, c):
    """
    Решает квадратное уравнение ax² + bx + c = 0.
    Возвращает кортеж с корнями.
    """
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise TypeError("Все коэффициенты должны быть числами")
    
    if a == 0:
        raise ValueError("Коэффициент 'a' не может быть равен нулю")
    
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        # Два действительных корня
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        # Возвращаем корни в порядке убывания
        return (max(root1, root2), min(root1, root2))
    elif discriminant == 0:
        # Один действительный корень
        root = -b / (2*a)
        return (root,)
    else:
        # Два комплексных корня
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        return (
            complex(real_part, imaginary_part),
            complex(real_part, -imaginary_part)
        )