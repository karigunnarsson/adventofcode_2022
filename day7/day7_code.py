# %%
import pandas as pd
import numpy as np
import re

# %%
data_file = "day7_data.txt"
with open(data_file) as f:
    lines = f.readlines()

# %%
# Start by creating a function that can process the output of a ls function
def process_ls(ls_list):
    dir_dict = {"directories" : [],
            "files" : {"file_name" : [],
                    "file_size" : []}}

    for i in ls_list:
        if i[:3] == "dir":
            dir_dict["directories"].append(i[4:-1])
        else:
            file_split = i.split(" ")
            dir_dict["files"]["file_name"].append(file_split[1][:-1])
            dir_dict["files"]["file_size"].append(int(file_split[0]))

    return dir_dict
# %%
# Secondly we create a function that can parse a cd function, and output new path
def find_path(current_path, cd_command):
    if cd_command == '$ cd /\n':
        new_path = [""]
    elif cd_command == '$ cd ..\n':
        new_path = current_path
        new_path.pop(-1)
    else:
        new_path = current_path
        new_path.append(cd_command[5:-1])

    return new_path


#%%
# Finally we run through all the commands in the list of commands
# We only do anything for real commands (starting with $)
def parse_comms(comm_list):
    # Initiate the file path and total dictionary containing contents of folders
    file_path_list = [""]
    all_dir_dict = {}

    # Iterate through all commands
    for i in range(len(comm_list)):
        comm = comm_list[i]

        # If cd command we calculate the new filepath
        if comm[:4] == '$ cd':
            file_path_list = find_path(file_path_list, comm)

        # Else if it's a ls command we extract the output of the ls, and parse it into a dictionary
        # containing all the contents (folders, filenames and file-sizes) on folder level
        elif comm[:4] == '$ ls':
            ls_list = []
            counter = 1
            first_letter = comm_list[i + counter][0]

            while first_letter != '$':
                ls_list.append(comm_list[i + counter])
                counter += 1

                if i+counter >= len(comm_list):
                    first_letter = '$'
                else:
                    first_letter = comm_list[i + counter][0]

            single_dir_dict = process_ls(ls_list)
            file_path = "/".join(file_path_list)
            all_dir_dict[file_path] = single_dir_dict
    
    return all_dir_dict

# %%
# Generate the total dictionary of folder contents, and extract a list of all folders in the system
all_dirs_parsed = parse_comms(lines)
all_dirs = list(all_dirs_parsed.keys())

# %%
# We now want to be able to calculate the size of a directory
def calc_dir_size(single_dir, all_dir_list, all_dir_dict):
    single_dir_len = len(single_dir)

    # Extract all sub-directorires of a single dir
    sub_dirs = [i for i in all_dir_list if i[:single_dir_len] == single_dir]

    # Calculate the size of all sub-directories and combine into one number
    total_size = 0
    for d in range(len(sub_dirs)):
        total_size += sum(all_dir_dict[sub_dirs[d]]["files"]["file_size"])

    return total_size

# %%
# Now lets calculate the total DIR size for all DIR, and transform to a pandas dataframe for easier sorting and viewing
results_dict = {"dir_path" : [],
                "dir_size" : []}
for c in range(len(all_dirs)):
    single_dir_size = calc_dir_size(all_dirs[c], all_dirs, all_dirs_parsed)

    results_dict["dir_path"].append(all_dirs[c])
    results_dict["dir_size"].append(single_dir_size)

all_dir_pd = pd.DataFrame(results_dict)
# %%
# Look for correct answer
all_dir_pd[all_dir_pd["dir_size"] <= 100000]["dir_size"].sum()
# %%
# Part 2, do the right answer here too
right_size = all_dir_pd[all_dir_pd["dir_size"] >= 8381165].sort_values(by = "dir_size").reset_index(drop = True)
# %%
print(str(right_size.iloc[0]["dir_size"]))

# %%
