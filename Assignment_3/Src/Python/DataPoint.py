import numpy as np

class DataPoint:

    def __init__(self, grid, data_vector, index):
        
        grid_rows, grid_cols = grid.shape

        open_space_found = False
        while (open_space_found == False):
            self.row = np.random.randint(low = 0, high = grid_rows)
            self.col = np.random.randint(low = 0, high = grid_cols)

            if (grid[self.row, self.col] == -1):
                grid[self.row, self.col] = index
                open_space_found = True

        self.data_vector = data_vector
        self.index = index
        self.dimentions = len(self.data_vector)
        self.picked_up = False

    def _euclidean_distance(self, data_point):
        return np.linalg.norm(self.data_vector - data_point.data_vector)