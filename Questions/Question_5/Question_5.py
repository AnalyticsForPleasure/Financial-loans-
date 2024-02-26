import numpy as np
import pandas as pd







if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('/home/shay_diy/PycharmProjects/Financial_loans/Data/financial_loan.csv')
    print('*')

    emp_length_his = df['emp_length'].value_counts().reset_index()
    print('*')

    groups_by_emp_length = df.groupby('emp_length')
    for number_of_years, mini_df_number_of_years in groups_by_emp_length:
        #print("The state name is: ", number_of_years)
        #print(mini_df_number_of_years)
        avg_loan_amount= mini_df_number_of_years['loan_amount'].mean()  # Midwest = 64,359.45 . Northeast = 72,319 , southeast = 67,252 , southwest = 72,438 , west = 70488
        print('*')
