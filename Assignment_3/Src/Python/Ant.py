import numpy as np

class Ant:

    def __init__(self, grid):

        grid_rows, grid_cols = grid.shape

        self.row = np.random.randint(low = 0, high = grid_rows)
        self.col = np.random.randint(low = 0, high = grid_cols)

        self.data_point_idx = None

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
        elif (cols_update == -1 and self.col == 0):
            self.col = grid_cols - 1
        else:
            self.col += cols_update

    def _pick_up(self, data_point_idx):
        self.data_point_idx = data_point_idx

    def _drop(self):
        data_point_idx = self.data_point_idx
        self.data_point_idx = None
        return data_point_idx

    def _has_datapoint(self):
        return self.data_point_idx != None
    
    def _local_density(self, grid, data_points, patch_size, gamma):

        grid_rows, grid_cols = grid.shape

        
        data_point_idx = grid[self.row, self.col]
        # If ant is carrier then data point holding is current data point.
        if (self._has_datapoint()):
            data_point_idx = self.data_point_idx
        
        current_data_point = data_points[data_point_idx]

        # Look at all local patch positions
        traversed_area = np.zeros((grid_rows, grid_cols))
        found_idxs = []
        self._traverse_local_patch(grid, patch_size, self.row, self.col, 0, traversed_area, found_idxs)

        if (len(found_idxs) == 0):
            return 0

        sum = 0
        for i in found_idxs:
            sum += 1 - (current_data_point._euclidean_distance(data_points[i]) / gamma)

        local_density = sum / (2 * patch_size + 1)**2

        #print(local_density)

        if (local_density <= 0):
            return 0

        return local_density 
    
    def _traverse_local_patch(self, grid, patch_size, row, col, radius, traversed_area, found_idxs):
        
        # Fix invalid rows and cols
        grid_rows, grid_cols = grid.shape
        if (row == -1):
            row = grid_rows - 1
        elif (row == grid_rows):
            row = 0

        if (col == -1):
            col = grid_cols - 1
        elif (col == grid_cols):
            col = 0

        # Check if index is found
        if (grid[row, col] != -1 and radius != 0):
            found_idxs.append(grid[row, col])

        # Base Case. If patch size nr of steps away or area already checked
        if (radius == patch_size or traversed_area[row, col] == 1):
            return

        # Mark current area as checked
        traversed_area[row, col] = 1

        self._traverse_local_patch(grid, patch_size, row + 1, col - 1,  radius + 1, traversed_area, found_idxs)
        self._traverse_local_patch(grid, patch_size, row + 1, col,      radius + 1, traversed_area, found_idxs)
        self._traverse_local_patch(grid, patch_size, row + 1, col + 1,  radius + 1, traversed_area, found_idxs)
        self._traverse_local_patch(grid, patch_size, row, col + 1,      radius + 1, traversed_area, found_idxs)
        self._traverse_local_patch(grid, patch_size, row - 1, col + 1,  radius + 1, traversed_area, found_idxs)
        self._traverse_local_patch(grid, patch_size, row - 1, col,      radius + 1, traversed_area, found_idxs)
        self._traverse_local_patch(grid, patch_size, row - 1, col - 1,  radius + 1, traversed_area, found_idxs)
        self._traverse_local_patch(grid, patch_size, row, col - 1,      radius + 1, traversed_area, found_idxs)
