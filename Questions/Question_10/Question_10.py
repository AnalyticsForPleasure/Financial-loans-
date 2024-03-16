import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
import squarify

# **************************************************************************************************************
# Function  name: get_later_date
# input:
# return value:
# ***************************************************************************************************************
def get_later_date(row):
    issue_date = pd.to_datetime(row['issue_date'], format='%d-%m-%Y')
    last_credit_pull_date = pd.to_datetime(row['last_credit_pull_date'], format='%d-%m-%Y')
    if issue_date > last_credit_pull_date:
        return 'issue_date'  # Return the actual date, not the column name
    else:
        return 'last_credit_pull_date'  # Return the actual date, not the column name


# **************************************************************************************************************
# Function  name: When_the_laons_been_given_Before_or_after_issue_date
# input:
# return value:
# ***************************************************************************************************************
def When_the_loans_been_given_Before_or_after_issue_date(df):
    # Convert dates to datetime objects
    df['issue_date'] = pd.to_datetime(df['issue_date'], format='%d-%m-%Y')
    df['last_credit_pull_date'] = pd.to_datetime(df['last_credit_pull_date'], format='%d-%m-%Y')
    # Create a DataFrame with only the required columns
    checking_connection = df[['issue_date', 'last_credit_pull_date']]
    # Apply the function to get the later date
    checking_connection['result_col'] = checking_connection.apply(get_later_date, axis=1)
    # More citizens take loans after the issue date ( 20,182)
    final_output_his = checking_connection['result_col'].value_counts()  ## issue_date = 20,182  || last credit pull date = 18,394
    percentages_output = (final_output_his / final_output_his.sum()) * 100
    #percentages_output = percentages_output.reset_index()
    print('*')

    return percentages_output
# **************************************************************************************************************
# Function  name: adding_the_chart
# input:
# return value:
# ***************************************************************************************************************
def adding_the_chart(percentages_output):
    print('*')

    colors = ['#D9042B', '#270140', '#F2B705', '#F28705', '#F22F1D']
    #sns.palplot(colors, size=3)

    #final_output_his = (df['Potability'].value_counts(normalize=True)).round(2)
    ##### plotting
    fig, ax = plt.subplots(figsize=(13, 3.5), dpi=100)
    fig.set_facecolor('#f5f6f6')
    ax.set_facecolor('#f5f6f6')
    # left side values
    ax.barh(percentages_output.index[0], width=percentages_output.values[0], height=0.4, color=colors[1])
    # right side values
    ax.barh(percentages_output.index[0], width=percentages_output.values[1], height=0.4, left=percentages_output.values[0], color=colors[2])
    for idx, pa in enumerate(ax.patches):

        # annotations
        if pa.get_width() < 0.5:
            x = -pa.get_width() +1.16
            color = colors[1]
            potable = 'Issue date'
        else:
            x = pa.get_width() / 2
            color = colors[2]
            potable = 'Last credit pull date'

        # This line below  - Issue date' or the 'Last credit pull date' title
        ax.text(x , pa.get_y() + 0.225, ('{}').format(potable),{'font': 'serif', 'size': 36, 'weight': 'normal', 'color': color}, alpha=1)
        # This line below  - is the percentage
        ax.text(x+20 , pa.get_y() + 0.165, ('{}%').format(str(int(pa.get_width() * 100))),{'font': 'serif', 'size': 24, 'weight': 'normal', 'color': color}, alpha=1)
    ## titles
    plt.text(0.05, 1.20, 'Are citizens taking out more loans before or\nafter the most recent credit pull date?',
             {'font': 'serif', 'color': 'black', 'weight': 'bold', 'size': 24}, alpha=1)
    # plt.text(0.05, 1.07, """This is class distribution of the potability of water.
    # So it is clear that, 39% water samples out of 3276 are drinkable.""",
    #          {'font': 'serif', 'color': 'black', 'weight': 'normal', 'size': 13}, alpha=0.9)
    # plt.text(0.8, -0.3, '© Made by Shay cohen | AnalyticsForPleasure.github.io', {'font': 'serif', 'size': 12, 'color': 'black'}, alpha=1)
    fig.show()
    ax.axis('off')

    plt.savefig('Question_10_image.jpg', dpi=250, bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('/home/shay_diy/PycharmProjects/Financial_loans/Data/financial_loan.csv')

    res = When_the_loans_been_given_Before_or_after_issue_date(df)
    adding_the_chart(res)

    print('*')



