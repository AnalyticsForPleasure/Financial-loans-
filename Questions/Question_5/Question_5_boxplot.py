import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# **************************************************************************************************************
# Function  name: creating_a_boxplot_for_emp_length
# input:
# return value:
# ***************************************************************************************************************
def creating_a_boxplot_for_emp_length(df):
    emp_length_his = df['emp_length'].value_counts().reset_index()
    print('*')


    table_result = df.loc[:, ['emp_length', 'loan_amount']]
    print('*')
    background_color = "#f6f5f5"
    color_map = ["#FFA500" for _ in range(3)]
    sns.set_palette(sns.color_palette(color_map))
    plt.rcParams['figure.dpi'] = 400
    fig = plt.figure(figsize=(10, 6), facecolor='#f6f5f5')
    gs = fig.add_gridspec(1, 1)
    gs.update(wspace=0, hspace=0)
    ax0 = fig.add_subplot(gs[0, 0])
    ax0.set_facecolor(background_color)
    for s in ["right", "top"]:
        ax0.spines[s].set_visible(True)
    # Create boxplot
    # Add labels and title
    ax0.text(-0.5, 39200, 'Relationship between Employment Length and Loan Amount Distribution ', color='black',
             fontsize=14, ha='left', va='bottom', weight='bold', fontfamily='serif')
    ax0.text(-0.5, 38450, 'How does the variability in employment duration impact the amount of loans taken?',
             color="#4b4b4c", fontsize=12, ha='left', weight='bold', va='top', fontfamily='serif')
    ax0_sns = sns.boxenplot(ax=ax0, x=table_result['emp_length'], y=table_result['loan_amount'],
                            zorder=3, linewidth=0.7, saturation=1)
    ax0_sns.set_xlabel("Variation in Length of Employment", fontsize=10, weight='bold', fontfamily='serif')
    ax0_sns.set_ylabel("Loan Amount have been taken by a citizen", fontsize=10, weight='bold', fontfamily='serif')
    ax0_sns.tick_params(labelsize=5)

    for s in ["right", "top"]:
        ax0.spines[s].set_visible(False)
    # Show plot
    plt.savefig('boxplot_for_emp_length.jpg', dpi=250, bbox_inches='tight')
    plt.show()

# **************************************************************************************************************
# Function  name: retrieving_the_plotbox_data
# input:
# return value:
# ***************************************************************************************************************
# def retrieving_the_plotbox_data(df):
# #    global quartiles
#     # Group by emp_length and calculate summary statistics for loan_amount
#     summary_stats = df.groupby('emp_length')['loan_amount'].describe()
#     # Define the quartiles
#     quartiles = np.percentile(df['loan_amount'], [25, 50, 75])
#
#     # Define a function to compute the quartile range
#     def compute_quartile_range(row):
#         return quartiles
#
#     # Apply the function to each row of the summary statistics dataframe
#     summary_stats[['25%', '50%', '75%']] = summary_stats.apply(compute_quartile_range, axis=1, result_type='expand')




if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('/home/shay_diy/PycharmProjects/Financial_loans/Data/financial_loan.csv')
    print('*')
    import numpy as np

    # Group by emp_length and calculate summary statistics for loan_amount
    summary_stats = df.groupby('emp_length')['loan_amount'].describe()

    # Define the quartiles
    quartiles = np.percentile(df['loan_amount'], [25, 50, 75])


    # Define a function to compute the quartile range
    def compute_quartile_range(row):
        return quartiles


    # Apply the function to each row of the summary statistics dataframe
    summary_stats[['25%', '50%', '75%']] = summary_stats.apply(compute_quartile_range, axis=1, result_type='expand')
    summary_stats_result = summary_stats.T
    # Display the result
    print(summary_stats)

    #retrieving_the_plotbox_data(df)
    creating_a_boxplot_for_emp_length(df)