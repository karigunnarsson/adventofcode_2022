# %%
import pandas as pd
import numpy as np
import re

# %%
data_file = "day8_data.txt"
with open(data_file) as f:
    lines = f.readlines()

# This extra step to remove the newline tag
lines = [i.rstrip() for i in lines]

# %%
def is_visible(pos):
    # Height of tree we're calculating
    tree_height = int(lines[pos[0]][pos[1]])

    # Define all the line of sights based of a X,Y (or Y,X actually) coordinate
    los_left = [int(i) for i in [*lines[pos[0]][:pos[1]]]]
    los_right = [int(i) for i in [*lines[pos[0]][(pos[1] + 1):]]]
    los_up = [int(lines[i][pos[1]]) for i in range(pos[0])]
    los_down = [int(lines[i][pos[1]]) for i in range(pos[0] + 1, len(lines))]

    # See if any tree is same height (or taller) than the tree we're calculating for
    # If it is, then it's not visible from outside the grid
    left_vis = all([i < tree_height for i in los_left])
    right_vis = all([i < tree_height for i in los_right])
    up_vis = all([i < tree_height for i in los_up])
    down_vis = all([i < tree_height for i in los_down])

    # Check if visible in any direction
    any_visible = any([left_vis, right_vis, up_vis, down_vis])

    return any_visible

# %%
# Define the range, we ignore the outer edge here (because it's always visible)
hor_range = [1, len(lines[0]) - 1]
ver_range = [1, len(lines) - 1]

# We add the outer edge as the default count
# Subtracting the two from the edges so we don't double count the corners
outer_trees_vis = 2 * len(lines[0]) + (len(lines) - 2) * 2
# %%
inner_trees_vis = 0
# Iterate through all
for h in range(hor_range[0], hor_range[1]):
    for v in range(ver_range[0], ver_range[1]):
        #print(str(h) + str(v))
        single_vis = is_visible([h,v])

        if single_vis:
            inner_trees_vis += 1
# %%
all_trees_vis = outer_trees_vis + inner_trees_vis
# %%
all_trees_vis

# %%
# Part two, need to calculate scenic score
# %%
# Function to calculate the number of trees seen
def trees_seen(tree_height, tree_list):
    # Create list of all tries in line of sight that's >= tree height
    bool_list = [i >= tree_height for i in tree_list]

    if any(bool_list):
        # If any tree in LoS is >= tree height, we count distance to that tree (plus count that tree)
        trees_seen = np.min(np.where(bool_list)) + 1
    else:
        # If no tree is taller, the number of trees seen is all trees in LoS
        trees_seen = len(tree_list)

    return trees_seen

def calc_scenic_score(pos):
    # Height of tree we're calculating
    tree_height = int(lines[pos[0]][pos[1]])

    # Define all the line of sights based of a X,Y (or Y,X actually) coordinate
    # Additionally for this part, we wish to sort them all in order of closest to furthest away
    los_left = [int(i) for i in [*lines[pos[0]][:pos[1]]]]
    los_left.reverse()
    los_right = [int(i) for i in [*lines[pos[0]][(pos[1] + 1):]]]
    los_up = [int(lines[i][pos[1]]) for i in range(pos[0])]
    los_up.reverse()
    los_down = [int(lines[i][pos[1]]) for i in range(pos[0] + 1, len(lines))]

    # Calculate the number of trees seen per path
    left_seen = trees_seen(tree_height, los_left)
    rightleft_seen = trees_seen(tree_height, los_right)
    up_seen = trees_seen(tree_height, los_up)
    down_seen = trees_seen(tree_height, los_down)

    # Calculate scenic score
    scenic_score = left_seen * rightleft_seen * up_seen * down_seen

    return scenic_score

# %%
max_scenic_score = 0
for h in range(hor_range[0], hor_range[1]):
    for v in range(ver_range[0], ver_range[1]):
        #print(str(h) + str(v))
        single_score = calc_scenic_score([h,v])

        max_scenic_score = max(max_scenic_score, single_score)
# %%
max_scenic_score
# %%
