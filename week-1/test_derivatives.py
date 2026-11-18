import pytest
from derivatives import numerical_gradient, d, numerical_derivative

def test_derivatives():
    assert numerical_gradient(d, [2.0, -3.0, 10.0]) == pytest.approx([-3, 2, 1], abs=1e-6)

def test_derivative_of_f():
    assert numerical_derivative(f, 3.0) == pytest.approx(14, abs=1e-4)

def test_chain_rule():
    assert numerical_derivative(u, 1.0) == pytest.approx(54, abs=1e-3)