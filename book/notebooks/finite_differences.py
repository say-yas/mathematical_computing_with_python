"""Finite-difference formulas for the first derivative.

Use in a notebook with
    from finite_differences import forward, backward, central, five_point

All formulas follow from Taylor's theorem:
    f(x +- h) = f(x) +- h f'(x) + h^2/2 f''(x) +- h^3/6 f'''(x) + ...
"""


def forward(f, x, h):
    """Forward difference (f(x+h) - f(x)) / h.  Error O(h)."""
    return (f(x + h) - f(x)) / h


def backward(f, x, h):
    """Backward difference (f(x) - f(x-h)) / h.  Error O(h)."""
    return (f(x) - f(x - h)) / h


def central(f, x, h):
    """Central difference (f(x+h) - f(x-h)) / (2h).  Error O(h^2)."""
    return (f(x + h) - f(x - h)) / (2 * h)


def five_point(f, x, h):
    """5-point central difference.  Error O(h^4)."""
    return (-f(x + 2 * h) + 8 * f(x + h) - 8 * f(x - h) + f(x - 2 * h)) / (12 * h)


# a list to loop over, with matching names
FD_NAMES = ["forward", "backward", "central", "5-point"]
FD_METHODS = [forward, backward, central, five_point]
