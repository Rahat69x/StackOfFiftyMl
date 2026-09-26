"""
Feature engineering definitions for Emotional Text-To-Speech Synthesis (ML039).
"""
import pandas as pd
import numpy as np

def extract_features(df: pd.DataFrame) -> pd.DataFrame:
    df_feat = df.copy()
    num_cols = df_feat.select_dtypes(include=[np.number]).columns
    if len(num_cols) >= 2:
        df_feat["feat_interaction"] = df_feat[num_cols[0]] * df_feat[num_cols[1]]
    return df_feat
