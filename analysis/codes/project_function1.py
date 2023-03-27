import numpy as np
import pandas as pd

def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
          pd.read_csv(url_or_path_to_csv_file))
    return df1
    
    
    

def get_batsman_stats(batsman_group):
    
    batsman_stats = (batsman_group
                     .agg(matches=('ID', 'nunique'),
                          total_runs=('batsman_run', 'sum'),
                          balls_faced=('ballnumber', 'count'),
                          wickets=('isWicketDelivery', 'sum')))
    

    batsman_stats = batsman_stats.rename(columns={'matches': 'Matches',
                                                  'total_runs': 'Total Runs',
                                                  'balls_faced': 'Balls Faced',
                                                  'wickets': 'Wickets'})
    
    return batsman_stats

def calculate_batsman_score(batsman_stats):
    score = (batsman_stats['Total Runs'] - batsman_stats['Balls Faced']) / \
            batsman_stats['Wickets'] * (batsman_stats['Matches'] ** (1/6)) * \
            (batsman_stats['Total Runs'] ** (1/6))
    return np.round(score, 2)