import numpy as np
import matplotlib.pyplot as plt
from numpy.random import normal
def val(mean,sig,bins):
   d=5
   d = 1/(sig * np.sqrt(2 * np.pi))*np.exp( - (bins - mean)**2 / (2 * sig**2) )
   return d

xaxes = ['x1','x2','x3']
yaxes = ['y1','y2','y3']
color = ['green','orange','violet']
mean=[0,5,5]
sig =[2,2,5]
min,max=-20,20

ran=np.arange(min, max, 0.1)
f,a = plt.subplots(4,1)
for m,s,c in zip(mean,sig, color):
   a[0].bar(ran,val(m,s,ran), color=c)
a[0].set_title('different normal distributions'+str([(x,y) for x,y in zip(mean,sig)]))
a[0].set_xlim(min,max)
for idx,ax in enumerate(a[1:]):
   n=normal(mean[idx],sig[idx], 1000)
   count, bins, ignored = ax.hist(n,20,density=True, color=color[idx])
   ax.plot(bins,val(mean[idx],sig[idx],bins),linewidth=2, color='r')
   ax.set_title("for mean and sigma"+str(mean[idx])+" "+str(sig[idx]))
   ax.set_xlabel(xaxes[idx])
   ax.set_ylabel(yaxes[idx])
   ax.set_xlim(min,max)
plt.tight_layout()
plt.show()
f.savefig('./ScreenShots/2_Normal_Distribution.png')
plt.close(f)