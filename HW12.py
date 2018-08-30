import numpy as np
from scipy.spatial.distance import pdist
import math


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


def foo(X, Y, Z):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
    #ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()

if __name__ == '__main__':
    #foo(X, Y, Z)
    X, Y = np.meshgrid(range(1, 100, 10), range(100, 1001, 100))

    Z = np.zeros(X.shape)
    #print X
    #print Y
    for i in range(Z.shape[0]):
        for j in range(Z.shape[1]):
            d, n = X[0][i], Y[j][0]
            pts = np.random.uniform(0, 100, size=(n, d))
            #dists = pdist(pts)
            dists = pdist(pts, 'minkowski', 1)
            maxdist, mindist = max(dists), min(dists)
            Z[i][j] = math.log((maxdist - mindist) / mindist)

        # visualization starting point
    foo(X, Y, Z)
