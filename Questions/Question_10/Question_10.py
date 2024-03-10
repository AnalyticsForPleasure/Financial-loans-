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
# Function  name: When_the_laons_been_given__Before_after_issue_date_
# input:
# return value:
# ***************************************************************************************************************
def When_the_laons_been_given_Before_or_after_issue_date(df):
    # Convert dates to datetime objects
    df['issue_date'] = pd.to_datetime(df['issue_date'], format='%d-%m-%Y')
    df['last_credit_pull_date'] = pd.to_datetime(df['last_credit_pull_date'], format='%d-%m-%Y')
    # Create a DataFrame with only the required columns
    checking_connection = df[['issue_date', 'last_credit_pull_date']]
    # Apply the function to get the later date
    checking_connection['result_col'] = checking_connection.apply(get_later_date, axis=1)
    # Display first few rows of the DataFrame
    final_output_his = checking_connection['result_col'].value_counts()  ## issue_date = 20,182  || last credit pull date = 18,394
    return final_output_his

if __name__ == '__main__':
    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('/home/shay_diy/PycharmProjects/Financial_loans/Data/financial_loan.csv')

    When_the_laons_been_given_Before_or_after_issue_date(df)
    print('*')



