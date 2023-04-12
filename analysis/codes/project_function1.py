import numpy as np
import pandas as pd

def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
          pd.read_csv(url_or_path_to_csv_file))
    return df1
    
    
    

def get_batsman_stats(df3):
    batsman_group = df3.groupby('batter')
    batsman_stats = (batsman_group
                     .apply(lambda x: pd.DataFrame({'Matches': x['ID'].nunique(),
                                                    'Total Runs': x['batsman_run'].sum(),
                                                    'Balls Faced': x['ballnumber'].count(),
                                                    'Wickets': x['isWicketDelivery'].sum()}, index=[x.name]))
                     .reset_index(level=1, drop=True)
                     .rename(columns={'Matches': 'Matches',
                                      'Total Runs': 'Total Runs',
                                      'Balls Faced': 'Balls Faced',
                                      'Wickets': 'Wickets'}))
    
    return batsman_stats

def get_chasing_stats(df3):
    df3 = df3[df3['innings'] > 1]
    batsman_group = df3.groupby('batter')
    batsman_stats = (batsman_group
                     .apply(lambda x: pd.DataFrame({'Matches': x['ID'].nunique(),
                                                    'Total Runs': x['batsman_run'].sum(),
                                                    'Balls Faced': x['ballnumber'].count(),
                                                    'Wickets': x['isWicketDelivery'].sum()}, index=[x.name]))
                     .reset_index(level=1, drop=True)
                     .rename(columns={'Matches': 'Matches',
                                      'Total Runs': 'Total Runs',
                                      'Balls Faced': 'Balls Faced',
                                      'Wickets': 'Wickets'}))
    
    return batsman_stats

def get_death_stats(df3):
    df3 = df3[df3['overs'] > 14]
    batsman_group = df3.groupby('batter')
    batsman_stats = (batsman_group
                     .apply(lambda x: pd.DataFrame({'Matches': x['ID'].nunique(),
                                                    'Total Runs': x['batsman_run'].sum(),
                                                    'Balls Faced': x['ballnumber'].count(),
                                                    'Wickets': x['isWicketDelivery'].sum()}, index=[x.name]))
                     .reset_index(level=1, drop=True)
                     .rename(columns={'Matches': 'Matches',
                                      'Total Runs': 'Total Runs',
                                      'Balls Faced': 'Balls Faced',
                                      'Wickets': 'Wickets'}))
    
    return batsman_stats






def calculate_batsman_score(batsman_stats):
    score = (batsman_stats['Total Runs'] - batsman_stats['Balls Faced']) / \
            batsman_stats['Wickets'] * (batsman_stats['Matches'] ** (1/6)) * \
            (batsman_stats['Total Runs'] ** (1/6))
    return np.round(score, 2)
