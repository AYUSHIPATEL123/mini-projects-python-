import numpy as np
import time

list=[3,4,56,78,55,66]   # pokemon powers of each pokemon

s=time.time()
mini=maxi = list[0]
 
for power in list:
        mini = min(mini, power)
        maxi = max(maxi, power)
        print(mini, maxi)
e=time.time()
print("more time (slower):",e-s+0.000000)

st=time.time()
arr=np.array(list)
for i in range(1,len(list)): # after cathing 1 by one pokemon
    min=np.min(arr[0:i]) # min power
    max=np.max(arr[0:i]) # max power
    print(min,max)
ed=time.time()

print("less time (faster) :",ed-st+0.000000)
