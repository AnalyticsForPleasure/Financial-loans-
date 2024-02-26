import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import squarify    # You need to install this library using pip: pip install squarify
import seaborn as sns
import matplotlib.ticker as mtick

#import dataframe_image as dfi
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap #

## Source: https://www.kaggle.com/datasets/nezukokamaado/auto-loan-dataset?select=financial_loan.csv

# **************************************************************************************************************
# Function  name: creating_a_cumulative_percentage_table
# input: 
# return value: 
# ***************************************************************************************************************
def creating_a_cumulative_percentage_table(df):
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
    total_sum = his_region['count'].sum()
    for index in range(len(his_region)):
        his_region.loc[index, 'Percentage'] = his_region.loc[index, 'count'] / total_sum * 100
    his_region['Cumulative Percentage'] = his_region['Percentage'].cumsum()
    his_region['Cumulative Percentage'] = his_region['Cumulative Percentage'].clip(upper=100)
    
    #his_region['Percentage'] = his_region['Percentage'].apply(lambda r: "{x:.4f}".format(x=r)) # {x:.1f}%
    his_region['Percentage'] = his_region['Percentage'].apply(lambda r: "{:.4f}".format(float(r)))# {x:.1f}%

    his_region['Cumulative Percentage'] = his_region['Cumulative Percentage'].apply(lambda r: "{x:.1f}%".format(x=r))

    his_region= his_region.T
    #his_region.reset_index()
    print('*')

    # Move the first row to column headers
    his_region.columns = his_region.iloc[0]

    # Interested in retrieving only the percentage "row"
    his_region = his_region[2:3].astype(float) # In addition I add the astype(float) - Super important here!

    print('*')
    return his_region

# **************************************************************************************************************
# Function  name: creating_a_rectangle_layers_chart
# input:
# return value:
# ***************************************************************************************************************
def creating_a_rectangle_layers_chart(cumulative_percentage_table):
    # Setting up figure and axes
    fig = plt.figure(figsize=(10, 16))  # create figure
    gs = fig.add_gridspec(3, 2)
    gs.update(wspace=0, hspace=0.8)
    ax0 = fig.add_subplot(gs[0, 0:2])


    # Color selection
    color_map = ["#bdbdbd" for _ in range(5)]
    color_map[0] ="#FFA500"

    # Change background color
    background_color = "#fbfbfb"
    fig.patch.set_facecolor(background_color)  # figure background color
    ax0.set_facecolor(background_color)  # axes background color
    print('*')

    # Plotting
    ax0.barh(cumulative_percentage_table.index, cumulative_percentage_table['Northeast'],
             color="#FFA500", zorder=3, label="Northeast") # ,hatch='.O'
    ax0.barh(cumulative_percentage_table.index, cumulative_percentage_table['West'],
             left=cumulative_percentage_table['Northeast'],
             color="#4b4b4c", zorder=3, label="West") # ,hatch='xx'
    ax0.barh(cumulative_percentage_table.index, cumulative_percentage_table['Southeast'],
             left=cumulative_percentage_table['West'] + cumulative_percentage_table['Northeast'],
             color="#676767", zorder=3, label="Southeast") #,hatch='.'
    ax0.barh(cumulative_percentage_table.index, cumulative_percentage_table['Midwest'],
             left=cumulative_percentage_table['Southeast'] + cumulative_percentage_table['West'] +
                  cumulative_percentage_table['Northeast'],
             color="#808080", zorder=3, label="Midwest")
    ax0.barh(cumulative_percentage_table.index, cumulative_percentage_table['Southwest'],
             left=cumulative_percentage_table['Midwest'] + cumulative_percentage_table['Southeast'] +
                  cumulative_percentage_table['West'] + cumulative_percentage_table['Northeast'],
             color="#989898", zorder=3, label="Southwest") #,hatch='..'

    # Formatting
    for s in ["top", "right", "left"]:
        ax0.spines[s].set_visible(False)
    ax0.xaxis.set_major_formatter(mtick.PercentFormatter())
    ax0.legend(loc='lower center', ncol=5, bbox_to_anchor=(0.48, -0.3))
    ax0.text(0, 0.8,
             'Which region sees the highest loan uptake by US citizens?',
             fontsize=21,
             fontweight='bold',
             fontfamily='serif')
    ax0.text(0, 0.67,
             'Top 3 loan takers:  Northheast = 10,810 | West = 10,051 | Southeast = 8,343',
             fontsize=15,
             fontweight='light',
             fontfamily='serif')
    ax0.text(0, 0.45,
             'Comprehensive Loan Information for Credit Risk',
             fontsize=13,
             fontweight='light',
             fontfamily='serif')
    plt.savefig('highest_loan_by_region.jpg', dpi=250, bbox_inches='tight')
    plt.show()


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

    res = creating_a_cumulative_percentage_table(df)
    creating_a_rectangle_layers_chart(res)
    print('*')
