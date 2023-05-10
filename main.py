#importing necessary modules

import math
from function_inventory import DataframeFunctions
from loss_function import squared_error, minimise_loss, find_classification


if __name__ == '__main__':

    # define the path of the files required in this project
    df_test = "data/test.csv"
    df_train = "data/train.csv"
    df_ideal_fun = "data/ideal.csv"

train_functions = DataframeFunctions(df_train)
ideal_functions = DataframeFunctions(df_ideal_fun)
test_functions = DataframeFunctions(df_test)
# print(train_functions.df_dict)
# print(ideal_functions.df_dict['DataFrame for y50'])
ideal_fun_list = []
for train_fun in train_functions.df_dict.keys():
    ideal_fun = minimise_loss(train_functions.df_dict[train_fun],ideal_functions,squared_error)
    ideal_fun_list.append(ideal_fun)

    
# print(ideal_fun_list)

test_fun = test_functions.df_dict["DataFrame for y"]
# print(test_fun)
pint_ls_ideal_fn = []
for index, row in test_fun.iterrows():
    # print( pint_ls.append(row["x"],row['y']))
    # print((row["x"],row["y"]))
    point = (row["x"],row["y"])
    ideal_function, delta_y = find_classification(point=point, ideal_functions=ideal_fun_list)
    result = {"point": point, "classification": ideal_function, "delta_y": delta_y}
    pint_ls_ideal_fn.append(result)



# print(pint_ls[0]["x"])







           
            
        

