import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
import squarify





if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('/home/shay_diy/PycharmProjects/Financial_loans/Data/financial_loan.csv')

    print('*')


    # The last credit pull date is often close to the issue date

    "issue date" and "last credit pull date"

    checking_connection = df.loc[:,["issue_date","last_credit_pull_date"]]
    print('*')

    # Convert string columns to datetime objects
    checking_connection['issue_date'] = pd.to_datetime(checking_connection['issue_date'], format='%d-%m-%Y')
    checking_connection['last_credit_pull_date'] = pd.to_datetime(checking_connection['last_credit_pull_date'], format='%d-%m-%Y')

    # Calculate the difference between the dates in days
    checking_connection['days_difference'] = (checking_connection['last_credit_pull_date'] - checking_connection['issue_date']).dt.days

    # Define the bins
    bins = [-300,-270, -240, -210, -180, -150, -120, -90, -60, -30, 0, 30, 60, 90, 120,150,180,210,240,270,300]

    # Define labels for the bins
    labels =['-300 to -270','-270 to -240','-240 to -210','-210 to -180' ,'-180 to -150','-150 to -120','-120 to -90', '-90 to -60', '-60 to -30', '-30 to 0', '0 to 30', '30 to 60', '60 to 90', '90 to 120','120 to 150','150 to 180','180 to 210','210 to 240','240 to 270','270 to 300']

    # Create a new column with the bins
    checking_connection['days_range'] = pd.cut(checking_connection['days_difference'], bins=bins, labels=labels, right=False)

    # Display the DataFrame
    print(checking_connection)

    # Calculate the correlation between the two columns
    correlation = checking_connection['issue_date'].corr(checking_connection['last_credit_pull_date'])

    # Display the correlation coefficient
    print("Correlation coefficient between issue_date and last_credit_pull_date:", correlation)
    #days_difference_His = checking_connection['days_difference'].value_counts()
    print('*')

