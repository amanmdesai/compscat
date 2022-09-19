from __future__ import annotations

from compscat import *

E = 0.1
N = 100000
w_sum, w_square, w_max = compscat.CrossSection(E / compscat.constants.m).integrate_xsec(
    N
)

# print(constants.convert)

sigma_x = w_sum * compscat.constants.convert / (N * 1e12)

print(sigma_x)

assert sigma_x < 0.0095
assert sigma_x > 0.0076
#    print("test_passed")
# else:
#    raise(Error)
