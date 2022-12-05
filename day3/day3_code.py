# %%
import pandas as pd
import numpy as np
import re

data_file = "day3_data.csv"
data_pd = pd.read_csv(data_file)
data_pd["compartment_size"] = (data_pd["rucksacks"].str.len() / 2).astype(int)

# %%
first_compartment_list = []
second_compartment_list = []

for i in range(len(data_pd["rucksacks"])):
    first_compartment = data_pd["rucksacks"].iloc[i][:data_pd["compartment_size"].iloc[i]]
    second_compartment = data_pd["rucksacks"].iloc[i][data_pd["compartment_size"].iloc[i]:]

    first_compartment_list.append(first_compartment)
    second_compartment_list.append(second_compartment)

# %%
data_pd["first_compartment"] = first_compartment_list
data_pd["second_compartment"] = second_compartment_list

# %%
duplicate_letter_list = []

for i in range(len(data_pd["rucksacks"])):
    first_compartment = data_pd["first_compartment"].iloc[i]
    second_compartment = data_pd["second_compartment"].iloc[i]

    duplicate_letter = 'NOT FOUND'

    for j in range(len(first_compartment)):
        single_letter = first_compartment[j]
        if bool(re.search(single_letter, second_compartment)):
            duplicate_letter = single_letter
            break
    duplicate_letter_list.append(duplicate_letter)
# %%
data_pd["duplicate_item"] = duplicate_letter_list

# %%
def assign_priority(letter):
    if letter.isupper():
        # 64 to get it so A = 1, and 26 to match the code requirement of starting uppercase at 27
        minus_factor = 64 - 26
    else:
        minus_factor = 96

    priority = ord(letter) - minus_factor

    return priority
# %%
data_pd["priority"] = data_pd["duplicate_item"].apply(lambda x: assign_priority(x))
# %%
# Second assignment
def common_letters(string1, string2):
    wordlist_1 = [*string1]
    wordlist_2 = [*string2] 

    filter_list = [i in wordlist_2 for i in wordlist_1]
    filtered_letters = [wordlist_1[i]for i in range(len(wordlist_1)) if filter_list[i]]

    # get unique letters and concatenate
    unique_letters = "".join(list(set(filtered_letters)))

    return unique_letters

# %%
jump_space = 3
total_priority = 0
num_iter = int(data_pd.shape[0] / jump_space)

# %%
for i in range(num_iter):
    current_pos = i * jump_space

    bag1 = data_pd["rucksacks"].iloc[current_pos]
    bag2 = data_pd["rucksacks"].iloc[current_pos + 1]
    bag3 = data_pd["rucksacks"].iloc[current_pos + 2]

    first_compare = common_letters(bag1, bag2)
    common_letter = common_letters(first_compare, bag3)

    total_priority += assign_priority(common_letter)
# %%
total_priority
# %%
