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
    df = bb_df
    df = df.loc[:, ['ID', 'kind', 'fielders_involved']]
    keeper_stats = df[(df['fielders_involved'].isin(us))]
    ks = keeper_stats

    temp = ks[ks['kind'] == 'caught']
    final_wicketkeeping =  ks.groupby(temp["fielders_involved"])[["kind"]].count()

    temp = ks[ks['kind'] == 'stumped']
    df2 =  ks.groupby(temp["fielders_involved"])[["kind"]].count()

    df3 = pd.DataFrame(ks.groupby('fielders_involved')['ID'].nunique())
    final_wicketkeeping['Stumpings'] = df2['kind']
    final_wicketkeeping['Innings'] = df3['ID']
    final_wicketkeeping = final_wicketkeeping.rename(columns={'kind': 'Catches'})
    
    
    final_wicketkeeping['Dismissals'] = (final_wicketkeeping['Catches'] + final_wicketkeeping['Stumpings'])
    final_wicketkeeping['Dis/Inn'] = (final_wicketkeeping['Dismissals'])/final_wicketkeeping['Innings']
    final_wicketkeeping= final_wicketkeeping.sort_values('Dis/Inn', ascending=False)
    final_wicketkeeping = final_wicketkeeping.round(2)
    
    return final_wicketkeeping


def find_and_merge_batting_stats_of_keepers(fws):
    kps = fws.index.tolist()
    btsmn = pd.read_csv('../data/processed/Ishaan/batsman_stats.csv')
    btsmn = btsmn[ btsmn['batter'].isin(kps)]
    fws = fws.reset_index().sort_values(by = 'fielders_involved')
    btsmn= btsmn.reset_index().sort_values(by = 'batter').rename(columns={'batter':'fielders_involved'})
    keeper_batsmen = pd.merge(fws, btsmn, on='fielders_involved', how='left').drop(columns=['index','Matches','Total Runs','Balls Faced', 'Wickets']).dropna().round(2).rename(columns={'Runs scored per wicket':'Runs Per Wicket'})
    return keeper_batsmen

def find_allrounder_stats():
    btsmn = pd.read_csv('../data/processed/Ishaan/batsman_stats.csv')
    x = btsmn['batter'].unique().tolist()
    bwlr = pd.read_csv('../data/processed/bowlerstatssparsh.csv')
    bwlr = bwlr[ bwlr['bowler'].isin(x)]
    btsmn= btsmn.rename(columns={'batter':'bowler'})
    allr = pd.merge(bwlr, btsmn, on='bowler', how='left').round(2)
   # allr = all.drop(columns=['index','Matches','Total Runs','Balls Faced', 'Wickets'])
    #allr.to_csv("../data/processed/allRounder_stats.csv")
    df = allr
    df['Runs Given per Wicket'] = df['total_run']/df['wickets_taken']
    df = df.drop(columns=['Wickets', 'Balls Faced', 'overs_bowled', 'balls_bowled', 'extras_given']).rename(columns={'total_run' : 'Runs Given', 'wickets_taken' : 'Wickets Taken', 'Total Runs' : 'Runs Scored'}).round(2)
    #df.to_csv("../data/processed/allRounder_stats1.csv")
    return df










