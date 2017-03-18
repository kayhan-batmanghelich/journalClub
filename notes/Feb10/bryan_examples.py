import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Gaussian
'''
x = np.linspace(-4,4,1000)
y0 = stats.norm.pdf(x,0,1)
y1 = stats.norm.pdf(x,1,1.2)
y2 = stats.norm.pdf(x,-1,0.8)
plt.plot(x,y0)
plt.plot(x,y1)
plt.plot(x,y2)
plt.show()
#'''

# Exponential
'''
x = np.linspace(0,10,1000)
y0 = stats.expon.pdf(x,0,1)
y1 = stats.expon.pdf(x,0,2)
y2 = stats.expon.pdf(x,0,3)
plt.plot(x,y0)
plt.plot(x,y1)
plt.plot(x,y2)
plt.show()
#'''

# Laplace
'''
x = np.linspace(-4,4,1000)
y0 = stats.laplace.pdf(x,0,1)
y1 = stats.laplace.pdf(x,1,1.2)
y2 = stats.laplace.pdf(x,-1,0.8)
plt.plot(x,y0)
plt.plot(x,y1)
plt.plot(x,y2)
plt.show()
#'''

# CLT
'''
x = []
for i in range(10):
    for j in range(10):
        mu = 0
        for k in range(10):
            mu += np.random.exponential()
        x.append(mu/10)
    plt.hist(x)
    plt.show()
for j in range(1000):
    mu = 0
    for k in range(10):
        mu += np.random.exponential()
    x.append(mu/10)
plt.hist(x)
plt.show()
#'''

# LLN
'''
x = [np.random.normal()]
#x = [np.random.exponential()]
#x = [np.random.laplace()]
mu = [x[0]]
for i in range(99):
    x.append(x[i]+np.random.normal())
    #x.append(np.random.exponential())
    #x.append(np.random.laplace())
    mu.append(x[i+1]/(i+1))
plt.plot(range(100),mu)
plt.show()    
#'''
