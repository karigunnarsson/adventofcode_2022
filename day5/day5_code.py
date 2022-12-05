# %%
import pandas as pd
import numpy as np
import re

# %%
# Read the sequence data, use move, from and too as delimiters in a CSV, and then just drop the first column.
# Gives a neat 3 column dataframe with all the sequence data stored
sequence_data = pd.read_csv("day5_sequence_data.csv", 
                            delimiter = "move|from|to", 
                            header = None,
                            engine='python').drop(columns = 0)
sequence_data.columns = ["amt", "from", "to"]
# %%
# Read the starting position data
with open('day5_start_data.csv') as f:
    lines = f.readlines()
# %%
# Generate a mapping dictionary to find the column position of each stack
col_pos_dict = {}
last_line = len(lines)-1
for i in range(1,10):
    col_pos_dict[i] = lines[last_line].find(str(i))

# %%
# Now generate a dictionary of all columns and the respective boxes
box_dict = {}

# Iterate through each stack, using the map of col position to find the boxes
for i in range(1,10):
    starting_boxes = []

    # On each stack, start at the bottom (hence reversed), and add to the list
    for j in reversed(range(len(lines) - 1)):
        if lines[j][col_pos_dict[i]] != ' ':
            starting_boxes.append(lines[j][col_pos_dict[i]])
        
    # Assign to dictionary ID
    box_dict[i] = starting_boxes
# %%
# Create a function that can perform a single crane action
def perform_action(amt, from_stack, to_stack):
    # Iterate through all boxes, must do one by one and update dictionary to make sure correct order is kept
    for box in range(amt):
        # Find the box letter we-re moving
        box_to_move = box_dict[from_stack][-1]
        
        # Remove from old stack
        box_dict[from_stack].pop(-1)

        # Add to new stack
        box_dict[to_stack].append(box_to_move)
# %%
# Now we iterate through all crane actions
for i in range(sequence_data.shape[0]):
    single_movement = sequence_data.iloc[i]

    perform_action(single_movement["amt"], single_movement["from"], single_movement["to"])

# %%
# Find the final string
final_string_list = []
for i in range(1,10):
    final_string_list.append(box_dict[i][-1])

print("Final sequence of last boxes : " + "".join(final_string_list))

# %%
# Part 2
def perform_action_9001(amt, from_stack, to_stack):
    # Find the list of boxes (in order) that we're removing
    boxes_to_move = box_dict[from_stack][-amt:]
    
    # Remove from old stack, probably smarter way to do this without loop, but it's easy to reuse code
    for i in range(amt):
        box_dict[from_stack].pop(-1)

    # Add to new stack
    box_dict[to_stack] = box_dict[to_stack] + boxes_to_move

# %%
# Now we iterate through all crane actions
for i in range(sequence_data.shape[0]):
    single_movement = sequence_data.iloc[i]

    perform_action_9001(single_movement["amt"], single_movement["from"], single_movement["to"])
    
# %%
# Find the final string
final_string_list = []
for i in range(1,10):
    final_string_list.append(box_dict[i][-1])

print("Final sequence of last boxes : " + "".join(final_string_list))
# %%
