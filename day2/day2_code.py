import pandas as pd
import numpy as np

data_file = "day2/day2_data.csv"
data_pd = pd.read_csv("day2/day2_data.csv", delimiter = ' ', header = None)
data_pd.columns = ["opp_pick", "self_pick"]

data_pd["opp_pick"] =  np.where(data_pd["opp_pick"] == 'A', 'rock',
                        np.where(data_pd["opp_pick"] == 'B', 'paper',
                        np.where(data_pd["opp_pick"] == 'C', 'scissor', 'error')))

data_pd["self_pick"] = np.where(data_pd["self_pick"] == 'X', 'rock',
                        np.where(data_pd["self_pick"] == 'Y', 'paper',
                        np.where(data_pd["self_pick"] == 'Z', 'scissor','error')))

data_pd["pick_score"] = np.where(data_pd["self_pick"] == 'rock', 1,
                        np.where(data_pd["self_pick"] == 'paper', 2,
                        np.where(data_pd["self_pick"] == 'scissor', 3, -1)))

data_pd["outcome_score"] =  np.where(data_pd["self_pick"] == data_pd["opp_pick"], 3,
                            np.where((data_pd["self_pick"] == 'rock') & (data_pd["opp_pick"] == 'paper'), 0,
                            np.where((data_pd["self_pick"] == 'rock') & (data_pd["opp_pick"] == 'scissor'), 6,
                            np.where((data_pd["self_pick"] == 'paper') & (data_pd["opp_pick"] == 'rock'), 6,
                            np.where((data_pd["self_pick"] == 'paper') & (data_pd["opp_pick"] == 'scissor'), 0,
                            np.where((data_pd["self_pick"] == 'scissor') & (data_pd["opp_pick"] == 'rock'), 0,
                            np.where((data_pd["self_pick"] == 'scissor') & (data_pd["opp_pick"] == 'paper'), 6, -1)))))))

data_pd["total_score"] = data_pd["pick_score"] + data_pd["outcome_score"]
data_pd["total_score"].sum()
# Part two
data_pd = pd.read_csv("day2/day2_data.csv", delimiter = ' ', header = None)
data_pd.columns = ["opp_pick", "desired_outcome"]
data_pd["opp_pick"] =   np.where(data_pd["opp_pick"] == 'A', 'rock',
                        np.where(data_pd["opp_pick"] == 'B', 'paper',
                        np.where(data_pd["opp_pick"] == 'C', 'scissor', 'error')))

data_pd["desired_outcome"] =    np.where(data_pd["desired_outcome"] == 'X', 'lose',
                                np.where(data_pd["desired_outcome"] == 'Y', 'draw',
                                np.where(data_pd["desired_outcome"] == 'Z', 'win','error')))

data_pd["self_pick"] =  np.where(data_pd["desired_outcome"] == 'draw', data_pd["opp_pick"],
                        np.where((data_pd["opp_pick"] == 'rock') & (data_pd["desired_outcome"] == 'win'), 'paper',
                        np.where((data_pd["opp_pick"] == 'rock') & (data_pd["desired_outcome"] == 'lose'), 'scissor',
                        np.where((data_pd["opp_pick"] == 'paper') & (data_pd["desired_outcome"] == 'win'), 'scissor',
                        np.where((data_pd["opp_pick"] == 'paper') & (data_pd["desired_outcome"] == 'lose'), 'rock',
                        np.where((data_pd["opp_pick"] == 'scissor') & (data_pd["desired_outcome"] == 'win'), 'rock',
                        np.where((data_pd["opp_pick"] == 'scissor') & (data_pd["desired_outcome"] == 'lose'), 'paper', 'error')))))))

data_pd["pick_score"] = np.where(data_pd["self_pick"] == 'rock', 1,
                        np.where(data_pd["self_pick"] == 'paper', 2,
                        np.where(data_pd["self_pick"] == 'scissor', 3, -1)))

data_pd["outcome_score"] =  np.where(data_pd["self_pick"] == data_pd["opp_pick"], 3,
                            np.where((data_pd["self_pick"] == 'rock') & (data_pd["opp_pick"] == 'paper'), 0,
                            np.where((data_pd["self_pick"] == 'rock') & (data_pd["opp_pick"] == 'scissor'), 6,
                            np.where((data_pd["self_pick"] == 'paper') & (data_pd["opp_pick"] == 'rock'), 6,
                            np.where((data_pd["self_pick"] == 'paper') & (data_pd["opp_pick"] == 'scissor'), 0,
                            np.where((data_pd["self_pick"] == 'scissor') & (data_pd["opp_pick"] == 'rock'), 0,
                            np.where((data_pd["self_pick"] == 'scissor') & (data_pd["opp_pick"] == 'paper'), 6, -1)))))))

data_pd["total_score"] = data_pd["pick_score"] + data_pd["outcome_score"]
data_pd["total_score"].sum()
