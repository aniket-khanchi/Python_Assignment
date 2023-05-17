# import pandas as pd

# # Example DataFrame
# df = pd.DataFrame({'x': [1, 2, 3],
#                    'y1': [4, 5, 6],
#                    'y2': [7, 8, 9],
#                    'y3': [10, 11, 12]})

# # Define a function to create a dictionary of functions
# def create_functions(df):
#     # Get list of y columns
#     y_columns = df.columns[1:]

#     # Create a dictionary to store the functions
#     func_dict = {}

#     # Iterate over y columns and create functions
#     for col in y_columns:
#         # Extract x and y column names
#         x_col = 'x'
#         y_col = col
        
#         # Create a function that takes x and y values as input and returns y/x
#         func = lambda x, y: y / x
        
#         # Bind x_col and y_col to the function
#         func.__name__ = f"function_for_{x_col}_{y_col}"
        
#         # Store the function in the dictionary with a key as the y column name
#         func_dict[col] = func

#     # Return the dictionary of functions
#     return func_dict

# # Create the dictionary of functions
# func_dict = create_functions(df)

# # Access the functions by y column name and call them with x and y values
# for col, func in func_dict.items():
#     print(f"Function for {col}:")
#     for i in range(len(df)):
#         x_val = df.loc[i, 'x']
#         y_val = df.loc[i, col]
#         result = func(x_val, y_val)
#         print(f"({x_val}, {y_val}) -> {result}")
#     print()


# import pandas as pd

# # create sample dataframes
# df1 = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [10, 20, 30, 40, 50]})
# df2 = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [12, 18, 32, 41, 52]})

# # merge dataframes on x value
# merged_df = pd.merge(df1, df2, on='x')

# # calculate difference between y values
# merged_df['diff'] = merged_df['y_x'] - merged_df['y_y']

# # take absolute value of difference
# merged_df['abs_diff'] = abs(merged_df['diff'])

# # find maximum absolute difference
# max_diff = merged_df['abs_diff'].max()
# print(merged_df)
# print(max_diff)
# import numpy as np
# import matplotlib.pyplot as plt

# # Example data
# x = np.array([1, 2, 3, 4, 5])
# y = np.array([2, 3, 5, 4, 6])

# # Calculate least squares line
# m, b = np.polyfit(x, y, 1)

# # Plot data and least squares line
# plt.scatter(x, y)
# plt.plot(x, m*x + b, color='red')
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# import mpld3

# # Example data
# x = np.array([1, 2, 3, 4, 5])
# y = np.array([2, 3, 5, 4, 6])

# # Calculate least squares line
# m, b = np.polyfit(x, y, 1)

# # Plot data and least squares line
# plt.scatter(x, y)
# plt.plot(x, m*x + b, color='red')

# # Convert plot to HTML
# html = mpld3.fig_to_html(plt.gcf())
# with open('plot.html', 'w') as f:
#     f.write(html)


# from bokeh.plotting import figure, show

# # Example data for two line graphs
# x = [1, 2, 3, 4, 5]
# y1 = [6, 7, 2, 4, 5]
# y2 = [3, 2, 5, 6, 4]

# # Create a figure
# p = figure(title="Comparison of Line Graphs", x_axis_label='X', y_axis_label='Y')

# # Add the first line graph
# p.line(x, y1, line_color='red', line_width=2, legend_label='Line Graph 1')

# # Add the second line graph
# p.line(x, y2, line_color='blue', line_width=2, legend_label='Line Graph 2')

# # Display the legend
# p.legend.location = "top_left"

# # Show the figure
# show(p)
# from bokeh.plotting import figure, show
# import numpy as np

# # Example data for a line graph and its deviation
# x = [1, 2, 3, 4, 5]
# y = [6, 7, 2, 4, 5]
# deviation = [1, 2, 1, 3, 1]

# # Create a figure
# p = figure(title="Line Graph with Deviation", x_axis_label='X', y_axis_label='Y')

# # Add the line graph
# p.line(x, y, line_width=2)

# # Create the x and y coordinates for the shaded region
# x_patch = x + x[::-1]
# y_patch = np.array(y) - np.array(deviation)
# y_patch = np.append(y_patch, (np.array(y) + np.array(deviation))[::-1])

# # Add the shaded region representing deviation
# p.patch(x_patch, y_patch, fill_alpha=0.2)

# # Show the figure
# show(p)

# import pandas as pd

# # Create a DataFrame
# df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# # Get the variable name of the DataFrame
# variable_name = None

# globals_copy = globals().copy()  # Create a copy of the globals dictionary

# for name, value in globals_copy.items():
#     if value is df:
#         variable_name = name
#         break

# # Print the variable name
# print(variable_name)

# from bokeh.plotting import figure, show
# from bokeh.layouts import gridplot

# # Create the individual plots
# plot1 = figure(title="Plot 1", width=300, height=300)
# plot1.circle([1, 2, 3], [4, 5, 6], size=10, color='red')

# plot2 = figure(title="Plot 2", width=300, height=300)
# plot2.line([1, 2, 3], [6, 2, 8], line_width=2, color='blue')

# plot3 = figure(title="Plot 3", width=300, height=300)
# plot3.square([1, 2, 3], [2, 4, 3], size=12, color='green')

# plot4 = figure(title="Plot 4", width=300, height=300)
# plot4.triangle([1, 2, 3], [5, 3, 1], size=8, color='orange')

# # Create a grid layout of the plots
# grid = gridplot([[plot1, plot2], [plot3, plot4]])

# # Show the grid layout
# show(grid)

from bokeh.plotting import figure, show
import numpy as np

# Define the functions
def f1(x):
    return np.sin(x)

def f2(x):
    return np.cos(x)

# Define the range of x values
x = np.linspace(0, 2*np.pi, 100)

# Calculate the absolute difference between the functions at each x value
deviation = np.abs(f1(x) - f2(x))

# Create a Bokeh figure
p = figure(title='Minimum Deviation', x_axis_label='x', y_axis_label='Deviation')

# Add a line plot for the deviation
p.line(x, deviation, line_width=2)

# Show the Bokeh figure
show(p)





