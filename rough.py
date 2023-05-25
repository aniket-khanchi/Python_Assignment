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

# from bokeh.plotting import figure, show
# import numpy as np

# # Define the functions
# def f1(x):
#     return np.sin(x)

# def f2(x):
#     return np.cos(x)

# # Define the range of x values
# x = np.linspace(0, 2*np.pi, 100)

# # Calculate the absolute difference between the functions at each x value
# deviation = np.abs(f1(x) - f2(x))

# # Create a Bokeh figure
# p = figure(title='Minimum Deviation', x_axis_label='x', y_axis_label='Deviation')

# # Add a line plot for the deviation
# p.line(x, deviation, line_width=2)

# # Show the Bokeh figure
# show(p)

# import numpy as np
# from bokeh.plotting import figure, show
# from bokeh.io import output_notebook

# def minimum_deviation(x, y1, y2):
#     # Convert lists to NumPy arrays
#     y1 = np.array(y1)
#     y2 = np.array(y2)
    
#     # Calculate the absolute difference between y1 and y2
#     deviation = np.abs(y1 - y2)
    
#     # Find the minimum deviation for each x value
#     min_deviation = np.min(deviation)
    
#     return min_deviation

# # Example data
# x = [1, 2, 3, 4, 5]  # x-axis values
# y1 = [1, 4, 9, 16, 25]  # y-axis values for function 1
# y2 = [2, 3, 8, 15, 24]  # y-axis values for function 2

# # Calculate the minimum deviation
# min_deviation = minimum_deviation(x, y1, y2)

# # Create a figure
# p = figure(title='Minimum Deviation Graph', x_axis_label='x', y_axis_label='Minimum Deviation')

# # Plot the minimum deviation graph
# p.line(x, [min_deviation] * len(x), line_width=2)

# # Display the plot
# output_notebook()
# show(p)

from bokeh.plotting import figure, show
from bokeh.models import Span

def generate_max_deviation_graph(data_points, reference_value):
    # Calculate the deviation for each data point
    deviations = [data_point - reference_value for data_point in data_points]

    # Find the index of the maximum deviation
    max_deviation_index = deviations.index(max(deviations))

    # Convert range to a list
    x_data_points = list(range(len(data_points)))

    # Create a Bokeh figure
    p = figure(title="Maximum Deviation Graph", x_axis_label="Data Points", y_axis_label="Deviation")

    # Plot the data points
    p.circle(x_data_points, deviations, size=8, color="blue")

    # Highlight the maximum deviation
    max_deviation = Span(dimension="height", line_color="red", line_dash="dashed", line_width=2, line_alpha=0.7, location=max_deviation_index)
    p.add_layout(max_deviation)

    # Display the graph
    show(p)

# Example usage
data_points = [10, 15, 12, 18, 14, 20]
reference_value = 15

generate_max_deviation_graph(data_points, reference_value)


{'y1': {'y42': 0.7037}, 'y2': {'y35': 0.7056}, 'y3': {'y21': 0.7027}, 'y4': {'y31': 0.702}}
{'y1_y42': {8.7: {'x': 8.7, 'y': -17.40402, 'ideal_column': 'y42', 'y_upperband': -16.67437, 'y_lowerband': -18.081770000000002}, 0.4: {'x': 0.4, 'y': -0.4778523, 'ideal_column': 'y42', 'y_upperband': -0.07354000000000005, 'y_lowerband': -1.48094}, 2.6: {'x': 2.6, 'y': -4.922625, 'ideal_column': 'y42', 'y_upperband': -4.47376, 'y_lowerband': -5.881160000000001}, 6.0: {'x': 6.0, 'y': -11.68606, 'ideal_column': 'y42', 'y_upperband': -11.274100000000002, 'y_lowerband': -12.681500000000002}, -13.9: {'x': -13.9, 'y': 27.935085, 'ideal_column': 'y42', 'y_upperband': 28.527890000000006, 'y_lowerband': 27.120490000000004}, 12.5: {'x': 12.5, 'y': -25.196226, 'ideal_column': 'y42', 'y_upperband': -24.27475, 'y_lowerband': -25.682150000000004}, 16.1: {'x': 16.1, 'y': -31.634138, 'ideal_column': 'y42', 'y_upperband': -31.47511000000001, 'y_lowerband': -32.88251000000001}, -12.6: {'x': -12.6, 'y': 24.758558, 'ideal_column': 'y42', 'y_upperband': 25.927760000000003, 'y_lowerband': 24.52036}, -3.6: {'x': -3.6, 'y': 7.3199873, 'ideal_column': 'y42', 'y_upperband': 7.926860000000001, 'y_lowerband': 6.5194600000000005}, 8.9: {'x': 8.9, 'y': -17.187662, 'ideal_column': 'y42', 'y_upperband': -17.07439, 'y_lowerband': -18.481790000000004}}
 , 'y2_y35': {-1.7: {'x': -1.7, 'y': 0.3718966, 'ideal_column': 'y35', 'y_upperband': 0.71186, 'y_lowerband': -0.69934}, 0.4: {'x': 0.4, 'y': -0.4778523, 'ideal_column': 'y35', 'y_upperband': 0.70388, 'y_lowerband': -0.7073200000000001}, 10.2: {'x': 10.2, 'y': 0.57523173, 'ideal_column': 'y35', 'y_upperband': 0.66664, 'y_lowerband': -0.74456}, -10.8: {'x': -10.8, 'y': -0.5637138, 'ideal_column': 'y35', 'y_upperband': 0.74644, 'y_lowerband': -0.66476}}, 'y3_y21': {}, 'y4_y31': {-4.7: {'x': -4.7, 'y': 10.2372875, 'ideal_column': 'y31', 'y_upperband': 10.719660000000001, 'y_lowerband': 9.315660000000001}, -10.5: {'x': -10.5, 'y': 
10.654169, 'ideal_column': 'y31', 'y_upperband': 10.7417, 'y_lowerband': 9.3377}, 11.6: {'x': 11.6, 'y': 10.605287, 'ideal_column': 'y31', 'y_upperband': 10.657720000000001, 'y_lowerband': 9.253720000000001}, 19.5: {'x': 19.5, 'y': 10.450922, 'ideal_column': 'y31', 'y_upperband': 10.6277, 'y_lowerband': 9.223700000000001}}}







