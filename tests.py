import math
import pytest
import random
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
    expected = (complex(-1, 2), complex(-1, -2))
    
    assert set(result) == set(expected)

def test_solve_quadratic_a_zero():
    """Тест вызова исключения при a = 0"""
    with pytest.raises(ValueError, match="Коэффициент 'a' не может быть равен нулю"):
        solve_quadratic(0, 1, 2)

def test_invalid_coefficients():
    """Тест невалидных коэффициентов"""
    with pytest.raises(ValueError):
        solve_quadratic(0, 2, 3)  
    with pytest.raises(TypeError):
        solve_quadratic("a", 2, 3)

def test_vieta_theorem_real_roots():
    """Тест на соответствие теореме Виета для действительных корней"""
   
    x1 = random.uniform(-10, 10)
    x2 = random.uniform(-10, 10)
    
    
    a = 1
    b = -(x1 + x2)
    c = x1 * x2
    
    roots = solve_quadratic(a, b, c)
    
    
    if len(roots) == 2:
        calculated_roots = sorted(roots, reverse=True)
        expected_roots = sorted([x1, x2], reverse=True)
        
        
        assert math.isclose(calculated_roots[0], expected_roots[0], rel_tol=1e-10)
        assert math.isclose(calculated_roots[1], expected_roots[1], rel_tol=1e-10)
        
       
        assert math.isclose(roots[0] + roots[1], -b, rel_tol=1e-10)
        assert math.isclose(roots[0] * roots[1], c, rel_tol=1e-10)

def test_vieta_theorem_multiple_cases():
    """Тест теоремы Виета на нескольких случайных случаях"""
    
    test_cases = [
       
        (2.0, 3.0),
        (-1.5, 4.0),
        (0.0, 5.0),
        (-2.0, -3.0),
        (1.0, 1.0),  
        (7.5, -2.5)
    ]
    
    for x1, x2 in test_cases:
        a = 1
        b = -(x1 + x2)
        c = x1 * x2
        
        roots = solve_quadratic(a, b, c)
        
        if len(roots) == 2:
            
            calculated_roots = sorted(roots, reverse=True)
            expected_roots = sorted([x1, x2], reverse=True)
            
            
            assert math.isclose(calculated_roots[0], expected_roots[0], rel_tol=1e-10)
            assert math.isclose(calculated_roots[1], expected_roots[1], rel_tol=1e-10)
            
            
            assert math.isclose(roots[0] + roots[1], -b, rel_tol=1e-10)
            assert math.isclose(roots[0] * roots[1], c, rel_tol=1e-10)
        else:
            
            assert len(roots) == 1
            assert math.isclose(roots[0], x1, rel_tol=1e-10)
            assert math.isclose(roots[0] + roots[0], -b, rel_tol=1e-10)
            assert math.isclose(roots[0] * roots[0], c, rel_tol=1e-10)

def test_vieta_complex_roots():
    """Тест теоремы Виета для комплексных корней"""
    
    
    real_part = random.uniform(-5, 5)
    imag_part = random.uniform(1, 5)  
    
    x1 = complex(real_part, imag_part)
    x2 = complex(real_part, -imag_part)
    
    
    a = 1
    b = -(x1 + x2)
    c = x1 * x2
    
    
    assert abs(b.imag) < 1e-15  
    assert abs(c.imag) < 1e-15
    
    b = b.real
    c = c.real
    
    
    roots = solve_quadratic(a, b, c)
    
    
    assert abs(roots[0].real - roots[1].real) < 1e-10
    assert abs(roots[0].imag + roots[1].imag) < 1e-10
    
   
    sum_roots = roots[0] + roots[1]
    product_roots = roots[0] * roots[1]
    
    assert abs(sum_roots.real + b) < 1e-10
    assert abs(sum_roots.imag) < 1e-10
    assert abs(product_roots.real - c) < 1e-10
    assert abs(product_roots.imag) < 1e-10

