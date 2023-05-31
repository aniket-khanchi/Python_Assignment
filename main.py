#importing necessary modules

import math
import pandas as pd
from function_inventory import DataframeFunction
from regression import Regression
from data_visualization import Graph
from data_db import add_table
import sys


if __name__ == '__main__':

    #Define the paths of input & output files
    ideal_csv = "data\\ideal.csv"
    test_csv = "data\\test.csv"
    train_csv = "data\\train.csv"

    #Create the object of DataframeFunction class
    test = DataframeFunction(test_csv)
    train = DataframeFunction(train_csv)
    ideal = DataframeFunction(ideal_csv)
    
    #Create the object of Regression & Graph class
    Reg = Regression(train=train._df,test=test._df,ideal=ideal._df)
    chart = Graph(train=train._df,test=test._df,ideal=ideal._df)

    #Calculate the least square method
    ls_dic = Reg.least_squares(ideal._df,train._df)
        
    best_fit_line_dict = Reg.best_fit_line_ideal_func(ls_dic)
    # {'y1': {'y42': 0.28961785540842777}, 'y2': {'y35': 0.29744511136874047}, 'y3': {'y21': 0.2825502509243733}, 'y4': {'y31': 0.2971635951370235}}
    
    #
    line_equ_train_data_df = Reg.line_eqn_para(train._df)
    line_equ_train_data_dict = line_equ_train_data_df.to_dict()
    line_qeu_ideal_data_df = Reg.line_eqn_para(ideal._df)
    line_equ_ideal_data_dict = line_qeu_ideal_data_df.to_dict()

    #Plot the line chart vs scatter plot for train functions
    train_chart = chart.line_chart(train._df,line_equ_train_data_dict,'train_functions')

    #Create the selected ideal function dataframe for chart generation
    ideal_fn_df  =  pd.DataFrame()
    ideal_fn_df['x'] = ideal._df['x']
    for column in best_fit_line_dict:
        first_key = next(iter(best_fit_line_dict[column]))
        ideal_fn_df[first_key] = ideal._df[first_key]
    
    #Plot the line chart vs scatter plot for selected ideal functions  Line->ideal, Scatter->train
    ideal_chart = chart.line_chart(ideal_fn_df,line_equ_ideal_data_dict,'ideal_functions')

    #Plot the line chart vs scatter plot for train functions with respect to ideal functions
    chart.min_deviation_chart(train._df,line_equ_train_data_dict,ideal_fn_df,line_equ_ideal_data_dict)
    
    # calculate the max deviation for ideal dataset with respect to train dataset
    max_deviation_train_ideal_dict = Reg.max_deviation_train_ideal_data(best_fit_line_dict)
    # print(max_deviation_train_ideal_dict)
    # {'y1': {'y42': 0.7037}, 'y2': {'y35': 0.7056}, 'y3': {'y21': 0.7027}, 'y4': {'y31': 0.702}}

    #validate the test data with in range of max deviation
    map_test_dataset_dict,df_ls = Reg.validate_max_deviation_test_data(max_deviation_train_ideal_dict)
    # print(map_test_dataset_dict,df_ls)

    #Create the dataframe for map data
    df_map = pd.DataFrame()
    for row in df_ls:
        df_map= df_map._append(row, ignore_index=True)
    fin_map_df = Reg.create_map_df(df_map,test._df,ideal._df)

    #Map the test data in chart
    chart.generate_map_test_data_chart(map_test_dataset_dict,max_deviation_train_ideal_dict)
 
    # Loading the data into database
    add_table(train._df,table_name = 'train_data' )
    add_table(ideal._df,table_name = 'ideal_data')
    add_table(fin_map_df,table_name = 'map_data' )



    



    















           
            
        

