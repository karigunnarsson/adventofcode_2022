# %%
import pandas as pd
import numpy as np
import re

# %%
data_file = "day4_data.csv"
data_pd = pd.read_csv(data_file, header = None)
data_pd.columns = ["elf1", "elf2"]
# %%
# Need to define a function that can take a range and convert it to a list
def create_range(range_string):
    range_start_stop = range_string.split("-")
    range_list = list(range(int(range_start_stop[0]), int(range_start_stop[1]) + 1))

    return range_list
# %%
# We define that range1 must be the shorter one
def fully_contained(short_range, long_range):
    filter_list = [i in long_range for i in short_range]
    is_contained = all(filter_list)

    return is_contained
# %%
def single_row_is_contained(elf1_str, elf2_str):
    range1 = create_range(elf1_str)
    range2 = create_range(elf2_str)

    if len(range1) >= len(range2):
        is_contained = fully_contained(range2, range1)
    else:
        is_contained = fully_contained(range1, range2)

    return is_contained

i = 4
# %%
# %%
data_pd["is_contained"] = data_pd.apply(lambda row: single_row_is_contained(row["elf1"], row["elf2"]), axis = 1)

# %%
data_pd["is_contained"].sum()
# %%
# Second part, we just need to redefine the fully_contained() to not use all
def any_contained(short_range, long_range):
    filter_list = [i in long_range for i in short_range]
    any_contained = any(filter_list)

    return any_contained

def single_row_is_contained(elf1_str, elf2_str):
    range1 = create_range(elf1_str)
    range2 = create_range(elf2_str)

    if len(range1) >= len(range2):
        is_contained = any_contained(range2, range1)
    else:
        is_contained = any_contained(range1, range2)

    return is_contained
# %%
data_pd["any_contained"] = data_pd.apply(lambda row: single_row_is_contained(row["elf1"], row["elf2"]), axis = 1)

# %%
data_pd["any_contained"].sum()
# %%
data_pd
# %%
range1 = create_range(data_pd["elf1"].iloc[14])
range2 = create_range(data_pd["elf2"].iloc[14])


filter_list = [i in range2 for i in range1]
any_contained = any(filter_list)
# %%
any_contained
# %%
any_contained(data_pd["elf1"].iloc[14], data_pd["elf2"].iloc[14])
# %%
