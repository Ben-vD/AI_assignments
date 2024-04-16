import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import orth

offspring_nr = 100
nr_parents_to_select = 4
parents_count = 20 

parents = np.random.uniform(size = (parents_count, 2), low = -10, high = 10)

selected_parents_idxs = np.random.choice(range(parents_count), nr_parents_to_select, replace = False)
selected_parents = parents[selected_parents_idxs, :]
selected_parents_avg = np.average(selected_parents, axis = 0)

selected_parent_idx = np.random.choice(range(nr_parents_to_select), 1)
selected_parent = selected_parents[selected_parent_idx, :].flatten()

plt.scatter(parents[:,0], parents[:,1], c = 'b')
plt.scatter(selected_parents[:,0], selected_parents[:,1], c = 'g')
plt.scatter(selected_parents_avg[0], selected_parents_avg[1], c = 'tab:orange')
plt.scatter(selected_parent[0], selected_parent[1], c = 'r')
plt.legend(["Parents", "Selected Parents", "Avg Selected Parents", "Breeding Parent"])

avg_to_parent_vector =  selected_parent - selected_parents_avg
plt.quiver(selected_parents_avg[0], selected_parents_avg[1], avg_to_parent_vector[0], avg_to_parent_vector[1], scale_units='xy', scale = 1, angles='xy')

# Orthogonal d to line
perp_vectors = []
print(perp_vectors)

a = avg_to_parent_vector
for i in range(nr_parents_to_select):
    if (i != selected_parent_idx):
        u =  selected_parents[i] - selected_parents_avg
        perp_vec = u - (np.dot(u, a) / np.dot(a, a)) * a
        u = selected_parents[i]
        plt.quiver(u[0], u[1], -perp_vec[0], -perp_vec[1], scale_units='xy', scale = 1, angles='xy')

        perp_vectors.append(perp_vec)

perp_vectors = np.array(perp_vectors)
orth_bases = orth(perp_vectors.T)
plt.quiver(0, 0, orth_bases[0], orth_bases[1], scale_units='xy', scale = 1, angles='xy')

avg_d = np.average(np.linalg.norm(perp_vectors, axis = 1), axis = 0)
print(avg_d)

plt.xlim(-15, 15) 
plt.ylim(-15, 15) 
plt.axis('square')

plt.grid()
plt.show()