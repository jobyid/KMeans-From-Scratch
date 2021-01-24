import pandas as pd
import numpy as np

def prep_file(file):
    if file[-3:] != 'csv':
        raise Exception("File must be a .csv file")
    df = pd.read_csv(file)
    X = df.values
    return X

prep_file('cars_test.csv')
