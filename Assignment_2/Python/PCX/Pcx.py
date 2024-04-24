import numpy as np
import matplotlib.pyplot as plt

np.random.seed()

nr_parents = 100
nr_selected_parents = 6

parents_idxs = np.arange(nr_parents)

parents = np.random.uniform(size = (nr_parents, 2), low = -10, high = 10)
selected_parents_idxs = np.random.choice(parents_idxs, nr_selected_parents, replace = False)
breeding_parent_idx = np.random.choice(selected_parents_idxs, 1)

plt.scatter(parents[:,0], parents[:,1], c = 'b')
plt.scatter(parents[selected_parents_idxs,0], parents[selected_parents_idxs,1], c = 'c')
plt.scatter(parents[breeding_parent_idx,0], parents[breeding_parent_idx,1], c = 'r')

# Find average of parents
selected_parents_avg = np.mean(parents[selected_parents_idxs,:], axis = 0)
plt.scatter(selected_parents_avg[0], selected_parents_avg[1], c = 'g')

di = (parents[breeding_parent_idx,:] - selected_parents_avg).flatten()

a = di

e = []
d = []

for p in selected_parents_idxs:
    if (p != breeding_parent_idx):
        current_selected_parent = parents[p,  :]
        u = current_selected_parent - selected_parents_avg
        orth_v = u - ((np.dot(u, a)) / (np.dot(a, a))) * a
        
        d.append(np.linalg.norm(orth_v))
        e.append(orth_v / np.linalg.norm(orth_v))

e = np.array(e)
d = np.array(d)
d_avg = np.mean(d)


std1 = 1 / np.sqrt(nr_selected_parents - 1)
std2 = 0.35 / np.sqrt(nr_parents - nr_selected_parents - 2)

for i in range(50):
    offspring = parents[breeding_parent_idx,:] + (np.random.normal(0, 0.2) * di) + (d_avg * np.random.normal(0, 0.3) * np.sum(e, axis = 0))
    plt.scatter(offspring[:,0], offspring[:,1], c = "m")

plt.show()