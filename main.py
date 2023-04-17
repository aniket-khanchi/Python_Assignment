# # importing necessary modules
import math
from function_inventory import DataframeFunctions
from loss_function import squared_error


if __name__ == '__main__':
    df_test = "data/test.csv"
    df_train = "data/train.csv"
    df_ideal_fun = "data/ideal.csv"

train_functions = DataframeFunctions(df_test)
ideal_functions = DataframeFunctions(df_ideal_fun)

# print(train_functions.df_dict)
print(ideal_functions.df_dict['DataFrame for y50'])

print(squared_error(ideal_functions.df_dict['DataFrame for y50'],ideal_functions.df_dict['DataFrame for y10']))





           
            
        

