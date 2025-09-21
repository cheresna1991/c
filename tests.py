#тесты, которые импортируются в основном коде
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