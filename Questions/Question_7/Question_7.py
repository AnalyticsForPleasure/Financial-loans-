import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def creating_a_sub_grade_table(table_specific_region,specific_region):
    list_of_grade_df = []
    list_of_sub_grade_df =[]
    list_of_number_of_loans_in_the_same_level= []



    ##  Second Path :
    groups_by_state = table_specific_region.groupby('sub_grade')
    for sub_grade_name, sub_grade_df in groups_by_state:
        # print("The state name is: ", sub_grade_name)
        # print(sub_grade_df)
        Number_of_loans_in_the_same_level = sub_grade_df.shape[0]

        list_of_grade_df
        list_of_sub_grade_df.append(sub_grade_name)
        list_of_number_of_loans_in_the_same_level.append(Number_of_loans_in_the_same_level)


        df_starting = {'Region_name': specific_region,
                           'Sub_grade': list_of_sub_grade_df,
                           'Counting_the_loans_within_a_Sub_grade': list_of_number_of_loans_in_the_same_level}

    final_table = pd.DataFrame(df_starting,
                                       columns=['Region_name', 'Sub_grade', 'Counting_the_loans_within_a_Sub_grade'])



    print('*')



    return final_table



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
    df['Region'] = df['address_state'].map(
        {state: region for region, states in region_dict.items() for state in states}).fillna('Other')  # TODO: ask

    Regions = ['West', 'Southwest', 'Mideast', 'Southeast', 'Northeast']

    for specific_region in Regions :
        table_specific_region = df.loc[df['Region'] == specific_region,:]
        res = creating_a_sub_grade_table(table_specific_region,specific_region)
    print('*')

