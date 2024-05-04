import Ant
import DataPoint as dp
import numpy as np
import sys
import matplotlib.pyplot as plt
import UtilFunctions as uf

class AntClustering:

    def __init__(self, grid_rows, grid_cols, nr_ants, data):
        
        self.grid = np.random.randint(size = (grid_rows, grid_cols), low = -1, high = 0)

        self.grid_rows = grid_rows
        self.grid_cols = grid_cols

        self.ants = []
        for i in range(nr_ants):
            self.ants.append(Ant.Ant(self.grid))

        self.data_points = []
        for i in range(len(data)):
            self.data_points.append(dp.DataPoint(self.grid, data[i], i))        

        uf.print_grid(self.ants, self.data_points)

        #self._find_clusters()


    def _find_clusters():
        pass


if __name__ == "__main__":
    
    grid_rows = int(sys.argv[1])
    grid_cols = int(sys.argv[2])

    nr_ants = int(sys.argv[3])

    #data = uf.random_data()

    data = np.random.uniform(size = (10, 4))

    AntClustering(grid_rows, grid_cols, nr_ants, data)
