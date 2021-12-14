from scipy.optimize import minimize
from parameters import *
from transportation_cost_function import *
from bounds import build_bounds
from constraints import build_constraints


# x0 is the initial guess vector containing ship parameters
x0 = [L, B, D, T, Cb, Vk]

# We then apply the optimization by calling the minimize function. See:
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html
result = minimize(
    x0=x0,  # Passing the initial guess vector
    fun=transportation_cost_function,  # Objective function to be optimized
    method="SLSQP",  # We are using the Sequential Least Squares Programming algorithm
    # Sequence of dictionaries defining the constraints
    constraints=build_constraints(),
    # Sequence of tuples defining lower and upper bounds for each parameter
    bounds=build_bounds()
)

# Get the Optimized transportation cost and the changed
# ship parameters as result of the optimization
optimized_transportation_cost = result.fun
L, B, D, T, Cb, Vk = result.x


# And finnally print the obtained values
print(
    f"Optimized transportation cost: {optimized_transportation_cost} [US$/ton] \n")
print(f"Length (L) after optimization: {L} [m]")
print(f"Breadth (B) after optimization: {B} [m]")
print(f"Depth (D) after optimization: {D} [m]")
print(f"Draught (T) after optimization: {T} [m]")
print(f"Block Coefficient (Cb) after optimization: {Cb}")
print(f"Speed in knots (Vk) after optimization: {Vk} [kn]")
