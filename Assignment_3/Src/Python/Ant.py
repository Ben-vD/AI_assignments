import numpy as np

class Ant:

    def __init__(self, grid):

        grid_rows, grid_cols = grid.shape

        self.row = np.random.randint(low = 0, high = grid_rows)
        self.col = np.random.randint(low = 0, high = grid_cols)

        self.data_point = None

    def _has_datapoint(self):
        return self.data_point != None

    def _move(self, grid):

        grid_rows, grid_cols = grid.shape

        row_update = np.random.randint(low = -1, high = 2)
        cols_update = np.random.randint(low = -1, high = 2)

        if (row_update == 1 and self.row == grid_rows - 1):
            self.row = 0
        elif (row_update == -1 and self.row == 0):
            self.row = grid_rows - 1
        else:
            self.row += row_update

        if (cols_update == 1 and self.col == grid_cols - 1):
            self.col = 0
        elif (cols_update == -1 and self.row == 0):
            self.col = grid_cols - 1
        else:
            self.col += cols_update
