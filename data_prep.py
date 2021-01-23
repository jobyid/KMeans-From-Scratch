import pandas as pd
import numpy as np

def prep_file(file):
    df = pd.read_csv(file)
    X = df.values
    return X


