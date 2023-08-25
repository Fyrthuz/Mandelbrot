import matplotlib.pyplot as plt
import numpy as np

# c is a complex number
def mandelbrot_kernel(c):
    max_iter = 100
    z = c
    for i in range(max_iter):
        #calcula de la iteracion
        z = z**2 + c
        #distanci del origen al punto
        if np.linalg.norm(z) > 4.0:
            return i * 255 / max_iter
    return 255

xmax = 1.5
xmin = -2.5
ymax = 1.5
ymin = -1.5

def compute_mandelbrot():
    result = [[0 for j in range(768)] for i in range (960)]
    dx = (xmax - xmin)/960
    dy = (ymax - ymin)/768

    for i in range(960):
        for j in range(768):
            result[i][j] = mandelbrot_kernel(complex(xmin + i*dx,ymin + j*dy))
    
    return result


plt.imshow(compute_mandelbrot(),cmap='gray',interpolation='nearest')
plt.show()