import pandas as pd
import numpy as np

def load_and_clean_data():
    df = pd.read_parquet("DDoS-Friday-no-metadata.parquet")

    # Convert label
    df['Label'] = df['Label'].apply(lambda x: 0 if x == 'Benign' else 1)

    # Remove bad values
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.dropna(inplace=True)

    # Separate
    y = df['Label'].astype(int)
    X = df.drop(columns=['Label'])

    # Keep only numeric
    X = X.select_dtypes(include=[np.number])

    # Combine again
    df_clean = X.copy()
    df_clean['Label'] = y.loc[X.index]

    print("Data cleaned:", df_clean.shape)

    return df_clean