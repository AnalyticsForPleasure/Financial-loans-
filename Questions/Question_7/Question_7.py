import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap
import dataframe_image as dfi

# **************************************************************************************************************
# Function  name: creating_a_sub_grade_table
# input:
# return value:
# ***************************************************************************************************************
def creating_a_sub_grade_table(df):

    list_of_sub_grade_df = []
    list_of_number_of_loans_in_the_same_level = []

    groups_by_state = df.groupby('sub_grade')
    for sub_grade_name, sub_grade_df in groups_by_state:
        Number_of_loans_in_the_same_level = sub_grade_df.shape[0]
        list_of_sub_grade_df.append(sub_grade_name)
        list_of_number_of_loans_in_the_same_level.append(Number_of_loans_in_the_same_level)

    # Extract the first letter of each sub_grade_name
    grade = [sub_grade[0] for sub_grade in list_of_sub_grade_df]
    sub_grade = [sub_grade[1] for sub_grade in list_of_sub_grade_df]

    # Create the dataframe
    df_starting = {
        'grade': grade,
        'Sub_grade': sub_grade,
        'Counting_the_loans_within_a_Sub_grade': list_of_number_of_loans_in_the_same_level
    }

    final_table = pd.DataFrame(df_starting,
                                columns=['grade', 'Sub_grade', 'Counting_the_loans_within_a_Sub_grade'])

    # Pivot the DataFrame
    pivot_df = final_table.pivot(index='Sub_grade', columns='grade', values='Counting_the_loans_within_a_Sub_grade')

    pivot_df= pivot_df.T

    # Adding style:
    pivot_df
    #res_2 = list(pivot_df.columns.values)
    table_style = pivot_df

    # Changing the column rows name :
    old_names = ['1', '2', '3', '4', '5']  ##list(table_style.columns.values)
    new_names = ['Sub-grades 1', 'Sub-grades 2', 'Sub-grades 3', 'Sub-grades 4', 'Sub-grades 5']
    table_style = table_style.rename(columns=dict(zip(old_names, new_names)), inplace=False)

    # Changing the  rows index names :
    # Add "Grade " to each index row
    table_style.index = ['Grade ' + str(index) for index in table_style.index]

    # Adding style to the dataframe
    rows_to_mark = {0,1,2,3,4,5,6} # name of the index

    # Adding the style:
    highlighted_df = table_style.style.apply(lambda x: ['background: #ffe4b2' if x.name in rows_to_mark else '' for i in x],axis=1)
    #highlighted_df.hide(axis='index')
    dfi.export(highlighted_df, filename='/home/shay_diy/PycharmProjects/Financial_loans/Questions/Question_7/grid_matrix_style.png') #/home/shay_diy/PycharmProjects/Financial_loans/Questions/Question_7
    print('*')

    return pivot_df

# **************************************************************************************************************
# Function  name: creating_the_chart_by_
# input:
# return value:
# ***************************************************************************************************************
def creating_the_chart_by_grade_groups(final_table, distinct_colors):

    # Setting up figure and axes
    fig = plt.figure(figsize=(20, 6))  # create figure
    gs = fig.add_gridspec(1, 1)
    gs.update(wspace=0, hspace=0.5)
    ax0 = fig.add_subplot(gs[0, 0], ylim=(0, 4100))
    # Change background color
    background_color = "#fbfbfb"
    fig.patch.set_facecolor(background_color)  # figure background color
    ax0.set_facecolor(background_color)  # axes background color
    x = np.arange(len(final_table))
    bar_width = 0.085

    #orange_palette = sns.color_palette("Oranges", 5)[::-1]
    ax0.grid(color='black', linestyle=':', axis='y', zorder=0, dashes=(1, 5))
    ax0.bar(x, final_table["1"], width=bar_width, color=distinct_colors[0], label="1", zorder=3)
    ax0.bar(x + bar_width + 0.01, final_table["2"], width=bar_width, color=distinct_colors[1], label="2", zorder=3)
    ax0.bar(x + bar_width * 2 + 0.01 * 2, final_table["3"], width=bar_width, color=distinct_colors[2], label="3", zorder=3)
    ax0.bar(x + bar_width * 3 + 0.01 * 3, final_table["4"], width=bar_width, color=distinct_colors[3], label="4", zorder=3)
    ax0.bar(x + bar_width * 4 + 0.01 * 4, final_table["5"], width=bar_width, color=distinct_colors[4], label="5", zorder=3)


    # Fix the x-axes.
    ax0.set_xticks(x + bar_width)
    x_labels = list(final_table.index)
    ax0.set_xticklabels(x_labels)

    ax0.text(-0.3, -800, 'Borrowers with excellent credit history,\nhigh income,\nlow debt-to-income ratio,\nand strong employment stability', fontsize=8, fontweight='bold', fontfamily='serif')
    ax0.text(0.65, 3020, 'Borrowers with good credit history,\nmoderate income,\nmanageable debt-to-income ratio,\nand stable employment', fontsize=8, fontweight='bold', fontfamily='serif')
    ax0.text(1.75, -800, 'Borrowers with fair credit history,\nmoderate income,\n higher debt-to-income ratio,\nand somewhat stable employment', fontsize=8, fontweight='bold', fontfamily='serif')
    ax0.text(2.8, 3020, 'Borrowers with average credit history,\nmoderate income,\n higher debt-to-income ratio,\nand less stable employment', fontsize=8, fontweight='bold', fontfamily='serif')
    ax0.text(3.75, -800, 'Borrowers with below-average credit\nhistory, lower income, higher\ndebt-to-income ratio,\nand less stable employment', fontsize=8, fontweight='bold', fontfamily='serif')
    ax0.text(4.85, 3020, 'Borrowers with poor credit history,\nlow income,\nhigh debt-to-income ratio,\nand unstable employment', fontsize=8, fontweight='bold', fontfamily='serif')
    ax0.text(5.85, -800,'Borrowers with very poor credit history,\nvery low income,\nvery high debt-to-income ratio,\nand highly unstable employment',fontsize=8, fontweight='bold', fontfamily='serif')

    ax0.text(-0.5, 4450,'Borrowers credit history', fontsize=30, fontweight='bold', fontfamily='serif')
    ax0.text(-0.5, 4150,"Assessing Borrower Risk: A Comprehensive Grading System from A to G", fontsize=13, fontweight='light',fontfamily='serif')

    for s in ["top", "right", "left"]:
        ax0.spines[s].set_visible(False)

    ax0.legend(loc='lower center', ncol=5, bbox_to_anchor=(0.48, -0.48))
    print('*')

    plt.savefig("grade_loans.jpg", dpi=250, bbox_inches='tight')
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

    # Your data processing code here

    # Define the colors for the colormap (from orange to gray)
    colors = ['#FFA500', 'gray']

    # Create a colormap using LinearSegmentedColormap
    cmap = LinearSegmentedColormap.from_list('OrangeToGray', colors)

    # Generate 5 distinct colors from the colormap
    distinct_colors = [cmap(i) for i in np.linspace(0, 1, 5)]
    print('*')


    res = creating_a_sub_grade_table(df)
    creating_the_chart_by_grade_groups(res, distinct_colors)
    print('*')

