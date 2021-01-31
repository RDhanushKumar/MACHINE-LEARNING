import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

x = np.array([1,2,3])
y = np.array([1.2,1.9,3.2])
beta = 1

"""Upon differentiating the log likelihood formula, to obtain the value of w0 and w1 
in the function y(x,w) => y = w1x+ w0, we get the values of w0,w1 as follows:
w0 = (RQ-PS)/(RN-P^2)
w1 = (Q - Nw0)/P
where P = x.sum()
      Q = y.sum()
      R = (np.square(x)).sum()
      S = (x*y).sum()
      N = len(x)"""

def Get_params(x,y):
    P = x.sum()
    Q = y.sum()
    R = (x*x).sum()
    S = (x*y).sum()
    N = len(x)
    
    w0 = ((R*Q) - (P*S))/((R*N) - (P**2))
#     w1 = ((P*Q) - (R*S))/((R*N) - (P**2))
    w1 = (Q - (N*w0))/P
    
    print("W is given by w1=",w1," w0=",w0)
    return w1, w0

m,c = Get_params(x,y)

abline_values = [m * i + c for i in x]
plt.scatter(x,y)
plt.plot(x, y, '--')
plt.plot(x, abline_values, 'b')
plt.show()