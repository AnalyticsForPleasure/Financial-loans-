import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

# **************************************************************************************************************
# Function  name:
# input:
# return value:
# ***************************************************************************************************************
def creating_a_sub_grade_table(table_specific_region, specific_region):

    list_of_sub_grade_df = []
    list_of_number_of_loans_in_the_same_level = []

    groups_by_state = table_specific_region.groupby('sub_grade')
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






    # old_names = ['A','B','C','D','E','F','G']
    # new_names = ["Borrowers with excellent credit history,\n high income,\n low debt-to-income ratio,\nand strong employment stability", # A
    #             "Borrowers with good credit history,\n moderate income,\n manageable debt-to-income ratio,\nand stable employment", # B
    #             "Borrowers with fair credit history,\n moderate income,\n higher debt-to-income ratio,\nand somewhat stable employment", #C
    #             "Borrowers with average credit history,\n moderate income,\n higher debt-to-income ratio,\nand less stable employment", # D
    #             "Borrowers with average credit history,\n moderate income,\n higher debt-to-income ratio,\nand less stable employment", # E
    #             "Borrowers with poor credit history,\n low income,\n high debt-to-income ratio,\nand unstable employment", # F
    #             "Borrowers with very poor credit history,\nvery low income,\n very high debt-to-income ratio,\n and highly unstable employment"] #G
    #
    # pivot_df.rename(columns=dict(zip(old_names, new_names)), inplace=False)
    pivot_df= pivot_df.T
    print('*')
    return pivot_df

# **************************************************************************************************************
# Function  name:
# input:
# return value:
# ***************************************************************************************************************
def creating_the_chart(final_table,distinct_colors):


    # Setting up figure and axes
    fig = plt.figure(figsize=(20, 4))  # create figure
    gs = fig.add_gridspec(1, 1)
    gs.update(wspace=0, hspace=0.5)
    ax0 = fig.add_subplot(gs[0, 0], ylim=(0, 1000))
    # Change background color
    background_color = "#fbfbfb"
    fig.patch.set_facecolor(background_color)  # figure background color
    ax0.set_facecolor(background_color)  # axes background color
    x = np.arange(len(final_table))
    bar_width = 0.085

    #orange_palette = sns.color_palette("Oranges", 5)[::-1]
    ax0.grid(color='black', linestyle=':', axis='y', zorder=0, dashes=(1, 5))
    ax0.bar(x, final_table["1"], width=bar_width, color=distinct_colors[0], label="A", zorder=3)
    ax0.bar(x + bar_width + 0.01, final_table["2"], width=bar_width, color=distinct_colors[1], label="B", zorder=3)
    ax0.bar(x + bar_width * 2 + 0.01 * 2, final_table["3"], width=bar_width, color=distinct_colors[2], label="C", zorder=3)
    ax0.bar(x + bar_width * 3 + 0.01 * 3, final_table["4"], width=bar_width, color=distinct_colors[3], label="D", zorder=3)
    ax0.bar(x + bar_width * 4 + 0.01 * 4, final_table["5"], width=bar_width, color=distinct_colors[4], label="E", zorder=3)


    # Fix the x-axes.
    ax0.set_xticks(x + bar_width)
    x_labels = list(final_table.index)
    ax0.set_xticklabels(x_labels)

    ax0.text(-0.5, -180, 'Borrowers with excellent credit history,\nhigh income,\nlow debt-to-income ratio,\nand strong employment stability', fontsize=8, fontweight='bold', fontfamily='serif')
    ax0.text(0.7, 700, 'Borrowers with good credit history,\nmoderate income,\nmanageable debt-to-income ratio,\nand stable employment', fontsize=8, fontweight='bold', fontfamily='serif')
    ax0.text(1.8, -180, 'Borrowers with fair credit history,\nmoderate income,\n higher debt-to-income ratio,\nand somewhat stable employment', fontsize=8, fontweight='bold', fontfamily='serif')
    ax0.text(2.9, 700, 'Borrowers with average credit history,\nmoderate income,\n higher debt-to-income ratio,\nand less stable employment', fontsize=8, fontweight='bold', fontfamily='serif')
    ax0.text(4, -180, 'Borrowers with below-average credit history,\nlower income,\nhigher debt-to-income ratio,\nand less stable employment', fontsize=8, fontweight='bold', fontfamily='serif')
    ax0.text(5.1, 700, 'Borrowers with poor credit history,\nlow income,\nhigh debt-to-income ratio,\nand unstable employment', fontsize=8, fontweight='bold', fontfamily='serif')
    ax0.text(6.2, -80,'Borrowers with very poor credit history,\nvery low income,\nvery high debt-to-income ratio,\nand highly unstable employment',fontsize=8, fontweight='bold', fontfamily='serif')

    ax0.text(-0.5, 1090, 'Borrowers credit history', fontsize=20, fontweight='bold', fontfamily='serif')
    ax0.text(-0.5, 1030, 'Grading system consists of grades A through G', fontsize=13, fontweight='light',fontfamily='serif')

    for s in ["top", "right", "left"]:
        ax0.spines[s].set_visible(False)

    ax0.legend(loc='lower center', ncol=4, bbox_to_anchor=(0.48, -0.48))
    print('*')

    plt.savefig('result.jpg', dpi=250, bbox_inches='tight')
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
    df['Region'] = df['address_state'].map(
        {state: region for region, states in region_dict.items() for state in states}).fillna('Other')  # TODO: ask

    Regions = ['West', 'Southwest', 'Mideast', 'Southeast', 'Northeast']

    # Your data processing code here

    # Define the colors for the colormap (from orange to gray)
    colors = ['#FFA500', 'gray']

    # Create a colormap using LinearSegmentedColormap
    cmap = LinearSegmentedColormap.from_list('OrangeToGray', colors)

    # Generate 5 distinct colors from the colormap
    distinct_colors = [cmap(i) for i in np.linspace(0, 1, 5)]
    print('*')

    for specific_region in Regions :
        table_specific_region = df.loc[df['Region'] == specific_region, :]
        res = creating_a_sub_grade_table(table_specific_region, specific_region)
        creating_the_chart(res, distinct_colors)
print('*')

