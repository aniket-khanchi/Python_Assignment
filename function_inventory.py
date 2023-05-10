import pandas as pd

class DataframeFunctions:
    
    def __init__(self,data_path) -> None:
        """
        A csv is a converted in a list of functions which can be iterated & used to get a function.
        Parameters:
            data_path:- A pandas dataframe argument is to be passed.
        
        """

        try:
            # Attempt to read the CSV file
            self._df = pd.read_csv(data_path)
            # Perform operations on the dataframe
        except FileNotFoundError:
            # Handle the case where the file is not found
            print("File not found. Please check the file path.")
        except Exception as e:
            # Handle any other exceptions that may occur during CSV file reading
         print(f"An error occurred: {e}")

        # Get list of y columns
        y_columns = self._df.columns[1:]

        # Create a dictionary to store the new DataFrames
        self.df_dict = {}

        # Iterate over y columns and create new DataFrames
        for col in y_columns:
            # Extract x and y columns
            x_col = 'x'
            y_col =  col
            
            # Create a new DataFrame with columns 'x' and 'y'
            new_df = pd.DataFrame({'x': self._df[x_col], 'y': self._df[y_col]})
            
            # Store the new DataFrame in the dictionary with a key as the y column name
            name = "DataFrame for " + col
            self.df_dict[name] = new_df



 



        
    
    
           


