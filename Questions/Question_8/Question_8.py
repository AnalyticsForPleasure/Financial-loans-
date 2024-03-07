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
def creating_the_dataframe_correlation_for_each_region(selected_df):
    Regions = ['West', 'Southwest', 'Midwest', 'Southeast', 'Northeast']




    # max_int_rate = Region_selected_df['int_rate'].max()
    # min_int_rate = Region_selected_df['int_rate'].min()
    # unique_purpose = pd.unique(Region_selected_df['purpose'])

    #purpose_his = Region_selected_df['purpose'].value_counts()
    print("*")
    # Changing the format of 'int_rate' column
    selected_df['int_rate'] *= 100
    # Define the labels for the bins
    interest_rate_list = ['0% - 4%', '4% - 8%', '8% - 12%', '12% - 16%', '16% - 20%', '20% - 24%', '24% - 28%']

    # Apply the custom function to categorize interest rates into groups
    selected_df['Interest Rate on Loans'] = selected_df['int_rate'].apply(categorize_interest_rate)

    three_columns = selected_df.loc[:,['Interest Rate on Loans',"int_rate","purpose", 'Region']]
    print('*')

    # Filtering th X-axis by this closed list
    relevant_reasons_for_taking_loans = ['Debt consolidation', 'home improvement','house', 'major purchase', 'small business','car','wedding','medical'] #'redit card'
    final_table = three_columns[three_columns['purpose'].isin(relevant_reasons_for_taking_loans)]

    #output_result= pd.crosstab(final_table["interest_rate_groups"],final_table["purpose"])

    print('*')


    return final_table




