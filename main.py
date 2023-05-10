#importing necessary modules

import math
import pandas as pd
from function_inventory import DataframeFunction
from regression import line_eqn_para,least_squares,best_fit_line_ideal_func
# from loss_function import squared_error, minimise_loss, find_classification


if __name__ == '__main__':

    #Define the paths of input & output files
    ideal_csv = "data\\ideal.csv"
    test_csv = "data\\test.csv"
    train_csv = "data\\train.csv"


    test = DataframeFunction(test_csv)
    train = DataframeFunction(train_csv)
    ideal = DataframeFunction(ideal_csv)

    # print(line_eqn_para(train._df).head())
    dic = least_squares(ideal._df,train._df)
    print(best_fit_line_ideal_func(dic))



    



    















           
            
        

