import numpy as np
import pandas as pd

def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
          pd.read_csv(url_or_path_to_csv_file))
    return df1
    
    
    
def calculate_bowling_stats(b):
    bo = (b.groupby('bowler')
          .apply(lambda x: pd.Series({
              'Matches': x['ID'].nunique(),
              'Total Runs': x['total_run'].sum(),
              'Balls Bowled': x['ballnumber'].count(),
              'Wickets': x['isWicketDelivery'].sum()
          }))
          .reset_index()
          .rename(columns={'bowler': 'Bowler'})
         )
    return bo

def calculate_death_stats(b):
    b = b[b['overs'] >14]
    bo = (b.groupby('bowler')
          .apply(lambda x: pd.Series({
              'Matches': x['ID'].nunique(),
              'Total Runs': x['total_run'].sum(),
              'Balls Bowled': x['ballnumber'].count(),
              'Wickets': x['isWicketDelivery'].sum()
          }))
          .reset_index()
          .rename(columns={'bowler': 'Bowler'})
         )
    return bo

def calculate_playoff_stats(new_ball, new_matches):
    id_list = new_matches['ID'].tolist()
    df3 = new_ball[new_ball['ID'].isin(id_list)]
    bo = (df3.groupby('bowler')
          .apply(lambda x: pd.Series({
              'Matches': x['ID'].nunique(),
              'Total Runs': x['total_run'].sum(),
              'Balls Bowled': x['ballnumber'].count(),
              'Wickets': x['isWicketDelivery'].sum()
          }))
          .reset_index()
          .rename(columns={'bowler': 'Bowler'})
         )
    return bo



def calculate_bowling_index(bowler_stats):
    bowling_index = 0.6 * ((((100-(bowler_stats["total_run"] / bowler_stats["wickets_taken"])) - bowler_stats["Economy Rate"]) ) *      (bowler_stats["overs_bowled"] ** 0.09))
    return bowling_index


def calculate_bowling_index1(bowler_stats):
    bowling_index = 0.2 * ((((100-(bowler_stats["Total Runs"] / bowler_stats["Wickets"])) - bowler_stats["Economy Rate"]) ) *      (bowler_stats["Overs"] ** 0.09))
    return bowling_index


