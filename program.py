
import matplotlib.pyplot as plt
def PlotLetter(c):
   plt.text(0.6, 0.7, c, size=50, rotation=30.,
         ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   )
         )
PlotLetter("Group1")

import numpy as np
import matplotlib.pyplot as plt

def MyfunctionSine(a,p):
  x=np.linspace(1,100,100)
  y=a*np.sin(p+x)
  plt.plot(x,y)
  print("Hello from a function")
  
MyfunctionSine(np.pi, 2*np.pi)
