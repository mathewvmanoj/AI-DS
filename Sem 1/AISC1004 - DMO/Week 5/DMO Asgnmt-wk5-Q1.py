from scipy.optimize import linprog

# Matrix relating to constraints derieved
lhs         = [[20, 12], [1/15, 1/15]]

# RHS of contraints 
rhs         = [1800, 8]

# Objective Function
objective   = [-25, -20]

result      = linprog(c=objective, A_ub=lhs, b_ub=rhs, 
                 bounds=[(0, None), (0, None)], 
                 method='simplex')

x           = result.x

print(f"Beer mugs: {x[0]}")
print(f"Cases of Champagne: {x[1]}")