def creating_the_correlation_chart_for_each_region(final_table):

    filtering_West_df = final_table.loc[final_table['Region'] == 'West']
    df_West= pd.crosstab(filtering_West_df["Interest Rate on Loans"],filtering_West_df["purpose"])

    filtering_Southwest_df = final_table.loc[final_table['Region'] == 'Southwest']
    df_Southwest = pd.crosstab(filtering_Southwest_df["Interest Rate on Loans"], filtering_Southwest_df["purpose"])

    filtering_Midwest_df = final_table.loc[final_table['Region'] == 'Midwest']
    df_Midwest = pd.crosstab(filtering_Midwest_df["Interest Rate on Loans"], filtering_Midwest_df["purpose"])

    filtering_Southeast_df = final_table.loc[final_table['Region'] == 'Southeast']
    df_Southeast = pd.crosstab(filtering_Southeast_df["Interest Rate on Loans"], filtering_Southeast_df["purpose"])

    filtering_Northeast_df = final_table.loc[final_table['Region'] == 'Northeast']
    df_Northeast = pd.crosstab(filtering_Northeast_df["Interest Rate on Loans"], filtering_Northeast_df["purpose"])

    print('*')



    fig = plt.figure(figsize=(15, 10))  # create figure
    gs = fig.add_gridspec(2, 3)
    gs.update(wspace=0.2, hspace=-0.4)
    # Positioning each plot over the chart
    ax0 = fig.add_subplot(gs[0, 0])
    ax1 = fig.add_subplot(gs[0, 1])
    #ax2 = fig.add_subplot(gs[0, 2])
    ax3 = fig.add_subplot(gs[1, 0])
    ax4 = fig.add_subplot(gs[1, 1])
    ax5 = fig.add_subplot(gs[1, 2])
    background_color = "#fbfbfb"
    fig.patch.set_facecolor(background_color)  # figure background color
    ax0.set_facecolor(background_color)  # axes background color
    ax1.set_facecolor(background_color)  # axes background color
    #ax2.set_facecolor(background_color)  # axes background color
    ax3.set_facecolor(background_color)  # axes background color
    ax4.set_facecolor(background_color)  # axes background color
    ax5.set_facecolor(background_color)  # axes background color
    # colors = [ "#4b4b4c", "#FFA500"]
    #
    # # Reverse the order of colors
    # #colors.reverse()
    #
    # # Create a colormap using LinearSegmentedColormap
    # cmap = LinearSegmentedColormap.from_list('OrangeToGray', colors)
    #
    # # Generate 5 distinct colors from the colormap
    # distinct_colors = [cmap(i) for i in np.linspace(0, 1, 50)]
    # print('*')

    colors = ["#fbfbfb", "#4b4b4c","#FFA500"]
    colormap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)

    # Print the generated distinct colors
    print(colormap)

    #colormap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)
    sns.heatmap(ax=ax0,
                data=df_West,
                linewidths=.2,
                square=True,
                cbar_kws={"orientation": "horizontal"},
                cbar=False,
                annot=True,  # Add annotations (numbers) over the cells
                cmap=colormap,
                fmt='.4g',
                annot_kws={"fontsize": 8,"fontweight": "bold"})
    sns.heatmap(ax=ax1,
                data=df_Southwest,
                linewidths=.1,
                square=True,
                cbar_kws={"orientation": "horizontal"},
                cbar=False,
                annot=True,  # Add annotations (numbers) over the cells
                cmap=colormap,
                fmt='.4g',
                annot_kws={"fontsize": 8,"fontweight": "bold"})
    sns.heatmap(ax=ax5,
                data=df_Midwest,
                linewidths=.1,
                square=True,
                cbar_kws={"orientation": "horizontal"},
                cbar=False,
                annot=True,  # Add annotations (numbers) over the cells
                cmap=colormap,
                fmt='.4g',
                annot_kws={"fontsize": 8,"fontweight": "bold"})
    sns.heatmap(ax=ax3,
                data=df_Northeast,
                linewidths=.1,
                square=True,
                cbar_kws={"orientation": "horizontal"},
                cbar=False,
                annot=True,  # Add annotations (numbers) over the cells
                cmap=colormap,
                fmt='.4g',
                annot_kws={"fontsize": 8,"fontweight": "bold"})
    sns.heatmap(ax=ax4,
                data=df_Southeast, # df_Southeast
                linewidths=.1,
                square=True,
                cbar_kws={"orientation": "horizontal"},
                cbar=False,
                annot=True,  # Add annotations (numbers) over the cells
                cmap=colormap,
                fmt='.4g',
                annot_kws={"fontsize": 8,"fontweight": "bold"})
    # # sns.heatmap(ax=ax5,
    #             data=df_Northeast,
    #             linewidths=.1,
    #             square=True,
    #             cbar_kws={"orientation": "horizontal"},
    #             cbar=False,
    #             cmap=colormap)

    ax0.text(-2.5, -1.7,
             'Exploring the Relationship Between Loan Purpose and Interest Rates',
             fontsize=22, fontweight='bold', fontfamily='serif')
    ax0.text(-2.5, -1.1,
             'Categorical Comparison: Loan Purpose versus Interest Rate Correlation Across States',
             fontsize=13, fontweight='light', fontfamily='serif')
    ax0.text(0, -0.2, 'West', fontsize=15, fontweight='bold', fontfamily='serif')
    ax1.text(0, -0.2, 'Southwest', fontsize=15, fontweight='bold', fontfamily='serif')
    ax3.text(0, -0.2, 'Southeast', fontsize=15, fontweight='bold', fontfamily='serif')
    ax4.text(0, -0.2, 'Northeast', fontsize=15, fontweight='bold', fontfamily='serif')
    ax5.text(0, -0.2, 'Midwest', fontsize=15, fontweight='bold', fontfamily='serif')

    ax0.set_xticklabels("")
    ax0.tick_params(bottom=False)
    y_labels = ['0% - 4%', '4% - 8%', '8% - 12%', '12% - 16%', '16% - 20%']
    ax0.set_yticklabels(y_labels, rotation=0, weight='bold', color='black')

    ax1.set_xticklabels("")
    ax1.set_yticklabels("")
    ax1.tick_params(left=False)
    ax1.tick_params(bottom=False)

    # ax3.set_xticklabels(
    #x_labels =  ['Debt\nconsolidation', 'Credit\ncard', 'Home\nimprovement','House', 'major purchase', 'small\nbusiness','car','wedding','medical']) #,rotation=270
    #ax3.tick_params(left=True) # False

    # Customize x-axis and y-axis labels
    x_labels =  ['Debt\nConsolidation', 'Credit-card', 'Home improvement','House', 'Major purchase', 'Small\nBusiness','Car','Wedding'] #'] # 'medical'
    y_labels_ax3 = ['0% - 4%', '4% - 8%', '8% - 12%', '12% - 16%', '16% - 20%','20% - 24%']#, '20% - 24%']#, '24% - 28%']

    # loop iterates over the two subplots (ax1 and ax2)
    for ax in [ ax3 ,ax5]: #[ax3,
        ax.set_xticklabels(x_labels, rotation=45, ha='right', weight='bold', color='black')
        #ax.set_yticklabels(y_labels, rotation=0, weight='bold', color='black')

    ax3.set_xticklabels(x_labels, rotation=45, ha='right', weight='bold', color='black')
    ax3.set_yticklabels(y_labels_ax3, rotation= 0, weight='bold', color='black')
    ax4.set_xticklabels("")
    ax4.set_yticklabels("")
    ax4.tick_params(left=False)
    ax4.set_yticklabels("")
    ax4.tick_params(left=False)
    # # ax4.set_xticklabels(
    # # ['Debt consolidation', 'redit card', 'home improvement', 'house', 'major purchase', 'small business', 'car','wedding', 'medical'])#,rotation=270)
    ax5.set_yticklabels("")
    ax5.tick_params(left=False)

    ax0.set_xlabel("")
    ax1.set_xlabel("")
    ax1.set_ylabel("")
    # ax2.set_xlabel("")
    # ax2.set_ylabel("")
    ax4.set_ylabel("")
    ax5.set_ylabel("")
    plt.savefig("my_corrrelation.jpg", dpi=250, bbox_inches='tight')
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

    res = creating_the_dataframe_correlation_for_each_region(df)
    creating_the_correlation_chart_for_each_region(res)






