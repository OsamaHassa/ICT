# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 18:22:26 2021

@author: oha003
"""
import numpy as np
import matplotlib.pyplot as plt

def PlotLetter(c):
   plt.text(0.6, 0.7, c, size=50, rotation=30.,
         ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   )
         )

PlotLetter("test module 3")
print("Option 1")
print("Option 2")
print("Option 3")
c=input("Type the option")
print(c)
if c=="1":
  print("You selected 1")
  MyfunctionSine(100,1)
if c=="2":
  print("You selected 2")
  PlotLetter("test MODULE 3")
if c=="3":
  print("You selected 3")
  print("Exit")