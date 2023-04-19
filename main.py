# # importing necessary modules
import math
from function_inventory import DataframeFunctions
from loss_function import squared_error, minimise_loss


if __name__ == '__main__':
    df_test = "data/test.csv"
    df_train = "data/train.csv"
    df_ideal_fun = "data/ideal.csv"

train_functions = DataframeFunctions(df_train)
ideal_functions = DataframeFunctions(df_ideal_fun)

# print(train_functions.df_dict)
# print(ideal_functions.df_dict['DataFrame for y50'])
ideal_fun_list = []
for train_fun in train_functions.df_dict.keys():
    ideal_fun = minimise_loss(train_functions.df_dict[train_fun],ideal_functions,squared_error)
    ideal_fun_list.append(ideal_fun)

    
print(ideal_fun_list)





           
            
        

