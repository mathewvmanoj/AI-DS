from scipy.optimize import linprog

# Matrix relating to constraints derieved
lhs_ineq            = [[0.30, 0.30, 0.10, 0.15, 0.50], [0, 0, 1.5, 2.5, 0], [4, 0, -1, 0, 0], [0, 4, 0, -1, 0], [1, 1, 0, 0, -1]]

# RHS of contraints 
rhs_ineq            = [80, 500, 0, 0, 0]

# Objective Function
objective           = [-30, -45, 0, 0, 0]

x_values            = [(0, None), (0, None), (0, None), (0, None), (0, None)]

result              = linprog(objective, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=x_values, method='simplex')
x1, x2, x3, x4, x5  = result.x
max_profit          = -result.fun

print(f"Value of x1: {x1:.2f}")
print(f"Value of x2: {x2:.2f}")
print(f"Value of x3: {x3:.2f}")
print(f"Value of x4: {x4:.2f}")
print(f"Value of x5: {x5:.2f}")
print(f"Maximum Profit: ${max_profit:.2f}")
