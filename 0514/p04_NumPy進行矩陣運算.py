import numpy as np
x = np.array([[2,3],[1,4]], dtype=np.float64)
y = np.array([[4,2],[1,3]], dtype=np.float64)
print('x + y:',np.add(x, y),sep='\n')
print('x - y:',np.subtract(x, y),sep='\n')
print('x * y:',np.multiply(x, y),sep='\n')
print('x / y:',np.divide(x, y),sep='\n')



x2 = np.array([[2,3],[1,4]], dtype=np.uint8)
y2 = np.array([[4,2],[1,0]], dtype=np.uint8)
z = x2/y2
z = z.astype(np.uint8)
print('x / y:',z,z.dtype,sep='\n')

y = np.array([[4,2],[1,0]], dtype=np.float64)
print('x / y:',np.divide(x, y),sep='\n')