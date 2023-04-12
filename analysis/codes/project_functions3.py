import numpy as np
import pandas as pd

def load_and_process(url_or_path_to_csv_file):
    df1 = (
          pd.read_csv(url_or_path_to_csv_file)
      )
    return df1 


def find_unique_wicketkeepers(df):
    df1 = (
            (df.loc[:, ['ID', 'kind', 'fielders_involved']]
             [(df['kind'] == 'stumped')])
            ['fielders_involved'].unique()
    )
    return df1

def find_wicketkeeper_stats(bb_df, us):
    final_wicketkeeping = (
        bb_df.loc[:, ['ID', 'kind', 'fielders_involved']]
        .query("fielders_involved in @us")
        .assign(
            Catches=lambda x: x['kind'].eq('caught').astype(int),
            Stumpings=lambda x: x['kind'].eq('stumped').astype(int)
            )
        .groupby('fielders_involved')
        .agg(
            Catches=('Catches', 'sum'),
            Stumpings=('Stumpings', 'sum'),
            Innings=('ID', 'nunique')
            )
        .assign(
            Dismissals=lambda x: x['Catches'] + x['Stumpings'],
            Dis_Inn=lambda x: x['Dismissals'] / x['Innings']
            )
        .rename(columns={'Catches': 'Catches', 'Stumpings': 'Stumpings', 'Innings': 'Innings', 'Dis_Inn': 'Dis/Inn'})
        .sort_values('Dis/Inn', ascending=False)
        .round(2)
    )
    
    return final_wicketkeeping


def find_and_merge_batting_stats_of_keepers(fws):
    btsmn = pd.read_csv('../data/processed/Ishaan/batsman_stats.csv')
    kps = fws.index.tolist()
    
    
    btsmn = btsmn[ btsmn['batter'].isin(kps)]
    fws = fws.reset_index().sort_values(by = 'fielders_involved')
    
    btsmn= (
            btsmn.reset_index()
            .sort_values(by = 'batter')
            .rename(columns={'batter':'fielders_involved'})
        )
    
    keeper_batsmen = (
            pd.merge(fws, btsmn, on='fielders_involved', how='left')
            .drop(columns=['index','Matches','Total Runs','Balls Faced', 'Wickets'])
            .dropna()
            .round(2)
            .rename(columns={'Runs scored per wicket':'Runs Per Wicket'})
        )
        
    return keeper_batsmen

def find_allrounder_stats():
    btsmn = pd.read_csv('../data/processed/Ishaan/batsman_stats.csv')
    bwlr = pd.read_csv('../data/processed/bowlerstatssparsh.csv')

    allr = (bwlr[bwlr['bowler'].isin(btsmn['batter'].unique().tolist())]
        .merge(btsmn.rename(columns={'batter': 'bowler'}), on='bowler', how='left')
        .assign(Runs_Given_per_Wicket=lambda x: x['total_run'] / x['wickets_taken'],
                Runs_Given=lambda x: x['total_run'],
                Wickets_Taken=lambda x: x['wickets_taken'],
                Runs_Scored=lambda x: x['Total Runs'])
        .round(2)
        .drop(columns=['Wickets', 'Balls Faced', 'overs_bowled', 'balls_bowled', 'extras_given', 'total_run', 'wickets_taken'])
    )
    
    #df.to_csv("../data/processed/allRounder_stats1.csv")
    return allr










