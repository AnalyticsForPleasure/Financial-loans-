import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

## seeing a blox plot chart :https://www.kaggle.com/code/dwin183287/covid-19-world-vaccination

# Given data
data = {
    'Number of citizens': [3229, 4382, 4088],
    'Average loan taken': [10183, 13090, 10261]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Calculate total rows needed
total_rows = df['Number of citizens'].sum()

# Initialize an empty DataFrame
scatter_df = pd.DataFrame(columns=['Number of emp length', 'Loan amount'])

# Generate DataFrame with same average loan taken
for index, row in df.iterrows():
    num_citizens = row['Number of citizens']
    loan_amount = row['Average loan taken']
    if index == 0:
        emp_length = '= 1 year'
    elif index == 1:
        emp_length = '< 2 year'
    elif index == 2:
        emp_length = '< 3 year'
    elif index == 3:
        emp_length = '< 4 year'
    elif index == 4:
        emp_length = '< 5 year'
    else:
        emp_length = '< 6 year'
    temp_df = pd.DataFrame({
        'Number of emp length': [emp_length] * num_citizens,
        'Loan amount': np.random.normal(loan_amount, 1000, num_citizens)  # Adding some noise for variety
    })
    scatter_df = pd.concat([scatter_df, temp_df], ignore_index=True)

# Plot the boxplot - starting here with the plot part

background_color = "#f6f5f5"

color_map = ["#FFA500" for _ in range(7)]
sns.set_palette(sns.color_palette(color_map))

plt.rcParams['figure.dpi'] = 400
fig = plt.figure(figsize=(5, 2), facecolor='#f6f5f5')
gs = fig.add_gridspec(1, 1)
gs.update(wspace=0, hspace=0)
ax0 = fig.add_subplot(gs[0, 0])
ax0.set_facecolor(background_color)
for s in ["right", "top"]:
    ax0.spines[s].set_visible(True)


# Create boxplot
#boxplot = scatter_df.boxplot(by='Number of emp length', column='Loan amount')

# Add labels and title
# plt.xlabel('Number of Employment Length', fontsize=14)
# plt.ylabel('Loan Amount', fontsize=14)
ax0.text(-0.5, 18800, 'Relationship between Employment Length and Loan Amount Distribution ', color='black', fontsize=14.5, ha='left', va='bottom', weight='bold',fontfamily='serif')
ax0.text(-0.5, 18200, 'How does the variability in employment duration impact the amount of loans taken?',color='#292929', fontsize=10, ha='left',weight='bold', va='top',fontfamily='serif')
ax0_sns = sns.boxenplot(ax=ax0, x=scatter_df['Number of emp length'], y=scatter_df['Loan amount'],
                         zorder=3, linewidth=0.7, saturation=1)
ax0_sns.set_xlabel("Variation in Length of Employment",fontsize=5, weight='bold', fontfamily='serif')
ax0_sns.set_ylabel("Loan Amount have been taken by a citizen",fontsize=5, weight='bold',fontfamily='serif')
ax0_sns.tick_params(labelsize=5)



#plt.title('Loan Amount Distribution by Employment Length', fontsize=16)

# Remove the automatic title
#plt.suptitle('')

# Show plot
plt.grid(True)

plt.savefig('boxplot_1.jpg', dpi=250, bbox_inches='tight')
plt.show()