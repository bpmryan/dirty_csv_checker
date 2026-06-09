import pandas as pd


def clean_user_data(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Filters a dataframe based on strict schema requirements.
    Invariants: 'age' must be within [0, 120], and 'email' must contain '@'.
    """
    if df.empty:
        return pd.DataFrame(columns=df.columns), pd.DataFrame(columns=df.columns)

    valid_age = df["age"].between(0, 120)
    valid_email = df["email"].str.contains("@", na=False)

    clean_mask = valid_age & valid_email
    return df[clean_mask], df[~clean_mask]
