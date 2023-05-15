import pandas as pd
import sys

class DataframeFunction:
    
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

    
    def dict_to_dataframe(self,my_dict):
        try:
            df = pd.DataFrame(my_dict)
            return df
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    
    




 



        
    
    
           


