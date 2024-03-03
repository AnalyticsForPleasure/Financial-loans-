import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import squarify    # You need to install this library using pip: pip install squarify
import seaborn as sns

#import dataframe_image as dfi
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap #


## Source: https://www.kaggle.com/datasets/nezukokamaado/auto-loan-dataset?select=financial_loan.csv
# **************************************************************************************************************
# Function  name: retrieving_the_amount_of_loan_taken_by_each_state
# input:
# return value:
# ***************************************************************************************************************
def retrieving_the_amount_of_loan_taken_by_each_state(df):
    list_of_states = []
    number_of_loans_in_specific_state_list = []


    groups_by_state = df.groupby('address_state')
    for state_name, mini_df_per_state in groups_by_state:
        # print("The state name is: ", state_name)
        # print(mini_df_per_state)

        number_of_loans_in_specific_state = mini_df_per_state.shape[0]
        number_of_loans_in_specific_state_list.append(number_of_loans_in_specific_state)
        list_of_states.append(state_name)

    list_of_full_names_states = ['Alaska', 'Alabama', 'Arkansas', 'Arizona', 'California', 'Colorado', 'Connecticut',
                                 'District of Columbia', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Iowa', 'Idaho',
                                 'Illinois', 'Indiana', 'Kansas', 'Kentucky', 'Louisiana',
                                 'Massachusetts', 'Maryland', 'Maine', 'Michigan', 'Minnesota', 'Missouri',
                                 'Mississippi', 'Montana', 'North Carolina', 'Nebraska', 'New Hampshire', 'New Jersey',
                                 'New Mexico', 'Nevada', 'New York', 'Ohio', 'Oklahoma', 'Oregon',
                                 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas',
                                 'Utah', 'Virginia', 'Vermont', 'Washington', 'Wisconsin', 'West Virginia', 'Wyoming']

    df_starting = {'States': list_of_full_names_states,
                   'State_abbreviations': list_of_states,
                   'Count_of_loans_within_a_particular_state': number_of_loans_in_specific_state_list}

    final_table = pd.DataFrame(df_starting,
                               columns=['States', 'State_abbreviations', 'Count_of_loans_within_a_particular_state'])

    final_table = final_table.sort_values(by = 'Count_of_loans_within_a_particular_state', ascending=False)
    # let's present only the states with more than 100 taken loans !!!

    output_data =final_table.loc[(final_table['Count_of_loans_within_a_particular_state'] > 110)]

    print('*')

    return output_data


# **************************************************************************************************************
# Function  name: creating_a_treemap_count_for_each_state
# input:
# return value:
# ***************************************************************************************************************
def creating_a_treemap_count_for_each_state(result_table):
    plt.figure(figsize=(20, 8), facecolor='#f6f5f5')

    # Concatenate state labels with their respective sizes (number of loans)
    labels_with_sizes = [f'{state}\n({size})' for state, size in zip(result_table['States'], result_table['Count_of_loans_within_a_particular_state'])] # TODO: Need to ask about this line

    #labels = list(result_table.loc[:,'States'])
    sizes =list(result_table.loc[:,'Count_of_loans_within_a_particular_state'])

    # Define a colormap with different shades of blue
    #cmap = plt.cm.get_cmap('Oranges', len(labels_with_sizes))

    # Generate a list of blue color strings
    #blue_colors = [cmap(i) for i in reversed(range(len(labels_with_sizes)))]

    # Plotting
    #plt.figure(figsize=(10, 4))
    squarify.plot(sizes=sizes, label=labels_with_sizes, color="#FFA500", alpha=0.7,pad=True,  text_kwargs={'fontsize':8.2,'fontfamily':'serif','fontweight':'bold'})
    # Adding title and axis labels
    #plt.title("Example Treemap")
    plt.axis('off')  # Turn off axis
    # Display the plot
    #plt.title('Count of Loans in Each State with More Than 100 Loans' ,fontsize=30, weight='bold',fontfamily='serif', color = 'dimgrey')
    plt.text(1.5 , 110,
             'Loan Amounts Distributed Across U.S. States',
             fontsize=25,
             fontweight='bold',
             fontfamily='serif')
    plt.text(1.5 , 101,
             'Top 3 States with Highest Loan Uptake :  California => 6,894  | New York => 3,701  |  Florida => 2,773 ',
             fontsize=16,
             fontweight='light',
             fontfamily='serif')

    plt.savefig('treemap_count_for_each_state.jpg', dpi=250, bbox_inches='tight')
    plt.show()


if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('/home/shay_diy/PycharmProjects/Financial_loans/Data/financial_loan.csv')
    print('*')

    column_headers = list(df.columns.values)
    print("The Column Header :", column_headers)
    print('*')
# **************************************************************************************************************
# Starting with getting a short glance information about the data
# ***************************************************************************************************************
    unique_application_type = pd.unique(df['application_type'])
    unique_emp_length = pd.unique(df['emp_length']) #  emp_length = Number of years in the job
    unique_loan_status = pd.unique(df['loan_status']) # unique_loan_status : Charged Off , Fully Paid , Current
    unique_purpose =  pd.unique(df['purpose']) # purpose : car , credit card , Debt consolidation , educational , home improvement , house , major purchase , medical , other , small business , vacation , wedding
    unique_home_ownership = pd.unique(df['home_ownership']) # home_ownership : 'Rent' , 'Own' , 'Mortgage'
    unique_address_state = pd.unique(df['address_state'])

    purpose_his = df['purpose'].value_counts()
    emp_length_his = df['emp_length'].value_counts()
    id_his = df['id'].value_counts()

    loan_amount_his  = df['loan_amount'].value_counts().reset_index()
    loan_size_info = loan_amount_his.sort_values(by=['loan_amount'])
    print('*')
# ***************************************************************************************************************



    res = retrieving_the_amount_of_loan_taken_by_each_state(df)
    creating_a_treemap_count_for_each_state(res)
    print('*')