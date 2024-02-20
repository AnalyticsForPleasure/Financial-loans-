import matplotlib.pyplot as plt
import squarify    # You need to install this library using pip: pip install squarify

# Example data
sizes = [500, 300, 200, 100]
labels = ['A', 'B', 'C', 'D']

# Plotting
plt.figure(figsize=(8, 6))
squarify.plot(sizes=sizes, label=labels, color=["red","green","blue", "orange"], alpha=0.7)

# Adding title and axis labels
plt.title("Example Treemap")
plt.axis('off')    # Turn off axis

# Display the plot
plt.show()