import numpy as np
import pandas as pd

def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
          pd.read_csv(url_or_path_to_csv_file)
          .dropna()
      )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    df2 = (
          df1
          .assign(...)
      )

    # Make sure to return the latest dataframe

    return df2 


def find_unique_wicketkeepers(df):
    df1 = (
            (df.loc[:, ['ID', 'kind', 'fielders_involved']]
             [(df['kind'] == 'stumped')])
            ['fielders_involved'].unique()
    )
    
#df = ball_by_ball
#df = df.loc[:, ['ID', 'kind', 'fielders_involved']]

#stumped = df[(df['kind'] == 'stumped')]
#unique_stumpers = stumped['fielders_involved'].unique()
    return df1