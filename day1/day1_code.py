import pandas as pd
import numpy as np
import csv

data_file = "day1/day1_data.csv"

with open(data_file, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

    elf_calorie_dict = {}
    elf_counter = 1
    elf_num = 'elf_'+str(elf_counter)
    elf_calorie_list = []

    for row in spamreader:
        if len(row) == 0:
            elf_calorie_dict[elf_num] = sum(elf_calorie_list)
            elf_counter += 1
            elf_num = 'elf_'+str(elf_counter)
            elf_calorie_list = []
        else:
            elf_calorie_list.append(int(row[0]))
max(list(elf_calorie_dict.values()))

as_df = pd.DataFrame.from_dict(elf_calorie_dict, orient = 'index')
as_df.columns = ["calories"]

as_df.sort_values(by = "calories", ascending = False).iloc[:3].sum()
