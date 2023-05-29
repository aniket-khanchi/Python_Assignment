#importing necessary modules

import math
import pandas as pd
from function_inventory import DataframeFunction
from regression import Regression
from data_visualization import Graph
from data_db import add_table
import sys
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
    Reg = Regression(train=train._df,test=test._df,ideal=ideal._df)
    chart = Graph(train=train._df,test=test._df,ideal=ideal._df)


    
    dic = Reg.least_squares(ideal._df,train._df)
    # print(line_equ_train_data_df)
    # print(dic)
    
    
    best_fit_line_dict = Reg.best_fit_line_ideal_func(dic)
    # print(best_fit_line_dict)
    # {'y1': {'y42': 0.28961785540842777}, 'y2': {'y35': 0.29744511136874047}, 'y3': {'y21': 0.2825502509243733}, 'y4': {'y31': 0.2971635951370235}}
    
    line_equ_train_data_df = Reg.line_eqn_para(train._df)
    line_equ_train_data_dict = line_equ_train_data_df.to_dict()
    line_qeu_ideal_data_df = Reg.line_eqn_para(ideal._df)
    line_equ_ideal_data_dict = line_qeu_ideal_data_df.to_dict()
    # print(line_equ_ideal_data_dict)
    # sys.exit()
    # train_chart_df = chart.line_chart(train._df,line_equ_train_data_dict,'train')
    ideal_fn_df  =  pd.DataFrame()
    ideal_fn_df['x'] = ideal._df['x']
    for column in best_fit_line_dict:
        first_key = next(iter(best_fit_line_dict[column]))
        ideal_fn_df[first_key] = ideal._df[first_key]
    # print(ideal_fn_df)
    
    # ideal_chart_df = chart.line_chart(ideal_fn_df,line_equ_ideal_data_dict,'ideal')
    chart.min_deviation_chart(train._df,line_equ_train_data_dict,ideal_fn_df,line_equ_ideal_data_dict)
    
    
    
    # calculate the max deviation for ideal dataset with respect to train dataset
    max_deviation_train_ideal_dict = Reg.max_deviation_train_ideal_data(best_fit_line_dict,line_equ_train_data_dict)
    # print(max_deviation_train_ideal_dict)
    # {'y1': {'y42': 0.7037}, 'y2': {'y35': 0.7056}, 'y3': {'y21': 0.7027}, 'y4': {'y31': 0.702}}
    #validate the test data with in range of max deviation
    map_test_dataset_dict = Reg.validate_max_deviation_test_data(max_deviation_train_ideal_dict)
    print(len(map_test_dataset_dict))

    # def map_dataframe(map_test_dataset_dict):
    # df_map = pd.DataFrame(map_test_dataset_dict)
    # for column in df_map:
    #     print(column)
    #     non_na = df_map[column].dropna()
    #     print(type(non_na))
    #     for i in range(1,len(non_na)):
    #         print(non_na[i])

  
        #Map the test data in chart
    chart.generate_map_test_data_chart(map_test_dataset_dict,max_deviation_train_ideal_dict)

    # Loading the data into database
    # add_table(train._df,table_name = 'train_data', if_exists='replace', index=False)
    # add_table(ideal._df,table_name = 'ideal_data', if_exists='replace', index=False)
    # add_table(df_map,table_name = 'map_data')



    



    















           
            
        

