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
    background_color = "#f6f5f5"

    plt.rcParams['figure.dpi'] = 400
    fig = plt.figure(figsize=(10, 6), facecolor='#f6f5f5')
    gs = fig.add_gridspec(1, 1)
    gs.update(wspace=0, hspace=0)
    ax0 = fig.add_subplot(gs[0, 0])
    ax0.set_facecolor(background_color)
    for s in ["right", "top"]:
        ax0.spines[s].set_visible(True)
    # Create boxplot


    # Plot scatter plot
    #plt.figure(figsize=(10, 6),facecolor='#f6f5f5')
    plt.scatter(df['loan_amount'], df['int_rate'], color="#FFA500", alpha=0.5, marker='o', facecolor='none',s=100)

    # Add labels and title
    ax0.text(-0.5, 38900, 'Relationship between Interest Rate vs Loan Amount', color='black',
             fontsize=14, ha='left', va='bottom', weight='bold', fontfamily='serif')
    # ax0.text(-0.5, 38100, 'How does the variability in employment duration impact the amount of loans taken?',
    #          color="#4b4b4c", fontsize=12, ha='left', weight='bold', va='top', fontfamily='serif')
    #plt.title('Interest Rate vs Loan Amount', fontsize=20, weight='bold', fontfamily='serif')
    plt.xlabel('Loan Amount', fontsize=14, weight='bold', fontfamily='serif')
    plt.ylabel('Interest Rate', fontsize=14, weight='bold', fontfamily='serif')
    plt.grid(False)

    #plt.spines['top'].set_visible(False)
    # plt.spines['right'].set_visible(False)
    # plt.spines['bottom'].set_visible(False)
    # plt.spines['left'].set_visible(False)
    #Removing y-axis ticks and labels
    ax0.tick_params(left=False)
    ax0.set_yticklabels([])

    # Show plot
    plt.savefig('Relationship_between_int_rate_to_loan_amount.jpg')#,# dpi=250, bbox_inches='tight')

    plt.show()