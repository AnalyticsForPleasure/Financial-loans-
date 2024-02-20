import numpy as np
import pandas as pd
#import dataframe_image as dfi
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap #


## Source: https://www.kaggle.com/datasets/nezukokamaado/auto-loan-dataset?select=financial_loan.csv

if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('/home/shay_diy/PycharmProjects/Financial_loans/Data/financial_loan.csv')
    print('*')


# **************************************************************************************************************
# Starting with getting a short glance information about the data
# ***************************************************************************************************************
    unique_application_type = pd.unique(df['application_type'])
    unique_emp_length = pd.unique(df['emp_length']) #  emp_length = Number of years in the job
    unique_loan_status = pd.unique(df['loan_status']) # unique_loan_status : Charged Off , Fully Paid , Current
    unique_purpose =  pd.unique(df['purpose']) # purpose : car , credit card , Debt consolidation , educational , home improvement , house , major purchase , medical , other , small business , vacation , wedding
    unique_home_ownership = pd.unique(df['home_ownership']) # home_ownership : 'Rent' , 'Own' , 'Mortgage'


    purpose_his = df['purpose'].value_counts()
    unique_emp_length = df['emp_length'].value_counts()
    unique_loan_amount  = df['loan_amount'].value_counts().reset_index()
    loan_size_info = unique_loan_amount.sort_values(by=['loan_amount'])
    print('*')


# ***************************************************************************************************************
