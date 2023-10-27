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


# In[ ]:




