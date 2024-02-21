import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import squarify    # You need to install this library using pip: pip install squarify
import seaborn as sns

#import dataframe_image as dfi
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap #


## Source: https://www.kaggle.com/datasets/nezukokamaado/auto-loan-dataset?select=financial_loan.csv

if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('/home/shay_diy/PycharmProjects/Financial_loans/Data/financial_loan.csv')
    print('*')

    my_lookup = {'AK': 'Alaska',
                'AL':'Alabama',
                'AR':'Arkansas',
                'AZ':'Arizona',
                'CA':'California',
                'CO':'Colorado',
                'CT':'Connecticut',
                'DC':'District of Columbia',
                'DE':'Delaware',
                'FL':'Florida',
                'GA':'Georgia',
                'HI':'Hawaii',
                'IA':'Iowa',
                'ID':'Idaho',
                'IL':'Illinois',
                'IN':'Indiana',
                'KS':'Kansas',
                'KY':'Kentucky',
                'LA':'Louisiana',
                'MA':'Massachusetts',
                'MD':'Maryland',
                'ME':'Maine',
                'MI':'Michigan',
                'MN':'Minnesota',
                'MO':'Missouri',
                'MS':'Mississippi',
                'MT':'Montana',
                'NC':'North Carolina',
                'NE':'Nebraska',
                'NH':'New Hampshire',
                'NJ':'New Jersey',
                'NM':'New Mexico',
                'NV':'Nevada',
                'NY':'New York',
                'OH':'Ohio',
                'OK':'Oklahoma',
                'OR':'Oregon',
                'PA':'Pennsylvania',
                'RI':'Rhode Island',
                'SC':'South Carolina',
                'SD':'South Dakota',
                'TN':'Tennessee',
                'TX':'Texas',
                'UT':'Utah',
                'VA':'Virginia',
                'VT':'Vermont',
                'WA':'Washington',
                'WI':'Wisconsin',
                'WV':'West Virginia',
                'WY':'Wyoming',
                }

    df['full_name'] = df['address_state'].apply(lambda x: my_lookup[x])
    print('*')

    precentage_for_each_region = []
    region_dict = {
        'West': ['AK', 'CA', 'CO', 'HI', 'ID', 'MT', 'NV', 'OR', 'UT', 'WA', 'WY'],
        'Southwest': ['AZ', 'NM', 'OK', 'TX'],
        'Midwest': ['IA', 'IL', 'IN', 'KS', 'MI', 'MN', 'MO', 'ND', 'NE', 'OH', 'SD', 'WI'],
        'Southeast': ['AL', 'AR', 'FL', 'GA', 'KY', 'LA', 'MS', 'NC', 'SC', 'TN', 'VA', 'WV'],
        'Northeast': ['CT', 'DC', 'DE', 'MA', 'MD', 'ME', 'NH', 'NJ', 'NY', 'PA', 'RI', 'VT'],
    }

    # Create a new column to classify states into regions based on the dictionary
    df['Region'] = df['address_state'].map({state: region for region, states in region_dict.items() for state in states}).fillna('Other') # TODO: ask

    his_region =df['Region'].value_counts().reset_index()
    total_sum = his_region['count'].sum()

    #his_region = his_region.rename(index={1: 'Count of loans issued in each geographic region'})

    for index in range(len(his_region)):
        his_region.loc[index, 'Percentage'] = his_region.loc[index, 'count'] / total_sum * 100

    #his_region['Percentage'] = his_region['Percentage'].apply(lambda r: "{x:.1f}%".format(x=r))
    his_region['Cumulative Percentage'] = his_region['Percentage'].cumsum()
    his_region['Cumulative Percentage'] = his_region['Cumulative Percentage'].clip(upper=100)


    his_region['Percentage'] = his_region['Percentage'].apply(lambda r: "{x:.1f}%".format(x=r))
    his_region['Cumulative Percentage'] = his_region['Cumulative Percentage'].apply(lambda r: "{x:.1f}%".format(x=r))
    print('*')

    # ***************************************************************************************************************
