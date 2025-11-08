import matplotlib.pyplot as plt

def plot_linear_graph(slope=1, intercept=0):
    """
    Plots a linear graph based on the equation y = mx + c.

    Parameters:
    - slope (m): The slope of the line.
    - intercept (c): The y-intercept of the line.
    """
    # Generate x values
    x = range(-10, 11)  # From -10 to 10

    # Compute y values based on the linear equation y = mx + c
    y = [slope * xi + intercept for xi in x]

    # Create the plot
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f"y = {slope}x + {intercept}", color='r', linewidth=2)

    # Add title, labels, and grid
    plt.title("Linear Graph", fontsize=16)
    plt.xlabel("X-axis", fontsize=12)
    plt.ylabel("Y-axis", fontsize=12)
    plt.axhline(0, color='black', linewidth=0.5)  # X-axis line
    plt.axvline(0, color='black', linewidth=0.5)  # Y-axis line
    plt.grid(True, linestyle='--', linewidth=0.5)

    # Add legend
    plt.legend(fontsize=12)

    # Show the plot
    plt.show()

# Call the function with default slope and intercept
plot_linear_graph()

# Call the function with custom slope and intercept
# plot_linear_graph(slope=2, intercept=-3)
