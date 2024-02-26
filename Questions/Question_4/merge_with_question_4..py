import matplotlib.pyplot as plt
import numpy as np

# Data
regions = ['Northeast', 'West', 'Southeast', 'Midwest', 'Southwest']
num_loans = [10810, 10051, 8348, 5399, 3973]
avg_income = [72319, 70488, 67252, 64359, 67252]

# Set the width of the bars
bar_width = 0.40

fig = plt.figure(figsize=(10, 3.5), facecolor='#f6f5f5')
ax = fig.add_subplot(111)

# Set the x locations for the groups
r1 = np.arange(len(regions))
r2 = r1 + bar_width

# Plotting the grouped bars
bars1 = ax.bar(r1, num_loans, color='#989898', width=bar_width, edgecolor='grey', label='Number of Loans')
bars2 = ax.bar(r2, avg_income, color='orange', width=bar_width, edgecolor='grey', label='Average Income', hatch='xx')

# Adding annotations
for i, (loan, income) in enumerate(zip(num_loans, avg_income)):
    plt.text(i, loan + 100, str(loan), ha='center', va='bottom', fontweight='bold', fontfamily='serif')
    plt.text(i + bar_width, income + 100, str(income), ha='center', va='bottom', fontweight='bold', fontfamily='serif')

# Adding labels and title
ax.set_xlabel('Region', fontweight='bold', fontfamily='serif')
ax.set_ylabel('Counts', fontweight='bold', fontfamily='serif')
#ax.set_title('Is there any correlation between the average income in each region and the number of loans taken?', fontweight='bold', fontfamily='serif')
ax.text(-0.4, 97000,
         'Average Income vs. Number of Loans',
         fontsize=17.5,
         fontweight='bold',
         fontfamily='serif')

ax.text(-0.4, 81500,
         'Is there any correlation between the average income in each region and the number of \nloans taken?',
         fontsize=11.5,
         fontweight='bold',
         fontfamily='serif',
         color = "#4b4b4c")
ax.set_xticks(np.arange(len(regions)) + bar_width / 2)
ax.set_xticklabels(regions)

# Removing spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# Removing y-axis ticks and labels
ax.tick_params(left=False)
ax.set_yticklabels([])

# Adding legend at the bottom
ax.legend(loc='lower center', ncol=2, bbox_to_anchor=(0.5, -0.3))

plt.savefig('avg_income_1.jpg', dpi=250, bbox_inches='tight')

# Show plot
plt.show()