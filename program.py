import numpy as np
import matplotlib.pyplot as plt

def MyfunctionSine(a,p):
  x=np.linspace(1,100,100)
  y=a*np.sin(p+x)
  plt.plot(x,y)
  print("Hello from a function")
  
MyfunctionSine(np.pi, 2*np.pi)