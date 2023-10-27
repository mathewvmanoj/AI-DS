from scipy.optimize import linprog

# Matrix relating to constraints derieved
lhs_ineq            = [[0.25, 0.30, 0, 0, 0], [0.005, 0.007, 0.002, 0, 0], [-3, 0, 1, 0, 0], [0, -3, 0, 1, 0], [0, -18, 0, 0, 1]]
 
# RHS of contraints 
rhs_ineq           = [200, 40, 0, 0, 0]
 
# Objective Function
objective           = [-5, -7, 0, 0, 0]

x_bounds            = [(0, None), (0, None), (0, None), (0, None), (0, None)]
result              = linprog(objective, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=x_bounds, method='simplex')
x1, x2, x3, x4, x5  = result.x
max_profit          = -result.fun
 
print(f"Value of x1: {x1:.2f}")
print(f"Value of x2: {x2:.2f}")
print(f"Value of x3: {x3:.2f}")
print(f"Value of x4: {x4:.2f}")
print(f"Value of x5: {x5:.2f}")
print(f"Maximum Profit: ${max_profit:.2f}")
