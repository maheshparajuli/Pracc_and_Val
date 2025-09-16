import numpy as np

height=np.round(np.random.normal(1.75,0.20,5000),2)
weight=np.round(np.random.normal(60.75,15,5000),2)

whole=np.column_stack((height,weight))

print(whole)