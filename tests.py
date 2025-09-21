#тесты, которые импортируются в основном коде
import math
from main import solve_quadratic

def test_solve_quadratic_two_real_roots():
    """Тест уравнения с двумя действительными корнями"""
    result = solve_quadratic(1, -5, 6)
    expected = (3.0, 2.0)
    assert result == expected
def test_solve_quadratic_one_real_root():
    """Тест уравнения с одним действительным корнем: x² - 4x + 4 = 0"""
    result = solve_quadratic(1, -4, 4)
    expected = (2.0,)
    assert result == expected
def test_solve_quadratic_complex_roots():
    """Тест уравнения с комплексными корнями: x² + 2x + 5 = 0"""
    result = solve_quadratic(1, 2, 5)
    # Ожидаемые корни: -1 ± 2i
    expected = (complex(-1, 2), complex(-1, -2))
    
    # Сравниваем без сортировки - порядок не важен для корней
    assert set(result) == set(expected)