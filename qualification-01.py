import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial
from numpy.random import poisson
def val(lam,t):
   d = np.exp(-lam)*np.power(lam, t)/factorial(t)
   return d

xaxes = ['x1','x2','x3']
yaxes = ['y1','y2','y3']
color = ['green','orange','violet']
lam=[10,15,20]
min,max=0,40

ran=np.arange(min, max, 0.1)
f,a = plt.subplots(4,1)
for l,c in zip(lam, color):
   a[0].bar(ran,val(l,ran), color=c)
a[0].set_title('different poisson distributions'+str(lam))
a[0].set_xlim(min,max)
for idx,ax in enumerate(a[1:]):
   p=poisson(lam[idx], 1000)
   count, bins, ignored = ax.hist(p,30,density=True, color=color[idx])
   ax.plot(bins,val(lam[idx],bins),linewidth=2, color='r')
   ax.set_title("for lamda"+str(lam[idx]))
   ax.set_xlabel(xaxes[idx])
   ax.set_ylabel(yaxes[idx])
   ax.set_xlim(min,max)
plt.tight_layout()
plt.show()
f.savefig('./ScreenShots/1_Poisson_distribution.png')
plt.close(f)