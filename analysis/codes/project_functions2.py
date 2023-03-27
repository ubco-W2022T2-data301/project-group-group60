import numpy as np
import pandas as pd

def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
          pd.read_csv(url_or_path_to_csv_file))
    return df1
    
    
    
def calculate_bowling_stats(b):
    bo = (b
          .agg({'ID': 'nunique', 'total_run': 'sum', 'ballnumber': 'count', 'isWicketDelivery': 'sum'})
          .rename(columns={'ID': 'Matches', 'total_run': 'Total Runs', 'ballnumber': 'Balls Bowled', 'isWicketDelivery': 'Wickets'})
         )
    return bo

def calculate_bowling_index(bowler_stats):
    bowling_index = (0.6 * (((bowler_stats["wickets_taken"] / bowler_stats["overs_bowled"]) / bowler_stats["Economy Rate"]) * 100) - (0.005 * bowler_stats["extras_given"])) *      (bowler_stats["overs_bowled"] ** 0.1)
    return bowling_index


def calculate_bowling_index1(bowler_stats):
    bowling_index = (0.2 * (((bowler_stats["Wickets"] / bowler_stats["Overs"]) / bowler_stats["Economy Rate"]) * 100)  * (bowler_stats["Overs"] ** 0.1))
    return bowling_index


