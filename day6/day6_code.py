# %%
import pandas as pd
import numpy as np
import re

with open('day6_data.txt') as f:
    lines = f.readlines()
# %%
def find_unique_seq(input_str, num_seq):
    start_pos = 0
    unique_seq = False
    while not unique_seq:
        seq_list = [*input_str[start_pos:(start_pos+num_seq)]]
        
        if len(list(set(seq_list))) == num_seq:
            print("Unique sequence found: " + "".join(seq_list))
            print("Position at end of seq: " + str(start_pos + num_seq))
            unique_seq = True

        start_pos += 1
    
# %%
find_unique_seq(lines[0], 4)
# %%
find_unique_seq(lines[0], 14)
# %%
