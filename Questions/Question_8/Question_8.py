import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
import squarify

from matplotlib.colors import LinearSegmentedColormap





if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('/home/shay_diy/PycharmProjects/Financial_loans/Data/financial_loan.csv')

    print('*')

    max_int_rate = df['int_rate'].max()
    min_int_rate = df['int_rate'].min()

    unique_purpose =  pd.unique(df['purpose'])
    purpose_his = df['purpose'].value_counts()
    print("*")

    # Changing the format of 'int_rate' column
    df['int_rate'] *= 100

    # Define the labels for the bins
    interest_rate_list = ['0% - 4%', '4% - 8%', '8% - 12%', '12% - 16%', '16% - 20%', '20% - 24%', '24% - 28%']


    # Define a custom function to categorize interest rates into groups
    def categorize_interest_rate(rate):
        if rate < 4:
            return '0% - 4%'
        elif 4 <= rate < 8:
            return '4% - 8%'
        elif 8 <= rate < 12:
            return '8% - 12%'
        elif 12 <= rate < 16:
            return '12% - 16%'
        elif 16 <= rate < 20:
            return '16% - 20%'
        elif 20 <= rate < 24:
            return '20% - 24%'
        elif 24 <= rate <= 28:
            return '24% - 28%'
        else:
            return 'Other'


    # Apply the custom function to categorize interest rates into groups
    df['interest_rate_groups'] = df['int_rate'].apply(categorize_interest_rate)
    print('*')



