import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
import squarify

from matplotlib.colors import LinearSegmentedColormap

# **************************************************************************************************************
# Function  name: categorize_interest_rate
# input:
# return value:
# ***************************************************************************************************************
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



# **************************************************************************************************************
# Function  name: creating_the_dataframe_correlation_for_each_region
# input:
# return value:
# ***************************************************************************************************************
def creating_the_dataframe_correlation_for_each_region(Region_selected_df):
    max_int_rate = Region_selected_df['int_rate'].max()
    min_int_rate = Region_selected_df['int_rate'].min()
    unique_purpose = pd.unique(Region_selected_df['purpose'])

    purpose_his = Region_selected_df['purpose'].value_counts()
    print("*")
    # Changing the format of 'int_rate' column
    Region_selected_df['int_rate'] *= 100
    # Define the labels for the bins
    interest_rate_list = ['0% - 4%', '4% - 8%', '8% - 12%', '12% - 16%', '16% - 20%', '20% - 24%', '24% - 28%']

    # Apply the custom function to categorize interest rates into groups
    Region_selected_df['interest_rate_groups'] = Region_selected_df['int_rate'].apply(categorize_interest_rate)

    Region_selected_df
    print('*')


    return

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

    region_dict = {
        'West': ['AK', 'CA', 'CO', 'HI', 'ID', 'MT', 'NV', 'OR', 'UT', 'WA', 'WY'],
        'Southwest': ['AZ', 'NM', 'OK', 'TX'],
        'Midwest': ['IA', 'IL', 'IN', 'KS', 'MI', 'MN', 'MO', 'ND', 'NE', 'OH', 'SD', 'WI'],
        'Southeast': ['AL', 'AR', 'FL', 'GA', 'KY', 'LA', 'MS', 'NC', 'SC', 'TN', 'VA', 'WV'],
        'Northeast': ['CT', 'DC', 'DE', 'MA', 'MD', 'ME', 'NH', 'NJ', 'NY', 'PA', 'RI', 'VT'],
    }
    # Create a new column to classify states into regions based on the dictionary
    df['Region'] = df['address_state'].map({state: region for region, states in region_dict.items() for state in states}).fillna('Other')  # TODO: ask

    Regions = ['West', 'Southwest', 'Mideast', 'Southeast', 'Northeast']

    #Specific_region =[]


    for Region_selected in Regions:
        Region_selected_df = df.loc[df['Region'] == Region_selected, :]
        res = creating_the_dataframe_correlation_for_each_region(Region_selected_df)






