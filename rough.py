import pandas as pd

# Example DataFrame
df = pd.DataFrame({'x': [1, 2, 3],
                   'y1': [4, 5, 6],
                   'y2': [7, 8, 9],
                   'y3': [10, 11, 12]})

# Define a function to create a dictionary of functions
def create_functions(df):
    # Get list of y columns
    y_columns = df.columns[1:]

    # Create a dictionary to store the functions
    func_dict = {}

    # Iterate over y columns and create functions
    for col in y_columns:
        # Extract x and y column names
        x_col = 'x'
        y_col = col
        
        # Create a function that takes x and y values as input and returns y/x
        func = lambda x, y: y / x
        
        # Bind x_col and y_col to the function
        func.__name__ = f"function_for_{x_col}_{y_col}"
        
        # Store the function in the dictionary with a key as the y column name
        func_dict[col] = func

    # Return the dictionary of functions
    return func_dict

# Create the dictionary of functions
func_dict = create_functions(df)

# Access the functions by y column name and call them with x and y values
for col, func in func_dict.items():
    print(f"Function for {col}:")
    for i in range(len(df)):
        x_val = df.loc[i, 'x']
        y_val = df.loc[i, col]
        result = func(x_val, y_val)
        print(f"({x_val}, {y_val}) -> {result}")
    print()