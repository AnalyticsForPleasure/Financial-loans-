import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('/home/shay_diy/PycharmProjects/Financial_loans/Data/financial_loan.csv')
    print('*')

    max_loan_amount = df['loan_amount'].max()  # 35,000
    min_loan_amount  = df['loan_amount'].min() # 500
    print('*')

    max_int_rate = df['int_rate'].max()
    min_int_rate = df['int_rate'].min()
    print('*')

    y_values_intrest_rate= df.loc[:,'int_rate'] # Y axis
    x_values_loan_amount = df.loc[:,'loan_amount']
    # Generate random data for loan amount and interest rate
    #np.random.seed(0)  # for reproducibility
    # loan_amount = np.random.uniform(min_loan_amount, max_loan_amount, 10000) # 10000 rows / dots
    # int_rate = np.random.uniform(min_int_rate, max_int_rate, 10000)

    # Create DataFrame
    df = pd.DataFrame({'loan_amount': x_values_loan_amount, 'int_rate': y_values_intrest_rate})



    # fig = plt.figure(figsize=(10, 5), )
    # ax = fig.add_subplot(111)
    #
    # ax.text(-0.4, 97000,
    #         'Loan Amounts vs. Interest Rates',
    #         fontsize=17.5,
    #         fontweight='bold',
    #         fontfamily='serif')
    # ax.text(-0.4, 81500,
    #         'Does a relationship exist between loan amounts and interest rates?',
    #         fontsize=11.5,
    #         fontweight='bold',
    #         fontfamily='serif',
    #         color="#4b4b4c")

    # Plot scatter plot
    plt.figure(figsize=(10, 6),facecolor='#f6f5f5')
    plt.scatter(df['loan_amount'], df['int_rate'], color="#FFA500", alpha=0.5, marker='o', facecolor='none',s=100)
    plt.title('Interest Rate vs Loan Amount', fontsize=16)
    plt.xlabel('Loan Amount', fontsize=14)
    plt.ylabel('Interest Rate', fontsize=14)
    plt.grid(False)

    # plt.spines['top'].set_visible(False)
    # plt.spines['right'].set_visible(False)
    # plt.spines['bottom'].set_visible(False)
    # plt.spines['left'].set_visible(False)
    # Removing y-axis ticks and labels
    # ax.tick_params(left=False)
    # ax.set_yticklabels([])


    plt.show()