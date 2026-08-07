import sys 
import numpy as np 
import pandas as pd 
import matplotlib 
import matplotlib.pyplot as plt 



print("A new print statement is added and modified and modified again  . [change 3]")
print("Python :", sys.version.split()[0]) 
print("numpy :", np.__version__ )
print("pandas :", pd.__version__ ) 
print("matplotlib:", matplotlib.__version__) # a one-line smoke test of the plotting back-end 
print("My roll number : 25EC01004")
plt.plot([0, 1, 2, 3], [0, 1, 4, 9], marker="o") 
plt.title("If you can see this window, the setup works") 
plt.xlabel("x [change 2]"); plt.ylabel("x squared") 
plt.grid(True) 
plt.show() 