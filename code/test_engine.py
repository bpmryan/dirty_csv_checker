import io
import pandas as pd
from clean_engine import clean_user_data

# Test Case 1: Evaluates normal data (forces Python to run lines 8-12)
def test_clean_user_data_filtering():
    raw_csv = "name,age,email\nAlice,24,alice@okc.edu\nBob,-12,bad_mail\nCharlie,150,charlie@acm.org"
    df = pd.read_csv(io.StringIO(raw_csv))
    
    clean_df, dirty_df = clean_user_data(df)
    
    assert len(clean_df) == 1
    assert len(dirty_df) == 2
    assert clean_df.iloc[0]['name'] == 'Alice'

# Test Case 2: Evaluates a completely blank data frame (forces Python to run line 6)
def test_clean_user_data_handles_empty_dataframe():
    empty_df = pd.DataFrame(columns=['name', 'age', 'email'])
    
    clean_df, dirty_df = clean_user_data(empty_df)
    
    assert clean_df.empty
    assert dirty_df.empty