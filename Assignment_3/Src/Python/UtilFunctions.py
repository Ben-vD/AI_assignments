import numpy as np
import matplotlib.pyplot as plt

def random_data():
    # Training data - two randomly-generated Gaussian-distributed clouds of points in 2d space
    np.random.seed(0)
    # Number of points
    N = 200
    # Labels for each cluster
    y = np.random.randint(low=0, high=2, size = N)
    # Mean of each cluster
    means = np.array([[-2, 2], [-2, 2],])
    # Covariance (in X and Y direction) of each cluster
    covariances = np.random.random_sample((2, 2))
    # Dimensions of each point
    X = np.vstack([np.random.randn(N)*covariances[0, y] + means[0, y],
                np.random.randn(N)*covariances[1, y] + means[1, y]])
    
    return X.T

def print_all(ants, grid):
    ants_grid = np.random.randint(size = grid.shape, low = -1, high = 0)

    for ant in ants:
        if (ant._has_datapoint()):
            ants_grid[ant.row, ant.col] = 10
        else:
            ants_grid[ant.row, ant.col] = 0

    print("Data Points")
    print(grid)
    print("Ants")
    print(ants_grid)

def plt_grid(ants, data_points, grid):

    plt_grid = np.zeros(grid.shape)

    for data_point in data_points:
        if (data_point.picked_up == False):
            plt_grid[data_point.row, data_point.col] = 1

    for ant in ants:
        if (ant._has_datapoint()):
            plt_grid[ant.row, ant.col] = 2
        else:
            plt_grid[ant.row, ant.col] = 3

    plt.matshow(plt_grid)
    #plt.show()