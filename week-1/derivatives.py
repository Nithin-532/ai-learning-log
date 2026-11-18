def numerical_derivative(f, x: float, h: float = 1e-5) -> float:
    return (f(x + h) - f(x)) / h

def f(x):
    return 3 * x ** 2 - 4 * x + 5

def u(x):
    return (2 * x + 1) ** 3

def d(a, b, c):
    return a * b + c

def numerical_gradient(f, inputs: list[float], h: float = 1e-5) -> list[float]:
    """Return ∂f/∂input for every input, nudging one at a time."""
    result = []
    base = f(*inputs)
    for i in range(len(inputs)):
        new_input = inputs[:]
        new_input[i] += h
        slope = (f(*new_input) - base) / h
        result.append(slope)

    return result

inputs = [2.0, -3.0, 10.0]
step_size = 0.01

for i in range(20):
    print("before:", d(*inputs))
    grads = numerical_gradient(d, inputs)

    new_inputs = [old_value - step_size * derivative for old_value, derivative in zip(inputs, grads, strict=True)]

    print("after: ", d(*new_inputs))
    inputs = new_inputs

# if __name__ == "__main__":
#     a, b, c = 2.0, -3.0, 10.0
#     print(numerical_gradient(d, [a, b, c]))

#     h = [0.1, 1e-3, 1e-5, 1e-10, 1e-15]

#     for value in h:
#         estimate = numerical_derivative(f, 3, value)
#         error = abs(estimate - 14)
#         print(f"{value:.10f},  {estimate:.10f},   {error:.10f}")
