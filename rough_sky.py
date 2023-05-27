from bokeh.plotting import figure, show

# Example data
x_data = [1, 2, 3, 4, 5]
y_upper = [5, 6, 7, 8, 9]
y_lower = [3, 4, 5, 6, 7]

# Create a Bokeh figure
p = figure(title="Deviation", x_axis_label="X", y_axis_label="Y")

# Plot the upper and lower bands
p.line(x_data, y_upper, line_color="blue", line_width=2, legend_label="Upper Band")
p.line(x_data, y_lower, line_color="red", line_width=2, legend_label="Lower Band")

# Create a shaded region between the upper and lower bands
p.varea(x=x_data, y1=y_upper, y2=y_lower, fill_color="gray", fill_alpha=0.5)

# Add a legend
p.legend.location = "top_left"

# Display the graph
show(p)




