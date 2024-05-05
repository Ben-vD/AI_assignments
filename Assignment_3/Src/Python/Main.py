import Ant
import DataPoint as dp
import numpy as np
import sys
import matplotlib.pyplot as plt
import UtilFunctions as uf
from tqdm import tqdm
from sklearn import datasets

class AntClustering:

    def __init__(self, grid_rows, grid_cols, nr_ants, data, iterations, gamma, gamma_1, gamma_2, patch_size):
        
        self.grid = np.random.randint(size = (grid_rows, grid_cols), low = -1, high = 0)

        self.grid_rows = grid_rows
        self.grid_cols = grid_cols
        self.gamma = gamma
        self.gamma_1 = gamma_1
        self.gamma_2 = gamma_2
        self.path_size = patch_size

        self.ants = []
        for i in range(nr_ants):
            self.ants.append(Ant.Ant(self.grid))

        self.data_points = []
        for i in range(len(data)):
            self.data_points.append(dp.DataPoint(self.grid, data[i], i))        

        uf.plt_grid(self.ants, self.data_points, self.grid)
        plt.show()

        #uf.print_all(self.ants, self.grid)

        self._find_clusters(iterations)

        uf.plt_grid(self.ants, self.data_points, self.grid)
        plt.show()

    def _find_clusters(self, iterations):
        for i in tqdm(range(iterations)):
            self._next_time_step()

            #uf.plt_grid(self.ants, self.data_points, self.grid)
            #plt.show()

            #print()
            #uf.print_all(self.ants, self.grid)

    def _next_time_step(self):

        for ant in self.ants:
            # If a data point is found and ant is not a carrier
            position_value = self.grid[ant.row, ant.col]
            if (position_value != -1 and ant._has_datapoint() == False):

                current_data_point_idx = position_value
                local_density = ant._local_density(self.grid, self.data_points, self.path_size, self.gamma)
                p_pick_up = ((self.gamma_1) / (self.gamma_1 + local_density))**2

                if (np.random.uniform() <= p_pick_up):
                    ant._pick_up(current_data_point_idx)
                    self.data_points[current_data_point_idx].picked_up = True
                    self.grid[ant.row, ant.col] = -1

            elif (position_value == -1 and ant._has_datapoint() == True):

                local_density = ant._local_density(self.grid, self.data_points, self.path_size, self.gamma)

                p_drop = 1
                if (local_density < self.gamma_2):
                    p_drop = 2 * local_density

                if (np.random.uniform() <= p_drop):
                    dropped_data_point_idx = ant._drop()
                    self.data_points[dropped_data_point_idx].picked_up = False

                    self.data_points[dropped_data_point_idx].row = ant.row
                    self.data_points[dropped_data_point_idx].col = ant.col

                    self.grid[ant.row, ant.col] = dropped_data_point_idx

            ant._move(self.grid)


if __name__ == "__main__":
    
    grid_rows = int(sys.argv[1])
    grid_cols = int(sys.argv[2])
    nr_ants = int(sys.argv[3])
    iterations = int(sys.argv[4])
    gamma = float(sys.argv[5])
    gamma_1 = float(sys.argv[6])
    gamma_2 = float(sys.argv[7])
    patch_size = int(sys.argv[8])


    data = uf.random_data()

    #np.random.seed(0)
    #data = np.concatenate((np.random.randint(low = 0, high = 5, size = (5, 2)), np.random.randint(low = 20, high = 25, size = (5, 2))))

    #print(data)

    #iris = datasets.load_iris()
    #data = iris.data[:,:2]
    #print(data)
    #sys.exit()

    AntClustering(grid_rows, grid_cols, nr_ants, data, iterations, gamma, gamma_1, gamma_2, patch_size)
