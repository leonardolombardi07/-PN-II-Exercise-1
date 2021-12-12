from scipy.optimize import minimize
from parameters import *
from transportation_cost_function import transportation_cost_function
from bounds import build_bounds
from constraints import build_constraints


# Optimization
# See:
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html

x0 = [L, B, D, T, Cb, Vk, DWT, GMt, froude_number]

res = minimize(
    x0=x0,
    fun=transportation_cost_function,
    method='SLSQP',
    constraints=build_constraints(),
    bounds=build_bounds())
print(res)
