import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import squarify    # You need to install this library using pip: pip install squarify
import seaborn as sns
import matplotlib.ticker as mtick

#import dataframe_image as dfi
import matplotlib.pyplot as plt


## Source: https://www.kaggle.com/datasets/nezukokamaado/auto-loan-dataset?select=financial_loan.csv

# **************************************************************************************************************
# Function  name: creating_the_data
# input:
# return value:
# ***************************************************************************************************************
def creating_the_data(his_region):
    list_of_regions = []
    list_of_avg_annual_income_per_region = []
    list_of_number_loans_per_region = []


    groups_by_region = df.groupby('Region')
    for region_name, mini_df_per_region in groups_by_region:
        # print("The state name is: ", state_name)
        # print(mini_df_per_state)
        avg_income_per_region = mini_df_per_region['annual_income'].mean().round(1)  # Midwest = 64,359.45 . Northeast = 72,319 , southeast = 67,252 , southwest = 72,438 , west = 70488
        counting_the_number_of_laons = mini_df_per_region.shape[0]
        print('*')

        list_of_regions.append(region_name)
        list_of_avg_annual_income_per_region.append(avg_income_per_region)
        list_of_number_loans_per_region.append(counting_the_number_of_laons)

    df_starting = {'Region': list_of_regions,
                   'Avg_annual_income': list_of_avg_annual_income_per_region,
                   'Number_of_loans_taken': list_of_number_loans_per_region}

    final_table = pd.DataFrame(df_starting,
                               columns=['Region', 'Avg_annual_income', 'Number_of_loans_taken'])
    print('*')
    return final_table

# **************************************************************************************************************
# Function  name: creating_the_data
# input:
# return value:
# ***************************************************************************************************************


def creating_the_column_chart(final_table):

    # Data
    regions = list(final_table.loc[:,"Region"])#['Northeast', 'West', 'Southeast', 'Midwest', 'Southwest']
    num_loans = list(final_table.loc[:,"Number_of_loans_taken"]) #[10810, 10051, 8348, 5399, 3973]
    avg_income = list(final_table.loc[:,"Avg_annual_income"]) #[72319, 70488, 67252, 64359, 67252]

    # Set the width of the bars
    bar_width = 0.40
    fig = plt.figure(figsize=(10, 3.5), facecolor='#f6f5f5')
    ax = fig.add_subplot(111)
    # Set the x locations for the groups
    r1 = np.arange(len(regions))
    r2 = r1 + bar_width
    # Plotting the grouped bars
    bars1 = ax.bar(r1, num_loans, color='#989898', width=bar_width, edgecolor='grey', label='Number of Loans')
    bars2 = ax.bar(r2, avg_income, color='orange', width=bar_width, edgecolor='grey', label='Average Income',
                   hatch='xx')
    # Adding annotations
    for i, (loan, income) in enumerate(zip(num_loans, avg_income)):
        plt.text(i, loan + 100, str(loan), ha='center', va='bottom', fontweight='bold', fontfamily='serif')
        plt.text(i + bar_width, income + 100, str(income), ha='center', va='bottom', fontweight='bold',
                 fontfamily='serif')
    # Adding labels and title
    ax.set_xlabel('Region', fontweight='bold', fontfamily='serif')
    ax.set_ylabel('Counts', fontweight='bold', fontfamily='serif')
    # ax.set_title('Is there any correlation between the average income in each region and the number of loans taken?', fontweight='bold', fontfamily='serif')
    ax.text(-0.4, 97000,
            'Average Income vs. Number of Loans',
            fontsize=17.5,
            fontweight='bold',
            fontfamily='serif')
    ax.text(-0.4, 81500,
            'Is there any correlation between the average income in each region and the number of \nloans taken?',
            fontsize=11.5,
            fontweight='bold',
            fontfamily='serif',
            color="#4b4b4c")
    ax.set_xticks(np.arange(len(regions)) + bar_width / 2)
    ax.set_xticklabels(regions)
    # Removing spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    # Removing y-axis ticks and labels
    ax.tick_params(left=False)
    ax.set_yticklabels([])
    # Adding legend at the bottom
    ax.legend(loc='lower center', ncol=2, bbox_to_anchor=(0.5, -0.3))
    plt.savefig('avg_income_1.jpg', dpi=250, bbox_inches='tight')
    # Show plot
    plt.show()


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

    res =creating_the_data(his_region)
    creating_the_column_chart(res)