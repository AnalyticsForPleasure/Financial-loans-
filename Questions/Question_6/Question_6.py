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
    # Generate random data for loan amount and interest rate
    np.random.seed(0)  # for reproducibility
    loan_amount = np.random.uniform(min_loan_amount, max_loan_amount, 10000) # 10000 rows / dots
    int_rate = np.random.uniform(min_int_rate, max_int_rate, 10000)

    # Create DataFrame
    df = pd.DataFrame({'Loan Amount': loan_amount, 'Interest Rate': int_rate})

    # Plot scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Loan Amount'], df['Interest Rate'], color='blue', alpha=0.5)
    plt.title('Interest Rate vs Loan Amount', fontsize=16)
    plt.xlabel('Loan Amount', fontsize=14)
    plt.ylabel('Interest Rate', fontsize=14)
    plt.grid(True)
    plt.show()