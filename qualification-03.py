import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial
from numpy.random import normal, poisson
from random import sample
def val_n(mean,sig,bins):
   d = 1/(sig * np.sqrt(2 * np.pi))*np.exp( - (bins - mean)**2 / (2 * sig**2) )
   return d
def val_p(lam,t):
   d = np.exp(-lam)*np.power(lam, t)/factorial(t)
   return d

xaxes = ['x1','x2','x3']
yaxes = ['y1','y2','y3']
color = ['green','orange','violet']
lam=[10,15,20]
mean=[0,5,5]
sig =[2,2,5]
min,max=-20,20

ran=np.arange(min, max, 0.1)
f,a = plt.subplots(4,2)
for idx,ax in enumerate(a[0]):
   if idx==0:
      for l,c in zip(lam, color):
         ax.bar(ran,val_p(l,ran), color=c)
      ax.set_title('different poisson distributions'+str(lam))
   else:
      for m,s,c in zip(mean,sig, color):
         ax.bar(ran,val_n(m,s,ran), color=c)
      ax.set_title('different normal distributions'+str([(x,y) for x,y in zip(mean,sig)]))
   ax.set_xlim(min,max)
for idx,ax1 in enumerate(a[1:]):
   for idx1,ax in enumerate(ax1):
      if idx1==0:
         p=[sum(sample(list(poisson(lam[idx], 1000)), 100))/100 for x in range(100)]
         count, bins, ignored = ax.hist(p,20,density=True, color=color[idx])
         #print(bins)
         ax.plot(bins,val_p(lam[idx],bins),linewidth=2, color='r')
         ax.set_title("for lamda"+str(lam[idx]))
      else:
         n=[sum(sample(list(normal(mean[idx],sig[idx], 1000)), 100))/100 for x in range(100)]
         count, bins, ignored = ax.hist(n,20,density=True, color=color[idx])
         ax.plot(bins,val_n(mean[idx],sig[idx],bins),linewidth=2, color='r')
         ax.set_title("for mean and sigma"+str(mean[idx])+" "+str(sig[idx]))
      ax.set_xlabel(xaxes[idx])
      ax.set_ylabel(yaxes[idx])
      #ax.set_xlim(min,max)
plt.tight_layout()
plt.show()