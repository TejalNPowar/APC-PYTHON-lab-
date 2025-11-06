import numpy as np
ar=np.array([1,2,3,4,5,6])
new_ar=ar.reshape(2,3)
print("Reshaped (original unchanged:)\n",new_ar)

ar.resize(2,3)
print("Resize (original changed):\n",ar)

