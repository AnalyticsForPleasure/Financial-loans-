import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import squarify    # You need to install this library using pip: pip install squarify
import seaborn as sns
import matplotlib.ticker as mtick

#import dataframe_image as dfi
import matplotlib.pyplot as plt


## Source: https://www.kaggle.com/datasets/nezukokamaado/auto-loan-dataset?select=financial_loan.csv



if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('/home/shay_diy/PycharmProjects/Financial_loans/Data/financial_loan.csv')
    print('*')

    # Prepering the data :

    ## Step 1: adding the full name to the country

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

    # Step 2 : Dividing the countries to regions
    region_dict = {
        'West': ['AK', 'CA', 'CO', 'HI', 'ID', 'MT', 'NV', 'OR', 'UT', 'WA', 'WY'],
        'Southwest': ['AZ', 'NM', 'OK', 'TX'],
        'Midwest': ['IA', 'IL', 'IN', 'KS', 'MI', 'MN', 'MO', 'ND', 'NE', 'OH', 'SD', 'WI'],
        'Southeast': ['AL', 'AR', 'FL', 'GA', 'KY', 'LA', 'MS', 'NC', 'SC', 'TN', 'VA', 'WV'],
        'Northeast': ['CT', 'DC', 'DE', 'MA', 'MD', 'ME', 'NH', 'NJ', 'NY', 'PA', 'RI', 'VT'],
    }
    # Create a new column to classify states into regions based on the dictionary
    df['Region'] = df['address_state'].map(
        {state: region for region, states in region_dict.items() for state in states}).fillna('Other')  # TODO: ask
    his_region = df['Region'].value_counts().reset_index()

    groups_by_region = df.groupby('Region')
    for region_name, mini_df_per_region in groups_by_region:
        # print("The state name is: ", state_name)
        # print(mini_df_per_state)
        avg_income_per_region= mini_df_per_region['annual_income'].mean()  # Midwest = 64,359.45 . Northeast = 72,319 , southeast = 67,252 , southwest = 72,438 , west = 70488
        print('*')

