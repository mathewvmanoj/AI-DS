#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np
from scipy.optimize import linprog

A = np.array([[0.3, 0.3, 0.1, 0.15, 0.5], 
              [0, 0, 1.5, 2.5, 0], 
              [-4, 0, 1, 0, 0],
              [0, -4, 0, 1, 0],
              [1, 1, 0, 0, -1]])
A


# In[19]:


b = np.array([80, 500, 0, 0, 0])
b


# In[17]:


c = np.array([30, 45, 0, 0, 0])


# In[21]:


res = linprog(c, A_ub=A, b_ub=b)
res


# In[22]:


print('Optimal value:', round(res.fun, ndigits=2),
      '\nx values:', res.x,
      '\nNumber of iterations performed:', res.nit,
      '\nStatus:', res.message)


# In[32]:


from scipy.optimize import linprog

 
# Coefficients of the objective function
c = [-5, -7, 0, 0, 0]

 
# Coefficients of the inequality constraints (left-hand side)
A = [[0.25, 0.30, 0, 0, 0], [0.002 * 10, 0.002 * 18, 0.005, 0.007, 0], [0, 0, -1, 0, 0], [0, 0, 0, -1, 0], [0, 0, 0, 0, -1]]
b = [200, 40, 0, 0, 0]

 
# Bounds for the variables
x1_bounds = (0, None)
x2_bounds = (0, None)
x3_bounds = (0, None)
x4_bounds = (0, None)
x5_bounds = (0, None)

 
# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x1_bounds, x2_bounds, x3_bounds, x4_bounds, x5_bounds], method='highs')


# Extract the optimal solution
x1 = result.x[0]
x2 = result.x[1]
x3 = result.x[2]
x4 = result.x[3]
x5 = result.x[4]

 
# Print the optimal solution and profit
print(f"Number of standard palettes assembled and sold: {x1}")
print(f"Number of extra long palettes assembled and sold: {x2}")
print(f"Number of standard separators manufactured: {x3}")
print(f"Number of extra long separators manufactured: {x4}")
print(f"Number of cross pieces manufactured: {x5}")
print(f"Optimal profit: ${-result.fun}")


# In[29]:


from scipy.optimize import linprog

 

# Coefficients of the objective function
c = [-30, -45, 0, 0, 0]

 

# Coefficients of the inequality constraints (left-hand side)
A = [[0.10, 0.15, 0, 0, 0], [0.50, 0.50, 0, 0, 0], [0, 0, -1, 0, 0], [0, 0, 0, -1, 0], [0, 0, 0, 0, -1], [-1, 0, 0, 0, 1], [0, -1, 0, 0, 1]]
b = [80, 80, 0, 0, 0, 0, 0]

 

# Bounds for the variables
x_bounds = (0, None)
y_bounds = (0, None)
z_bounds = (0, None)
w_bounds = (0, None)
v_bounds = (0, None)

 

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds, z_bounds, w_bounds, v_bounds], method='highs')

 

# Extract the optimal solution
x1 = result.x[0]
x2 = result.x[1]
x3 = result.x[2]
x4 = result.x[3]
x5 = result.x[4]

 

# Print the optimal solution and profit
print(f"Number of model A tables assembled and sold: {x1}")
print(f"Number of model B tables assembled and sold: {x2}")
print(f"Number of short legs manufactured: {x3}")
print(f"Number of long legs manufactured: {x4}")


# In[42]:


from scipy.optimize import linprog

# Coefficients of the objective function to maximize (profit)
c = [-30, -45, 0, 0, 0]  # Minimize -30x1 - 45x2 (negative sign because linprog minimizes)

# Coefficients of the inequality constraints (Ax <= b)
A = [
    [0.10, 0.15, 0.50, 0.30, 0],  # Labor Hour Constraint
    [18, 30, 0, 0, 0]  # Leg Stock Constraint
]

b = [80, 500]  # Right-hand side values for the constraints

# Bounds for the decision variables (x1, x2, x3, x4, x5)
x_bounds = [(0, None), (0, None), (0, None), (0, None), (0, None)]

# Define a custom LP solver function
res = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method="highs")


# Solve the LP problem using the custom function
x_optimal, profit = custom_linprog(c, A, b, x_bounds)

# Extract the results
x1_optimal, x2_optimal, x3_optimal, x4_optimal, x5_optimal = x_optimal

print("Optimal Plan:")
print(f"Number of model A tables assembled and sold (x1): {x1_optimal}")
print(f"Number of model B tables assembled and sold (x2): {x2_optimal}")
print(f"Maximized Profit: ${profit:.2f}")

print(f"Number of model B tables assembled and sold (x3): {x3_optimal}")
print(f"Number of model B tables assembled and sold (x4): {x4_optimal}")
print(f"Number of model B tables assembled and sold (x5): {x5_optimal}")
print(f"Maximized Profit: ${profit:.2f}")


# In[43]:


from scipy.optimize import linprog

c = [-5, -7, 0, 0, 0]

A = [

  [0.25, 0.30, 0, 0, 0],

  [0.005, 0.007, 0.002, 0, 0],

  [-3, 0, 1, 0, 0],

  [0, -3, 0, 1, 0],

  [-5, -9, 0, 0, 1]

]

 

 

b = [200, 40, 0, 0, 0]

 

x_bounds = [(0, None), (0, None), (0, None), (0, None), (0, None)]

result = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='simplex')

x1, x2, x3, x4, x5 = result.x

max_profit = -result.fun

 

print(f"Optimal number of standard palettes (x1): {x1:.2f}")

print(f"Optimal number of extralong palettes (x2): {x2:.2f}")

print(f"Optimal number of standard separators (x3): {x3:.2f}")

print(f"Optimal number of extralong separators (x4): {x4:.2f}")

print(f"Optimal number of cross pieces (x5): {x5:.2f}")

print(f"Maximum Profit: ${max_profit:.2f}")


# In[46]:


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


# In[49]:


from scipy.optimize import linprog
c = [-5, -7, 0, 0, 0]
A = [
  [0.25, 0.30, 0, 0, 0],
  [0.005, 0.007, 0.002, 0, 0],
  [-3, 0, 1, 0, 0],
  [0, -3, 0, 1, 0],
  [0, -18, 0, 0, 1]
]
 
 
b = [200, 40, 0, 0, 0]
 
x_bounds = [(0, None), (0, None), (0, None), (0, None), (0, None)]
result = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='simplex')
x1, x2, x3, x4, x5 = result.x
max_profit = -result.fun
 
print(f"Optimal number of standard palettes (x1): {x1:.2f}")
print(f"Optimal number of extralong palettes (x2): {x2:.2f}")
print(f"Optimal number of standard separators (x3): {x3:.2f}")
print(f"Optimal number of extralong separators (x4): {x4:.2f}")
print(f"Optimal number of cross pieces (x5): {x5:.2f}")
print(f"Maximum Profit: ${max_profit:.2f}")


# In[ ]:




